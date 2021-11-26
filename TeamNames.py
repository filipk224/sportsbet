import Calculative

    # # #Copy def parse stock

    # # def parse_(self, response):
    # #     ladder=[]

    # #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    # #         if team == '':
    # #             ladder.append('')
    # #         else:
    # #              ladder.append(team)

    # #     print(ladder)
    # #     response.request.meta['ladder']=ladder
    # #     Calculative.compare(response, , )

class Cricket():

    def parse_Cricket_WBBL(self, response):
        ladder = []

        for team in response.xpath("(//table)[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Brisbane Heat W':
                ladder.append('Brisbane Heat WBBL')
            elif team == 'Perth Scorchers W':
                ladder.append('Perth Scorchers WBBL')
            elif team == 'Adelaide Strikers W':
                ladder.append('Adelaide Strikers WBBL')
            else:
                ladder.append(team)

        #print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 7)

class Handball():

    def parse_Handball_Swedish_Elitserien_Men(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Aranas':
                ladder.append('HK Aranas')
            elif team == 'Onnereds':
                ladder.append('Onnereds HK')
            elif team == 'Skjern':
                ladder.append('Skjern Haandbold')
            elif team == 'Hammarby':
                ladder.append('Hammarby HB')
            elif team == 'Lugi':
                ladder.append('Lugi HF')
            elif team == 'Alingsas':
                ladder.append('Alingsaas HK')
            elif team == 'Malmo':
                ladder.append('HK Malmo')
            elif team == 'Eskilstuna Guif':
                ladder.append('IF Guif')
            else:
                ladder.append(team)

        #print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 12)

    def parse_Handball_Spanish_ASOBAL_League(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Puente Genil':
                ladder.append('BM Puente Genil')
            elif team == 'Atletico Valladolid':
                ladder.append('BM Atletico Valladolid')
            elif team == 'Barcelona':
                ladder.append('FC Barcelona')
            elif team == 'Antequera':
                ladder.append('BM Antequera')
            elif team == 'Huesca':
                ladder.append('BM Huesca')
            elif team == 'Torrelavega':
                ladder.append('BM Torrelavega')
            elif team == 'Morrazo Cangas':
                ladder.append('CB Cangas')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 3, 14)

    def parse_Handball_Norwegian_League_Men(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Fjellhammer':
                ladder.append('Fjellhammer IL')
            elif team == 'Kolstad':
                ladder.append('Kolstad Handball')
            else:
                ladder.append(team)

        #print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 12)

    def parse_Handball_German_Bundesliga(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Bergischer':
                ladder.append('Bergischer HC')
            elif team == 'Erlangen':
                ladder.append('HC Erlangen')
            elif team == 'Balingen/Weilstetten':
                ladder.append('HBW Balingen-Weilstetten')
            elif team == 'Frisch Auf Goppingen':
                ladder.append('FRISCH AUF! Goppingen')
            elif team == 'TuS N-Lubbecke':
                ladder.append('TUS N-Lubbecke')
            elif team == 'Lemgo':
                ladder.append('TBV Lemgo Lippe')
            elif team == 'Kiel':
                ladder.append('THW Kiel')
            elif team == 'Leipzig':
                ladder.append('SC DHfK Leipzig')
            else:
                ladder.append(team)

        #print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 15)

    def parse_Handball_French_Div1_Men(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Cesson':
                ladder.append('Cesson Rennes Metropole HB')
            elif team == 'Saran':
                ladder.append('Saran Loiret Handball')
            elif team == 'Dunkerque':
                ladder.append('Dunkerque HB')
            elif team == 'Nantes':
                ladder.append('HBC Nantes')
            elif team == 'Creteil':
                ladder.append('US Creteil Handball')
            elif team == 'Nancy':
                ladder.append('Grand Nancy Metropole HB')
            elif team == 'Istres':
                ladder.append('Istres Ouest Provence')
            elif team == 'Montpellier HB':
                ladder.append('Montpellier Handball')
            elif team == 'Limoges':
                ladder.append('Limoges Handball')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 14)

    def parse_Handball_Danish_League_Men(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Skanderborg':
                ladder.append('Skanderborg-Aarhus Haandbold')
            elif team == 'Skjern':
                ladder.append('Skjern Haandbold')
            elif team == 'Kolding':
                ladder.append('KIF Kolding')
            elif team == 'Skive':
                ladder.append('Skive FH')
            elif team == 'Holstebro':
                ladder.append('Tth Holstebro')
            elif team == 'Aalborg Handbold':
                ladder.append('Aalborg Haandbold')
            elif team == 'GOG Handball':
                ladder.append('GOG Handbold')
            elif team == 'Sonderjyske':
                ladder.append('Soenderjyske HK')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 13)

class Basketball_AusOther():

    def parse_Basketball_Italian_Serie_A2(self, response):
        ladder = {}

        for team in response.xpath("//div[@class='sp-livetable__wrap']/table[1]/tbody/tr[position()>1]"):
            # ext=team.xpath('.//tbody/tr[position()>1]')
            name = team.xpath('.//td[@title=""]/div/div/div/a/text()').get()
            if name == 'Urania Basket Milano':
                name = 'Urania Milano'

            temp = []
            for added in ladder:
                temp.append(added)
            temp.append({'Name': name, 'W':team.xpath('.//td[@title="win"]/div/text()').get(), 'L':team.xpath('.//td[@title="loss"]/div/text()').get()})
            ladder = temp

        sorted_ladder = []
        for team in sorted(ladder, key=lambda x: int(x['W']), reverse=True):
            sorted_ladder.append(team['Name'])

        # print(sorted_ladder)
        response.request.meta['ladder'] = sorted_ladder
        yield Calculative.compare(response, 4, 23)

    def parse_Basketball_Greek_A1(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Olympiacos':
                ladder.append('Olympiacos BC')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 11)

    def parse_Basketball_Swedish_Ligan(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 8)

    def parse_Basketball_Romanian_Liga_Nationala(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 15)

    def parse_Basketball_Korean_WKBL(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Shinhan S-Birds W':
                ladder.append("Shinhan Bank S'Birds Women")
            elif team == 'KB Stars W':
                ladder.append('Cheongju KB Stars Women')
            elif team == 'Hansae W':
                ladder.append('Asan Woori Bank Wibee Women')
            elif team == 'KDB L. Winnus W':
                ladder.append('Busan BNK Sum Women')
            else:
                ladder.append(team)

        #print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 5)

    def parse_Basketball_German_BBL(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 15)

    def parse_Basketball_French_ProA_League(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 15)

    def parse_Basketball_British_BBL_Championship(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 9)

    def parse_Basketball_Brazilian_NBB(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 14)

    def parse_Rugby_Union_AIL_Division_1A(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 9)

    def parse_Basketball_Israeli_National_League(self, response):
        ladder = []

        # Don't think is the right standing.
        for team in response.xpath("(//div[@class='sp-livetable__wrap']/table)[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 11)

    def parse_Basketball_Hungarian_A_Division(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 12)

    def parse_Basketball_EuroCup(self, response):
        # Watch for this one on how it results
        ladder = []
        allbets = response.request.meta['allbets']

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # Group A Split
        response.request.meta['ladder'] = ladder[0:9]
        response.request.meta['allbets'] = allbets[0:9]

        for team in response.request.meta['allbets']:
            team['Group'] = 'A'

        # print(ladder[0:9])
        Calculative.compare(response, 1, 9)

        # Group B Split
        response.request.meta['ladder'] = ladder[10:19]
        response.request.meta['allbets'] = allbets[10:19]

        for team in response.request.meta['allbets']:
            team['Group'] = 'B'

        # print(ladder[10:19])
        Calculative.compare(response, 1, 9)

    def parse_Basketball_Czech_ZBL(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Chance U19 W':
                ladder.append('BK Strakonice Chance Women U19')
            else:
                ladder.append(team)

        #print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 9)

    def parse_Basketball_Cyprus_League(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 10)

    def parse_Basketball_Bulgarian_NBL(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 8)

    def parse_Basketball_Spanish_LEB_Oro(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'CB Valladolid':
                ladder.append('CB Ciudad de Valladolid')
            elif team == 'Amics Castello':
                ladder.append('TAU Castello')
            elif team == 'Caceres':
                ladder.append('Caceres Patrimonio de la Humanidad')
            elif team == 'Penas Huesca':
                ladder.append('Levitec Huesca')
            elif team == 'Palencia':
                ladder.append('Chocolates Trapa Palencia')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 15)

    def parse_Basketball_Spanish_ACB(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 15)

    def parse_Basketball_Russian_Super_League(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 12)

    def parse_Basketball_Norway_BLNO(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Froeya':
                ladder.append('Froya')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 9)

    def parse_Basketball_Latvian_Estonian_League(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'BC Tartu':
                ladder.append('Tartu Ulikool')
            elif team == 'Tallinna Kalev':
                ladder.append('Tallinna Kalev/TLU')
            elif team == 'Rakvere Tarvas':
                ladder.append('BC Rakvere Tarvas')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 11)

    def parse_Basketball_Japanese_B_League_1(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 19)

    def parse_Basketball_French_ProB_League(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Evreux':
                ladder.append('ALM Evreux Basket')
            elif team == 'Denain':
                ladder.append('Denain Voltaire')
            elif team == 'Nantes':
                ladder.append('Hermine De Nantes')
            elif team == 'Lille Mb':
                ladder.append('Lille Metropole')
            elif team == 'Antibes':
                ladder.append('Antibes Sharks')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 16)

    def parse_Basketball_Chinese_CBA(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 17)

    def parse_Basketball_Finnish_Korisliiga(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Salon Vilpas':
                ladder.append('Salon Vilpas Vikings')
            elif team == 'Lapuan Korikobrat':
                ladder.append('Kobrat Lapua')
            elif team == 'Kataja':
                ladder.append('Kataja Basket')
            elif team == 'Namika Lahti':
                ladder.append('Lahti Basketball')
            elif team == 'Loimaa Bisons':
                ladder.append('LoKoKo Bisons')
            elif team == 'KTP Basket':
                ladder.append('KTP Basket Kotka')
            elif team == 'Pyrinto':
                ladder.append('Tampereen Pyrinto')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 10)

    def parse_Basketball_Czech_NBL(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Opava':
                ladder.append('BK Opava')
            elif team == 'Pardubice':
                ladder.append('BK JIP Pardubice')
            elif team == 'CEZ Nymburk':
                ladder.append('ERA Nymburk')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 10)

    def parse_Basketball_FIBA_Eurocup_Women(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 15, 15)

    def parse_Basketball_EuroLeague(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Crvena Zvezda':
                ladder.append('Crvena Zvezda MTS Belgrade')
            elif team == 'Alba Berlin':
                ladder.append('ALBA Berlin')
            elif team == 'Panathinaikos':
                ladder.append('Panathinaikos OPAP Athens')
            elif team == 'Unics Kazan':
                ladder.append('UNICS Kazan')
            elif team == 'Barcelona':
                ladder.append('FC Barcelona')
            elif team == 'Baskonia':
                ladder.append('TD Systems Baskonia Vitoria Gasteiz')
            elif team == 'Zenit Petersburg':
                ladder.append('Zenit Saint-Petersburg')
            elif team == 'Fenerbahce Ulker':
                ladder.append('Fenerbahce BEKO')
            elif team == 'Monaco':
                ladder.append('AS Monaco Basket')
            elif team == 'Anadolu Efes SK':
                ladder.append('Anadolu Efes')
            elif team == 'Zalgiris Kaunas':
                ladder.append('BC Zalgiris')
            elif team == 'Olympiacos':
                ladder.append('Olympiacos BC')
            elif team == 'ASVEL':
                ladder.append('LDLC ASVEL Lyon-Villeurbanne')
            elif team == 'Maccabi Tel Aviv':
                ladder.append('Maccabi Playtika Tel Aviv')
            elif team == 'Olimpia Milano':
                ladder.append('AX Armani Exchange Olimpia Milan')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 15)

    def parse_Basketball_Danish_Basket_Ligaen(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Bakken Bears':
                ladder.append('Bears Academy')
            elif team == 'Randers':
                ladder.append('Randers Cimbria')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 9)

    def parse_Baskebtall_Bahraini_Premier_League(self, response):
        ladder = []

        for team in response.xpath("//div[@class='standingdetails']/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 10)

    def parse_Baskebtall_BNXT_League(self, response):
        ladder = []

        for team in response.xpath("//table/tbody/tr/td/a/span[1]/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 10)

    def parse_Basketball_Argentinian_Super_20(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 3)

    def parse_Baskebtall_ABA_League(self, response):
        ladder = []

        # Normalize space didn't work at time, something to look in
        for team in response.xpath("//table/tbody/tr/td/a/text()").getall():
            team = team.replace('\t', '').replace('\n', '').rstrip()
            if team == 'FMP':
                ladder.append('KK FMP')
            elif team == 'Split':
                ladder.append('KK Split')
            elif team == 'SC Derby':
                ladder.append('KK SC Derby')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 12)

    def parse_Basketball_Italian_A2_Supercup(self, response):
        ladder = []

        # Is in 2 parts, see if ladders work without non-league style

        for team in response.xpath("").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 12)

    def parse_Basketball_Club_Friendly_Men(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'BC Irkut':
                ladder.append('Irkutsk')
            elif team == 'Temp Sumz Revda':
                ladder.append('TEMP-SUMZ Revda')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 12)

    def parse_Polish_PLK(self, response):
        ladder = []

        # .get() returns '\n', .getll() returns 3 with text() in team[1]
        # Find if text in string command
        for team in response.xpath("//table[@class='table table-hover table-sm text-default-emp']/tbody/tr/td/a"):
            team = team.xpath('.//text()').getall()
            team = team[1].replace('\n', '').strip()
            if team == 'Zastal Zielona Góra':
                ladder.append('Enea Zastal BC Zielona Gora')
            elif team =='STK Czarni Słupsk':
                ladder.append('STK Czarni Slupsk')
            elif team =='Wilki Morskie Szczecin':
                ladder.append('KING Wilki Morskie Szczecin')
            elif team =='Anwil Włocławek':
                ladder.append('Anwil Wloclawek')
            elif team == 'BM Slam Stal Ostrów Wielkopolski':
                ladder.append('Arged BM Slam Stal Ostrow Wielkopolski')
            elif team == 'Astoria Bydgoszcz':
                ladder.append('Enea Astoria Bydgoszcz')
            elif team == 'TBV Start Lublin':
                ladder.append('Start Lublin')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 14)

    def parse_Mexican_LNBP(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Fuerza Regia':
                ladder.append('Fuerza Regia de Monterrey')
            elif team == 'Abejas':
                ladder.append('Abejas de Leon')
            elif team == 'Soles De Mexicali':
                ladder.append('Soles de Mexicali')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 9)

    def parse_Basketball_Brazilian_Campeonato_Paulista(self, response):
        ladder = []

        for team in response.xpath("//div[@class='standingsContent']/div/a/text()").getall():
            if team == 'Pinheiros':
                ladder.append('EC Pinheiros')
            elif team == 'Rio Claro':
                ladder.append('ACBD Rio Claro')
            elif team == 'Franca':
                ladder.append('Sesi SP/Franca BC')
            elif team == 'Osasco':
                ladder.append('Osasco Basket')
            elif team == 'LSB / B2B':
                ladder.append('Liga Sorocabana')
            elif team == 'Mogi':
                ladder.append('Mogi das Cruzes')
            elif team =='Bauru':
                ladder.append('ZOPONE Bauru Basket')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 8)

    def parse_Basketball_Uruguayan(self, response):
        ladder = []

        for team in response.xpath("//div[@class='standingLink']/a/text()").getall():
            if team == 'Tabare':
                ladder.append('Club Atletico Tabare')
            elif team == 'L.Borges':
                ladder.append('Larre Borges')
            elif team == 'U.Atletica':
                ladder.append('Union Atletica')
            elif team == 'Sayago':
                ladder.append('CS Deportivo Sayago')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 2, 9)

    def parse_Basketball_Dominican_Republic(self, response):
        ladder = []

        # Normalize space is getting rid of all text
        for team in response.xpath("//table[@class='table table-hover table-sm text-default-emp']/tbody/tr/td/a/text()").getall():

            # normalize-space returns empty string in this case, look into at further track
            # team=competitor.xpath("normalize-space").get()
            team = team.replace(' ', '').replace('\n', '')

            if team =='':
                continue
            elif team == 'Huracanes del Atlántico':
                ladder.append('Huracanes del Atlantico')
            elif team == 'TitanesdelDistritoNacional':
                ladder.append('Titanes del Licey')
            elif team == 'RealesDeLaVega':
                ladder.append('Reales de La Vega')
            elif team == 'LeonesDeSantoDomingo':
                ladder.append('Leones de Santo Domingo')
            elif team == 'IndiosdeSanFrancisco':
                ladder.append('Indios de San Francisco')
            elif team == 'SolesdeSantoDomingoEste':
                ladder.append('Soles de Santo Domingo Este')
            elif team == 'MetrosdeSantiago':
                ladder.append('Metros de Santiago')
            elif team == 'CañerosdelEste':
                ladder.append('Caneros del Este')
            # if team.xpath("normalize-space(.//text())").get() =='Huracanes del Atlántico':
            #    ladder.append('Huracanes del Atlantico')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 6)

    def parse_Australian_Big_V(self, response):
        ladder = []

        for team in response.xpath("//section[@id='ladder']/div/div/div/div/div/div/h5"):
            if team.xpath("normalize-space(.//text())").get() == 'Hume':
                ladder.append('Hume City Broadmeadows Broncos')
            elif team.xpath("normalize-space(.//text())").get() =='Wyndham':
                ladder.append('Wyndham Basketball')
            elif team.xpath("normalize-space(.//text())").get() =='Keilor':
                ladder.append('Keilor Thunder')
            elif team.xpath("normalize-space(.//text())").get() =='Sunbury':
                ladder.append('Sunbury Jets')
            elif team.xpath("normalize-space(.//text())").get() =='Casey':
                ladder.append('Casey Cavaliers')
            elif team.xpath("normalize-space(.//text())").get() =='McKinnon':
                ladder.append('McKinnon Cougars')
            elif team.xpath("normalize-space(.//text())").get() =='Chelsea':
                ladder.append('Chelsea Gulls')
            elif team.xpath("normalize-space(.//text())").get() =='Hawthorn':
                ladder.append('Hawthorn Magic')
            elif team.xpath("normalize-space(.//text())").get() =='Blackburn':
                ladder.append('Blackburn Vikings')
            else:
                ladder.append(team.xpath(
                    "normalize-space(.//text())").get())

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 9)

    def parse_Basketball_Chinese_NBL(self, response):
        ladder = []

        for team in response.xpath("//div[@class='standingdetails']/div/div/a/text()").getall():
            if team == 'Guangxi':
                ladder.append('Guangxi Weizhuang')
            elif team == 'Henan':
                ladder.append('Henan Shedian Laojiu')
            elif team == 'Xinjiang':
                ladder.append('Xinjiang Tianshan Eagle')
            elif team == 'Wuhan':
                ladder.append('Wuhan Dangdai')
            elif team == 'Anhui P.':
                ladder.append('Putian Xingfa')
            elif team == 'Jiangsu YS':
                ladder.append('Jiangsu Yannan Suke')
            elif team == 'Hunan':
                ladder.append('Hunan Jinjian Miye')
            elif team =='Shaanxi':
                ladder.append('Shaanxi Xinda')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 12)

    def parse_Basketball_PBA_Philippine_Cup(self, response):
        ladder = []

        for team in response.xpath("(//table/tbody)[1]/tr/td[3]/div/div/div/a/text()").getall():
            if team == 'Ginebra Kings':
                ladder.append('Barangay Ginebra San Miguel')
            elif team == 'Blackwater Elite':
                ladder.append('Blackwater Bossing')
            elif team == 'Nlex Road Warriors':
                ladder.append('NLEX Road Warriors')
            elif team in ['Rain or Shine Elasto Painters', 'Rain Or Shine Paint.']:
                ladder.append('Rain Or Shine Elasto Painters')
            elif team == 'Global Port':
                ladder.append('NorthPort Batang Pier')
            elif team in ['B-Meg Llamados', 'Magnolia Hotshots']:
                ladder.append('Magnolia Hotshots Pambansang Manok')
            elif team in ['Barako EC Masters', 'Phoenix Fuel Masters']:
                ladder.append('Phoenix Super LPG Fuel Masters')
            elif team =='Columbian Dyip':
                ladder.append('Terrafirma Dyip')
            elif team in ["Talk 'N Text Tropang Texters", "Talk N Text"]:
                ladder.append('TnT Tropang Giga')
            elif team =='Ginebra San Miguel':
                ladder.append('Barangay Ginebra San Miguel')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 9)

    def parse_Basketball_New_Zealand_NBL(self, response):
        ladder = []

        for team in response.xpath("(//table/tbody)[1]/tr/td[3]/div/div/div/a/text()").getall():
            if team == 'Bay Hawks':
                ladder.append('Taylor Hawks')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 9)

    def parse_Basketball_Chilean_LNB(self, response):
        ladder = []

        for team in response.xpath("(//table/tbody)[1]/tr[@class='sp-livetable__tableRow spm-dataRow']/td[3]/div/div/div/a/text()").getall():
            if team == 'Quilicura':
                ladder.append('CD Quilicura Basket')
            elif team == 'Leones Quilpue':
                ladder.append('Colegio Los Leones')
            elif team == 'Deportivo Valdivia':
                ladder.append('C. D. Deportes Valdivia')
            elif team == 'Temuco':
                ladder.append('C.D. AB Temuco')
            elif team =='Espanol De Talca':
                ladder.append('C. D. Espanol de Talca')
            elif team =='U. De Concepcion':
                ladder.append('Universidad de Concepcion')
            elif team =='Catolica':
                ladder.append('Club Deportivo Universidad Catolica')
            elif team =='Las Animas':
                ladder.append('C. D. Las Animas')
            elif team =='CD Puerto Varas':
                ladder.append('CD Atletico PTO. Varas')
            elif team =='Puente Alto':
                ladder.append('Mun. Puente Alto')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 9)

    def parse_Basketball_NBL1(self, response):
        group_ladder = response.request.meta['group_ladder']
        ladder = []
        loop_count = response.request.meta['loop_count']

        # Collect names in current district
        for team in response.xpath('//tbody/tr/'):
            if team.xpath('.//th/div/span/text()').get() == '':
                ladder.append(
                    {'Name': '', 'W': team.xpath('.//td[3]/text()').get()})
            else:
                ladder.append(team.xpath('.//text()').get())

        group_ladder.append(ladder)

        # Repeat with next district
        while loop_count <=4:
            if loop_count ==1:
                yield response.follow(url='https://nbl1.com.au/stats/ladder/south/men', callback=self.parse_Basketball_NBL1, meta={'allbets': response.request.meta['allbets'], 'group_ladder': group_ladder, 'loop_count': loop_count+1})
            if loop_count ==2:
                yield response.follow(url='https://nbl1.com.au/stats/ladder/central/men', callback=self.parse_Basketball_NBL1, meta={'allbets': response.request.meta['allbets'], 'group_ladder': group_ladder, 'loop_count': loop_count+1})
            if loop_count ==3:
                yield response.follow(url='https://nbl1.com.au/stats/ladder/west/men', callback=self.parse_Basketball_NBL1, meta={'allbets': response.request.meta['allbets'], 'group_ladder': group_ladder, 'loop_count': loop_count+1})
            if loop_count ==4:
                self.Basketball_NBL1_evaluate(self, response, group_ladder)

        # Basketball - Aus/Other

    def Basketball_NBL1_evaluate(self, response, ladder):
        print()
        print(ladder)

        # Order all districts in terms of wins
        sorted_ladder = []
        for team in sorted(ladder, key=lambda x: x['W'], reverse=True):
            sorted_ladder.append(team['Name'])

        # print(ladder)
        response.request.meta['ladder'] = sorted_ladder
        yield Calculative.compare(response, 9, 47)

    def parse_Basketball_Argentina_La_Liga(self, response):
        ladder = []

        for team in response.xpath("//tr[position()>2]/td[3]/p/text()").getall():
            if team == 'Atenas (Patagones)':
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
            elif team == 'Barrio Parque (Córdoba)':
                ladder.append('Barrio Parque')
            elif team == 'Estudiantes (Olavarría)':
                ladder.append('Estudiantes de Olavarria')
            elif team == 'Estudiantes (Concordia)':
                ladder.append('Estudiantes Concordia')
            elif team == 'Ciclista (Junín)':
                ladder.append('Ciclista Juninense')
            elif team == 'Zárate Basket':
                ladder.append('Zarate Basket Club Union de la Ciudad de Zarate')
            elif team == 'Pergamino Basquet':
                ladder.append('Asociacion Civil Club Pergamino Basquet')
            else:
                ladder.append(team)

        #print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 5, 22)

    def parse_Basketball_Australian_NBL(self, response):
        ladder=[]

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                 ladder.append(team)

        #print(ladder)
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)

