# -*- coding: utf-8 -*-
import scrapy


class SportsbetSpider(scrapy.Spider):
    name = 'sportsbet'
    allowed_domains = ['www.sportsbet.com.au', 'afltables.com', 'www.msn.com','basketball.draftcentral.com.au']
    start_urls = ['https://www.sportsbet.com.au/betting/basketball-us/nba','https://www.sportsbet.com.au/betting/rugby-league/nrl']
    # 'https://www.sportsbet.com.au/betting/basketball-aus-other/australian-nbl'

    def parse(self, response):
        games=[]

        ## Trying to read href to have the right league go through to statistics
        print(response.xpath("//head/link[@data-automation-id='canonical']/@href").get())
        if response.xpath("//base/@href").get()=='https://www.sportsbet.com.au/betting/basketball-us/nba':
            print('Pulled')
            league='Basketball - US'
        elif response.xpath("//head/base[@href='https://www.sportsbet.com.au/betting/basketball-aus-other/australian-nbl']") == True:
            league='Australian NBL'
        elif response.xpath("//head/base[@href='https://www.sportsbet.com.au/betting/rugby-league/nrl']") == True:
            league='Rugby League - NRL'

        for a in response.xpath("//div[starts-with(@class, 'groupTitleContainerMobile')]"):
            ## Date
            for b in a.xpath(".//following-sibling::ul//li[starts-with(@class, 'cardOuterItem')]"):
                ## Time
                participant=1
                for c in b.xpath(".//div[starts-with(@class, 'outcomeDetails')]"):
                    ## Button
                    if participant==1:
                        Participant1={'Name':c.xpath(".//span[contains(@data-automation-id, 'captioned-outcome-name')]/text()").get(), 'Price':c.xpath(".//span[contains(@data-automation-id, 'price-text')]/text()").get()}
                        participant+=1
                    elif participant==2:
                        Participant2={'Name':c.xpath(".//span[contains(@data-automation-id, 'captioned-outcome-name')]/text()").get(), 'Price':c.xpath(".//span[contains(@data-automation-id, 'price-text')]/text()").get()}
               ## Got it
                games.append({
                    'Sport': response.xpath('//h1/text()').get(),
                    'Date':a.xpath(".//text()").get(),
                    'Time':b.xpath(".//text()").get(),
                    'Participant1':Participant1,
                    'Participant2':Participant2
                })

        #print(games[0]['Sport'])

        ## yield response.follow(url='https://afltables.com/afl/seas/2021.html', callback=self.parse_AFLladder, meta={'ladder':standing})
        ## Once names change, correct the names here
        if games[0]['Sport']=='Basketball - US':
            yield response.follow(url='https://www.msn.com/en-us/sports/nba/standings/sp-vw-lge', callback=self.parse_Basketball_US, meta={'allbets':games})
        elif games[0]['Sport']=='Basketball - Aus/Other':
            yield response.follow(url='https://basketball.draftcentral.com.au/table/2021-nbl-ladder/', callback=self.parse_Basketball_Australian_NBL, meta={'allbets':games})
        elif games[0]['Sport']=='Rugby League':
            ## Have 'Round 4, Round5' buttons to work with:
            yield response.follow(url='https://www.msn.com/en-au/sport/rugby-league/nrl/ladder/sp-s-r', callback=self.parse_Rugby_League, meta={'allbets':games})
        #games=response.xpath("//h2/span/text()").getall()
        ##bet=response.xpath("//span[@data-automation-id='price-text']/text()").getall()

        ##rounds={'title':title, 'dates':dates, 'games':games, 'bets':bet}
        ##print(rounds)
    
    def parse_Rugby_League(self, response):
        ## Still Early in season, (building at round 4), Working
        bets=response.request.meta['allbets']
        ladder=[]

        for a in response.xpath("//tr/td[@class='shortteamname']"):
            if a.xpath('.//text()').get() == 'PEN':
                ladder.append('Penrith Panthers')
            elif a.xpath('.//text()').get() == 'PAR':
                ladder.append('Parramatta Eels')
            elif a.xpath('.//text()').get() == 'SYD':
                ladder.append('Sydney Roosters')
            elif a.xpath('.//text()').get() == 'SOU':
                ladder.append('South Sydney Rabbitohs')
            elif a.xpath('.//text()').get() == 'CBR':
                ladder.append('Canberra Raiders')
            elif a.xpath('.//text()').get() == 'STI':
                ladder.append('St George Illawarra Dragons')
            elif a.xpath('.//text()').get() == 'MEL':
                ladder.append('Melbourne Storm')
            elif a.xpath('.//text()').get() == 'CRO':
                ladder.append('Cronulla Sharks')
            elif a.xpath('.//text()').get() == 'GLD':
                ladder.append('Gold Coast Titans')
            elif a.xpath('.//text()').get() == 'NEW':
                ladder.append('Newcastle Knights')
            elif a.xpath('.//text()').get() == 'WAR':
                ladder.append('New Zealand Warriors')
            elif a.xpath('.//text()').get() == 'BRI':
                ladder.append('Brisbane Broncos')
            elif a.xpath('.//text()').get() == 'WST':
                ladder.append('Wests Tigers')
            elif a.xpath('.//text()').get() == 'NQL':
                ladder.append('Nth Queensland Cowboys')
            elif a.xpath('.//text()').get() == 'CBY':
                ladder.append('Canterbury Bulldogs')
            elif a.xpath('.//text()').get() == 'MAN':
                ladder.append('Manly Sea Eagles')

        for game in bets:
            if ladder.index(game['Participant1']['Name'])<3:
                if ladder.index(game['Participant2']['Name'])>12:
                    yield ('Bet'), game
                    print()
            elif ladder.index(game['Participant1']['Name'])>12:
                if ladder.index(game['Participant2']['Name'])<3:
                    yield ('Bet'), game
                    print()

    def parse_AFLladder(self, response):
        ## Early in the season
        standing=response.request.meta['allbets']
        print('worked')

    def parse_Basketball_US(self, response):
        ## Good to go I believe
        bets=response.request.meta['allbets']
        ladder=[]

        print('_US')

        for a in response.xpath("//tr[@class='rowlink']/td[@class='teamname']"):
            ladder.append(a.xpath('.//text()').get())

        #response.follow(callback=self.compare(bets=bets, ladder=ladder, high=5, low=23))
        for game in bets:
            if ladder.index(game['Participant1']['Name'])<5:
                if ladder.index(game['Participant2']['Name'])>23:
                    yield game
                    print()
            elif ladder.index(game['Participant1']['Name'])>23:
                if ladder.index(game['Participant2']['Name'])<5:
                    yield game
                    print()
        print('Did response, now self')
        #self.compare(ladder=ladder, high=5, low=23)

    def parse_Basketball_Australian_NBL(self, response):
        bets=response.request.meta['allbets']
        ladder=[]

        ## Still reads all 3 tables on site
        for a in response.xpath("(//table[@class='sp-league-table sp-data-table sp-sortable-table sp-scrollable-table sp-paginated-table'][1]/tbody)[1]/tr/td[@class='data-name has-logo']/a"):
            if a.xpath('.//text()').get() == 'Melbourne':
                ladder.append('Melbourne United')
            elif a.xpath('.//text()').get() == 'Perth':
                ladder.append('Perth Wildcats')
            elif a.xpath('.//text()').get() == 'SE Melbourne':
                ladder.append('South East Melbourne Phoenix')
            elif a.xpath('.//text()').get() == 'Sydney':
                ladder.append('Sydney Kings')
            elif a.xpath('.//text()').get() == 'Hawks':
                ladder.append('The Hawks')
            elif a.xpath('.//text()').get() == 'Brisbane':
                ladder.append('Brisbane Bullets')
            elif a.xpath('.//text()').get() == 'Adelaide':
                ladder.append('Adelaide 36ers')
            elif a.xpath('.//text()').get() == 'New Zealand':
                ladder.append('New Zealand Breakers')
            elif a.xpath('.//text()').get() == 'Cairns':
                ladder.append('Cairns Taipans')
            
        #print(ladder)

        self.compare(ladder=ladder, high=5, low=23)

        for game in bets:
            if ladder.index(game['Participant1']['Name'])<5:
                if ladder.index(game['Participant2']['Name'])>23:
                    yield game
                    print()
            elif ladder.index(game['Participant1']['Name'])>23:
                if ladder.index(game['Participant2']['Name'])<5:
                    yield game
                    print()

    def compare(self, response, bets, ladder, high, low):
        print('entered')
        for game in bets:
            if ladder.index(game['Participant1']['Name'])<high:
                if ladder.index(game['Participant2']['Name'])>low:
                    yield game
                    print()
            elif ladder.index(game['Participant1']['Name'])>low:
                if ladder.index(game['Participant2']['Name'])<high:
                    yield game
                    print()