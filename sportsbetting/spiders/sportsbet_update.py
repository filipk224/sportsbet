import scrapy
import Constants as Constant
import TeamNames
from datetime import date

class SportsbetSpider(scrapy.Spider):
    name = 'sportsbet_update'
    allowed_domains = ['www.sportsbet.com.au',
    'www.liveladders.com',
    'www.pickandroll.com.ar',
    'nbl1.com.au',
    'www.scorespro.com',
    'www.asia-basket.com',
    'gameday.bigv.com.au',
    'tipsscore.com',
    'www.latinbasket.com',
    'www.espncricinfo.com',
    'www.bbc.com',
    'www.world.rugby',
    ]

    start_urls = ['https://www.sportsbet.com.au/betting/sports-az']

    def parse(self, response):

        ## Available sports
        for line in response.xpath("//a[@data-automation-id='sports-a-to-z-class-link']"):
            sport=line.xpath(".//div/div/span/text()").get()

            if sport in Constant.allowedSport:
                yield response.follow(url=f'https://www.sportsbet.com.au{line.xpath(".//@href").get()}', callback=self.parse_bets)
            elif sport in Constant.disallowedSport:
                continue
            else:
                print('Un-included Sport: ', sport)

        
    def parse_bets(self, response):
        
        year_for_link=Constant.year_for_link
        legal_days_away=Constant.legal_days_away
        games=[]

        sport = response.xpath('//h1/text()').get()


        ## Collect slips
        # If type 1 layout
        if response.xpath("//div[contains(@class, 'market-coupon-grid')]"):

            # Days played
            for container in response.xpath("//div[@data-automation-id='class-featured-events-container']/div"):
                gameDate = container.xpath(".//div/div/text()").get()
                year = int('20'+gameDate[-2:])
                month = int(gameDate[-5:-3])
                day = int(gameDate[-8:-6])

                # If not far, collect
                if (date(year, month, day)-date.today()).days < legal_days_away:
                    for card in container.xpath(".//ul/li"):
                        league = card.xpath(".//div/div/div/div/a/div/div/span/span[2]/text()").get()
                        time = card.xpath(".//span[@data-automation-id='competition-event-card-time']/text()").get()

                        # If the league qualifys
                        if league and league not in Constant.disallowed_leagues:
                            Participant1 = {
                                'Name': card.xpath(".//div[@data-automation-id='participant-one']/text()").get(),
                                'Price': card.xpath("(.//span[@data-automation-id='price-text'])[1]/text()").get()
                                }
                            Participant2 = {
                                'Name': card.xpath(".//div[@data-automation-id='participant-two']/text()").get(),
                                'Price': card.xpath("(.//span[@data-automation-id='price-text'])[2]/text()").get()
                                }

                            try:
                                if Participant1['Name'] and Participant1['Name'] != None:
                                    games.append({
                                        'Sport': sport,
                                        'League': league,
                                        'Date': gameDate,
                                        'Time': time,
                                        'Participant1': Participant1,
                                        'Participant2': Participant2
                                    })
                            except:
                                print('\n')
                                print('# Unsuccesful collection: ')
                                print(sport)
                                print(league)
                                print(gameDate)
                                print(time)
                                print(Participant1)
                                print(Participant2)
                                print('#####')

        # If Type 2 layout
        elif response.xpath("//ul[@class='upcomingEventsListDesktop_fri609p']/div[position()>1]"):

            # Days played
            for container in response.xpath("//ul[@class='upcomingEventsListDesktop_fri609p']/div[position()>1]"):
                gameDate = container.xpath(".//div/div/text()").get()
                year = int('20'+gameDate[-2:])
                month = int(gameDate[-5:-3])
                day = int(gameDate[-8:-6])

                # If not far, collect
                if (date(year, month, day)-date.today()).days < legal_days_away:
                    for slip in container.xpath(".//ul/li"):
                        league=slip.xpath(".//span[@data-automation-id='competition-name']/text()").get()
                        time = slip.xpath(".//span[@data-automation-id='competition-event-card-time']/text()").get()

                        # If the league qualifys
                        if league not in Constant.disallowed_leagues:
                            if slip.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get() == None:
                                Participant1=''
                                continue
                            else:
                                ext=slip.xpath(".//div/div/div")

                                # If contains draw button
                                if ext.xpath(".//div/div[3]"):
                                    name1=slip.xpath("(.//span[contains(@data-automation-id, 'outcome-name')])[1]/text()").get()
                                    name2=slip.xpath("(.//span[contains(@data-automation-id, 'outcome-name')])[3]/text()").get()

                                    # Name sometimes has handicap numbers contained.
                                    try:
                                        name1.index('(')
                                    except:
                                        None
                                    else:    
                                        name1 = name1[:name1.index('(')-1]
                                        name2 = name2[:name2.index('(')-1]

                                    
                                    Participant1={
                                        'Name':name1, 
                                        'Price':slip.xpath("(.//span[@data-automation-id='price-text'])[1]/text()").get()
                                        }
                                    Participant2={
                                        'Name':name2, 
                                        'Price':slip.xpath("(.//span[@data-automation-id='price-text'])[3]/text()").get()
                                        }

                                # If standard 2 button
                                elif slip.xpath(".//div[@class='priceButtonContentMultiLine_f1nrpck2']"):

                                    Participant1={
                                        'Name':slip.xpath("(.//span[contains(@data-automation-id, 'outcome-name')])[1]/text()").get(), 
                                        'Price':slip.xpath("(.//span[@data-automation-id='price-text'])[1]/text()").get()
                                        }
                                    Participant2={
                                        'Name':slip.xpath("(.//span[contains(@data-automation-id, 'outcome-name')])[2]/text()").get(), 
                                        'Price':slip.xpath("(.//span[@data-automation-id='price-text'])[2]/text()").get()
                                        }

                                # If bet isn't for score points
                                elif ext.xpath(".//div/div/span/text()").get() != ('Odd' or 'Even'):

                                    Participant1={
                                        'Name':ext.xpath(".//div[1]/div[1]/span/text()").get()[:-7], 
                                        'Price':ext.xpath(".//div[2]/div[1]/div/div/div/div/button/div/div/div/span/div/div/div/span/text()").get()
                                        }
                                    Participant2={
                                        'Name':ext.xpath(".//div[1]/div[2]/span/text()").get()[:-7], 
                                        'Price':ext.xpath(".//div[2]/div[2]/div/div/div/div/button/div/div/div/span/div/div/div/span/text()").get()
                                        }


                                    if Participant1['Name'] in ['Over (', 'Under (']:
                                        participants = slip.xpath('.//div/div/a/div/div/h2/text()').get()

                                        Participant1={
                                            'Name':participants[:participants.index(' v ')], 
                                            'Price':ext.xpath(".//div[2]/div[1]/div/div/div/div/button/div/div/div/span/div/div/div/span/text()").get()
                                            }
                                        Participant2={
                                            'Name':participants[participants.index(' v ')+3:], 
                                            'Price':ext.xpath(".//div[2]/div[2]/div/div/div/div/button/div/div/div/span/div/div/div/span/text()").get()
                                            }

                                    
                                try:
                                    if Participant1['Name'] and Participant1['Name']!=None:
                                        games.append({
                                        'Sport':sport,
                                        'League':league,
                                        'Date':gameDate,
                                        'Time':time,
                                        'Participant1':Participant1,
                                        'Participant2':Participant2
                                        })
                                except:
                                    print('\n')
                                    print('# Unsuccesful collection: ')
                                    print(sport)
                                    print(league)
                                    print(gameDate)
                                    print(time)
                                    print(Participant1)
                                    print(Participant2)
                                    print('#####')     
        
        # If type 3 layout
        elif response.xpath("//div[@data-automation-id='class-featured-events-container']"):

            # Days played
            for container in response.xpath("//div[@data-automation-id='class-featured-events-container']/div"):
                gameDate = container.xpath(".//div/div/text()").get()
                year = int('20'+gameDate[-2:])
                month = int(gameDate[-5:-3])
                day = int(gameDate[-8:-6])

                # If not far, collect
                if (date(year, month, day)-date.today()).days < legal_days_away:
                    for slip in container.xpath(".//ul/li"):
                        league = slip.xpath(".//span[@data-automation-id='competition-name']/text()").get()
                        time = slip.xpath(".//span[@data-automation-id='competition-event-card-time']/text()").get()

                        # If the league qualifys
                        if league not in Constant.disallowed_leagues:
                            
                            # If has draw button
                            if slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[3]"):
                                ext1=slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[1]")
                                ext2=slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[3]")

                                Participant1={
                                    'Name':ext1.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 
                                    'Price':ext1.xpath(".//span[@data-automation-id='price-text']/text()").get()
                                    }
                                Participant2={
                                    'Name':ext2.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 
                                    'Price':ext2.xpath(".//span[@data-automation-id='price-text']/text()").get()
                                    }

                            # If standard 2 button
                            elif not slip.xpath(".//div[@class='outcomeCardItems_f4kk892']"):
                                Participant1={
                                    'Name':slip.xpath(".//h2/span[1]/text()").get(), 
                                    'Price':'Internal Button'
                                    }
                                Participant2={
                                    'Name':slip.xpath(".//h2/span[2]/text()").get(), 
                                    'Price':'Internal Button'
                                    }

                            # Otherwise
                            else:
                                ext1=slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[1]")
                                ext2=slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[2]")

                                Participant1={
                                    'Name':ext1.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 
                                    'Price':ext1.xpath(".//span[@data-automation-id='price-text']/text()").get()
                                    }
                                Participant2={
                                    'Name':ext2.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 
                                    'Price':ext2.xpath(".//span[@data-automation-id='price-text']/text()").get()
                                    }

                            try:
                                if Participant1['Name'] and Participant1['Name']!=None:
                                    games.append({
                                    'Sport':sport,
                                    'League':league,
                                    'Date':gameDate,
                                    'Time':time,
                                    'Participant1':Participant1,
                                    'Participant2':Participant2
                                    })
                            except:
                                print('\n')
                                print('# Unsuccesful collection: ')
                                print(sport)
                                print(league)
                                print(gameDate)
                                print(time)
                                print(Participant1)
                                print(Participant2)
                                print('#####')                  

        ## Seperate Sport Leagues
        league_seperate={}

        for game in games:
            if game['League'] in league_seperate.keys():
                league_seperate[game['League']].append(game)
            else:
                league_seperate[game['League']]=[game]

        # League Specific directions
        league={
            'Basketball - Aus/Other': {  # High Low Test Done at 3
                            'Liga ABA 2': ['https://www.scorespro.com/basketball/europe/aba-league-2/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Liga_ABA_2],
                            'Australian NBL': ['https://www.scorespro.com/basketball/australia/nbl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Australian_NBL],
                            # link year dependant\/
                            'Argentina La Liga': [f'http://www.pickandroll.com.ar/basquet/adc/liga-argentina/{year_for_link-1}-{year_for_link}/estadisticas/?opci=acumuladas&modo=puntos', TeamNames.Basketball_AusOther().parse_Basketball_Argentina_La_Liga],
                            'Australian NBL1': ['https://nbl1.com.au/stats/ladder/north/men', TeamNames.Basketball_AusOther().parse_Basketball_NBL1, {'loop_count': 1, 'group_ladder': []}],
                            'Chilean LNB': ['https://www.scorespro.com/basketball/chile/lnb/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Chilean_LNB],
                            'New Zealand NBL': ['https://www.scorespro.com/basketball/new-zealand/nbl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_New_Zealand_NBL],
                            'PBA Philippine Cup': ['https://www.scorespro.com/basketball/philippines/pba-philippine-cup/standings/', TeamNames.Basketball_AusOther().parse_Basketball_PBA_Philippine_Cup],
                            'Chinese NBL': ['https://www.asia-basket.com/China/basketball-League-NBL.aspx', TeamNames.Basketball_AusOther().parse_Basketball_Chinese_NBL],
                            'Australian Big V': ['https://gameday.bigv.com.au/#ladder', TeamNames.Basketball_AusOther().parse_Basketball_Australian_Big_V],
                            'Dominican Rep LNB': ['https://tipsscore.com/en/basketball/league/dominican-republic-lnb', TeamNames.Basketball_AusOther().parse_Basketball_Dominican_Republic],
                            'Uruguayan Metro League': ['https://www.latinbasket.com/Uruguay/basketball-Metropolitan-League.aspx', TeamNames.Basketball_AusOther().parse_Basketball_Uruguayan],
                            'Brazilian Campeonato Paulista': ['https://www.latinbasket.com/Brazil/basketball-League-Paulista.asp', TeamNames.Basketball_AusOther().parse_Basketball_Brazilian_Campeonato_Paulista],
                            'Mexican LNBP': ['https://www.scorespro.com/basketball/mexico/lnbp/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Mexican_LNBP],
                            'Polish PLK': ['https://www.scorespro.com/basketball/poland/energa-basket-liga/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Polish_PLK],
                            'Club Friendly Men': ['https://www.scorespro.com/basketball/russia/super-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Club_Friendly_Men],
                            'Italian A2 Super Cup': ['https://www.scorespro.com/basketball/italy/a2/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Italian_A2_Supercup],
                            'ABA League': ['https://www.scorespro.com/basketball/europe/aba-league/standings/', TeamNames.Basketball_AusOther().parse_Baskebtall_ABA_League],
                            'Argentinian Super 20': ['https://www.scorespro.com/basketball/argentina/torneo-super-20/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Argentinian_Super_20],
                            'BNXT League': ['https://hosted.dcd.shared.geniussports.com/bnxt/en/standings?', TeamNames.Basketball_AusOther().parse_Baskebtall_BNXT_League],
                            'Bahraini Premier League': ['https://basketball.asia-basket.com/Bahrain/basketball.aspx', TeamNames.Basketball_AusOther().parse_Baskebtall_Bahraini_Premier_League],
                            'Danish Basket Ligaen': ['https://www.scorespro.com/basketball/denmark/basketligaen/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Danish_Basket_Ligaen],
                            'EuroLeague': ['https://www.scorespro.com/basketball/europe/euroleague/standings/', TeamNames.Basketball_AusOther().parse_Basketball_EuroLeague],
                            'FIBA EuroCup Women': ['https://www.scorespro.com/basketball/europe/eurocup-women/standings/', TeamNames.Basketball_AusOther().parse_Basketball_FIBA_Eurocup_Women],
                            'Czech NBL': ['https://www.scorespro.com/basketball/czech-republic/nbl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Czech_NBL],
                            'Finnish Korisliiga': ['https://www.scorespro.com/basketball/finland/korisliiga/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Finnish_Korisliiga],
                            'Chinese CBA': ['https://www.scorespro.com/basketball/china/cba/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Chinese_CBA],
                            'French ProB League': ['https://www.scorespro.com/basketball/france/pro-b/standings/', TeamNames.Basketball_AusOther().parse_Basketball_French_ProB_League],
                            'Japanese B League 1': ['https://www.scorespro.com/basketball/japan/b-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Japanese_B_League_1],
                            'Latvian Estonian League': ['https://www.scorespro.com/basketball/europe/latvia-estonian-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Latvian_Estonian_League],
                            'Norway BLNO': ['https://www.scorespro.com/basketball/norway/blno/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Norway_BLNO],
                            'Russian Super League': ['https://www.scorespro.com/basketball/russia/super-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Russian_Super_League],
                            'Spanish ACB': ['https://www.scorespro.com/basketball/spain/acb/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Spanish_ACB],
                            'Spanish LEB Oro': ['https://www.scorespro.com/basketball/spain/leb-oro/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Spanish_LEB_Oro],
                            'Bulgarian NBL': ['https://www.scorespro.com/basketball/bulgaria/nbl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Bulgarian_NBL],
                            'Cyprus League': ['https://www.scorespro.com/basketball/cyprus/division-a/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Cyprus_League],
                            'Czech ZBL': ['https://www.scorespro.com/basketball/czech-republic/zbl-women/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Czech_ZBL],
                            'EuroCup': ['https://www.scorespro.com/basketball/europe/eurocup/standings/', TeamNames.Basketball_AusOther().parse_Basketball_EuroCup],
                            'Hungarian A Division': ['https://www.scorespro.com/basketball/hungary/nb-i-a/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Hungarian_A_Division],
                            'Israeli Supreme League': ['https://www.scorespro.com/basketball/israel/super-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Israeli_Supreme_League],
                            'Brazilian NBB': ['https://www.scorespro.com/basketball/brazil/nbb/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Brazilian_NBB],
                            'British BBL Championship': ['https://www.scorespro.com/basketball/united-kingdom/bbl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_British_BBL_Championship],
                            'French ProA League': ['https://www.scorespro.com/basketball/france/lnb/standings/', TeamNames.Basketball_AusOther().parse_Basketball_French_ProA_League],
                            'German BBL': ['https://www.scorespro.com/basketball/germany/bbl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_German_BBL],
                            'Korean WKBL': ['https://www.scorespro.com/basketball/south-korea/wkbl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Korean_WKBL],
                            'Romanian Liga Nationala': ['https://www.scorespro.com/basketball/romania/divizia-a/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Romanian_Liga_Nationala],
                            'Swedish Ligan': ['https://www.scorespro.com/basketball/sweden/ligan/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Swedish_Ligan],
                            'Greek A1': ['https://www.scorespro.com/basketball/greece/basket-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Greek_A1],
                            'Italian Serie A2': ['https://www.scorespro.com/basketball/italy/a2/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Italian_Serie_A2],
                            'Korean KBL': ['https://www.scorespro.com/basketball/south-korea/kbl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Korean_KBL],
                            'FIBA EuroLeague Women': ['https://www.scorespro.com/basketball/europe/euroleague-women/standings/', TeamNames.Basketball_AusOther().parse_Basketball_FIBA_EuroLeague_Women],
                            'Lithuanian LKL': ['https://www.scorespro.com/basketball/lithuania/lkl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Lithuanian_LKL],
                            'North Macedonia Prva League': ['https://www.scorespro.com/basketball/north-macedonia/super-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_North_Macedonia_Prva_League],
                            'Turkish TBSL': ['https://www.scorespro.com/basketball/turkey/super-ligi/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Turkish_TBSL],
                            "PBA Governors' Cup": ['https://www.scorespro.com/basketball/philippines/pba-governors-cup/standings/', TeamNames.Basketball_AusOther().parse_Basketball_PBA_Governors_Cup],
                            'VTB United League': ['https://www.scorespro.com/basketball/russia/vtb-united-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_VTB_United_League],
                            'German Pro A': ['https://www.scorespro.com/basketball/germany/pro-a/standings/', TeamNames.Basketball_AusOther().parse_Basketball_German_Pro_A],
                            'Polish League Women': ['https://www.scorespro.com/basketball/poland/energa-basket-liga-women/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Polish_League_Women],
                            'Austrian Bundesliga': ['https://www.scorespro.com/basketball/austria/abl/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Austrian_Bundesliga],
                            'Italian Serie A': ['https://www.scorespro.com/basketball/italy/lega-a/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Italian_Serie_A],
                            'Italian Serie A Women': ['https://www.scorespro.com/basketball/italy/serie-a-women/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Italian_Serie_A_Women],
                            'Bosnia Herzegovina 1 Division': ['https://www.scorespro.com/basketball/bosnia-and-herzegovina/prvenstvo-biH/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Bosnia_Herzegovina_1_Division],
                            'Slovenian League': ['https://www.scorespro.com/basketball/slovenia/liga-nova-kbm/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Slovenian_League],
                            'Portuguese LPB': ['https://www.scorespro.com/basketball/portugal/lpb/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Portuguese_LPB],
                            'Australian WNBL': ['https://www.scorespro.com/basketball/australia/wnbl-women/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Australian_WNBL],
                            'British BBL Cup': ['https://www.scorespro.com/basketball/united-kingdom/bbl-cup/standings/', TeamNames.Basketball_AusOther().parse_Basketball_British_BBL_Cup],
                            'Swiss Basketball League': ['https://www.scorespro.com/basketball/switzerland/sb-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Swiss_Basketball_League],
                            'Lithuanian NKL': ['https://tipsscore.com/en/basketball/league/lithuania-nkl', TeamNames.Basketball_AusOther().parse_Basketball_Lithuanian_NKL],
                            'Balkan BIBL': ['https://www.scorespro.com/basketball/europe/eurohold-balkan-league/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Balkan_BIBL],
                            'Icelandic League Men': ['https://tipsscore.com/en/basketball/league/iceland-urvalsdeild-1', TeamNames.Basketball_AusOther().parse_Basketball_Icelandic_League_Men],
                            'Spanish League Women': ['https://tipsscore.com/en/basketball/league/spain-liga-femenina', TeamNames.Basketball_AusOther().parse_Basketball_Spanish_League_Women],
                            'Uruguayan LUB': ['https://www.scorespro.com/basketball/uruguay/liga-uruguaya/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Uruguayan_LUB],
                            'Danish Damligaen': ['https://www.scorespro.com/basketball/denmark/dameligaen/standings/', TeamNames.Basketball_AusOther().parse_Basketball_Danish_Damligaen],
                            },

            'Volleyball':{  # High Low Test Done at 2.5
                    'Korean League Women': ['https://www.scorespro.com/volleyball/south-korea/v-league-women/standings/', TeamNames.Volleyball().parse_Volleyball_Korean_League_Women],
                    'Turkish League Men': ['https://www.scorespro.com/volleyball/turkey/league-1/standings/', TeamNames.Volleyball().parse_Volleyball_Turkish_League_Men],
                    'Polish League Women': ['https://www.scorespro.com/volleyball/poland/orlen-liga-women/standings/', TeamNames.Volleyball().parse_Volleyball_Polish_League_Women],
                    'German Bundesliga Men': ['https://www.scorespro.com/volleyball/germany/1-bundesliga/standings/', TeamNames.Volleyball().parse_Volleyball_German_Bundesliga_Men],
                    'Polish League Men': ['https://www.scorespro.com/volleyball/poland/plusliga/standings/', TeamNames.Volleyball().parse_Volleyball_Polish_League_Men],
                    'Brazilian Superliga Men': ['https://www.scorespro.com/volleyball/brazil/superliga/standings/', TeamNames.Volleyball().parse_Volleyball_Brazilian_Superliga_Men],
                    'Serbian League Men': ['https://www.scorespro.com/volleyball/serbia/superliga/standings/', TeamNames.Volleyball().parse_Volleyball_Serbian_League_Men],
                    'Italian Serie A2 Men': ['https://www.scorespro.com/volleyball/italy/a2/standings/', TeamNames.Volleyball().parse_Volleyball_Italian_Serie_A2_Men],
                    'Italian Serie A2 Women': ['https://www.scorespro.com/volleyball/italy/a2-women/standings/', TeamNames.Volleyball().parse_Volleyball_Italian_Serie_A2_Women],
                    'Italian Serie A1 Women': ['https://www.scorespro.com/volleyball/italy/a1-women/standings/', TeamNames.Volleyball().parse_Volleyball_Italian_Serie_A1_Women],
                    'Finnish Mestaruusliiga Men': ['https://www.scorespro.com/volleyball/finland/smliiga/standings/', TeamNames.Volleyball().parse_Volleyball_Finnish_Mestaruusliiga_Men],
                    'French Ligue A Men': ['https://www.scorespro.com/volleyball/france/ligue-a/standings/', TeamNames.Volleyball().parse_Volleyball_French_Ligue_A_Men],
                    'Finnish Mestaruusliiga Women': ['https://www.scorespro.com/volleyball/finland/smliiga-women/standings/', TeamNames.Volleyball().parse_Volleyball_Finnish_Mestaruusliiga_Women],
                    'Russian Superleague Men': ['https://www.scorespro.com/volleyball/russia/superleague/standings/', TeamNames.Volleyball().parse_Volleyball_Russian_Superleague_Men],
                    'Greek League Women': ['https://www.scorespro.com/volleyball/greece/a1-women/standings/', TeamNames.Volleyball().parse_Volleyball_Greek_League_Women],
                    'French Ligue A Women': ['https://www.scorespro.com/volleyball/france/ligue-a-women/standings/', TeamNames.Volleyball().parse_Volleyball_French_Ligue_A_Women],
                    'Austrian League': ['https://www.scorespro.com/volleyball/austria/avl/standings/', TeamNames.Volleyball().parse_Volleyball_Austrian_League],
                    'Turkish League Women': ['https://www.scorespro.com/volleyball/turkey/league-1-women/standings/', TeamNames.Volleyball().parse_Volleyball_Turkish_League_Women],
                    'Czech Extraliga Men': ['https://www.scorespro.com/volleyball/czech-republic/extraliga/standings/', TeamNames.Volleyball().parse_Volleyball_Czech_Extraliga_Men],
                    'Romanian Divizia A1 Women': ['https://www.scorespro.com/volleyball/romania/divizia-a1-women/standings/', TeamNames.Volleyball().parse_Volleyball_Romanian_Divizia_A1_Women],
                    'Czech Extraliga Women': ['https://www.scorespro.com/volleyball/czech-republic/extraliga-women/standings/', TeamNames.Volleyball().parse_Volleyball_Czech_Extraliga_Women],
                    'Spanish Superliga Men': ['https://www.scorespro.com/volleyball/spain/superliga/standings/', TeamNames.Volleyball().parse_Volleyball_Spanish_Superliga_Men],
                    'Romanian Divizia A1 Men': ['https://www.scorespro.com/volleyball/romania/divizia-a1/standings/', TeamNames.Volleyball().parse_Volleyball_Romanian_Divizia_A1_Men],
                    },
            
            'Handball':{  # High Low Test Done at 3.5
                    'Champions League Men': ['https://www.scorespro.com/handball/europe/champions-league/standings/', TeamNames.Handball().parse_Handball_Champions_League_Men],
                    'Danish League Men': ['https://www.scorespro.com/handball/denmark/handball-league/standings/', TeamNames.Handball().parse_Handball_Danish_League_Men],
                    'French Div1 Men': ['https://www.scorespro.com/handball/france/division-1/standings/', TeamNames.Handball().parse_Handball_French_Div1_Men],
                    'German Bundesliga': ['https://www.scorespro.com/handball/germany/bundesliga-1/standings/', TeamNames.Handball().parse_Handball_German_Bundesliga],
                    'Norwegian League Men': ['https://www.scorespro.com/handball/norway/postenligaen/standings/', TeamNames.Handball().parse_Handball_Norwegian_League_Men],
                    'Spanish ASOBAL League': ['https://www.scorespro.com/handball/spain/liga-asobal/standings/', TeamNames.Handball().parse_Handball_Spanish_ASOBAL_League],
                    'Swedish Elitserien Men': ['https://www.scorespro.com/handball/sweden/handball-elitserien/standings/', TeamNames.Handball().parse_Handball_Swedish_Elitserien_Men],
                    'Russian Superleague Men': ['https://www.scorespro.com/handball/russia/super-league/standings/', TeamNames.Handball().parse_Handball_Russian_Superleague_Men],
                    'Swedish League Women': ['https://www.scorespro.com/handball/sweden/elitserien-women/standings/', TeamNames.Handball().parse_Handball_Swedish_League_Women],
                    'Russian Superleague Women': ['https://www.scorespro.com/handball/russia/super-league-women/standings/', TeamNames.Handball().parse_Handball_Russian_Superleague_Women],
                    'Danish League Women': ['https://www.scorespro.com/handball/denmark/handball-league-women/standings/', TeamNames.Handball().parse_Handball_Danish_League_Women],
                    'European Championship Qualifiers Men': ['https://www.scorespro.com/handball/europe/european-championship/standings/', TeamNames.Handball().parse_Handball_European_Championship_Qualifiers_Men],
                    'Champions League Women': ['https://www.scorespro.com/handball/europe/champions-league-women/standings/', TeamNames.Handball().parse_Handball_Champions_League_Women],
                    'Norwegian League Women': ['https://www.scorespro.com/handball/norway/postenligaen-women/standings/', TeamNames.Handball().parse_Handball_Norwegian_League_Women],
                    'French Div1 Women': ['https://www.scorespro.com/handball/france/division-1-women/standings/', TeamNames.Handball().parse_Handball_French_Div1_Women],
                    'Romanian League Women': ['https://www.scorespro.com/handball/romania/liga-nationala-women/standings/', TeamNames.Handball().parse_Handball_Romanian_League_Women],
                    'European Championship Men': ['https://www.scorespro.com/handball/europe/european-championship/standings/', TeamNames.Handball().parse_Handball_European_Championship_Men],
                    'Romanian League Men': ['https://www.scorespro.com/handball/romania/liga-nationala/standings/', TeamNames.Handball().parse_Handball_Romanian_League_Men],
                    },

            'Rugby Union':{ # High Low Test Done at 2
                'The Six Nations': ['https://www.scorespro.com/rugby-union/europe/six-nations/standings/', TeamNames.Rugby_Union().parse_Rugby_Union_The_Six_Nations],
                'The Rugby Championship': ['https://www.scorespro.com/rugby-union/world/rugby-championship/standings/', TeamNames.Rugby_Union().parse_Rugby_Union_Rugby_Championship],
                'Currie Cup': ['https://www.scorespro.com/rugby-union/south-africa/currie-cup/standings/', TeamNames.Rugby_Union().parse_Rugby_Union_Currie_Cup],
                'French Top 14': ['https://www.scorespro.com/rugby-union/france/top-14/standings/', TeamNames.Rugby_Union().parse_Rugby_Union_French_Top_14],
                'New Zealand NPC': ['https://www.scorespro.com/rugby-union/new-zealand/itm-cup/standings/', TeamNames.Rugby_Union().parse_Rugby_Union_New_Zealand_NPC],
                'United Rugby Championship': ['https://www.scorespro.com/rugby-union/world/pro14/standings/', TeamNames.Rugby_Union().parse_Rugby_Union_United_Rugby_Championship],
                'Gallagher Premiership': ['https://www.bbc.com/sport/rugby-union/english-premiership/table', TeamNames.Rugby_Union().parse_Rugby_Union_Gallagher_Premiership],
                'AIL Division 1A': ['https://www.scorespro.com/rugby-union/rep-of-ireland/all-ireland-league/standings/', TeamNames.Rugby_Union().parse_Rugby_Union_AIL_Division_1A],
                'French Pro D2': ['https://www.scorespro.com/rugby-union/france/pro-d2/standings/', TeamNames.Rugby_Union().parse_Rugby_Union_French_Pro_D2],
                'World Rugby Sevens': ['https://www.world.rugby/sevens-series/standings/mens', TeamNames.Rugby_Union().parse_Rugby_Union_World_Rugby_Sevens],
                "Women's Sevens": ['https://www.world.rugby/sevens-series/standings/womens', TeamNames.Rugby_Union().parse_Rugby_Union_Womens_Sevens],
                'European Champions Cup': ['https://www.bbc.com/sport/rugby-union/european-cup/table', TeamNames.Rugby_Union().parse_Rugby_Union_European_Champions_Cup],
                },

            'Cricket':{ # High Low Test Done at 2
                'WBBL': ['https://www.scorespro.com/cricket/australia/Womens-big-bash-league/standings/', TeamNames.Cricket().parse_Cricket_WBBL],
                'Super Smash T20': ['https://www.scorespro.com/cricket/new-zealand/super-smash/standings/', TeamNames.Cricket().parse_Cricket_Super_Smash_T20],
                'Twenty20 Big Bash': ['https://www.scorespro.com/cricket/australia/big-bash-league/standings/', TeamNames.Cricket().parse_Cricket_Twenty20_Big_Bash],
                'Test Matches': ['https://www.espncricinfo.com/series/icc-world-test-championship-2021-2023-1268315/points-table-standings', TeamNames.Cricket().parse_Cricket_Test_Matches],
                'Bangladesh Premier League': ['https://www.scorespro.com/cricket/bangladesh/bangladesh-premier-league/standings/', TeamNames.Cricket().parse_Cricket_Bangladesh_Premier_League],
                'Pakistan Super League': ['https://www.scorespro.com/cricket/pakistan/pakistan-super-league/standings/', TeamNames.Cricket().parse_Cricket_Pakistan_Super_League],
                },

            'Basketball - US':{ # High Low Test Done at 3
                        'NBA': ['https://www.scorespro.com/basketball/usa/nba/standings/', TeamNames.Basketball_US().parse_Basketball_US_NBA],
                        'Big3 Basketball Matches': ['https://www.scorespro.com/basketball/usa/big3-3x3/standings/', TeamNames.Basketball_US().parse_Basketball_Big3_Basketball_Matches],
                        'NBA Summer League Matches': ['https://www.scorespro.com/basketball/usa/nba-summer-league/standings/', TeamNames.Basketball_US().parse_Basketball_NBA_Summer_League],
                        },

            'Australian Rules':{ # High Low Test Done at
                        'AFL': ['https://www.liveladders.com/AFL/no-gaps.html', TeamNames.Australian_Rules().parse_Australian_Rules_AFL],
                        'SANFL': ['https://www.scorespro.com/aussie-rules/australia/sanfl/ladder/', TeamNames.Australian_Rules().parse_Australian_SANFL],
                        },

            'Rugby League':{ # High Low Test Done at 
                    'NRL': ['https://www.scorespro.com/rugby-league/australia/nrl/standings/', TeamNames.Rugby_League().parse_Rugby_League_NRL],
                    },

            'American Football':{ # High Low Test Done at 3
                    'NFL': ['https://www.scorespro.com/american-football/usa/nfl/standings/', TeamNames.American_Football().parse_American_Football_NFL],
                    },

            'Ice Hockey - US':{
                
                    },
        }
        
        ##  Send for comparison
        for single_league in league_seperate:

            try:
                url=league[sport][single_league][0]
                callback=league[sport][single_league][1]
            except KeyError:
                print('** League not inserted: ',  sport+', ', single_league)
            else:
                try:
                    league[sport][single_league][2]
                except IndexError:
                    meta= {'allbets':league_seperate[single_league]}
                else:
                    meta= {'allbets':league_seperate[single_league], 'Extra':league[sport][single_league][2:]}
                finally:
                    yield scrapy.Request(url=url, callback=callback, meta=meta)