class Rugby_Union():

    def parse_Rugby_Union_New_Zealand_NPC(self, response):

        # Imbalanced league. Some teams aren't playing as much through the season as the others
        # Found when breaking down xpath to take

        ladder = {}

        for team in response.xpath("//div[@class='sp-livetable__wrap']"):
            ext = team.xpath('.//tbody/tr')
            name = ext.xpath('.//td/a/text()').get()
            if name == '':
                name = ''

            temp = []
            for added in ladder:
                temp.append(added)
            temp.append({'Name': name, 'W':ext.xpath('.//td[@class="nba_win st-br"]/text()').get(), 'L':ext.xpath('.//td[@class="nba_lost st-br"]/text()').get()})
            ladder = temp
            # print(temp)


        sorted_ladder = []
        for team in sorted(ladder, key=lambda x: int(x['W']), reverse=True):
            sorted_ladder.append(team['Name'])

        print(sorted_ladder)
        response.request.meta['ladder'] = sorted_ladder
        yield Calculative.compare(response, 1, 11)

    def parse_Rugby_Union_French_Top_14(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Clermont Auvergne':
                ladder.append('Clermont')
            elif team == 'Section Paloise':
                ladder.append('Pau')
            elif team == 'Biarritz Olympique':
                ladder.append('Biarritz')
            elif team == 'Bordeaux-Begles':
                ladder.append('Bordeaux Begles')
            elif team == 'Racing-Metro 92':
                ladder.append('Racing 92')
            elif team == 'RC Toulonnais':
                ladder.append('Toulon')
            elif team == 'Castres Olympique':
                ladder.append('Castres')
            elif team == 'Stade Francais Paris':
                ladder.append('Stade Francais')
            elif team == 'Stade Toulousain':
                ladder.append('Toulouse')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 12)

    def parse_Rugby_Union_Currie_Cup(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Blue Bulls':
                ladder.append('Bulls')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 6)

    def parse_Rugby_Union_Rugby_Championship(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 0, 3)

