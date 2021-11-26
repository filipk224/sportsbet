# -*- coding: utf-8 -*-
from typing import Counter
import scrapy
import Constants as Constant
import TeamNames

class SportsbetSpider(scrapy.Spider):
    name = 'sportsbet_update'
    allowed_domains = ['www.sportsbet.com.au', # Bets
    'www.msn.com', # Rugby League [NRL], Basketball - US [NBA] 
    'basketball.draftcentral.com.au', # Basketball - Aus/Other [NBL]
    'www.liveladders.com', # Australian Rules [AFL]
    'www.nfl.com', # American Football [NFL]
    'www.pickandroll.com.ar', # Basketball - Aus/Other [Argentina La Liga]
    'nbl1.com.au', # Basketball - Aus/Other [Australian NBL1]
    'www.scorespro.com', # Basketball [Chilean LNB, Big3 3x3(US)], Australian Rules [SANFL], Rugby Union [Rugby Championship, Currie Cup]
    'www.asia-basket.com', # Basketball [Chinese NBL]
    'gameday.bigv.com.au', # Basketball [Aus Big V]
    'tipsscore.com', # Basketball [Dominican Republic, Polish PLK]
    'www.latinbasket.com', # Basketball [Uruguayan Metro League, Brazilian Campeonato Paulista]
    'www.aba-liga.com' # Basketball [ABA League]
    ]
    start_urls = ['https://www.sportsbet.com.au/betting/sports-az']

    def parse(self, response):
        
        ## Available sports
        for sport in response.xpath("//a[@data-automation-id='sports-a-to-z-class-link']"):
            if sport.xpath(".//div/div/span/text()").get() in Constant.allowedSport:
                yield response.follow(url=f'https://www.sportsbet.com.au{sport.xpath(".//@href").get()}', callback=self.parse_bets)
            elif sport.xpath(".//div/div/span/text()").get() in Constant.disallowedSport:
                continue
            else:
                print('Un-included Sport: ', sport.xpath(".//div/div/span/text()").get())


    def parse_bets(self, response):
        set_year_for_link=Constant.year_for_link
        games=[]

        ## Collect open bets
        if response.xpath("//div[contains(@class, 'market-coupon-grid')]"):
            for container in response.xpath("//div[@data-automation-id='class-featured-events-container']/div"):
                for card in container.xpath(".//ul/li"):
                    league = card.xpath(".//div/div/div/div/a/div/div/span/span[2]/text()").get()
                    if league and league not in Constant.disallowed_leagues:
                        Participant1 = {'Name': card.xpath(".//div[@data-automation-id='participant-one']/text()").get(), 'Price': card.xpath("(.//span[@data-automation-id='price-text'])[1]/text()").get()}
                        Participant2 = {'Name': card.xpath(".//div[@data-automation-id='participant-two']/text()").get(), 'Price': card.xpath("(.//span[@data-automation-id='price-text'])[2]/text()").get()}

                        try:
                            if Participant1['Name'] and Participant1['Name'] != None:
                                games.append({
                                    'Sport': response.xpath('//h1/text()').get(),
                                    'League': league,
                                    'Date': container.xpath(".//div/div/text()").get(),
                                    'Time': card.xpath(".//span[@data-automation-id='competition-event-card-time']/text()").get(),
                                    'Participant1': Participant1,
                                    'Participant2': Participant2
                                })
                        except:
                            None
                        else:
                            continue
        elif response.xpath("//ul[@class='upcomingEventsListDesktop_fri609p']/div[position()>1]"):
            for container in response.xpath("//ul[@class='upcomingEventsListDesktop_fri609p']/div[position()>1]"):
                for slip in container.xpath(".//ul/li"):
                    if slip.xpath(".//div/div/a/div/div/div/span/span[2]/text()").get() not in Constant.disallowed_leagues:
                        if slip.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get() == None:
                            participant=1
                            Participant1=''
                            continue
                        else:
                            participant=1
                            button = slip.xpath(".//div[@class='priceButtonContentMultiLine_f1nrpck2']")
                            if button:
                                for content in button:
                                    if participant==1:
                                        Participant1={'Name':content.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 'Price':content.xpath(".//span[@data-automation-id='price-text']/text()").get()}
                                        participant+=1
                                    elif participant==2:
                                        Participant2={'Name':content.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 'Price':content.xpath(".//span[@data-automation-id='price-text']/text()").get()}
                            else:
                                # Made with a Rugby Union button come where main screen showed handicap type with names outside the button. Hadn't finished.
                                ext=slip.xpath(".//div/div/div")
                                if ext.xpath(".//div/div/span/text()").get() != ('Odd' or 'Even'):
                                    Participant1={'Name':(ext.xpath(".//div[1]/div[1]/span/text()").get())[:-7], 'Price':(ext.xpath(".//div[2]/div[1]/div/div/div/div/button/div/div/div/span/div/div/div/span/text()").get())}
                                    Participant2={'Name':(ext.xpath(".//div[1]/div[2]/span/text()").get())[:-7], 'Price':(ext.xpath(".//div[2]/div[2]/div/div/div/div/button/div/div/div/span/div/div/div/span/text()").get())}
                        try:
                            if Participant1['Name'] and Participant1['Name']!=None:
                                #spec=slip.xpath(".//div[@class='time_fbgyqei'])")
                                games.append({
                                'Sport':response.xpath('//h1/text()').get(),
                                'League':slip.xpath(".//span[@data-automation-id='competition-name']/text()").get(),
                                'Date':container.xpath(".//div/div/text()").get(),
                                'Time':slip.xpath(".//span[@data-automation-id='competition-event-card-time']/text()").get(),
                                'Participant1':Participant1,
                                'Participant2':Participant2
                                })
                                participant=1
                        except:
                            None
                        else:
                            continue      
        elif response.xpath("//div[@data-automation-id='class-featured-events-container']"): # Checking under Handball 
            for container in response.xpath("//div[@data-automation-id='class-featured-events-container']/div"):
                for slip in container.xpath(".//ul/li"):
                    league=slip.xpath(".//span[@data-automation-id='competition-name']/text()").get()
                    if slip.xpath(".//span[@data-automation-id='competition-name']/text()").get() not in Constant.disallowed_leagues:
                        if slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[3]"):
                            ext1=slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[1]")
                            ext2=slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[3]")
                            Participant1={'Name':ext1.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 'Price':ext1.xpath(".//span[@data-automation-id='price-text']/text()").get()}
                            Participant2={'Name':ext2.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 'Price':ext2.xpath(".//span[@data-automation-id='price-text']/text()").get()}
                        else:
                            ext1=slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[1]")
                            ext2=slip.xpath("(.//div[starts-with(@class, 'outcomeCardItems')]/div)[2]")
                            Participant1={'Name':ext1.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 'Price':ext1.xpath(".//span[@data-automation-id='price-text']/text()").get()}
                            Participant2={'Name':ext2.xpath(".//span[contains(@data-automation-id, 'outcome-name')]/text()").get(), 'Price':ext2.xpath(".//span[@data-automation-id='price-text']/text()").get()}
                        try:
                            if Participant1['Name'] and Participant1['Name']!=None:
                                games.append({
                                'Sport':response.xpath('//h1/text()').get(),
                                'League':league,
                                'Date':container.xpath(".//div/div/text()").get(),
                                'Time':slip.xpath(".//span[@data-automation-id='competition-event-card-time']/text()").get(),
                                'Participant1':Participant1,
                                'Participant2':Participant2
                                })
                        except:
                            None
                        else:
                            continue  

        ## Seperate into leagues
        league_seperate={}
        for game in games:
            if game['League'] in league_seperate:
                list=[]
                for Game in league_seperate[game["League"]]:
                    list.append(Game)
                list.append(game)
                league_seperate[game["League"]]=list
            elif game['League'] not in league_seperate:
                league_seperate[game['League']]=[game]

        #print(league_seperate)

        ##  Send league bets for compare
        for league in league_seperate:
            if league_seperate[league][0]['Sport'] == 'Basketball - US':
                if league == 'NBA':
                    yield response.follow(url='https://www.scorespro.com/basketball/usa/nba/standings/', callback=TeamNames.Basketball_US().parse_Basketball_US_NBA, meta={'allbets': league_seperate[f'{league}']})
                elif league=='Big3 Basketball Matches':
                    yield response.follow(url='https://www.scorespro.com/basketball/usa/big3-3x3/standings/', callback=TeamNames.Basketball_US().parse_Basketball_Big3_Basketball_Matches, meta={'allbets':league_seperate[f'{league}']})
                elif league=='NBA Summer League Matches':
                    yield response.follow(url='https://www.scorespro.com/basketball/usa/nba-summer-league/standings/', callback=TeamNames.Basketball_US().parse_Basketball_NBA_Summer_League, meta={'allbets':league_seperate[f'{league}']})
            
            elif league_seperate[league][0]['Sport'] == 'Basketball - Aus/Other':
                if league == 'Australian NBL':
                    yield response.follow(url=f'https://basketball.draftcentral.com.au/table/{set_year_for_link}-nbl-ladder/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Australian_NBL, meta={'allbets': league_seperate[f'{league}']})
                elif league=='Argentina La Liga':   # link year dependant
                    yield response.follow(url=f'http://www.pickandroll.com.ar/basquet/adc/liga-argentina/{set_year_for_link-1}-{set_year_for_link}/estadisticas/?opci=acumuladas&modo=puntos', callback=TeamNames.Basketball_AusOther().parse_Basketball_Argentina_La_Liga, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Australian NBL1':
                    yield response.follow(url='https://nbl1.com.au/stats/ladder/north/men', callback=TeamNames.Basketball_AusOther().parse_Basketball_NBL1, meta={'allbets':league_seperate[f'{league}'], 'loop_count': 1, 'group_ladder': []})
                elif league=='Chilean LNB':
                    yield response.follow(url='https://www.scorespro.com/basketball/chile/lnb/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Chilean_LNB, meta={'allbets':league_seperate[f'{league}']})
                elif league=='New Zealand NBL':
                    yield response.follow(url='https://www.scorespro.com/basketball/new-zealand/nbl/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_New_Zealand_NBL, meta={'allbets':league_seperate[f'{league}']})
                elif league=='PBA Philippine Cup':
                    yield response.follow(url='https://www.scorespro.com/basketball/philippines/pba-philippine-cup/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_PBA_Philippine_Cup, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Chinese NBL':
                    yield response.follow(url='https://www.asia-basket.com/China/basketball-League-NBL.aspx', callback=TeamNames.Basketball_AusOther().parse_Basketball_Chinese_NBL, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Australian Big V':
                    yield response.follow(url='https://gameday.bigv.com.au/#ladder', callback=TeamNames.Basketball_AusOther().parse_Australian_Big_V, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Dominican Rep LNB':
                    yield response.follow(url='https://tipsscore.com/en/basketball/league/dominican-republic-lnb', callback=TeamNames.Basketball_AusOther().parse_Basketball_Dominican_Republic, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Uruguayan Metro League':
                    yield response.follow(url='https://www.latinbasket.com/Uruguay/basketball-Metropolitan-League.aspx', callback=TeamNames.Basketball_AusOther().parse_Basketball_Uruguayan, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Brazilian Campeonato Paulista':
                    yield response.follow(url='https://www.latinbasket.com/Brazil/basketball-League-Paulista.asp', callback=TeamNames.Basketball_AusOther().parse_Basketball_Brazilian_Campeonato_Paulista, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Mexican LNBP':
                    yield response.follow(url='https://www.scorespro.com/basketball/mexico/lnbp/standings/', callback=TeamNames.Basketball_AusOther().parse_Mexican_LNBP, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Polish PLK':
                    yield response.follow(url='https://tipsscore.com/en/basketball/league/poland-plk', callback=TeamNames.Basketball_AusOther().parse_Polish_PLK, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Club Friendly Men':
                    yield response.follow(url='https://www.scorespro.com/basketball/russia/super-league/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Club_Friendly_Men, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Italian A2 Super Cup':
                    yield response.follow(url='https://www.scorespro.com/basketball/italy/a2/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Italian_A2_Supercup, meta={'allbets':league_seperate[f'{league}']})
                elif league=='ABA League':
                    yield response.follow(url='https://www.aba-liga.com/standings/21/1/', callback=TeamNames.Basketball_AusOther().parse_Baskebtall_ABA_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Argentinian Super 20':
                    yield response.follow(url='https://www.scorespro.com/basketball/argentina/torneo-super-20/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Argentinian_Super_20, meta={'allbets':league_seperate[f'{league}']})
                elif league=='BNXT League':
                    yield response.follow(url='https://hosted.dcd.shared.geniussports.com/bnxt/en/standings?', callback=TeamNames.Basketball_AusOther().parse_Baskebtall_BNXT_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Bahraini Premier League':
                    yield response.follow(url='https://basketball.asia-basket.com/Bahrain/basketball.aspx', callback=TeamNames.Basketball_AusOther().parse_Baskebtall_Bahraini_Premier_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Danish Basket Ligaen':
                    yield response.follow(url='https://www.scorespro.com/basketball/denmark/basketligaen/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Danish_Basket_Ligaen, meta={'allbets':league_seperate[f'{league}']})
                elif league=='EuroLeague':
                    yield response.follow(url='https://www.scorespro.com/basketball/europe/euroleague/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_EuroLeague, meta={'allbets':league_seperate[f'{league}']})
                elif league=='FIBA EuroCup Women':
                    yield response.follow(url='https://www.scorespro.com/basketball/europe/eurocup-women/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_FIBA_Eurocup_Women, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Czech NBL':
                    yield response.follow(url='https://www.scorespro.com/basketball/czech-republic/nbl/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Czech_NBL, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Finnish Korisliiga':
                    yield response.follow(url='https://www.scorespro.com/basketball/finland/korisliiga/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Finnish_Korisliiga, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Chinese CBA':
                    yield response.follow(url='https://www.scorespro.com/basketball/china/cba/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Chinese_CBA, meta={'allbets':league_seperate[f'{league}']})
                elif league=='French ProB League':
                    yield response.follow(url='https://www.scorespro.com/basketball/france/pro-b/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_French_ProB_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Japanese B League 1':
                    yield response.follow(url='https://www.scorespro.com/basketball/japan/b-league/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Japanese_B_League_1, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Latvian Estonian League':
                    yield response.follow(url='https://www.scorespro.com/basketball/europe/latvia-estonian-league/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Latvian_Estonian_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Norway BLNO':
                    yield response.follow(url='https://www.scorespro.com/basketball/norway/blno/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Norway_BLNO, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Russian Super League':
                    yield response.follow(url='https://www.scorespro.com/basketball/russia/super-league/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Russian_Super_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Spanish ACB':
                    yield response.follow(url='https://www.scorespro.com/basketball/spain/acb/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Spanish_ACB, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Spanish LEB Oro':
                    yield response.follow(url='https://www.scorespro.com/basketball/spain/leb-oro/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Spanish_LEB_Oro, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Bulgarian NBL':
                    yield response.follow(url='https://www.scorespro.com/basketball/bulgaria/nbl/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Bulgarian_NBL, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Cyprus League':
                    yield response.follow(url='https://www.scorespro.com/basketball/cyprus/division-a/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Cyprus_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Czech ZBL':
                    yield response.follow(url='https://www.scorespro.com/basketball/czech-republic/zbl-women/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Czech_ZBL, meta={'allbets':league_seperate[f'{league}']})
                elif league=='EuroCup':
                    yield response.follow(url='https://www.scorespro.com/basketball/europe/eurocup/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_EuroCup, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Hungarian A Division':
                    yield response.follow(url='https://www.scorespro.com/basketball/hungary/nb-i-a/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Hungarian_A_Division, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Israeli National League':
                    yield response.follow(url='https://www.scorespro.com/basketball/israel/super-league/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Israeli_National_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='AIL Division 1A':
                    yield response.follow(url='https://www.scorespro.com/rugby-union/rep-of-ireland/all-ireland-league/standings/', callback=TeamNames.Basketball_AusOther().parse_Rugby_Union_AIL_Division_1A, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Brazilian NBB':
                    yield response.follow(url='https://www.scorespro.com/basketball/brazil/nbb/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Brazilian_NBB, meta={'allbets':league_seperate[f'{league}']})
                elif league=='British BBL Championship':
                    yield response.follow(url='https://www.scorespro.com/basketball/united-kingdom/bbl/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_British_BBL_Championship, meta={'allbets':league_seperate[f'{league}']})
                elif league=='French ProA League':
                    yield response.follow(url='https://www.scorespro.com/basketball/france/lnb/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_French_ProA_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='German BBL':
                    yield response.follow(url='https://www.scorespro.com/basketball/germany/bbl/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_German_BBL, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Korean WKBL':
                    yield response.follow(url='https://www.scorespro.com/basketball/south-korea/wkbl/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Korean_WKBL, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Romanian Liga Nationala':
                    yield response.follow(url='https://www.scorespro.com/basketball/romania/divizia-a/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Romanian_Liga_Nationala, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Swedish Ligan':
                    yield response.follow(url='https://www.scorespro.com/basketball/sweden/ligan/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Swedish_Ligan, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Greek A1':
                    yield response.follow(url='https://www.scorespro.com/basketball/greece/basket-league/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Greek_A1, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Italian Serie A2':
                    yield response.follow(url='https://www.scorespro.com/basketball/italy/a2/standings/', callback=TeamNames.Basketball_AusOther().parse_Basketball_Italian_Serie_A2, meta={'allbets':league_seperate[f'{league}']})
            
            elif league_seperate[league][0]['Sport'] == 'Rugby League':
                if league=='NRL':
                    ## Have 'Round 4, Round5' buttons to work with:
                    yield response.follow(url='https://www.scorespro.com/rugby-league/australia/nrl/standings/', callback=TeamNames.Rugby_League().parse_Rugby_League_NRL, meta={'allbets':league_seperate[f'{league}']})
            
            elif league_seperate[league][0]['Sport'] == 'Australian Rules':
                if league=='AFL':
                    yield response.follow(url='https://www.liveladders.com/AFL/no-gaps.html', callback=TeamNames.Australian_Rules().parse_Australian_Rules_AFL, meta={'allbets':league_seperate[f'{league}']})
                elif league=='SANFL':
                    yield response.follow(url='https://www.scorespro.com/aussie-rules/australia/sanfl/ladder/', callback=TeamNames.Australian_Rules().parse_Australian_SANFL, meta={'allbets':league_seperate[f'{league}']})
            
            elif league_seperate[league][0]['Sport'] == 'American Football':
                if league=='NFL':   ## Link is year based, starts 10/09/21
                    yield response.follow(url=f'https://www.nfl.com/standings/league/{set_year_for_link}/PRE', callback=TeamNames.American_Football().parse_American_Football_NFL, meta={'allbets':league_seperate[f'{league}']})
            
            elif league_seperate[league][0]['Sport'] == 'Rugby Union':
                if league=='The Rugby Championship':
                    yield response.follow(url='https://www.scorespro.com/rugby-union/world/rugby-championship/standings/', callback=TeamNames.Rugby_Union().parse_Rugby_Union_Rugby_Championship, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Currie Cup':
                    yield response.follow(url='https://www.scorespro.com/rugby-union/south-africa/currie-cup/standings/', callback=TeamNames.Rugby_Union().parse_Rugby_Union_Currie_Cup, meta={'allbets':league_seperate[f'{league}']})
                elif league=='French Top 14':
                    yield response.follow(url='https://www.scorespro.com/rugby-union/france/top-14/standings/', callback=TeamNames.Rugby_Union().parse_Rugby_Union_French_Top_14, meta={'allbets':league_seperate[f'{league}']})
                # elif league=='New Zealand NPC':   ## Rugby Union, Found some teams play less through the league
                #     yield response.follow(url='https://www.scorespro.com/rugby-union/new-zealand/itm-cup/standings/', callback=TeamNames.Rugby_Union().parse_Rugby_Union_New_Zealand_NPC, meta={'allbets':league_seperate[f'{league}']})
            
            elif league_seperate[league][0]['Sport'] == 'Ice Hockey - US':
                # elif league=='NHL Matches':   ## low score for now
                #     yield response.follow(url='https://www.scorespro.com/ice-hockey/usa/nhl/standings/', callback=TeamNames.parse_Ice_Hockey_US_NHL_Matches, meta={'allbets':league_seperate[f'{league}']})
                None
            
            elif league_seperate[league][0]['Sport'] == 'Handball':
                if league=='Danish League Men':
                    yield response.follow(url='https://www.scorespro.com/handball/denmark/handball-league/standings/', callback=TeamNames.Handball().parse_Handball_Danish_League_Men, meta={'allbets':league_seperate[f'{league}']})
                elif league=='French Div1 Men':
                    yield response.follow(url='https://www.scorespro.com/handball/france/division-1/standings/', callback=TeamNames.Handball().parse_Handball_French_Div1_Men, meta={'allbets':league_seperate[f'{league}']})
                elif league=='German Bundesliga':
                    yield response.follow(url='https://www.scorespro.com/handball/germany/bundesliga-1/standings/', callback=TeamNames.Handball().parse_Handball_German_Bundesliga, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Norwegian League Men':
                    yield response.follow(url='https://www.scorespro.com/handball/norway/postenligaen/standings/', callback=TeamNames.Handball().parse_Handball_Norwegian_League_Men, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Spanish ASOBAL League':
                    yield response.follow(url='https://www.scorespro.com/handball/spain/liga-asobal/standings/', callback=TeamNames.Handball().parse_Handball_Spanish_ASOBAL_League, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Swedish Elitserien Men':
                    yield response.follow(url='https://www.scorespro.com/handball/sweden/handball-elitserien/standings/', callback=TeamNames.Handball().parse_Handball_Swedish_Elitserien_Men, meta={'allbets':league_seperate[f'{league}']})
            
            elif league_seperate[league][0]['Sport'] == 'Cricket':
                if league=='WBBL':
                    yield response.follow(url='https://www.scorespro.com/cricket/australia/Womens-big-bash-league/standings/', callback=TeamNames.Cricket().parse_Cricket_WBBL, meta={'allbets':league_seperate[f'{league}']})
            
            elif league_seperate[league][0]['Sport'] == 'Volleyball':
                if league=='Korean League Women':
                    yield response.follow(url='https://www.scorespro.com/volleyball/south-korea/v-league-women/standings/', callback=TeamNames.Volleyball().parse_Volleyball_Korean_League_Women, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Turkish League Men':
                    yield response.follow(url='https://www.scorespro.com/volleyball/turkey/league-1/standings/', callback=TeamNames.Volleyball().parse_Volleyball_Turkish_League_Men, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Polish League Women':
                    yield response.follow(url='https://www.scorespro.com/volleyball/poland/orlen-liga-women/standings/', callback=TeamNames.Volleyball().parse_Volleyball_Polish_League_Women, meta={'allbets':league_seperate[f'{league}']})
                elif league=='German Bundesliga Men':
                    yield response.follow(url='https://www.scorespro.com/volleyball/germany/1-bundesliga/standings/', callback=TeamNames.Volleyball().parse_Volleyball_German_Bundesliga_Men, meta={'allbets':league_seperate[f'{league}']})
                elif league=='Polish League Men':
                    yield response.follow(url='https://www.scorespro.com/volleyball/poland/plusliga/standings/', callback=TeamNames.Volleyball().parse_Volleyball_Polish_League_Men, meta={'allbets':league_seperate[f'{league}']})

            
            else:
                yield (print('** League not inserted: ',  league_seperate[league][0]['Sport'] + ', ', league))


            # ## Copy elif stock

                # # elif league=='':
                # #     yield response.follow(url='', callback=TeamNames.().parse_, meta={'allbets':league_seperate[f'{league}']})
