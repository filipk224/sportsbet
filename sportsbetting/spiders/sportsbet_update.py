# -*- coding: utf-8 -*-
import scrapy

class SportsbetSpider(scrapy.Spider):
    name = 'sportsbet_update'
    allowed_domains = ['www.sportsbet.com.au', # Bets
    'www.msn.com', # Rugby League [NRL], Basketball - US [NBA] 
    'basketball.draftcentral.com.au', # Basketball - Aus/Other [NBL]
    'www.liveladders.com', # Australian Rules [AFL]
    'www.nfl.com', # American Football [NFL]
    'www.pickandroll.com.ar', # Basketball - Aus/Other [Argentina La Liga]
    'nbl1.com.au', # Basketball - Aus/Other [Australian NBL1]
    'www.scorespro.com', # Basketball [Chilean LNB, Big3 3x3(US)], Australian Rules [SANFL]
    'www.asia-basket.com', # Basketball [Chinese NBL]
    'gameday.bigv.com.au' # Basketball [Aus Big V]
    ]
    start_urls = ['https://www.sportsbet.com.au/betting/sports-az']

    def parse(self, response):
        allowed=(
            'Australian Rules', 
            'Rugby League',
            'Basketball - Aus/Other',
            'Basketball - US',
            'Athletics',  # See what other it does outside Olympics
            'Canoeing', # If they do 4person outside of olympics
            'Gymnastics',
            'Rowing', # Might 4 person
            'Sport Climbing', # See if just climbing?
            'Badminton', # Watching if always non-team
            )

        disallowed=({
            'American Football': 'Season start September',
            'Boxing': 'Not-team',
            'Chess': 'Non-team',
            'Cycling': 'Non-team',
            'Darts': 'Non-team',
            'Golf': 'Non-team',
            'Motor Racing': 'Non-team',
            'Politics': 'Non-team',
            'Snooker': 'Non-team',
            'Surfing': 'Non-team',
            'Table Tennis': 'Non-team',
            'Tennis': 'Non-team',
            'UFC - MMA': 'Non-team',
            'Archery': 'Non-team',
            'Fencing': 'Non-team',
            'Judo': 'Non-team',
            'Karate': 'Non-team',
            'Shooting': 'Non-team',
            'Sailing': 'Non-team',
            'Skateboarding': 'Non-team',
            'Soccer': 'Low Scoring',
            'Swimming': 'Non-team',
            'Taekwondo': 'Non-team',
            'Weightlifting': 'Non-team',
            'Wrestling': 'Non-team',
            'Diving': 'Non-team',
            'Artistic Swimming': 'Non-team',
            'Bowls': 'Non-team',
            'Equestrian': 'Non-team',
            'Modern Pentathlon': 'Non-team',
            'Novelties and Entertainment': 'Non-team',
            'Olympic Games': 'Too Competitive',
            'Triathlon': 'Non-team',
            'Sports Novelties': 'Not Sport',
            })

        ## Available sports
        for sport in response.xpath("//a[@data-automation-id='sports-a-to-z-class-link']"):
            if sport.xpath(".//div/div/span/text()").get() in allowed:
                yield response.follow(url=f'https://www.sportsbet.com.au{sport.xpath(".//@href").get()}', callback=self.parse_bets)
            elif sport.xpath(".//div/div/span/text()").get() in disallowed:
                continue
            else:
                print('Un-included Sport: ', sport.xpath(".//div/div/span/text()").get())

    def parse_bets(self, response):
        set_year_for_link=2021
        games=[]

        disallowed_leagues=({
            'International Friendly Men': 'Basketball - Aus/Other', # Unreliable league
            'State of Origin': 'Rugby League', # 2 Teams always
            'State of Origin - Man of the Match': 'Rugby League', # Not a league
            "Men's Olympics 2020": 'Basketball - Aus/Other', # Unreliable league
            "Men's Olympics 3x3 2020": 'Basketball - Aus/Other', # Unreliable league
            "Women's Olympics 2020": 'Baskebtall - Aus/Other', # Unreliable league
            "Women's Olympics 3x3 2020": 'Basketball - Aus/Other', # Unreliable league
            'Rugby League Extra Markets': 'Rugby League', # Extra's Market
            'NBA Draft Markets': 'Basketball - US', # Not a league
            'The Basketball Tournament': 'Basketball - US', # Not a league
            'AFL Team Futures Multis': 'Australian Rules', # Not a league
            'Australian Big V Women': 'Basketball - Aus/Other', # Only standing can find needs selenium
            })

        ## Collect open bets
        #base=response.xpath("//ul[starts-with(@class, 'upcomingEventsListDesktop')]")
        # for date in response.xpath("//div[@data-automation-id='competition-event-group-title']"):
        #     for card in date.xpath(".//parent::div/following-sibling::ul/li"):
        #         participant=1
        #         league=card.xpath(".//span[@data-automation-id='competition-name']/text()").get()
        #         if league not in disallowed_leagues:
        #             if card.xpath(".//div[@data-automation-id='multi-market-coupon-event']"):
        #                 Participant1={'Name':card.xpath(".//div[@data-automation-id='participant-one']/text()").get(), 'Price': card.xpath(".//span[@data-automation-id'price-text'][1]/text()").get()}
        #                 Participant2={'Name':card.xpath(".//div[@data-automation-id='participant-two']/text()").get(), 'Price': card.xpath(".//span[@data-automation-id'price-text'][2]/text()").get()}
        #             else:    
        #                 for contendor in card.xpath(".//div[contains(@class, 'outcomeDetails')]"):
        #                     if contendor.xpath(".//span[contains(@data-automation-id, 'name')]/text()").get() == None:
        #                         participant=1
        #                         continue
        #                     if participant==1:
        #                         Participant1={'Name':contendor.xpath(".//span[contains(@data-automation-id, 'name')]/text()").get(), 'Price':contendor.xpath(".//div/div/span[@data-automation-id='price-text']/text()").get()}
        #                         participant+=1
        #                     elif participant==2:
        #                         Participant2={'Name':contendor.xpath(".//span[contains(@data-automation-id, 'name')]/text()").get(), 'Price':contendor.xpath(".//div/div/span[@data-automation-id='price-text']/text()").get()}
        #             else:
        #                 Participant1=''
                    
        #             try:
        #                 if Participant1['Name']:
        #                  if Participant1['Name']!=None:
        #                     games.append({
        #                     'Sport':response.xpath('//h1/text()').get(),
        #                     'League':league,
        #                     'Date':date.xpath(".//text()").get(),
        #                     'Time':card.xpath(".//span[@data-automation-id='competition-event-card-time']/text()").get(),
        #                     'Participant1':Participant1,
        #                     'Participant2':Participant2
        #                 })
        #             except:
        #                 None
        #         else:
        #             continue

        for date in response.xpath("//div[starts-with(@class, 'groupTitleContainerMobile')]"):
            for card in date.xpath(".//following-sibling::ul//li[starts-with(@class, 'cardOuterItem')]"):
                participant=1
                league=card.xpath(".//span[@data-automation-id='competition-name']/text()").get()
                if league not in disallowed_leagues:
                    if card.xpath(".//div[@data-automation-id='multi-market-coupon-event']"):
                        Participant1={'Name':card.xpath(".//div[@data-automation-id='participant-one']/text()").get(), 'Price': card.xpath(".//span[@data-automation-id'price-text'][1]/text()").get()}
                        Participant2={'Name':card.xpath(".//div[@data-automation-id='participant-two']/text()").get(), 'Price': card.xpath(".//span[@data-automation-id'price-text'][2]/text()").get()}
                    else:    
                        for contendor in card.xpath(".//div[starts-with(@class, 'outcomeDetails')]"):
                            if contendor.xpath(".//span[contains(@data-automation-id, 'name')]/text()").get() == None:
                                participant=1
                                Participant1=''
                                continue
                            if participant==1:
                                Participant1={'Name':contendor.xpath(".//span[contains(@data-automation-id, 'name')]/text()").get(), 'Price':contendor.xpath(".//span[@data-automation-id='price-text']/text()").get()}
                                participant+=1
                            elif participant==2:
                                Participant2={'Name':contendor.xpath(".//span[contains(@data-automation-id, 'name')]/text()").get(), 'Price':contendor.xpath(".//span[@data-automation-id='price-text']/text()").get()}
                    
                    try:
                        if Participant1['Name']:
                         if Participant1['Name']!=None:
                            games.append({
                            'Sport':response.xpath('//h1/text()').get(),
                            'League':league,
                            'Date':date.xpath(".//text()").get(),
                            'Time':card.xpath(".//span[@data-automation-id='competition-event-card-time']/text()").get(),
                            'Participant1':Participant1,
                            'Participant2':Participant2
                        })
                    except:
                        None
                else:
                    continue        

        #Might not even need to .sort
        games.sort(key=self.sort_league)

        ## Seperate sport into leagues
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

        ##  Send bets for compare
        for league in league_seperate:
            ## print(league_seperate(f'{league}'))
            if league=='NBA':   ## Basketball - US
                yield response.follow(url='https://www.msn.com/en-au/sport/nba/ladder/sp-s-l', callback=self.parse_Basketball_US, meta={'allbets':league_seperate[f'{league}']})
            elif league=='Australian NBL':  ## Basketball - Aus/Other
                yield response.follow(url=f'https://basketball.draftcentral.com.au/table/{set_year_for_link}-nbl-ladder/', callback=self.parse_Basketball_Australian_NBL, meta={'allbets':league_seperate[f'{league}']})
            elif league=='NRL':  ## Rugby League
                ## Have 'Round 4, Round5' buttons to work with:
                yield response.follow(url='https://www.msn.com/en-au/sport/rugby-league/nrl/ladder', callback=self.parse_Rugby_League_NRL, meta={'allbets':league_seperate[f'{league}']})
            elif league=='AFL':   ## Australian Rules
                yield response.follow(url='https://www.liveladders.com/AFL/no-gaps.html', callback=self.parse_Australian_Rules_AFL, meta={'allbets':league_seperate[f'{league}']})
            elif league=='NFL':   ## American Football, link is year based, starts 10/09/21
                yield response.follow(url=f'https://www.nfl.com/standings/league/{set_year_for_link}/PRE', callback=self.parse_American_Football_NFL, meta={'allbets':league_seperate[f'{league}']})
            elif league=='Argentina La Liga':   ## Basketball - Aus/Other, Argentina La Liga # link year dependant
                yield response.follow(url=f'http://www.pickandroll.com.ar/basquet/adc/liga-argentina/{set_year_for_link-1}-{set_year_for_link}/estadisticas/?opci=acumuladas&modo=puntos', callback=self.parse_Basketball_Argentina_La_Liga, meta={'allbets':league_seperate[f'{league}']})
            elif league=='Australian NBL1':   ## Basketball - Aus/Other
                yield response.follow(url='https://nbl1.com.au/stats/ladder/north/men', callback=self.parse_Basketball_NBL1, meta={'allbets':league_seperate[f'{league}'], 'loop_count': 1, 'group_ladder': []})
            elif league=='Chilean LNB':   ## Basketball - Aus/Other
                yield response.follow(url='https://www.scorespro.com/basketball/chile/lnb/standings/', callback=self.parse_Basketball_Chilean_LNB, meta={'allbets':league_seperate[f'{league}']})
            elif league=='Big3 Basketball Matches': ## Basketball US
                yield response.follow(url='https://www.scorespro.com/basketball/usa/big3-3x3/standings/', callback=self.parse_Basketball_Big3_Basketball_Matches, meta={'allbets':league_seperate[f'{league}']})
            elif league=='New Zealand NBL':   ## Basketball - Aus/Other
                yield response.follow(url='https://www.scorespro.com/basketball/new-zealand/nbl/standings/', callback=self.parse_Basketball_New_Zealand_NBL, meta={'allbets':league_seperate[f'{league}']})
            elif league=='PBA Philippine Cup':   ## Basketball - Aus/Other
                yield response.follow(url='https://www.scorespro.com/basketball/philippines/pba-philippine-cup/standings/', callback=self.parse_Basketball_PBA_Philippine_Cup, meta={'allbets':league_seperate[f'{league}']})
            elif league=='Chinese NBL':   ## Basketball - Aus/Other
                yield response.follow(url='https://www.asia-basket.com/China/basketball-League-NBL.aspx', callback=self.parse_Basketball_Chinese_NBL, meta={'allbets':league_seperate[f'{league}']})
            elif league=='SANFL':  ## Australian Rules
                yield response.follow(url='https://www.scorespro.com/aussie-rules/australia/sanfl/ladder/', callback=self.parse_Australian_SANFL, meta={'allbets':league_seperate[f'{league}']})
            elif league=='Australian Big V':
                yield response.follow(url='https://gameday.bigv.com.au/#ladder', callback=self.parse_Australian_Big_V, meta={'allbets':league_seperate[f'{league}']})

            ## Copy elif stock

            # elif league=='':   ## 
            #     yield response.follow(url='', callback=self.parse_, meta={'allbets':league_seperate[f'{league}']})
            
            else:
                yield (print('** League not inserted: ',  league_seperate[f'{league}'][0]['Sport'] + ', ', league))        
    
    ## Copy def stock

    # def parse_(self, response):
    #     ladder=[]

    #     for team in response.xpath(""):
    #         if team.xpath('').get() =='':
    #             ladder.append('')
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     self.compare(response, , )

    # Basketball - Aus/Other
    def parse_Australian_Big_V(self, response):
        ladder=[]

        for team in response.xpath("//section[@id='ladder']/div/div/div/div/div/div/h5"):
            if team.xpath("normalize-space(.//text())").get() =='Hume':
                ladder.append('Hume City Broadmeadows Broncos')
            elif team.xpath("normalize-space(.//text())").get()=='Wyndham':
                ladder.append('Wyndham Basketball')
            elif team.xpath("normalize-space(.//text())").get()=='Keilor':
                ladder.append('Keilor Thunder')
            elif team.xpath("normalize-space(.//text())").get()=='Sunbury':
                ladder.append('Sunbury Jets')
            elif team.xpath("normalize-space(.//text())").get()=='Casey':
                ladder.append('Casey Cavaliers')
            elif team.xpath("normalize-space(.//text())").get()=='McKinnon':
                ladder.append('McKinnon Cougars')
            elif team.xpath("normalize-space(.//text())").get()=='Chelsea':
                ladder.append('Chelsea Gulls')
            elif team.xpath("normalize-space(.//text())").get()=='Hawthorn':
                ladder.append('Hawthorn Magic')
            elif team.xpath("normalize-space(.//text())").get()=='Blackburn':
                ladder.append('Blackburn Vikings')
            else:
                 ladder.append(team)

        response.request.meta['ladder']=ladder
        self.compare(response, 1, 9)
    
    # Australian Rules
    def parse_Australian_SANFL(self, response):
        ladder=[]

        for team in response.xpath("(//table[@class='sp-livetable__table']/tbody)[1]/tr[position()>1]/td[3]/div/div/div/a/text()").getall():
            if team =='':
                ladder.append('')
            else:
                 ladder.append(team)

        print(ladder)
        response.request.meta['ladder']=ladder
        self.compare(response, 1, 9)

    # Basketball - Aus/Other
    def parse_Basketball_Chinese_NBL(self, response):
        ladder=[]

        for team in response.xpath("//div[@class='standingdetails']/div/div/a/text()").getall():
            if team =='Guangxi':
                ladder.append('Guangxi Weizhuang')
            elif team =='Henan':
                ladder.append('Henan Shedian Laojiu')
            elif team =='Xinjiang':
                ladder.append('Xinjiang Tianshan Eagle')
            elif team =='Wuhan':
                ladder.append('Wuhan Dangdai')
            elif team =='Anhui P.':
                ladder.append('Putian Xingfa')
            elif team =='Jiangsu YS':
                ladder.append('Jiangsu Yannan Suke')
            elif team =='Hunan':
                ladder.append('Hunan Jinjian Miye')
            elif team=='Shaanxi':
                ladder.append('Shaanxi Xinda')
            else:
                 ladder.append(team)

        response.request.meta['ladder']=ladder
        self.compare(response, 1, 12)
    
    # Basketball - Aus/Other
    def parse_Basketball_PBA_Philippine_Cup(self, response):
        ladder=[]

        for team in response.xpath("(//table/tbody)[1]/tr/td[3]/div/div/div/a/text()").getall():
            if team =='Ginebra Kings':
                ladder.append('Barangay Ginebra San Miguel')
            elif team =='Blackwater Elite':
                ladder.append('Blackwater Bossing')
            elif team =='Nlex Road Warriors':
                ladder.append('NLEX Road Warriors')
            elif team =='Rain Or Shine Paint.':
                ladder.append('Rain Or Shine Elasto Painters')
            elif team =='Global Port':
                ladder.append('NorthPort Batang Pier')
            elif team =='B-Meg Llamados':
                ladder.append('Magnolia Hotshots Pambansang Manok')
            elif team=='Barako EC Masters':
                ladder.append('Phoenix Super LPG Fuel Masters')
            elif team=='Columbian Dyip':
                ladder.append('Terrafirma Dyip')
            elif team=="Talk 'N Text Tropang Texters":
                ladder.append('TnT Tropang Giga')
            else:
                 ladder.append(team)

        response.request.meta['ladder']=ladder
        self.compare(response, 1, 9)

    # Basketball - Aus/Other
    def parse_Basketball_New_Zealand_NBL(self, response):
        ladder=[]

        for team in response.xpath("(//table/tbody)[1]/tr/td[3]/div/div/div/a/text()").getall():
            if team =='Bay Hawks':
                ladder.append('Taylor Hawks')
            else:
                 ladder.append(team)
        
        response.request.meta['ladder']=ladder
        self.compare(response, 1, 9)

    # Basketball US
    # Dissapeared quick
    def parse_Basketball_Big3_Basketball_Matches(self, response):
        ladder=[]

        # Check if xPath /tbody works
        for team in response.xpath("(//table/tbody)[1]/tr/td[3]/div/div/div/a/text()").getall():
            if team =='':
                ladder.append('')
            else:
                 ladder.append(team)
        
        print(ladder)
        response.request.meta['ladder']=ladder
        self.compare(response, 1, 9)
    
    # Basketball - Aus/Other
    def parse_Basketball_Chilean_LNB(self, response):
        ladder=[]

        # Check if xPath /tbody work
        for team in response.xpath("(//table/tbody)[1]/tr[@class='sp-livetable__tableRow spm-dataRow']/td[3]/div/div/div/a/text()").getall():
            if team =='Quilicura':
                ladder.append('CD Quilicura Basket')
            elif team == 'Leones Quilpue':
                ladder.append('Colegio Los Leones')
            elif team =='Deportivo Valdivia':
                ladder.append('C. D. Deportes Valdivia')
            elif team =='Temuco':
                ladder.append('C.D. AB Temuco')
            elif team=='Espanol De Talca':
                ladder.append('C. D. Espanol de Talca')
            elif team=='U. De Concepcion':
                ladder.append('Universidad de Concepcion')
            elif team=='Catolica':
                ladder.append('Club Deportivo Universidad Catolica')
            elif team=='Las Animas':
                ladder.append('C. D. Las Animas')
            elif team=='CD Puerto Varas':
                ladder.append('CD Atletico PTO. Varas')
            else:
                 ladder.append(team)
        
        response.request.meta['ladder']=ladder
        self.compare(response, 1, 9)

    ## Basketball - Aus/Other
    def parse_Basketball_NBL1(self, response):
        group_ladder=response.request.meta['group_ladder']
        ladder=[]
        loop_count=response.request.meta['loop_count']
        for team in response.xpath('//tbody/tr/'):
            if team.xpath('.//th/div/span/text()').get() =='':
                ladder.append({'Name': '', 'W': team.xpath('.//td[3]/text()').get()})
            else:
                ladder.append(team.xpath('.//text()').get())
        
        group_ladder.append(ladder)

        while loop_count<=4:
            if loop_count==1:
                yield response.follow(url='https://nbl1.com.au/stats/ladder/south/men', callback=self.parse_Basketball_NBL1, meta={'allbets': response.request.meta['allbets'], 'group_ladder': group_ladder, 'loop_count': loop_count+1})
            if loop_count==2:
                yield response.follow(url='https://nbl1.com.au/stats/ladder/central/men', callback=self.parse_Basketball_NBL1, meta={'allbets': response.request.meta['allbets'], 'group_ladder': group_ladder, 'loop_count': loop_count+1})
            if loop_count==3:
                yield response.follow(url='https://nbl1.com.au/stats/ladder/west/men', callback=self.parse_Basketball_NBL1, meta={'allbets': response.request.meta['allbets'], 'group_ladder': group_ladder, 'loop_count': loop_count+1})
            if loop_count==4:
                print()
                #print(group_ladder)
                #print(response.request.meta['allbets'])
                print()
                self.Basketball_NBL1_evaluate(self, response, group_ladder)
    
    # For def parse_Basketball_NBL1 only:
    def Basketball_NBL1_evaluate(self, response, ladder):
        print()
        print(ladder)

        sorted_ladder=[]
        for team in sorted(ladder, key=lambda x: x['W'], reverse=True):
            sorted_ladder.append(team['Name'])

        response.request.meta['ladder']=sorted_ladder
        yield self.compare(response, 9, 47)
        
        # for game in response.request.meta['allbets']:
        #     for district in ladder:
        #         if district.index(game['Participant1']['Name'])<2:
        #             if district.index(game['Participant2']['Name'])>11:
        #                 yield game
        #         elif district.index(game['Participant1']['Name'])>11:
        #             if district.index(game['Participant2']['Name'])<2:
        #                 yield game

    ## Basketball - Aus/Other
    def parse_Basketball_Argentina_La_Liga(self, response):
        ladder=[]

        for team in response.xpath("//tr[position()>2]/td[3]/p/text()").getall():
            if team =='Atenas (Patagones)':
                ladder.append('Atenas')
            elif team == 'Racing Chivilcoy':
                ladder.append('Racing de Chivilcoy')
            elif team == 'Colón (Santa Fe)':
                ladder.append('Colon Santa Fe')
            elif team == 'Sportivo América':
                ladder.append('Sportivo America')
            elif team == 'San Isidro (San Francisco)':
                ladder.append('San Isidro')
            elif team == 'Villa San Martín':
                ladder.append('Club Atletico Villa San Martin')
            elif team == 'Del Progreso':
                ladder.append('Club Del Progreso')
            elif team == 'Lanús':
                ladder.append('Club Atletico Lanus')
            elif team == 'Gimnasia y Esgrima (La Plata)':
                ladder.append('Gimnasia y Esgrima La Plata')
            elif team == 'Echagüe (Paraná)':
                ladder.append('Echague')
            elif team == 'Unión (Santa Fe)':
                ladder.append('Union De Santa Fe')
            elif team == 'Independiente BBC':
                ladder.append('Independiente Santiago Del Estero')
            elif team == 'Estudiantes (Tucumán)':
                ladder.append('Club Atletico Estudiantes de Tucuman')
            elif team == 'Quilmes (Mar del Plata)':
                ladder.append('Club Atletico Quilmes')
            elif team == 'Villa Mitre':
                ladder.append('Club Villa Mitre de Bahia Blanca')
            else:
                ladder.append(team)

        response.request.meta['ladder']=ladder
        self.compare(response, 5, 22)
        
        # for game in response.request.meta['allbets']:
        #     if ladder.index(game['Participant1']['Name'])<5:
        #         if ladder.index(game['Participant2']['Name'])>22:
        #             yield game
        #     elif ladder.index(game['Participant1']['Name'])>22:
        #         if ladder.index(game['Participant2']['Name'])<5:
        #             yield game

    ## American Football
    def parse_American_Football_NFL(self, response):
        ladder=[]

        print('** Starts 10/09/21 American Footbal NFL')

        for team in response.xpath("//div[@class='d3-o-club-fullname']").getall():
            #if team =='':
            ladder.append(team)
        
        response.request.meta['ladder']=ladder
        yield self.compare(response, 9, 22)

        # for game in response.request.meta['allbets']:
        #     if ladder.index(game['Participant1']['Name'])<9:
        #         if ladder.index(game['Participant2']['Name'])>22:
        #             yield game
        #     elif ladder.index(game['Participant1']['Name'])>22:
        #         if ladder.index(game['Participant2']['Name'])<9:
        #             yield game

    ## Australian Rules
    def parse_Australian_Rules_AFL(self, response):
        ladder=[]

        for team in response.xpath("//tr/td[@rowspan='1'][2]/text()").getall():
            if team =='WC Eagles':
                ladder.append('West Coast')
            elif team =='Port Adel':
                ladder.append('Port Adelaide')
            elif team =='North Melb':
                ladder.append('North Melbourne')
            elif team =='GWS Giants':
                ladder.append('Greater Western Sydney')
            elif team =='W Bulldogs':
                ladder.append('Western Bulldogs')
            else:
                ladder.append(team)

        response.request.meta['ladder']=ladder
        yield self.compare(response, 4, 14)
        
    ## Rugby League
    def parse_Rugby_League_NRL(self, response):
        ## From 1/05 will have played everyone once
        ladder=[]

        ## Found xpath to have changed once
        ## XPath changed again and structure of ladder bounced from acronyms to full name and back under ladder tab
        
        #print(response.body)
        for competitor in response.xpath("//tr[position()>1]/td[3]/child::node()[@class='b_promtxt']"):
            team=competitor.xpath("normalize-space(.//text())").get()
            if team == ('SGI' or 'St. George Illawarra Dragons'):
                ladder.append('St George Illawarra Dragons')
            elif team == ('CSS' or 'Cronulla-Sutherland Sharks'):
                ladder.append('Cronulla Sharks')
            elif team == ('NQU' or 'North Queensland Cowboys'):
                ladder.append('Nth Queensland Cowboys')
            elif team == ('CBB' or 'Canterbury-Bankstown Bulldogs'):
                ladder.append('Canterbury Bulldogs')
            elif team == ('MAN' or 'Manly-Warringah Sea Eagles'):
                ladder.append('Manly Sea Eagles')
            elif team == 'MBS':
                ladder.append('Melbourne Storm')
            elif team == 'PEN':
                ladder.append('Penrith Panthers')
            elif team == 'SSY':
                ladder.append('South Sydney Rabbitohs')
            elif team == 'PAR':
                ladder.append('Parramatta Eels')
            elif team == 'SYD':
                ladder.append('Sydney Roosters')
            elif team == 'CBR':
                ladder.append('Canberra Raiders')
            elif team == 'WAR':
                ladder.append('New Zealand Warriors')
            elif team == 'NEW':
                ladder.append('Newcastle Knights')
            elif team == 'GCO':
                ladder.append('Gold Coast Titans')
            elif team == 'WTG':
                ladder.append('Wests Tigers')
            elif team == 'BRI':
                ladder.append('Brisbane Broncos')
            # elif team == '':
            #     ladder.append('')
            else:
                ladder.append(team)

        #print(ladder)

        response.request.meta['ladder']=ladder
        yield self.compare(response, 3, 12)   

        # for game in response.request.meta['allbets']:
        #     if ladder.index(game['Participant1']['Name'])<3:
        #         if ladder.index(game['Participant2']['Name'])>12:
        #             yield ('Bet'), game
        #     elif ladder.index(game['Participant1']['Name'])>12:
        #         if ladder.index(game['Participant2']['Name'])<3:
        #             yield ('Bet'), game

    ## Basketball - US
    def parse_Basketball_US(self, response):
        ## Good to go I believe
        ladder=[]

        for team in response.xpath("//tbody/tr/td/a/text()").getall():
                ladder.append(team)

        try:
            ladder[0]
        except:
            yield response.follow(url='https://www.msn.com/en-au/sport/nba/teams', callback=self.parse_Basketball_US_backup, meta={'allbets':response.request.meta['allbets']})
        else:
            print(ladder)

            response.request.meta['ladder']=ladder
            yield self.compare(response, 5, 23)

        # for game in response.request.meta['allbets']:
        #     if ladder.index(game['Participant1']['Name'])<5:
        #         if ladder.index(game['Participant2']['Name'])>23:
        #             yield game
        #     elif ladder.index(game['Participant1']['Name'])>23:
        #         if ladder.index(game['Participant2']['Name'])<5:
        #             yield game

    def parse_Basketball_US_backup(self, response):
        ladder={}
        list=response.xpath("//tr/td[2]/div/div/text()").getall()

        for info in list:
            info=info.replace('\n', '')
            if info.replace(' ', '').isalpha():
                if info=='Suns':
                    name='Phoenix Suns'
                elif info=='Bucks':
                    name='Milwaukee Bucks'
                else:
                    name=info
            elif info=='76ers':
                name='76ers'
            else:
                temp=[]
                pos=info.index('-')
                info.strip()
                for added in ladder:
                    temp.append(added)
                temp.append({'Name': name,'W':info[:pos], 'L':info[pos+1:]})
                ladder=temp

        sorted_ladder=[]
        for team in sorted(ladder, key=lambda x: x['W'], reverse=True):
            sorted_ladder.append(team['Name'])

        response.request.meta['ladder']=sorted_ladder
        yield self.compare(response, 5, 23)

    ## Basketball - Aus/Other
    def parse_Basketball_Australian_NBL(self, response):
        ladder=[]

        ## Still reads all 3 tables on site (Might be done now)
        for team in response.xpath("(//div[@id='DataTables_Table_0_wrapper']/table/tbody/tr/td[@class='data-name has-logo']/a"):
            print(team)
            if team.xpath(".//text()").get() == 'Melbourne':
                ladder.append('Melbourne United')
            elif team.xpath(".//text()").get() == 'Perth':
                ladder.append('Perth Wildcats')
            elif team.xpath(".//text()").get() == 'SE Melbourne':
                ladder.append('South East Melbourne Phoenix')
            elif team.xpath(".//text()").get() == 'Sydney':
                ladder.append('Sydney Kings')
            elif team.xpath(".//text()").get() == 'Hawks':
                ladder.append('The Hawks')
            elif team.xpath(".//text()").get() == 'Brisbane':
                ladder.append('Brisbane Bullets')
            elif team.xpath(".//text()").get() == 'Adelaide':
                ladder.append('Adelaide 36ers')
            elif team.xpath(".//text()").get() == 'New Zealand':
                ladder.append('New Zealand Breakers')
            elif team.xpath(".//text()").get() == 'Cairns':
                ladder.append('Cairns Taipans')

        response.request.meta['ladder']=ladder
        yield self.compare(response, 5, 23)

        # for game in response.request.meta['allbets']:
        #     if ladder.index(game['Participant1']['Name'])<5:
        #         if ladder.index(game['Participant2']['Name'])>23:
        #             yield game
        #     elif ladder.index(game['Participant1']['Name'])>23:
        #         if ladder.index(game['Participant2']['Name'])<5:
        #             yield game

    ## Calculative
    def sort_league(self, games):
        return games['League']

    def compare(self, response, high, low):

        print('### Entering: ', response.request.meta['allbets'][0]['Sport']+',', response.request.meta['allbets'][0]['League'])

        #print (response.request.meta['allbets'])
        #print (response.request.meta['ladder'])
        try:
            response.request.meta['ladder'][0]
        except:
            print('* ', response.request.meta['allbets'][0]['League'], 'ladder unaffirmed')
        else:
            for game in response.request.meta['allbets']:
                if response.request.meta['ladder'].index(game['Participant1']['Name'])<high:
                    if response.request.meta['ladder'].index(game['Participant2']['Name'])>low:
                        print(game)
                elif response.request.meta['ladder'].index(game['Participant1']['Name'])>low:
                    if response.request.meta['ladder'].index(game['Participant2']['Name'])<high:
                        print(game)

        # print(response.request.meta['League'], 'unaffirmed')
        
        return None