class Basketball_US():

    def parse_Basketball_NBA_Summer_League(self, response):
        ladder = []

        for team in response.xpath("((//table/tbody)[1]/tr/td/div/div/div/a/text())[position()<31]").getall():
            if team == 'Los Angeles Clippers':
                ladder.append('LA Clippers')
            elif team == 'Portland Trailblazers':
                ladder.append('Portland Trail Blazers')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 4, 26)

    # Dissapeared quick
    def parse_Basketball_Big3_Basketball_Matches(self, response):
        ladder = []

        # Check if xPath /tbody works
        for team in response.xpath("(//table/tbody)[1]/tr/td[3]/div/div/div/a/text()").getall():
            if team == '':
                ladder.append('')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 9)

    def parse_Basketball_US_NBA(self, response):
        ladder = {}

        for team in response.xpath("//div[@id='standings_1a']/table[starts-with(@class, 'blocks')]"):
            ext = team.xpath('.//tbody/tr')
            name = ext.xpath('.//td/a/text()').get()
            if name == 'Portland Trailblazers':
                name = 'Portland Trail Blazers'

            temp = []
            for added in ladder:
                temp.append(added)
            temp.append({'Name': name, 'W':ext.xpath('.//td[@class="nba_win st-br"]/text()').get(), 'L':ext.xpath('.//td[@class="nba_lost st-br"]/text()').get()})
            ladder = temp

        sorted_ladder = []
        for team in sorted(ladder, key=lambda x: int(x['W']), reverse=True):
            sorted_ladder.append(team['Name'])

        # print(sorted_ladder)
        response.request.meta['ladder'] = sorted_ladder
        yield Calculative.compare(response, 5, 23)

class Australian_Rules():

    def parse_Australian_SANFL(self, response):
        ladder = []

        for team in response.xpath("(//table[@class='sp-livetable__table']/tbody)[1]/tr[position()>1]/td[3]/div/div/div/a/text()").getall():
            if team == 'Woodville-West Eagles':
                ladder.append('Woodville-West Torrens')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        Calculative.compare(response, 1, 9)

    def parse_Australian_Rules_AFL(self, response):
        ladder = []

        for team in response.xpath("//tr/td[@rowspan='1'][2]/text()").getall():
            if team == 'WC Eagles':
                ladder.append('West Coast')
            elif team == 'Port Adel':
                ladder.append('Port Adelaide')
            elif team == 'North Melb':
                ladder.append('North Melbourne')
            elif team == 'GWS Giants':
                ladder.append('Greater Western Sydney')
            elif team == 'W Bulldogs':
                ladder.append('Western Bulldogs')
            else:
                ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        yield Calculative.compare(response, 4, 14)

class American_Football():

    def parse_American_Football_NFL(self, response):
        ladder = []

        # Future note
        print('** Starts 10/09/21 American Footbal NFL')

        for team in response.xpath("//div[@class='d3-o-club-fullname']").getall():
            # if team =='':
            ladder.append(team)

        # print(ladder)
        response.request.meta['ladder'] = ladder
        yield Calculative.compare(response, 9, 22)

class Rugby_League():

    def parse_Rugby_League_NRL(self, response):
        ladder = []

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == ('Manly-Warringah Sea Eagles'):
                ladder.append('Manly Sea Eagles')
            elif team == ('North Queensland Cowboys'):
                ladder.append('Nth Queensland Cowboys')
            else:
                ladder.append(team)

        #print(ladder)
        response.request.meta['ladder'] = ladder
        yield Calculative.compare(response, 3, 12)

class Volleyball():

    def parse_Volleyball_Polish_League_Men(self, response):
        ladder=[]

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Slepsk Suwalki':
                ladder.append('MKS Slepsk Suwalki')
            elif team == 'Asseco Resovia Rzeszow':
                ladder.append('Resovia Rzeszow')
            elif team == 'Lotos Trefl Gdansk':
                ladder.append('Trefl Gdansk')
            elif team == 'Indykpol Olsztyn':
                ladder.append('AZS Olsztyn')
            elif team == 'Cuprum Lubin':
                ladder.append('Cuprum Lubin SA')
            else:
                 ladder.append(team)

        #print(ladder)
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)

    def parse_Volleyball_German_Bundesliga_Men(self, response):
        ladder=[]

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Herrsching':
                ladder.append('Wwk Volleys Herrsching')
            else:
                 ladder.append(team)

        #print(ladder)
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 8)

    def parse_Volleyball_Polish_League_Women(self, response):
        ladder=[]

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Budowlani Lodz W':
                ladder.append('Budowlani Lodz')
            elif team == 'Chemik Police W':
                ladder.append('Chemik Police')
            elif team == 'Joker Swiecie W':
                ladder.append('Joker Swiecie')
            elif team == 'Opole W':
                ladder.append('Uni Opole')
            elif team == 'Legionowo W':
                ladder.append('Legionovia Legionowo')
            elif team == 'Radom W':
                ladder.append('Radomka Radom')
            else:
                 ladder.append(team)

        #print(ladder)
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 11)

    def parse_Volleyball_Turkish_League_Men(self, response):
        ladder=[]

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Altekma':
                ladder.append('TFL Altekma')
            elif team == 'Fenerbahce Istanbul':
                ladder.append('Fenerbahce SK Istanbul')
            elif team == 'Sorgun Bld':
                ladder.append('Sorgun BLD')
            elif team == 'Belediye Plevne':
                ladder.append('Tokat Belediye')
            elif team == 'Afyon Karahisar Bld':
                ladder.append('Afyon Belediye Yuntas')
            elif team == 'Ziraat Bankasi':
                ladder.append('Ziraat Bankasi Ankara')
            elif team == 'Halk Bankasi':
                ladder.append('Halkbank Ankara')
            elif team == 'Kiziltepe':
                ladder.append('Yeni Kiziltepe Spor')
            elif team == 'Arkas Spor':
                ladder.append('Arkas Izmir')
            else:
                 ladder.append(team)

        #print(ladder)
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)

    def parse_Volleyball_Korean_League_Women(self, response):
        ladder=[]

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team == 'Hyundai Greenfox W':
                ladder.append('Suwon Hillstate')
            elif team == 'Hungkuk Pinkspiders W':
                ladder.append('Incheon Pink Spiders')
            else:
                 ladder.append(team)

        #print(ladder)
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 6)


# Ice Hockey - US - Low score for now
# def parse_Ice_Hockey_US_NHL_Matches(self, response):
#     ladder={}

#     for team in response.xpath("(//table[@class='sp-livetable__table '])[position()<5]/tbody/tr[position()>1]"):
#         name=team.xpath('.//td/div/div/div/a/text()').get()
#         if name == '':
#             name = ''

#         temp=[]
#         for added in ladder:
#             temp.append(added)
#         temp.append({'Name': name,'W':team.xpath('.//td[@title="win"]/div/text()').get(), 'L':team.xpath('.//td[@title="loss"]/div/text()').get()})
#         ladder=temp

#     sorted_ladder=[]
#     for team in sorted(ladder, key=lambda x:int(x['W']), reverse=True):
#         sorted_ladder.append(team['Name'])

#     print(sorted_ladder)
#     response.request.meta['ladder']=sorted_ladder
#     yield Calculative.compare(response, 3, 27)
