import Calculative

    # # #Copy def parse stock

    # # def parse_(self, response):
    # #     ladder=[]

    # #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    # #         if team == '':
    # #             ladder.append()
    # #         else:
    # #              ladder.append(team)

    # #     print(ladder)
    # #     response.request.meta['ladder']=ladder
    # #     Calculative.compare(response, , )


    ## Copy def parse keys stock

    # def parse_(self, response):
    #     ladder=[]
    #     teams={
    #         '': [''],
    #         '': [''],
    #         '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)


    ## Test high/low stock

    # Calculative.highlowTest(response)


class Cricket():

    # def parse_Cricket_(self, response):
    #     ladder=[]
    #     teams={
    #        '': [''],
    #        '': [''],
    #        '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)


    # def parse_Cricket_(self, response):
    #     ladder=[]

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team == '':
    #             ladder.append()
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )

    def parse_Cricket_Pakistan_Super_League(self, response):
        ladder=[]
        teams={
           'Multan Sultans': ['Multan  Sultans'],
           '': [''],
           '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print(' *Check ladder for compare as was not there prior to league starting, base off previous season')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 5)
        # results = Calculative.compare(response, 1, 5)
        # print(results)

    def parse_Cricket_Bangladesh_Premier_League(self, response):
        ladder=[]
        teams={
           '': [''],
           '': [''],
           '': [''],
            }

        for team in response.xpath("(//table)[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n** Using old league')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 6)
        # results = Calculative.compare(response, 1, 6)
        # print(results)

    def parse_Cricket_WBBL(self, response):
        ladder=[]
        teams={
            'Brisbane Heat W': ['Brisbane Heat WBBL'],
            'Perth Scorchers W': ['Perth Scorchers WBBL'],
            'Adelaide Strikers W': ['Adelaide Strikers WBBL'],
            '': [''],
            }

        for team in response.xpath("(//table)[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 6)
        # results = Calculative.compare(response, 1, 6)
        # print(results)

    def parse_Cricket_Super_Smash_T20(self, response):
        ladder=[]
        teams={
            'Otago Volts': ['Otago'],
            'Wellington Firebirds': ['Wellington'],
            'Canterbury Kings': ['Canterbury'],
            'Northern Knights': ['Northern Brave'],
            }

        for team in response.xpath("(//table[1])[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 5)
        # results = Calculative.compare(response, 1, 5)
        # print(results)

    def parse_Cricket_Twenty20_Big_Bash(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("(//table)[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 6)
        # results = Calculative.compare(response, 1, 6)
        # print(results)

    def parse_Cricket_Test_Matches(self, response):
        ladder=[]
        teams={
           '': [''],
           '': [''],
           '': [''],
            }

        for team in response.xpath("//tbody/tr/td/a/div/div/div/h5/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('Needs More Games Played**')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 7)
        # results = Calculative.compare(response, 1, 7)
        # print(results)

class Handball():

    # def parse_Handball_(self, response):
    #     ladder=[]

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team == '':
    #             ladder.append()
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )

    # def parse_Handball_(self, response):
    #     ladder=[]
    #     teams={
    #         '': [''],
    #         '': [''],
    #         '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)

    def parse_Handball_Champions_League_Men(self, response):
        ladder=[]
        teams={
            'Meshkov Brest': ['HC Meshkov Brest'],
            'Aalborg Handbold': ['Aalborg Haandbold'],
            'Montpellier HB': ['Montpellier Handball'],
            'Vardar Vatrost Skopje': ['HC Vardar 1961'],
            'Flensburg-Handewitt': ['SG Flensburg-Handewitt'],
            'Kielce': ['KS Vive Kielce'],
            'Veszprem': ['Veszprem KC'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.group_split(response, 0, 7)
        # results = Calculative.compare(response, , )
        # print(results)

    def parse_Handball_Romanian_League_Men(self, response):
        ladder=[]
        teams={
            'Alexandria': ['Csm Alexandria'],
            'Baia Mare': ['CS Minaur Baia Mare'],
            'Dobrogea Sud': ['AHC Dobrogea Sud'],
            'Potaissa Turda': ['AHC Potaissa Turda'],
            'CSM Focsani': ['CSM Focsani 2007'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, , )
        # print(results)

    def parse_Handball_European_Championship_Men(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table[@id='standings_1a201425']/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 21)
        # results = Calculative.compare(response, , )
        # print(results)

    def parse_Handball_Romanian_League_Women(self, response):
        ladder=[]
        teams={
            'CSM Bucuresti W': ['CSM Bucuresti'],
            'CSM Slatina W': ['CSM Slatina'],
            'CS Magura Cisnadie W': ['CS Magura Cisnadie'],
            'Mioveni W': ['CS Dacia Mioveni 2012'],
            'Ramnicu Valcea W': ['SCM Ramnicu Valcea'],
            'Bistrita W': ['CS Gloria 2018 Bistrita-Nasaud'],
            'Buzau W': ['SCM Gloria Buzau'],
            'Baia Mare W': ['CS Minaur Baia Mare'],
            'CSU Stiinta Bucuresti W': ['CSU Stiinta Bucuresti'],
            'Dunarea Braila W': ['HC Dunarea Braila'],
            'HC Zalau W': ['HC Zalau'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Handball_French_Div1_Women(self, response):
        ladder=[]
        teams={
            'Bourg de Peage W': ['Bourg De Peage'],
            'Paris 92 W': ['Paris 92'],
            'Merignac W': ['Merignac Handball'],
            'Dijon W': ['JDA Dijon Handball'],
            'Toulon W': ['Toulon Metropole Var Handball'],
            'Fleury Loiret W': ['Fleury Loiret HB'],
            'Metz W': ['Metz Handball'],
            'Nice W': ['OGC Nice Cote D`Azur HB'],
            'Brest W': ['Brest Bretagne HB'],
            'Chambray W': ['Chambray Touraine'],
            'Nantes W': ['Les Neptunes de Nantes'],
            'Besancon W': ['ESBF Besancon'],
            'Celles W': ['HBC Celles-Sur-Belle'],
            'Plan de Cuques W': ['HB Plan de Cuques'],
            }
        
        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Handball_Norwegian_League_Women(self, response):
        ladder=[]
        teams={
            'Larvik W': ['Larvik HK'],
            'Tertnes W': ['Tertnes HE Bergen'],
            'Sola W': ['Sola HK'],
            'Molde W': ['Molde HK'],
            'Fana W': ['Fana HE Bergen'],
            'Byasen W': ['Byaasen HE Trondheim'],
            'Romerike Ravens W': ['Romerike Ravens'],
            'Kristiansand W': ['Vipers Kristiansand'],
            'Fredrikstad W': ['Fredrikstad BK'],
            'Storhamar W': ['Storhamar HE'],
            'Follo HK W': ['Follo HK'],
            'Aker W': ['Aker Topphaandball Bygdoey'],
            'Flint Tonsberg W': ['Flint Toensberg'],
            'Oppsal W': ['Oppsal IF Oslo'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Handball_Champions_League_Women(self, response):
        ladder=[]
        teams={
            'Rostov-Don W': ['GK Rostov-Don'],
            'Ferencvarosi Torna W': ['Ferencvarosi TC'],
            'Brest W': ['Brest Bretagne HB'],
            'Kristiansand W': ['Vipers Kristiansand'],
            'Esbjerg W': ['Team Esbjerg'],
            'Buducnost W': ['ZRK Buducnost'],
            'Podravka Vegeta W': ['Podravka Koprivnica'],
            'Borussia Dortmund W': ['Borussia Dortmund'],
            'Odense W': ['HC Odense'],
            'CSKA Moscow W': ['HBC CSKA Moscow'],
            'Metz W': ['Metz Handball'],
            'Kastamanu Bld W': ['Kastamonu GSK'],
            'Savehof W': ['IK Savehof'],
            'Gyori Audi ETO KC W': ['Gyori ETO KC'],
            'Krim Mercator W': ['RK Krim Ljubljana'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print("Watch for how ladder result**")
        response.request.meta['ladder']=ladder
        Calculative.group_split(response, 0, 7)
        # results = Calculative.group_split(response, 0, 7)
        # print(results)

    def parse_Handball_European_Championship_Qualifiers_Men(self, response):
        print('Come back standings to see position**')
        print('Ran High Low Test while message was here')

        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table[@class='sp-livetable__table standingsTaba201425']/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 21)
        # results = Calculative.compare(response, 2, 21)
        # print(results)

    def parse_Handball_Danish_League_Women(self, response):
        ladder=[]
        teams={
            'Ajax KBH W': ['Ajax Copenhagen'],
            'Herning Ikast W': ['Herning-Ikast Haandbold'],
            'Randers HK W': ['Randers HK'],
            'Odense W': ['HC Odense'],
            'Silkeborg-Voel KFUM W': ['Silkeborg Voel KFUM'],
            'Nykobing F. W': ['Nykoebing Falster HB'],
            'Esbjerg W': ['Team Esbjerg'],
            'Holstebro W': ['Holstebro Haandbold'],
            'SK Aarhus W': ['Aarhus United'],
            'Viborg HK W': ['Viborg HK'],
            'Skanderborg Handbold W': ['Skanderborg Haandbold'],
            'Kobenhavn Handbold W': ['Copenhagen Handball'],
            'Ringkobing W': ['Ringkoebing Haandbold'],
            'Horsens HK W': ['HH Elite'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Handball_Swedish_Elitserien_Men(self, response):
        ladder=[]
        teams={
            'Aranas': ['HK Aranas'],
            'Onnereds': ['Onnereds HK'],
            'Skjern': ['Skjern Haandbold'],
            'Hammarby': ['Hammarby HB'],
            'Lugi': ['Lugi HF'],
            'Alingsas': ['Alingsaas HK'],
            'Malmo': ['HK Malmo'],
            'Eskilstuna Guif': ['IF Guif'],
            'Hallby': ['IF Hallby'],
            'Skovde': ['IFK Skovde'],
            'Redbergslids': ['Redbergslids IK'],
            'IFK Ystads': ['IFK Ystad'],
            'Savehof': ['IK Savehof'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Handball_Spanish_ASOBAL_League(self, response):
        ladder=[]
        teams={
            'Puente Genil': ['BM Puente Genil'],
            'Atletico Valladolid': ['BM Atletico Valladolid'],
            'Barcelona': ['FC Barcelona'],
            'Antequera': ['BM Antequera'],
            'Huesca': ['BM Huesca'],
            'Torrelavega': ['BM Torrelavega'],
            'Morrazo Cangas': ['CB Cangas'],
            'Anaitasuna': ['SCDR Anaitasuna'],
            'Ciudad Encantada Cuenca': ['BM Ciudad Encantada'],
            'Benidorm': ['BM Benidorm'],
            'Sinfin': ['BM Sinfin'],
            'Viveros Herol Nava': ['BM Nava'],
            'La Rioja': ['BM Logrono La Rioja'],
            'Granollers': ['BM Granollers'],
            'Irun': ['Bidasoa Irun'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 14)
        # results = Calculative.compare(response, 1, 14)
        # print(results)

    def parse_Handball_Norwegian_League_Men(self, response):
        ladder=[]
        teams={
            'Fjellhammer': ['Fjellhammer IL'],
            'Kolstad': ['Kolstad Handball'],
            'Elverum': ['Elverum Handball'],
            'Drammen': ['Drammen HK'],
            'Kristiansand': ['Kristiansand Topphandball'],
            'Notteroy': ['Noetteroey Haandball'],
            'Halden Topphandbal': ['Halden Topphandball'],
            'Runar': ['Runar Sandefjord IL'],
            'Naerbo': ['Naerboe IL'],
            'Baekkelaget Elite': ['BSK Haandball Elite'],
            'Arendal': ['OIF Arendal Elite'],
            'Sandefjord': ['Sandefjord Haandball'],
            'Fyllingen': ['FyllingenBergen'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Handball_German_Bundesliga(self, response):
        ladder=[]
        teams={
            'Bergischer': ['Bergischer HC'],
            'Erlangen': ['HC Erlangen'],
            'Balingen/Weilstetten': ['HBW Balingen-Weilstetten'],
            'Frisch Auf Goppingen': ['FRISCH AUF! Goppingen'],
            'TuS N-Lubbecke': ['TUS N-Lubbecke'],
            'Lemgo': ['TBV Lemgo Lippe'],
            'Kiel': ['THW Kiel'],
            'Leipzig': ['SC DHfK Leipzig'],
            'Flensburg-Handewitt': ['SG Flensburg-Handewitt'],
            'TVB 1898 Stuttgart': ['TVB Stuttgart'],
            'Minden': ['GWD Minden'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 16)
        # results = Calculative.compare(response, 2, 16)
        # print(results)

    def parse_Handball_French_Div1_Men(self, response):
        ladder=[]
        teams={
            'Cesson': ['Cesson Rennes Metropole HB'],
            'Saran': ['Saran Loiret Handball'],
            'Dunkerque': ['Dunkerque HB'],
            'Nantes': ['HBC Nantes'],
            'Creteil': ['US Creteil Handball'],
            'Nancy': ['Grand Nancy Metropole Hb', 'Grand Nancy Metropole HB'],
            'Istres': ['Istres Ouest Provence'],
            'Montpellier HB': ['Montpellier Handball'],
            'Limoges': ['Limoges Handball'],
            'Pays d Aix': ['PAUC Handball'],
            'Nimes': ['USAM Nimes Gard'],
            'Chartres': ['Chartres Metropole Handball'],
            'Toulouse': ['Toulouse Handball'],
            'Paris SG': ['Paris Saint-Germain'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 14)
        # results = Calculative.compare(response, 1, 14)
        # print(results)

    def parse_Handball_Danish_League_Men(self, response):
        ladder=[]
        teams={
            'Skanderborg': ['Skanderborg-Aarhus Haandbold'],
            'Skjern': ['Skjern Haandbold'],
            'Kolding': ['KIF Kolding'],
            'Skive': ['Skive FH'],
            'Holstebro': ['Tth Holstebro'],
            'Aalborg Handbold': ['Aalborg Haandbold'],
            'GOG Handball': ['GOG Handbold'],
            'Sonderjyske': ['Soenderjyske HK'],
            'Ringsted': ['TMS Ringsted'],
            'HF Mors': ['Mors-Thy Haandbold'],
            'Nordsjalland Handbold': ['Nordsjaelland Haandbold'],
            'Fredericia': ['Fredericia HK 1990'],
            'Lemvig Thyboron': ['Lemvig-Thyboroen Haandbold'],
            'Bjerringbro/Silkeborg': ['Bjerringbro-Silkeborg Haandbold'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 13)
        # results = Calculative.compare(response, 1, 13)
        # print(results)

    def parse_Handball_Russian_Superleague_Men(self, response):
        ladder=[]
        teams={
            'Akbuzat UGNTU-VNZM': ['UGNTU-VNZM'],
            'Sungul': ['Dinamo Sungul'],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 11)
        # results = Calculative.compare(response, 1, 11)
        # print(results)

    def parse_Handball_Swedish_League_Women(self, response):
        ladder=[]
        teams={
            'Karra W': ['Karra HF'],
            'Lugi W': ['Lugi HF'],
            'Savehof W': ['IK Savehof'],
            'Onnereds W': ['Onnereds HK'],
            'H 65 Hoor W': ['H65 Hoor HK'],
            'Vasteras W': ['Vasteraasirsta HF'],
            'BK Heid W': ['BK Heid'],
            'Kungalvs W': ['Kungalvs HK'],
            'Skovde W': ['Skovde HF'],
            'Kristianstad W': ['Kristianstad HK'],
            'Skuru W': ['Skuru IK'],
            'Skara W': ['Skara HF'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 11)
        # results = Calculative.compare(response, 1, 11)
        # print(results)

    def parse_Handball_Russian_Superleague_Women(self, response):
        ladder=[]
        teams={
            'Kuban W': ['HC Kuban Krasnodar'],
            'Astrakhanochka W': ['Astrakhanochka Astrakhan'],
            'Rostov-Don W': ['GK Rostov-Don'],
            'Zvezda W': ['Zvezda'],
            'Ufa-Alice W': ['Ufa-Alisa'],
            'Dinamo Volgograd W': ['Dinamo Sinara'],
            'CSKA Moscow W': ['HBC CSKA Moscow'],
            'University Izhevsk W': ['Universitet'],
            'AGU-ADIIF W': ['Agu-Adyif'],
            'Stavropol W': ['Stavropoliye'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print("Watch for how this ladder results")
        response.request.meta['ladder']=ladder
        Calculative.group_split(response, 0, 5)
        # results = Calculative.group_split(response, 0, 5)
        # print(results)

class Basketball_AusOther():

    # def parse_Basketball_(self, response):
    #     ladder=[]

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team == '':
    #             ladder.append()
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )

    # def parse_Basketball_(self, response):
    #     ladder=[]
    #     teams={
    #         '': [''],
    #         '': [''],
    #         '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)

    def parse_Basketball_Liga_ABA_2(self, response):
        ladder=[]
        teams={
            'Helios Domzale': ['KK Helios Suns'],
            'Mladost': ['KK Mladost Zemun'],
            'Spars Sarajevo': ['OKK Spars Realway'],
            'Zlatibor': ['KK Zlatibor Cajetina'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, , )
        # print(results)

    def parse_Basketball_Danish_Damligaen(self, response):
        ladder=[]
        teams={
            'BK Amager W': ['BK Amager Women'],
            'Sisu W': ['SISU Copenhagen Women'],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 4)
        # results = Calculative.compare(response, , )
        # print(results)

    def parse_Basketball_Uruguayan_LUB(self, response):
        ladder=[]
        teams={
            'Penarol': ['CA Penarol'],
            'Urupan': ['Urupan de Pando'],
            'Urunday': ['Urunday Universitario'],
            'Atletico Bigua': ['Bigua'],
            'Goes': ['Atletico Goes'],
            'Hebraica Macabi': ['Asociacion Hebraica y Macabi'],
            'Malvin': ['Club Malvin'],
            'NutriBullet Treviso Basket': ['Nutribullet Treviso Basket'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_Spanish_League_Women(self, response):
        ladder=[]
        teams={
            'CDB Clarinos': ['Clarinos De La Laguna Women'],
            'BAXI Uni Ferrol': ['Baxi Ferrol Women'],
            'Gran Canaria 2014': ['Spar Gran Canaria Women'],
            }

        for team in response.xpath('//table[@class="table table-hover table-sm text-default-emp"]/tbody/tr/td/a').getall():
            # team=team.xpath('normalize-space(//text())').get()
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 14)
        # results = Calculative.compare(response, 2, 14)
        # print(results)

    def parse_Basketball_Icelandic_League_Men(self, response):
        ladder=[]
        teams={
            'Breiðablik': ['Breiablik'],
            'KR Reykjavik': ['K.R. Basket Reykjavik'],
            'UMF Tindastoll': ['Tindastoll'],
            'UMF Njardvik': ['Njarvik'],
            }

        for team in response.xpath("//table[@class='table table-hover table-sm text-default-emp']/tbody/tr/td/a"):
            team=team.xpath("normalize-space(.//text())").get()
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_Balkan_BIBL(self, response):
        ladder=[]
        teams={
            'Prishtina': ['KB Prishtina'],
            'Kk Ibar Rozaje': ['KK Ibar Rozaje'],
            'TFT Skopje': ['TFT Basketball Club'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.group_split(response, 0, 5, split=(6,5))
        # results = Calculative.compare(response, 0, 5)
        # print(results)

    def parse_Basketball_Lithuanian_NKL(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table[@class='table table-hover table-sm text-default-emp']/tr/td/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_Swiss_Basketball_League(self, response):
        ladder=[]
        teams={
            'Bbc Nyon': ['BBC Nyon'],
            'Monthey': ['BBC Monthey'],
            'Sam Massagno': ['Spinelli Massagno'],
            'Lions Geneve': ['Les Lions de Geneve'],
            'Boncourt R.T.': ['BC Boncourt'],
            'Neuchatel': ['Union Neuchatel Basket'],
            'Regio Basel': ['Starwings Basket Regio Basel'],
            'Swiss Central': ['Swiss Central Basket'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Korean_KBL(self, response):
        ladder=[]
        teams={
            'Changwon LG': ['Changwon LG Sakers'],
            'Wonju Dongbu': ['Wonju Dongbu Promy'],
            'Goyang Orions': ['Goyang Orion Orions'],
            'Ulsan Mobis': ['Ulsan Hyundai Mobis Phoebus'],
            'Busan Kt': ['Suwon KT Sonicboom'],
            'Daegu Pegasus': ['Daegu KOGAS Pegasus'],
            'Seoul Thunders': ['Seoul Samsung Thunders'],
            'Anyang': ['Anyang KGC'],
            'LG Sakers': ['Changwon LG Sakers'],
            'Sonic Boom': ['Suwon KT Sonicboom'],
            'Seoul Knights': ['Seoul SK Knights'],
            'Mobis Phoebus': ['Ulsan Hyundai Mobis Phoebus'],
            'Goyang': ['Goyang Orion Orions'],
            'KCC Egis': ['Jeonju KCC Egis'],
            'Dongbu Promy': ['Wonju Dongbu Promy'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_FIBA_EuroLeague_Women(self, response):
        ladder=[]
        teams={
            'Ekaterinburg W': ['UMMC Ekaterinburg Women'],
            'Lattes Montpellier Gazelles W': ['Basket Lattes Montpellier Gazelles Women'],
            'Dynamo Kursk W': ['Dinamo Kursk Women'],
            'Fenerbahce W': ['Fenerbahce Women'],
            'MBA Moscow W': ['MBA Moscow Women'],
            'Szekszard W': ['Atomeromu Szekszard Women'],
            'USK Prague W': ['ZVVZ USK Praha Women'],
            'Arka Gdynia W': ['VBW Arka Gdynia Women'],
            'Galatasaray W': ['Galatasaray Women'],
            'Schio W': ['Famila Basket Schio Women'],
            'Riga W': ['TTT Riga Women'],
            'Landes W': ['Basket Landes SASP Women'],
            'Perfumerias Avenida W': ['Perfumerias Avenida Women'],
            'PF Schio W': ['Famila Basket Schio Women'],
            'Sopron W': ['Sopron Basket Women'],
            'Venezia W': ['Umana Reyer Venezia Women'],
            }

        for team in response.xpath("//table[@id='standings_1a203617']/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 14)
        # results = Calculative.compare(response, 2, 14)
        # print(results)

    def parse_Basketball_Lithuanian_LKL(self, response):
        ladder=[]
        teams={
            'Juventus': ['BC Juventus Utena'],
            'Dzukija': ['Alytaus Dzukija'],
            'Lietuvos Rytas': ['Rytas Vilnius'],
            'Pieno Zvaigzdes': ['Pasvalio Pieno zvaigzdes'],
            'Nevezis': ['Kedainiai Nevezis'],
            'Prienai': ['Labas Gas Prienai'],
            'Jonava': ['BC Cbet Jonava'],
            'Siauliai': ['BC Siauliai'],
            'BC Neptunas': ['Neptunas Klaipeda'],
            'BC Dzukija': ['Alytaus Dzukija'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_VTB_United_League(self, response):
        ladder=[]
        teams={
            'Stelmet Zielona Gora': ['Enea Zastal BC Zielona Gora'],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_Italian_Serie_A2(self, response):
        ladder=[]
        teams={
            'Urania Basket Milano': ['Urania Milano'],
            'Forli': ['Unieuro 2.015 Forli'],
            'Stella Azzurra Roma': ['Stella Azzura Roma'],
            'Latina': ['Latina Basket'],
            'San Severo': ['Allianz Pazienza San Severo'],
            'Baltur Cento': ['Tramec Cento'],
            'Orlandina Basket': ["Benfapp Capo d'Orlando"],
            'Piacenza Basket': ['UCC Assigeco Piacenza'],
            'Trapani': ['2B Control Trapani'],
            'The Flexx Pistoia': ['OriOra Pistoia'],
            }

        for team in response.xpath("//div[@class='sp-livetable__wrap']/table[1]/tbody/tr[position()>1]"):
            ext=team.xpath('.//tbody/tr[position()>1]')
            name = team.xpath('.//td[@title=""]/div/div/div/a/text()').get()

            if name in teams.keys():
                name = teams[name]
            else:
                name = [name]

            ladder.append({'Name': name, 'W':team.xpath('.//td[@title="win"]/div/text()').get(), 'L':team.xpath('.//td[@title="loss"]/div/text()').get()})
        
        sorted_ladder = []
        for team in sorted(ladder, key=lambda x: int(x['W']), reverse=True):
            sorted_ladder.append(team['Name'])

        response.request.meta['ladder']=sorted_ladder
        Calculative.compare(response, 4, 23)
        # results = Calculative.compare(response, 4, 23)
        # print(results)

    def parse_Basketball_Greek_A1(self, response):
        ladder=[]
        teams={
            'Olympiacos': ['Olympiacos BC'],
            'Larisa': ['Larisa B.C. Bread Factory'],
            'Panathinaikos': ['Panathinaikos OPAP Athens'],
            'Iraklis': ['Iraklis Thessaloniki'],
            'Ionikos Nikeas BC': ['Ionikos BC Hellenic Coin'],
            'Apollon Patras': ['AS Apollon Patras'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 11)
        # results = Calculative.compare(response, 1, 11)
        # print(results)

    def parse_Basketball_Swedish_Ligan(self, response):
        ladder=[]
        teams={
            'Kfum Nassjo': ['KFUM Nassjo Basket'],
            'Norrkoping Dolphins': ['Norrkoeping Dolphins'],
            'Kfum Umea': ['Umea'],
            'Kfum Fryshuset': ['KFUM Fryshuset Basket'],
            'Sodertalje BBK': ['Soedertaelje Kings'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 8)
        # results = Calculative.compare(response, 1, 8)
        # print(results)

    def parse_Basketball_Romanian_Liga_Nationala(self, response):
        ladder=[]
        teams={
            'CSM Oradea': ['CSM CSU Oradea'],
            'BC Timba Timisoara': ['BC SCM Timisoara'],
            'Cs Dinamo Bucharest': ['CS Dinamo Bucuresti'],
            'CSU Ploiesti': ['CS Municipal Ploiesti'],
            'Voluntari': ['CSO Voluntari'],
            'Constanta': ['ABC Athletic Constanta'],
            'Rapid Bucuresti': ['CS Rapid Bucuresti'],
            'CSM Focsani': ['CSM Focsani ', 'CSM Focsani'],
            'Miercurea Ciuc': ['CSM Miercurea Ciuc'],
            'Cs Phoenix Galati': ['CSM Galati'],
            'CSA Steaua': ['CSA Steaua Bucuresti'],
            'U-BT Cluj-Napoca': ['U-Banca Transilvania Cluj-Napoca'],
            'BCM U Pitesti': ['BCMU Pitesti'],
            'SCM U. Craiova': ['CSM Universitatea Craiova'],
            'CSU Sibiu': ['BC CSU Sibiu'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 14)
        # results = Calculative.compare(response, 2, 14)
        # print(results)

    def parse_Basketball_Korean_WKBL(self, response):
        ladder=[]
        teams={
            'Shinhan S-Birds W': ["Shinhan Bank S'Birds Women"],
            'KB Stars W': ['Cheongju KB Stars Women'],
            'Hansae W': ['Asan Woori Bank Wibee Women'],
            'KDB L. Winnus W': ['Busan BNK Sum Women'],
            'Keb-Hana W': ['Bucheon Hana 1Q Women'],
            'Blue Minx W': ['Yongin Samsung Blueminx Women'],
            'Busan BNK Sum W': ['Busan BNK Sum Women'],
            'KEB Hana W': ['Bucheon Hana 1Q Women'],
            'S-Birds W': ["Shinhan Bank S'Birds Women"],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 5)
        # results = Calculative.compare(response, 0, 5)
        # print(results)

    def parse_Basketball_German_BBL(self, response):
        ladder=[]
        teams={
            'Giessen': ['JobStairs Giessen 46ers'],
            'Bayern': ['FC Bayern Munchen'],
            'Heidelberg': ['MLP Academics Heidelberg'],
            'Ludwigsburg': ['MHP RIESEN Ludwigsburg'],
            'Bayreuth': ['Medi Bayreuth'],
            'Braunschweig': ['Basketball Lowen Braunschweig'],
            'Crailsheim Merlins': ['HAKRO Merlins Crailsheim'],
            'Bonn': ['Telekom Baskets Bonn'],
            'Mitteldeutscher': ['SYNTAINICS MBC'],
            'Frankfurt': ['FRAPORT SKYLINERS'],
            'Chemnitz': ['BV Chemnitz 99'],
            'Ulm': ['Ratiopharm Ulm'],
            'Alba Berlin': ['ALBA Berlin'],
            'Gottingen': ['BG Gottingen'],
            'Würzburg': ['s.Oliver Wurzburg'],
            'Giessen 46ers': ['JobStairs Giessen 46ers'],
            'Basketball Loewen Braunschweig': ['Basketball Lowen Braunschweig'],
            'Wuerzburg': ['s.Oliver Wurzburg'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 15)
        # results = Calculative.compare(response, 2, 15)
        # print(results)

    def parse_Basketball_French_ProA_League(self, response):
        ladder=[]
        teams={
            'Le Portel': ['ESSM Le Portel'],
            'Strasbourg': ['SIG Strasbourg'],
            'Monaco': ['AS Monaco Basket'],
            'ASVEL': ['LDLC ASVEL Lyon-Villeurbanne'],
            'Provence': ['Fos Provence Basket'],
            'Orleans': ['Orleans Loiret Basket'],
            'Chorale de Roanne': ['Chorale Roanne'],
            'Cholet': ['Cholet Basket'],
            'Dijon': ['JDA Dijon Basket'],
            'Pau-Orthez': ['Elan Bearnais Pau-Lacq-Orthez'],
            'Levallois': ['Metropolitans 92'],
            'Le Mans': ['Le Mans Sarthe Basket'],
            'Gravelines Dunkerque': ['BCM Gravelines Dunkerque'],
            'Chalon-Reims': ['Champagne Basket'],
            'Chalons-Reims': ['Champagne Basket'],
            'Nanterre': ['Nanterre 92'],
            'ASVEL Lyon-Villeurbanne': ['LDLC ASVEL Lyon-Villeurbanne'],
            'Roanne': ['Chorale Roanne'],
            'Provence Basket': ['Fos Provence Basket'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 15)
        # results = Calculative.compare(response, 2, 15)
        # print(results)

    def parse_Basketball_British_BBL_Championship(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Brazilian_NBB(self, response):
        ladder=[]
        teams={
            'Bauru': ['ZOPONE Bauru Basket'],
            'Flamengo BC': ['Flamengo Rio De Janeiro'],
            'Pinheiros': ['EC Pinheiros'],
            'Brasilia': ['Universo Brasilia'],
            'Cerrado Basquete': ['Cerrado Iesplan'],
            'Franca': ['Sesi SP/Franca BC'],
            'Cearense': ['Fortaleza Basquete Cearense'],
            'Pato Basquete': ['Pato'],
            'Mogi': ['Mogi das Cruzes'],
            'Uniao Corinthians': ['Luvix/Uniao Corinthians'],
            'Caxias Do Sul': ['Caxias do Sul'],
            'Flamengo': ['Flamengo Rio De Janeiro'],
            'Rio Claro': ['ACBD Rio Claro'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 15)
        # results = Calculative.compare(response, 2, 15)
        # print(results)

    def parse_Basketball_Israeli_Supreme_League(self, response):
        ladder=[]
        teams={
            'Nes Ziona': ['Ironi Hai Motors Nes Ziona'],
            'Maccabi Tel Aviv': ['Maccabi Playtika Tel Aviv'],
            'Hapoel Tel Aviv': ['Hapoel SP Tel-Aviv'],
            'Hapoel Eilat': ['Hapoel Yossi Avrahami Eilat'],
            'Galil Elyon': ['Hapoel Galil Elyon'],
            'Hapoel Holon': ['Hapoel U-NET Holon'],
            'Hapoel Jerusalem': ['Hapoel Bank Yahav Jerusalem'],
            'Bnei Herzliya': ['Bnei Rav-Bariach Herzliya'],
            'Hapoel Haifa': ['Hapoel B-Cure Laser Haifa BC'],
            'Hapoel Gilboa/Galil': ['Hapoel Gilboa Galil'],
            'Maccabi Rishon Lezion': ['Maccabi Rishon Le-Zion'],
            'Hapoel Beer Sheva': ['Hapoel Altshuler Shaham Beer Sheva'],
            }

        for team in response.xpath("(//div[@class='sp-livetable__wrap']/table)[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_Hungarian_A_Division(self, response):
        ladder=[]
        teams={
            'Szolnoki Olaj': ['Szolnoki Olajbanyasz KK'],
            'Soproni': ['Soproni KC'],
            'Kecskemeti TE': ['KTE Duna Aszfalt'],
            'Szedeak': ['Naturtex-SZTE-Szedeak'],
            'Kormend': ['BC Kormend'],
            'Kaposvari': ['Kaposvari KK'],
            'Nyiregyhaza': ['Hubner Nyiregyhaza'],
            'DEAC': ['Debreceni Egyetem KE'],
            'Szombathely': ['Falco Szombathely'],
            'Atomeromu': ['Atomeromu Paks SE'],
            'PVSK Panthers': ['Pecsi VSK-Veolia'],
            'Atomeromu SE': ['Atomeromu Paks SE'],
            'Falco KC Szombathely': ['Falco Szombathely'],
            'Koermend': ['BC Kormend'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_EuroCup(self, response):
        ladder=[]
        teams={
            'Lokomotiv Kuban': ['Lokomotiv-Kuban Krasnodar'],
            'Trento': ['Dolomiti Energia Trento'],
            'Lietkabelis': ['BC Lietkabelis'],
            'Joventut Badalona': ['Club Joventut Badalona'],
            'Andorra': ['MoraBanc Andorra'],
            'Ulm': ['Ratiopharm Ulm'],
            'Buducnost': ['Buducnost VOLI'],
            'Turk Telekom': ['Turk Telekom BK'],
            'Slask Wroclaw': ['WKS Slask Wroclaw'],
            'Bourg-en-Bresse': ['JL Bourg'],
            'Partizan': ['Partizan NIS'],
            'Joventut': ['Club Joventut Badalona'],
            'Valencia': ['Valencia Basket'],
            'Bursaspor': ['Frutti Extra Bursaspor'],
            'Cedevita Olimpija': ['KK Cedevita Olimpija Ljubljana'],
            'Gran Canaria': ['Herbalife Gran Canaria'],
            'ASP Promitheas': ['Promitheas Patras BC'],
            'Basquet Club Andorra': ['MoraBanc Andorra'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.group_split(response, 1, 9)
        # results = Calculative.group_split(response, 1, 9)
        # print(results)

    def parse_Basketball_Czech_ZBL(self, response):
        ladder=[]
        teams={
            'Chance U19 W': ['BK Strakonice Chance Women U19 '],
            'Hradec Kralove W': ['Sokol Hradec Kralove Women'],
            'Ostrava W': ['SBS Ostrava Women'],
            'Levharti Chomutov W': ['Levhartice Chomutov Women'],
            'USK Prague W': ['ZVVZ USK Praha Women'],
            'Slovanka W': ['Basket Slovanka Women'],
            'Slavia Prague W': ['BLK Slavia Praha Women'],
            'Trutnov W': ['BK Loko Trutnov Women'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Cyprus_League(self, response):
        ladder=[]
        teams={
            'Apoel': ['APOEL Nicosia'],
            'Omonia': ['Omonia Nicosia'],
            'Anorthosis': ['Anorthosis Famagusta'],
            'AEK Larnaca': ['AEK Larnacas'],
            'Achilleas Kaimakli': ['Achilleas Kaimakliou'],
            'Apop': ['APOP Pafou'],
            'Etha BC': ['Etha Engomis'],
            'E.N. Paralimniou': ['Enosis Neon Paralimniou BC'],
            'ENP': ['Enosis Neon Paralimniou BC'],
            'Keravnos Strovolos': ['Keravnos BC'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_Bulgarian_NBL(self, response):
        ladder=[]
        teams={
            'Academic Bultex': ['Academic'],
            'Beroe': ['BC Beroe'],
            'Yambol': ['BC Yambol'],
            'Cherno More': ['Cherno More Ticha'],
            'Rilski Sportist': ['Rilski Sportist Samokov'],
            'Chernomorets': ['Chernomorets Burgas'],
            'BC Balkan': ['Balkan Botevgrad'],
            'Cherno More Varna': ['Cherno More Ticha'],
            'Academic Plovdiv': ['Academic'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Spanish_LEB_Oro(self, response):
        ladder=[]
        teams={
            'CB Valladolid': ['CB Ciudad de Valladolid'],
            'Amics Castello': ['TAU Castello'],
            'Caceres': ['Caceres Patrimonio de la Humanidad'],
            'Penas Huesca': ['Levitec Huesca'],
            'Palencia': ['Chocolates Trapa Palencia'],
            'CB Prat': ['CB Prat Joventut'],
            'Iraurgi Saski Baloia': ['Iraurgi SB'],
            'Basquet Coruna': ['Leyma Basquet Coruna'],
            'M. Alicante': ['HLA Alicante'],
            'Granada': ['Coviran Granada'],
            'Baloncesto Oviedo': ['Liberbank Oviedo Baloncesto'],
            'Mallorca Palma': ['Palmer Alma Mediterranea Palma'],
            'Estudiantes': ['Movistar Estudiantes'],
            'Valladolid': ['CB Ciudad de Valladolid'],
            'Forca Lleida CE': ['ICG Forca Lleida'],
            'Melilla': ['Club Melilla Baloncesto'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 15)
        # results = Calculative.compare(response, 2, 15)
        # print(results)

    def parse_Basketball_Spanish_ACB(self, response):
        ladder=[]
        teams={
            'Bilbao Basket': ['RETAbet Bilbao Basket'],
            'Cafes Candelas Breogan': ['Rio Breogan'],
            'Zaragoza': ['Casademont Zaragoza'],
            'Real Betis': ['Coosur Real Betis'],
            'Manresa BC': ['Baxi Manresa'],
            'CB Breogan Lugo': ['Rio Breogan'],
            'Saski Baskonia': ['TD Systems Baskonia Vitoria Gasteiz'],
            'Manresa': ['Baxi Manresa'],
            'Rio Natura Monbus': ['Monbus Obradoiro'],
            'Basket Zaragoza': ['Casademont Zaragoza'],
            'CB Murcia': ['UCAM Murcia'],
            'Fuenlabrada': ['Urbas Fuenlabrada'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 15)
        # results = Calculative.compare(response, 2, 15)
        # print(results)

    def parse_Basketball_Russian_Super_League(self, response):
        ladder=[]
        teams={
            'Ufimets': ['Ufimets Ufa'],
            'Temp Sumz Revda': ['TEMP-SUMZ Revda'],
            'Uralmash': ['Uralmash Yekaterinburg'],
            'BC Novosibirsk': ['BK Novosibirsk'],
            'Rodniki Izhevsk': ['Kupol Rodniki'],
            'BC Irkut': ['Irkutsk'],
            'Khimki': ['BC Khimki Moscow Region'],
            'Lokomotiv Kuban B': ['Lokomotiv Kuban TSOP'],
            'CSKA Moscow B': ['CSKA Moscow II'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_Norway_BLNO(self, response):
        ladder=[]
        teams={
            'Froeya': ['Froya'],
            'Baerum Basket': ['Baerum'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Latvian_Estonian_League(self, response):
        ladder=[]
        teams={
            'BC Tartu': ['Tartu Ulikool'],
            'Tallinna Kalev': ['Tallinna Kalev/TLU'],
            'Rakvere Tarvas': ['BC Rakvere Tarvas'],
            'Parnu': ['Parnu Sadam'],
            'Rapla': ['AVIS Utilitas Rapla'],
            'Kalev/Cramo': ['BC Kalev/Cramo'],
            'Valmiera/ORDO': ['Valmiera Glass VIA'],
            'Liepaja': ['BK Liepaja'],
            'TTU': ['TalTech Basketball'],
            'KK Viimsi': ['KK Viimsi/Sportland'],
            'BC Kalev': ['BC Kalev/Cramo'],
            'Ventspils': ['BK Ventspils'],
            'TTU Korvpalliklubi': ['TalTech Basketball'],
            'Valmiera Glass Via': ['Valmiera Glass VIA'],
            'Liepajas/Triobet': ['BK Liepaja'],
            'Rapla KK': ['AVIS Utilitas Rapla'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('**Old Standing Ladder**')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_Japanese_B_League_1(self, response):
        ladder=[]
        teams={
            'Shinshu Brave Warriors': ['Nagano Shinshu Brave Warriors'],
            'Ryukyu Golden Kings': ['Okinawa Ryukyu Golden Kings'],
            'Diamond Dolphins': ['Nagoya Diamond Dolphins'],
            'Niigata Albirex': ['Niigata Albirex BB'],
            'Aisin Seahorses': ['Mikawa Sea Horses'],
            'Shiga Lakestars': ['Shiga Lake Stars'],
            'Brave Thunders': ['Kawasaki Brave Thunders'],
            'Link Tochigi Brex': ['Utsunomiya Brex'],
            'Toyota Alvark': ['Alvark Tokyo'],
            'SeaHorses Mikawa': ['Mikawa Sea Horses'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 3, 19)
        # results = Calculative.compare(response, 3, 19)
        # print(results)

    def parse_Basketball_French_ProB_League(self, response):
        ladder=[]
        teams={
            'Evreux': ['ALM Evreux Basket'],
            'Denain': ['Denain Voltaire'],
            'Nantes': ['Hermine De Nantes'],
            'Lille Mb': ['Lille Metropole'],
            'Antibes': ['Antibes Sharks'],
            'Aix-Maurienne': ['Aix Maurienne Savoie Basket'],
            'Ada Blois Basket': ['ADA Blois Basket 41'],
            'Chalon/Saone': ['Elan Chalon'],
            'Boulazac': ['Boulazac Basket Dordogne'],
            'Tours': ['UTB Metropole'],
            'UJAP Quimper': ['Ujap Quimper 29'],
            'Nancy': ['SLUC Nancy'],
            'Saint-Vallier': ['Saint Vallier Basket Drome'],
            'ASC Denain-Voltaire': ['Denain Voltaire'],
            'Lille': ['Lille Metropole'],
            'Saint-Quentin': ['Saint-Quentin Basket-Ball'],
            'Rouen': ['Rouen Metropole Basket'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 15)
        # results = Calculative.compare(response, 2, 15)
        # print(results)

    def parse_Basketball_Chinese_CBA(self, response):
        ladder=[]
        teams={
            'Zhejiang Lions': ['Zhejiang Guangsha Lions'],
            'Guandong': ['Guangdong Southern Tigers'],
            'Qingdao': ['Qingdao DoubleStar Eagles'],
            'Beijing Ducks': ['Beijing Shougang Ducks'],
            'Xinjiang Flying Tigers': ['Xinjiang Guanghui Flying Tigers'],
            'Liaoning': ['Liaoning Flying Leopards'],
            'Tianjin Pioneers': ['Tianjin Ronggang Pioneers'],
            'Foshan': ['Guangzhou Loong Lions'],
            'Jilin': ['Jilin Northeast Tigers'],
            'Zhejiang Chouzhou': ['Zhejiang Golden Bulls'],
            'Fujian': ['Fujian SBS Xunxing'],
            'Nanjing Tongxi': ['Nanjing Tongxi Monkey King'],
            'Sichuan': ['Sichuan Jinqiang'],
            'Shanxi': ['Shanxi Loongs'],
            'Beikong': ['Beijing Royal Fighters'],
            'Shandong Hi-Speed Kirin': ['Shandong Heroes'],
            'Sichuan Blue Whales': ['Sichuan Jinqiang'],
            'Qingdao Eagles': ['Qingdao DoubleStar Eagles'],
            'Shenzhen Leopards': ['Shenzhen Aviators'],
            'Fujian Sturgeons': ['Fujian SBS Xunxing'],
            'Nanjing Monkey King': ['Nanjing Tongxi Monkey King'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 17)
        # results = Calculative.compare(response, 2, 17)
        # print(results)

    def parse_Basketball_Finnish_Korisliiga(self, response):
        ladder=[]
        teams={
            'Salon Vilpas': ['Salon Vilpas Vikings'],
            'Lapuan Korikobrat': ['Kobrat Lapua'],
            'Kataja': ['Kataja Basket'],
            'Namika Lahti': ['Lahti Basketball'],
            'Loimaa Bisons': ['LoKoKo Bisons'],
            'KTP Basket': ['KTP Basket Kotka'],
            'Pyrinto': ['Tampereen Pyrinto'],
            'Bc Nokia': ['BC Nokia'],
            'Kauhajoen Karhu': ['Kauhajoki Karhu'],
            'Kouvot': ['Kouvot Kouvola'],
            'Korihait': ['UU-Korihait Uusikaupunki'],
            'Hatay W': ['Hatayspor Women'],
            'Kobrat': ['Kobrat Lapua'],
            'Tampereen Pyrintoe': ['Tampereen Pyrinto'],
            'UU Korihait': ['UU-Korihait Uusikaupunki'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_Czech_NBL(self, response):
        ladder=[]
        teams={
            'Opava': ['BK Opava'],
            'Pardubice': ['BK JIP Pardubice'],
            'CEZ Nymburk': ['ERA Nymburk '],
            'Kolin': ['BC Geosan Kolin'],
            'Decin': ['BK ARMEX Decin'],
            'Usti Nad Labem': ['SLUNETA Usti nad Labem'],
            'BK Lions Jindrichuv Hradec': ['GBA Lions Jindrichuv Hradec'],
            'Basketball Brno': ['MMCITE Brno'],
            'NH Ostrava': ['BK Nova Hut Ostrava'],
            'Kralovsti Sokoli': ['Sokol Hradec Kralove'],
            'Nymburk': ['ERA Nymburk'],
            }

        for team in response.xpath("(//table)[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_FIBA_Eurocup_Women(self, response):
        ladder=[]
        teams={
            'Enisey Krasnoyarsk W': ['Enisey Krasnoyarsk Women'],
            'Fribourg W': ['BCF Elfic Fribourg Women'],
            'Prometey W': ['BC Prometey Women'],
            'Aydin W': ['Nesibe Aydin Women'],
            'PEAC-Pecs W': ['PEAC-Pecs Women'],
            'Ormanspor W': ['OGM Ormanspor Women'],
            'Nadezhda W': ['Nadezhda Orenburg Women'],
            'Ruzomberok W': ['MBK Ruzomberok Women'],
            'Olympiacos W': ['Olympiakos Piraeus BC Women'],
            'Zabiny Brno W': ['BK Zabiny Brno Women'],
            'Polkowice W': ['MKS Polkowice Women'],
            'Braine W': ['Mithra Castors Braine Women'],
            'Flammes Carolo W': ['Flammes Carolo Basket Ardennes Women'],
            'Mersin BSB W': ['CBK Mersin Yenisehir Belediyesi Women'],
            'Bourges W': ['Bourges Women'],
            'Lyon W': ['Lyon Asvel Basket Women'],
            'NIKA Syktyvkar W': ['Nika Siktivkar Women'],
            'Valencia W': ['Valencia B.C. Women'],
            'ESB Villeneuve W': ["ESB Villeneuve-d'Ascq Women"],
            'AZS UMCS Lublin W': ['AZS-UMCS Lublin Women'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 8, 44)
        # results = Calculative.compare(response, 8, 44)
        # print(results)

    def parse_Basketball_EuroLeague(self, response):
        ladder=[]
        teams={
            'Crvena Zvezda': ['Crvena Zvezda MTS Belgrade'],
            'Alba Berlin': ['ALBA Berlin'],
            'Panathinaikos': ['Panathinaikos OPAP Athens'],
            'Unics Kazan': ['UNICS Kazan'],
            'Barcelona': ['FC Barcelona'],
            'Baskonia': ['TD Systems Baskonia Vitoria Gasteiz'],
            'Zenit Petersburg': ['Zenit Saint-Petersburg'],
            'Fenerbahce Ulker': ['Fenerbahce BEKO'],
            'Monaco': ['AS Monaco Basket'],
            'Anadolu Efes SK': ['Anadolu Efes'],
            'Zalgiris Kaunas': ['BC Zalgiris'],
            'Olympiacos': ['Olympiacos BC'],
            'ASVEL': ['LDLC ASVEL Lyon-Villeurbanne'],
            'Maccabi Tel Aviv': ['Maccabi Playtika Tel Aviv'],
            'Olimpia Milano': ['AX Armani Exchange Olimpia Milan'],
            'Bayern': ['FC Bayern Munchen'],
            'BC Zenit': ['Zenit Saint-Petersburg'],
            'Fenerbahce': ['Fenerbahce BEKO'],
            'ASVEL Lyon-Villeurbanne': ['LDLC ASVEL Lyon-Villeurbanne'],
            'Crvena Zvezda Beograd': ['Crvena Zvezda MTS Belgrade'],
            'Saski Baskonia': ['TD Systems Baskonia Vitoria Gasteiz'],
            'AX Armani Exchange Milano': ['AX Armani Exchange Olimpia Milan'],
            'Olympiacos B.C.': ['Olympiacos BC'],

            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 15)
        # results = Calculative.compare(response, 2, 15)
        # print(results)

    def parse_Basketball_Danish_Basket_Ligaen(self, response):
        ladder=[]
        teams={
            'Randers': ['Randers Cimbria'],
            'Horsens': ['Horsens IC'],
            'Stevnsgade': ['theView Copenhagen'],
            'Copenhagen Wolfpack': ['BMS Herlev Wolfpack'],
            'Svendborg': ['Svendborg Rabbits'],
            'Bakken Bears': ['Bears Academy'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Baskebtall_Bahraini_Premier_League(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//div[@class='standingdetails']/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 10)
        # results = Calculative.compare(response, 0, 10)
        # print(results)

    def parse_Baskebtall_BNXT_League(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table/tbody/tr/td/a/span[1]/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 10)
        # results = Calculative.compare(response, 0, 10)
        # print(results)

    def parse_Basketball_Argentinian_Super_20(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 17)
        # results = Calculative.compare(response, 2, 17)
        # print(results)

    def parse_Baskebtall_ABA_League(self, response):
        ladder=[]
        teams={
            'Split': ['KK Split'],
            'Borac': ['KK Borac Cacak'],
            'Crvena Zvezda': ['Crvena Zvezda MTS Belgrade'],
            'FMP Beograd': ['KK FMP'],
            'KK Krka Novo Mesto': ['Krka'],
            'Igokea Aleksandrovac': ['Igokea'],
            'Partizan': ['Partizan NIS'],
            'Mega Mozzart': ['KK Mega Basket'],
            'Cedevita Olimpija': ['KK Cedevita Olimpija Ljubljana'],
            'Crvena Zvezda Beograd': ['Crvena Zvezda MTS Belgrade'],
            'KK Studentski centar': ['KK SC Derby'],
            'FMP': ['KK FMP'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_Italian_A2_Supercup(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        # # Is in 2 parts, see if ladders work without non-league style

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_Club_Friendly_Men(self, response):
        ladder=[]
        teams={
            'BC Irkut': ['Irkutsk'],
            'Temp Sumz Revda': ['TEMP-SUMZ Revda'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_Polish_PLK(self, response):
        ladder=[]
        teams={
            'TBV Start Lublin': ['Start Lublin'],
            'Ostrow Wielkopolski': ['Arged BM Slam Stal Ostrow Wielkopolski'],
            'Slask Wroclaw': ['WKS Slask Wroclaw'],
            'Astoria Bydgoszcz': ['Enea Astoria Bydgoszcz'],
            'King Szczecin': ['KING Wilki Morskie Szczecin'],
            'Zielona Gora': ['Enea Zastal BC Zielona Gora'],
            'Czarni Slupsk': ['STK Czarni Slupsk'],
            'Rosa Radom': ['HydroTruck Radom'],
            'MKS Dabrowa Gornicza': ['Dabrowa Gornicza'],
            'Stelmet Zielona Gora': ['Enea Zastal BC Zielona Gora'],
            'Spojnia Stargard': ['PGE Spojnia Stargard'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 14)
        # results = Calculative.compare(response, 2, 14)
        # print(results)

    def parse_Basketball_Mexican_LNBP(self, response):
        ladder=[]
        teams={
            'Fuerza Regia': ['Fuerza Regia de Monterrey'],
            'Abejas': ['Abejas de Leon'],
            'Soles De Mexicali': ['Soles de Mexicali'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Brazilian_Campeonato_Paulista(self, response):
        ladder=[]
        teams={
            'Pinheiros': ['EC Pinheiros'],
            'Rio Claro': ['ACBD Rio Claro'],
            'Franca': ['Sesi SP/Franca BC'],
            'Osasco': ['Osasco Basket'],
            'LSB / B2B': ['Liga Sorocabana'],
            'Mogi': ['Mogi das Cruzes'],
            'Bauru': ['ZOPONE Bauru Basket'],
            }

        for team in response.xpath("//div[@class='standingsContent']/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Uruguayan(self, response):
        ladder=[]
        teams={
            'Tabare': ['Club Atletico Tabare'],
            'L.Borges': ['Larre Borges'],
            'U.Atletica': ['Union Atletica'],
            'Sayago': ['CS Deportivo Sayago'],
            }

        for team in response.xpath("//div[@class='standingLink']/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_Dominican_Republic(self, response):
        ladder=[]
        teams={
            'Huracanes del Atlántico': ['Huracanes del Atlantico'],
            'TitanesdelDistritoNacional': ['Titanes del Licey'],
            'RealesDeLaVega': ['Reales de La Vega'],
            'LeonesDeSantoDomingo': ['Leones de Santo Domingo'],
            'IndiosdeSanFrancisco': ['Indios de San Francisco'],
            'SolesdeSantoDomingoEste': ['Soles de Santo Domingo Este'],
            'MetrosdeSantiago': ['Metros de Santiago'],
            'CañerosdelEste': ['Caneros del Este'],
            }

        ## If need to fix

        # for team in response.xpath("//table[@class='table table-hover table-sm text-default-emp']/tbody/tr/td/a/text()").getall():

        #     # normalize-space returns empty string in this case, look into at further track
        #     # team=competitor.xpath("normalize-space").get()
        #     team = team.replace(' ', '').replace('\n', '')

        # Normalize space was getting rid of all text
        for team in response.xpath("normalize-space(//table[@class='table table-hover table-sm text-default-emp']/tbody/tr/td/a/text())").getall():
            if team =='':
                continue
            elif team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 7)
        # results = Calculative.compare(response, 0, 7)
        # print(results)

    def parse_Basketball_Australian_Big_V(self, response):
        ladder=[]
        teams={
            'Hume': ['Hume City Broadmeadows Broncos'],
            'Wyndham': ['Wyndham Basketball'],
            'Keilor': ['Keilor Thunder'],
            'Sunbury': ['Sunbury Jets'],
            'Casey': ['Casey Cavaliers'],
            'McKinnon': ['McKinnon Cougars'],
            'Chelsea': ['Chelsea Gulls'],
            'Hawthorn': ['Hawthorn Magic'],
            'Blackburn': ['Blackburn Vikings'],
            }

        ## If need to fix

        # for team in response.xpath("//section[@id='ladder']/div/div/div/div/div/div/h5"):
        #     if team.xpath("normalize-space(.//text())").get() == 'Hume':
        #         ladder.append('Hume City Broadmeadows Broncos')

        for team in response.xpath("normalize-space(//section[@id='ladder']/div/div/div/div/div/div/h5/text())").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Chinese_NBL(self, response):
        ladder=[]
        teams={
            'Guangxi': ['Guangxi Weizhuang'],
            'Henan': ['Henan Shedian Laojiu'],
            'Xinjiang': ['Xinjiang Tianshan Eagle'],
            'Wuhan': ['Wuhan Dangdai'],
            'Anhui P.': ['Putian Xingfa'],
            'Jiangsu YS': ['Jiangsu Yannan Suke'],
            'Hunan': ['Hunan Jinjian Miye'],
            'Shaanxi': ['Shaanxi Xinda'],
            }

        for team in response.xpath("//div[@class='standingdetails']/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_PBA_Philippine_Cup(self, response):
        ladder=[]
        teams={
            'Ginebra Kings': ['Barangay Ginebra San Miguel'],
            'Blackwater Elite': ['Blackwater Bossing'],
            'Nlex Road Warriors': ['NLEX Road Warriors'],
            'Rain or Shine Elasto Painters': ['Rain Or Shine Elasto Painters'],
            'Rain Or Shine Paint.': ['Rain Or Shine Elasto Painters'],
            'Global Port': ['NorthPort Batang Pier'],
            'B-Meg Llamados': ['Magnolia Hotshots Pambansang Manok'], 
            'Magnolia Hotshots': ['Magnolia Hotshots Pambansang Manok'],
            'Barako EC Masters': ['Phoenix Super LPG Fuel Masters'],
            'Phoenix Fuel Masters': ['Phoenix Super LPG Fuel Masters'],
            'Columbian Dyip': ['Terrafirma Dyip'],
            "Talk 'N Text Tropang Texters": ['TnT Tropang Giga'],
            "Talk N Text": ['TnT Tropang Giga'],
            'Ginebra San Miguel': ['Barangay Ginebra San Miguel'],
            }

        for team in response.xpath("(//table/tbody)[1]/tr/td[3]/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_New_Zealand_NBL(self, response):
        ladder=[]
        teams={
            'Bay Hawks': ['Taylor Hawks'],
            '': [''],
            }

        for team in response.xpath("(//table/tbody)[1]/tr/td[3]/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Chilean_LNB(self, response):
        ladder=[]
        teams={
            'Quilicura': ['CD Quilicura Basket'],
            'Leones Quilpue': ['Colegio Los Leones'],
            'Deportivo Valdivia': ['C. D. Deportes Valdivia'],
            'Temuco': ['C.D. AB Temuco'],
            'Espanol De Talca': ['C. D. Espanol de Talca'],
            'U. De Concepcion': ['Universidad de Concepcion'],
            'Catolica': ['Club Deportivo Universidad Catolica'],
            'Las Animas': ['C. D. Las Animas'],
            'CD Puerto Varas': ['CD Atletico PTO. Varas'],
            'Puente Alto': ['Mun. Puente Alto'],
            'Tinguiririca': ['Tinguiririca San Fernando'],
            }

        for team in response.xpath("(//table/tbody)[1]/tr[@class='sp-livetable__tableRow spm-dataRow']/td[3]/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 11)
        # results = Calculative.compare(response, 1, 11)
        # print(results)

    def parse_Basketball_NBL1(self, response):
        group_ladder = response.request.meta['group_ladder']
        ladder = []
        loop_count = response.request.meta['loop_count']
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath('//tbody/tr/'):
            if team.xpath('.//th/div/span/text()').get() == '':
                if team in teams.keys():
                    ladder.append({'Name': teams[team], 'W': team.xpath('.//td[3]/text()').get()})
                else:
                    ladder.append({'Name': [team], 'W': team.xpath('.//td[3]/text()').get()})
            else:
                ladder.append(team.xpath('.//text()').get())

        group_ladder.append(ladder)

        # Repeat with next district
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
        # Order all districts in terms of wins
        sorted_ladder = []
        for team in sorted(ladder, key=lambda x: int(x['W']), reverse=True):
            sorted_ladder.append(team['Name'])

        response.request.meta['ladder'] = sorted_ladder
        Calculative.compare(response, 9, 47)
        # results = Calculative.compare(response, 9, 47)
        # print(results)

    def parse_Basketball_Argentina_La_Liga(self, response):
        ## Some teams left the league?
        ladder=[]
        teams={
            'Atenas (Patagones)': ['Atenas'],
            'Racing Chivilcoy': ['Racing de Chivilcoy'],
            'Colón (Santa Fe)': ['Colon Santa Fe'],
            'Sportivo América': ['Sportivo America'],
            'San Isidro (San Francisco)': ['San Isidro'],
            'Villa San Martín': ['Club Atletico Villa San Martin'],
            'Del Progreso': ['Club Del Progreso'],
            'Lanús': ['Club Atletico Lanus'],
            'Gimnasia y Esgrima (La Plata)': ['Gimnasia y Esgrima La Plata'],
            'Echagüe (Paraná)': ['Echague'],
            'Unión (Santa Fe)': ['Union De Santa Fe'],
            'Independiente BBC': ['Independiente Santiago Del Estero'],
            'Estudiantes (Tucumán)': ['Club Atletico Estudiantes de Tucuman'],
            'Quilmes (Mar del Plata)': ['Club Atletico Quilmes'],
            'Villa Mitre': ['Club Villa Mitre de Bahia Blanca'],
            'Barrio Parque (Córdoba)': ['Barrio Parque'],
            'Estudiantes (Olavarría)': ['Estudiantes de Olavarria'],
            'Estudiantes (Concordia)': ['Estudiantes Concordia'],
            'Ciclista (Junín)': ['Ciclista Juninense'],
            'Zárate Basket': ['Zarate Basket Club Union de la Ciudad de Zarate'],
            'Pergamino Basquet': ['Asociacion Civil Club Pergamino Basquet'],
            'Libertad (Sunchales)': ['Club Deportivo Libertad'],
            'Ameghino Basket': ['Atletico Juventud Florentino Ameghino de Villa Maria'],
            'Parque Sur (CdU)': ['Parque Sur'],
            'Central Argentino Olímpico': ['Central Argentino Olimpico Ceres'],
            'Rivadavia (Mendoza)': ['Centro Deportivo Rivadavia de Mendoza'],
            'Jáchal': ['Jachal Club De San Juan'],
            'Rocamora (C. del Uruguay)': ['Tomas de Rocamora'],
            'Bahía Basket (Bahía Blanca)': ['Weber Bahia'],
            }

        for team in response.xpath("//tr[position()>2]/td[3]/p/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 4, 25)
        # results = Calculative.compare(response, 4, 25)
        # print(results)

    def parse_Basketball_Australian_NBL(self, response):
        ladder=[]
        teams={
            'The Hawks': ['Illawarra Hawks'],
            'South East Melbourne Phoenix': ['S.E. Melbourne Phoenix'],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_North_Macedonia_Prva_League(self, response):
        ladder=[]
        teams={
            'MZT Skopje': ['MZT Skopje Aerodom'],
            'KK Pelister': ['Pelister'],
            'Euro Nickel': ['KK EuroNickel'],
            'TFT Skopje': ['TFT Basketball Club'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_Turkish_TBSL(self, response):
        ladder=[]
        teams={
            'Socar Spor': ['Petkim Spor'],
            'Merkezefendi': ['Merkezefendi Belediyesi Denizli Basket'],
            'Tofas': ['Tofas SK'],
            'Afyon Belediye': ['Afyon Belediye '],
            'Darussafaka Ct': ['Darussafaka Tekfen '],
            'Besiktas CT': ['Besiktas Icrypex'],
            'Gaziantep B.B.': ['Royal Hali Gaziantep BB'],
            'Galatasaray CC': ['Galatasaray NEF'],
            'Fenerbahce': ['Fenerbahce BEKO'],
            'Buyukcekmece': ['Demir Insaat Buyukcekmece'],
            'Gaziantep BB': ['Royal Hali Gaziantep BB'],
            'Besiktas': ['Besiktas Icrypex'],
            'Yalovaspor BK': ['Semt77 Yalova Belediyespor'],
            'Bursaspor': ['Frutti Extra Bursaspor'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 14)
        # results = Calculative.compare(response, 2, 14)
        # print(results)

    def parse_Basketball_PBA_Governors_Cup(self, response):
        ladder=[]
        teams={
            'Nlex Road Warriors': ['NLEX Road Warriors'],
            'Magnolia Hotshots': ['Magnolia Hotshots Pambansang Manok'],
            'Talk N Text': ['TnT Tropang Giga'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_VTB_United_League(self, response):
        ladder=[]
        teams={
            'Zenit Petersburg': ['Zenit Saint-Petersburg'],
            'Parma': ['Parma Perm'],
            'Tsmoki-Minsk': ['BC Tsmoki-Minsk'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_German_Pro_A(self, response):
        ladder=[]
        teams={
            'TBB Trier': ['ROMERSTROM Gladiators Trier'],
            'Bg Karlsruhe': ['PS Karlsruhe LIONS'],
            'Paderborn B.': ['Uni Baskets Paderborn'],
            'Panthers Schwenningen': ['Wiha Panthers Schwenningen'],
            'Jena': ['Science City Jena'],
            'Tubingen': ['Tigers Tubingen'],
            'Sc Rasta Vechta': ['Rasta Vechta'],
            'Bochum': ['VfL SparkassenStars Bochum'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 15)
        # results = Calculative.compare(response, 2, 15)
        # print(results)

    def parse_Basketball_Polish_League_Women(self, response):
        ladder=[]
        teams={
            'GTK Gdynia W': ['GTK Arka Gdynia Women'],
            'Gorzow Wielkopolski W': ['AZS-AJP Gorzow Wielkopolski Women'],
            'CTL Zaglebie Sosnowiec W': ['CTL Zaglebie Sosnowiec Women'],
            'AZS Poznan W': ['ENEA AZS Poznan Women'],
            'Sleza Wroclaw W': ['1KS Sleza Basket Women'],
            'AZS UMCS Lublin W': ['AZS-UMCS Lublin Women'],
            'Polonia Warszawa W': ['SKK Polonia Warszawa Women'],
            'Torun W': ['Energa Torun Women'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_Austrian_Bundesliga(self, response):
        ladder=[]
        teams={
            'Graz UBSC': ['UBSC Raiffeisen Graz'],
            'Traiskirchen': ['Arkadia Traiskirchen Lions'],
            'Wels': ['Raiffeisen Flyers Wels'],
            'Vienna': ['BC GGMT Vienna'],
            'St. Polten': ['SKN St. Polten'],
            'Kapfenberg': ['Ece Bulls Kapfenberg'],
            'Gmunden': ['Swans Gmunden'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Italian_Serie_A(self, response):
        ladder=[]
        teams={
            'Treviso': ['Nutribullet Treviso Basket'],
            'BK Costa W': ['Limonta Costa Masnaga Women'],
            'Germani Brescia': ['Germani Brescia Leonessa'],
            'Carpegna Prosciutto Pesaro': ['Carpegna Prosciutto Basket Pesaro'],
            'Vanoli Basket Cremona': ['Vanoli Cremona'],
            'GeVi Napoli Basket': ['Gevi Napoli'],
            'NutriBullet Treviso Basket': ['Nutribullet Treviso Basket'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 14)
        # results = Calculative.compare(response, 2, 14)
        # print(results)

    def parse_Basketball_Italian_Serie_A_Women(self, response):
        ladder=[]
        teams={
            'BK Costa W': ['Limonta Costa Masnaga Women'],
            'Schio W': ['Famila Basket Schio Women'],
            'Sassari W': ['Dinamo Sassari Women'],
            'Magnolia Campobasso W': ['La Molisana Magnolia Campobasso Women'],
            'PF Schio W': ['Famila Basket Schio Women ','Famila Basket Schio Women'],
            'Moncalieri W': ['Akronos Moncalieri Women '],
            'Faenza W': ['E-Work Faenza Women'],
            'Broni W': ['P.F. Broni 93 Women'],
            'San Martino W': ['Fila San Martino di Lupari Women'],
            'Venezia W': ['Umana Reyer Venezia Women'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 12)
        # results = Calculative.compare(response, 1, 12)
        # print(results)

    def parse_Basketball_Bosnia_Herzegovina_1_Division(self, response):
        ladder=[]
        teams={
            'Posusje': ['HKK Posusje'],
            'Spars Sarajevo': ['OKK Spars Realway'],
            'Mrkonjic Grad': ['KK Mladost Mrkonjic Grad'],
            'Sloboda': ['OKK Sloboda Tuzla'],
            'HKK Z. Mostar': ['HKK Zrinjski Mostar'],
            'Leotar Trebinje': ['KK Leotar'],
            'Siroki Brijeg': ['KK Siroki Brijeg'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 11)
        # results = Calculative.compare(response, 1, 11)
        # print(results)

    def parse_Basketball_Slovenian_League(self, response):
        ladder=[]
        teams={
            'Sencur Gorenjska': ['KK Sencur'],
            'Zlatorog': ['Zlatorog Lasko'],
            'KK Krka Novo Mesto': ['Krka'],
            'Podcetrtek': ['Terme Olimia Podcetrtek'],
            'Kk Helios Domzale': ['KK Helios Suns'],
            'Helios Domzale': ['KK Helios Suns'],
            'KK Tajfun Sentjur': ['KK Sentjur'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Basketball_Portuguese_LPB(self, response):
        ladder=[]
        teams={
            'Benfica': ['Benfica Basket'],
            'Imortal/Algarexperienc': ['Imortal LUZiGAS'],
            'Ovarense': ['Ovarense Basquetebol'],
            'Lusitania': ['Lusitania Basket'],
            'Povoa': ['CD Povoa'],
            'Vitoria': ['Vitoria SC'],
            'Madeira': ['CAB Madeira'],
            'Academia': ['Academica/Efapel'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_Australian_WNBL(self, response):
        ladder=[]
        teams={
            'Adelaide Lightning W': ['Adelaide Lightning Women'],
            'Perth Lynx W': ['Perth Lynx Women'],
            'Canberra Capitals W': ['UC Capitals Women'],
            'Bendigo W': ['Bendigo Spirit Women'],
            'Townsville W': ['Townsville Fire Women'],
            'Southside W': ['Southside Flyers Women'],
            'Sydney W': ['Sydney Uni Flames Women'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('Last position played 0 games, keep eye on if they start')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 7)
        # results = Calculative.compare(response, 0, 7)
        # print(results)

    def parse_Basketball_British_BBL_Cup(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//div[@class='sp-livetable__wrap']/table[1]/tbody/tr[position()>1]"):
            name = team.xpath('.//td/div/div/div/a/text()').get()
            
            if name in teams.keys():
                ladder.append({'Name': teams[name], 'W': team.xpath('.//td[@title="win"]/div/text()').get(), 'L': team.xpath('.//td[@title="loss"]/div/text()').get()})
            else:
                ladder.append({'Name': [name], 'W': team.xpath('.//td[@title="win"]/div/text()').get(), 'L': team.xpath('.//td[@title="loss"]/div/text()').get()})

        sorted_ladder = []
        for team in sorted(ladder, key=lambda x: int(x['W']), reverse=True):
            sorted_ladder.append(team['Name'])

        response.request.meta['ladder']=sorted_ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

class Rugby_Union():

    # def parse_Rugby_Union_(self, response):
    #     ladder=[]

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team == '':
    #             ladder.append()
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )

    # def parse_Rugby_Union_(self, response):
    #     ladder=[]
    #     teams={
    #         '': [''],
    #         '': [''],
    #         '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)

    def parse_Rugby_Union_The_Six_Nations(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 5)
        # results = Calculative.compare(response, , )
        # print(results)

    def parse_Rugby_Union_European_Champions_Cup(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//tbody/tr/td"):
            if team.xpath(".//a"):
                team = team.xpath(".//a/span/span[1]/text()").get()
                if team in teams.keys():
                    ladder.append(teams[team])
                else:
                    ladder.append([team])
            else:
                team = team.xpath(".//span/span[1]/text()").get()
                if team in teams.keys():
                    ladder.append(teams[team])
                else:
                    ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        response.request.meta['ladder']=ladder
        Calculative.group_split(response, 2, 10)
        # results = Calculative.group_split(response, 2, 10)
        # print(results)

    def parse_Rugby_Union_Womens_Sevens(self, response):
        ladder=[]
        teams={
            ## Portugal not on the ladder yet
            'Ireland 7s': ['Ireland '],
            'Poland 7s': ['Poland '],
            'Russia 7s': ['Russia '],
            'Brazil 7s': ['Brazil '],
            'Canada 7s': ['Canada'],
            'England 7s': ['England'],
            'USA 7s': ['USA '],
            'France 7s': ['France '],
            'Spain 7s': ['Spain '],
            'Australia 7s': ['Australia '],
            'Belgium 7s': ['Belgium '],
            }

        for team in response.xpath("//tbody/tr/td/a/span[2]/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        print(' Bottom 3 teams played 0 games so far')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 9)
        # results = Calculative.compare(response, 2, 9)
        # print(results)

    def parse_Rugby_Union_World_Rugby_Sevens(self, response):
        ladder=[]
        teams={
            'Canada 7s': ['Canada'],
            'Scotland 7s': ['Scotland'],
            'Australia 7s': ['Australia ','Australia'],
            'Kenya 7s': ['Kenya '],
            'France 7s': ['France ','France'],
            'Wales 7s': ['Wales '],
            'England 7s': ['England '],
            'Japan 7s': ['Japan '],
            'Ireland 7s': ['Ireland'],
            'Germany 7s': ['Germany'],
            'Argentina 7s': ['Argentina ','Argentina'],
            'Jamaica 7s': ['Jamaica '],
            'USA 7s': ['USA'],
            'Spain 7s': ['Spain'],

            }

        for team in response.xpath("//tbody/tr/td/a/span[2]/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        print(' Bottom 4 teams played 0 games so far')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 3, 12)
        # results = Calculative.compare(response, 3, 12)
        # print(results)

    def parse_Rugby_Union_French_Pro_D2(self, response):
        ladder=[]
        teams={
            'Rouen Normandie': ['Rouen Normandy', 'Rouen Normandy '],
            'Vannes': ['Rugby Club Vannes','Rugby Club Vannes '],
            'MN Montauban': ['US Montalbanaise','US Montalbanaise '],
            'Oyonnax': ['US Oyonnax ','US Oyonnax'],
            'Grenoble': ['Fc Grenoble Rugby ','FC Grenoble Rugby ','FC Grenoble Rugby'],
            'Carcassonnaise': ['US Carcassonne','US Carcassonne '],
            'Mont-de-Marsan': ['Stade Montois Rugby ','Stade Montois Rugby'],
            'Narbonne': ['RC Narbonne ','RC Narbonne'],
            'Bourg-en-Bresse': ['US Bressane ','US Bressane'],
            'USON Nevers': ['Uson Nevers ', 'Uson Nevers'],
            'Colomiers': ['Colomiers Rugby'],
            'Beziers': ['AS Beziers Herault'],
            'Aurillac': ['Stade Aurillacois'],
            'Aviron Bayonnais': ['Aviron Bayonne', 'Aviron Bayonne '],
            'Provence Rugby': ['Provence Rugby '],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 12)
        # results = Calculative.compare(response, 2, 12)
        # print(results)

    def parse_Rugby_Union_Gallagher_Premiership(self, response):
        ladder=[]
        teams={
                'Sale': ['Sale Sharks ', 'Sale Sharks'],
                'Exeter Chiefs': ['Exeter RC Chiefs ', 'Exeter RC Chiefs'],
                'Gloucester': ['Gloucester Rugby', 'Gloucester Rugby '],
                'Leicester Tigers': ['Leicester Tigers ','Leicester Tigers'],
                'Newcastle Falcons': ['Newcastle Falcons ', 'Newcastle Falcons'],
                'London Irish': ['London Irish ','London Irish'],
                'Bristol': ['Bristol RC Bears', 'Bristol RC Bears '],
                'Sale Sharks ': ['Sale Sharks'],
                'Harlequins': ['Harlequins FC','Harlequins FC '],
                'Saracens': ['Saracens RFC ','Saracens RFC'],
                'Bath': ['Bath Rugby', 'Bath Rugby '],
                'Worcester Warriors': ['Worcester Warriors RFC', 'Worcester Warriors RFC '],
                'Wasps': ['Wasps Rugby','Wasps Rugby '],
                'Northampton Saints': ['Northampton Saints ', 'Northampton Saints'],
                
            }


        for team in response.xpath("//tbody/tr/td/a/span/span[1]/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 10)
        # results = Calculative.compare(response, 2, 10)
        # print(results)

    def parse_Rugby_Union_New_Zealand_NPC(self, response):

        # Imbalanced league. Some teams aren't playing as much through the season as the others
        # Found when breaking down xpath to take

        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        ## If need to fix

        # for team in response.xpath("//div[@class='sp-livetable__wrap']"):
        #     ext = team.xpath('.//tbody/tr')
        #     name = ext.xpath('.//td/a/text()').get()
        #     if name == '':
        #         name = ''

        #     temp = []
        #     for added in ladder:
        #         temp.append(added)
        #     temp.append({'Name': name, 'W':ext.xpath('.//td[@class="nba_win st-br"]/text()').get(), 'L':ext.xpath('.//td[@class="nba_lost st-br"]/text()').get()})
        #     ladder = temp
        #     # print(temp)

        for team in response.xpath("//div[@class='sp-livetable__wrap']"):
            ext = team.xpath('.//tbody/tr')
            name = ext.xpath('.//td/a/text()').get()

            if name in teams.keys():
                ladder.append({'Name': teams[name], 'W':ext.xpath('.//td[@class="nba_win st-br"]/text()').get(), 'L':ext.xpath('.//td[@class="nba_lost st-br"]/text()').get()})
            else:
                ladder.append({'Name': [name], 'W':ext.xpath('.//td[@class="nba_win st-br"]/text()').get(), 'L':ext.xpath('.//td[@class="nba_lost st-br"]/text()').get()})

        sorted_ladder = []
        for team in sorted(ladder, key=lambda x: int(x['W']), reverse=True):
            sorted_ladder.append(team['Name'])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        print('**Found some teams play less through the league')
        response.request.meta['ladder']=sorted_ladder
        Calculative.compare(response, 1, 11)
        # results = Calculative.compare(response, 1, 11)
        # print(results)

    def parse_Rugby_Union_French_Top_14(self, response):
        ladder=[]
        teams={
            'Clermont Auvergne': ['Asm Clermont Auvergne'],
            'Section Paloise': ['Pau', 'Section Paloise'],
            'Biarritz Olympique': ['Biarritz','Biarritz Olympique', 'Biarritz Olympique '],
            'Bordeaux-Begles': ['Union Bordeaux Begles ', 'Union Bordeaux Begles'],
            'Racing-Metro 92': ['Racing 92', 'Racing 92 '],
            'RC Toulonnais': ['Toulon','RC Toulonnais','RC Toulonnais '],
            'Castres Olympique': ['Castres', 'Castres Olympique'],
            'Stade Francais Paris': ['Stade Francais Paris ','Stade Francais Paris'],
            'Stade Toulousain': ['Stade Toulousain ', 'Stade Toulousain'],
            'Lyon Rugby': ['Lyon Ou ', 'Lyon Ou'],
            'Perpignan': ['USA Perpignan','USA Perpignan '],
            'Brive': ['AC Brive', 'AC Brive '],
            'Montpellier': ['Montpellier Herault Rugby ', 'Montpellier Herault Rugby'],
            'La Rochelle': ['Stade Rochelais ','Stade Rochelais'],
            'Section Paloise': ['Section Paloise ', 'Section Paloise'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 3, 11)
        # results = Calculative.compare(response, 3, 11)
        # print(results)

    def parse_Rugby_Union_Currie_Cup(self, response):
        ladder=[]
        teams={
            'Blue Bulls': ['Bulls', 'Blue Bulls', 'Blue Bulls '],
            'Lions': ['Golden Lions', 'Golden Lions '],
            'Pumas': ['Ford Pumas'],
            'Sharks': ['Sharks B', 'Sharks B '],
            'Western Province': ['DHL Western Province', 'DHL Western Province '],
            'Cheetahs': ['Free State Cheetahs'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 6)
        # results = Calculative.compare(response, 1, 6)
        # print(results)

    def parse_Rugby_Union_Rugby_Championship(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 3)
        # results = Calculative.compare(response, 0, 3)
        # print(results)

    def parse_Rugby_Union_United_Rugby_Championship(self, response):
        ladder=[]
        teams={
            'Munster Rugby': ['Munster', 'Munster '],
            'Leinster Rugby': ['Leinster','Leinster '],
            'Benetton Treviso': ['Benetton Treviso ','Benetton Treviso'],
            'Cardiff Blues': ['Cardiff Rugby','Cardiff Rugby '],
            'Bulls': ['Blue Bulls', 'Blue Bulls '],
            'Ulster Rugby': ['Ulster Rugby ', 'Ulster Rugby'],
            'Scarlets': ['Scarlets ','Scarlets'],
            'Lions': ['Lions ', 'Lions'],
            'Sharks': ['The Sharks'],
            'Zebre': ['Zebre '],
            'Edinburgh Rugby': ['Edinburgh Rugby '],
            'Glasgow Warriors': ['Glasgow Warriors '],
            'Ospreys': ['Ospreys '],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 3, 12)
        # results = Calculative.compare(response, 3, 12)
        # print(results)

    def parse_Rugby_Union_AIL_Division_1A(self, response):
        ladder=[]
        teams={
            'Cork Con': ['Cork Constitution'],
            'University College Cork': ['Ucc'],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('\n"Check Win Markets, Match Betting to bet. Rugby Union shows Line Betting instead."')
        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 8)
        # results = Calculative.compare(response, 2, 8)
        # print(results)

class Basketball_US():

    # def parse_Basketball_US_(self, response):
    #     ladder=[]

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team == '':
    #             ladder.append()
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )

    # def parse_Basketball_(self, response):
    #     ladder=[]
    #     teams={
    #         '': [''],
    #         '': [''],
    #         '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)

    def parse_Basketball_NBA_Summer_League(self, response):
        ladder=[]
        teams={
            'Los Angeles Clippers': ['LA Clippers'],
            'Portland Trailblazers': ['Portland Trail Blazers'],
            }

        print('**Originally had xpath "Take all standings less than 31" which would have done if bottom teams stopped continuing but looks good, now started. Check')
        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 4, 27)
        # results = Calculative.compare(response, 4, 27)
        # print(results)

    # Dissapeared quick
    def parse_Basketball_Big3_Basketball_Matches(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        # # Check if xPath /tbody works
        for team in response.xpath("(//table/tbody)[1]/tr/td[3]/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Basketball_US_NBA(self, response):
        ladder=[]
        teams={
            'Portland Trailblazers': ['Portland Trail Blazers'],
            'LA Clippers': ['Los Angeles Clippers'],
            'LA Lakers': ['Los Angeles Lakers']
            }

        for team in response.xpath("//div[@id='standings_1a']/table[starts-with(@class, 'blocks')]"):
            ext = team.xpath('.//tbody/tr')
            name = ext.xpath('.//td/a/text()').get()

            if name in teams.keys():
                ladder.append({'Name': teams[name], 'W':ext.xpath('.//td[@class="nba_win st-br"]/text()').get(), 'L':ext.xpath('.//td[@class="nba_lost st-br"]/text()').get()})
            else:
                ladder.append({'Name': [name], 'W':ext.xpath('.//td[@class="nba_win st-br"]/text()').get(), 'L':ext.xpath('.//td[@class="nba_lost st-br"]/text()').get()})

        sorted_ladder = []
        for team in sorted(ladder, key=lambda x: int(x['W']), reverse=True):
            sorted_ladder.append(team['Name'])

        response.request.meta['ladder']=sorted_ladder
        Calculative.compare(response, 4, 24)
        # results = Calculative.compare(response, 4, 24)
        # print(results)

class Australian_Rules():

    # def parse_Australian_Rules_(self, response):
    #     ladder=[]

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team == '':
    #             ladder.append()
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )

    # def parse_Australian_(self, response):
    #     ladder=[]
    #     teams={
    #         '': [''],
    #         '': [''],
    #         '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)

    def parse_Australian_SANFL(self, response):
        ladder=[]
        teams={
            'Woodville-West Eagles': ['Woodville-West Torrens'],
            '': [''],
            }

        for team in response.xpath("(//table[@class='sp-livetable__table']/tbody)[1]/tr[position()>1]/td[3]/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 8)
        # results = Calculative.compare(response, 2, 8)
        # print(results)

    def parse_Australian_Rules_AFL(self, response):
        ladder=[]
        teams={
            'WC Eagles': ['West Coast'],
            'Port Adel': ['Port Adelaide'],
            'North Melb': ['North Melbourne'],
            'GWS Giants': ['Greater Western Sydney'],
            'W Bulldogs': ['Western Bulldogs'],
            }

        for team in response.xpath("//tr/td[@rowspan='1'][2]/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        print('League just starting')
        print('AFL change league to scorespro, either /standing/ or /league/..')

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 4, 14)
        # results = Calculative.compare(response, 4, 14)
        # print(results)

class American_Football():

    # def parse_American_Football_(self, response):
    #     ladder=[]

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team == '':
    #             ladder.append()
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )

    # def parse_American_Football_(self, response):
    #     ladder=[]
    #     teams={
    #         '': [''],
    #         '': [''],
    #         '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)

    def parse_American_Football_NFL(self, response):
        ladder=[]
        teams={
            'Washington Redskins':['Washington Football Team']
            }


        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])


        response.request.meta['ladder']=ladder
        Calculative.compare(response, 4, 27)
        # results = Calculative.compare(response, 4, 27)
        # print(results)
        

class Rugby_League():

    # def parse_Rugby_League_(self, response):
    #     ladder=[]

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team == '':
    #             ladder.append()
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )

    # def parse_American_Football_(self, response):
    #     ladder=[]
    #     teams={
    #         '': [''],
    #         '': [''],
    #         '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)

    def parse_Rugby_League_NRL(self, response):
        ladder=[]
        teams={
            'Manly-Warringah Sea Eagles': ['Manly Sea Eagles'],
            'North Queensland Cowboys': ['Nth Queensland Cowboys'],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 3, 12)
        # results = Calculative.compare(response, 3, 12)
        # print(results)

class Volleyball():

    # def parse_Volleyball_(self, response):
    #     ladder=[]

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team == '':
    #             ladder.append()
    #         else:
    #              ladder.append(team)

    #     print(ladder)
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )

    # def parse_Volleyball_(self, response):
    #     ladder=[]
    #     teams={
    #         '': [''],
    #         '': [''],
    #         '': [''],
    #         }

    #     for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
    #         if team in teams.keys():
    #             ladder.append(teams[team])
    #         else:
    #             ladder.append([team])

    #  
    #     response.request.meta['ladder']=ladder
    #     Calculative.compare(response, , )
    #     # results = Calculative.compare(response, , )
    #     # print(results)

    def parse_Volleyball_Romanian_Divizia_A1_Men(self, response):
        ladder=[]
        teams={
            'Steaua Bucuresti': ['Csa Steaua Bucuresti'],
            'Dinamo Bucarest': ['CS Dinamo Bucuresti'],
            'Municipal Zalau': ['Css Cne Lapi Dej Scm Zalau'],
            'Stiinta Bucuresti': ['CS Stiinta Explorari Baia Mare'],
            'Rapid Bucuresti': ['Rapid Bucharesti'],
            'U Cluj': ['CS Universitatea Cluj'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, , )
        # print(results)

    def parse_Volleyball_Spanish_Superliga_Men(self, response):
        ladder=[]
        teams={
            'Teruel': ['Cv Teruel'],
            'Valencia': ['Cv Valencia'],
            'Emeve': ['CV Eivissa'],
            'Melilla': ['CV Melilla'],
            'Rio Duero San Jose': ['Cdv Rio Duero Soria'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Volleyball_Czech_Extraliga_Women(self, response):
        ladder=[]
        teams={
            'Ostrava W': ['TJ Ostrava'],
            'Dukla Liberec W': ['Vk Dukla Liberec'],
            'Prostejov W': ['Vk Prostejov'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 8)
        # results = Calculative.compare(response, 1, 8)
        # print(results)

    def parse_Volleyball_Romanian_Divizia_A1_Women(self, response):
        ladder=[]
        teams={
            'Dacia Mioveni 2012 W': ['CS Dacia Mioveni'],
            'Craiova W': ['SCMU Craiova'],
            'Cristina Pirv Turda W': ['Acs Volei Turda'],
            'CSO Voluntari 2005 W': ['Cso Voluntari 2005'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Volleyball_Czech_Extraliga_Men(self, response):
        ladder=[]
        teams={
            'Karlovarsko': ['VK CEZ Karlovarsko'],
            'Usti nad Labem': ['Skv Usti Nad Labem'],
            'Kladno': ['Kladno Volejbal CZ'],
            'Ceske Budejovice': ['Vk Jihostroj Ceske Budejovice'],
            'Beskydy': ['Black Volley Beskydy'],
            'Zlin': ['Fatra Zlin'],
            'Pribram': ['Vk Pribram'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Volleyball_Turkish_League_Women(self, response):
        ladder=[]
        teams={
            'Yesilyurt W': ['Bakirkoy Bld Yesilyurt'],
            'Vakifbank W': ['Vakifbank SK'],
            'Eczacibasi Istanbul W': ['Eczacibasi Istanbul'],
            'Sariyer Bld. W': ['Sariyer Belediyesi'],
            'Aydin Bld W': ['Aydin Buyuksehir Bld'],
            'Sigorta Shop Kalecik W': ['Mert Grup Sigorta Kadin Voleybol'],
            'Galatasaray W': ['Galatasaray Istanbul'],
            'Nilufer Belediye W': ['Nilufer Belediye Bursa'],
            'Bolu Bld W': ['Bolu Belediye'],
            'Thy W': ['Turk Hava Yollari'],
            'Karayollari W': ['Ankara Karayollari'],
            'PTT Spor W': ['Ankara Ptt'],
            'Kuzeyboru Genclik W': ['Kuzeyboru Genclik'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 12)
        # results = Calculative.compare(response, 2, 12)
        # print(results)

    def parse_Volleyball_Austrian_League(self, response):
        ladder=[]
        ## Only using regular season ladder, as a result, 'Posojilnica Aich/Dob' and 'UVC Holding Graz' not included.
        teams={
            'Ried im Innkreis': ['UVC Ried'],
            'Waldviertel': ['Union Volleyball Waldviertel'],
            'VBK Klagenfurt': ['VBK WSL Klagenfurt'],
            'TSV Volksbank Hartberg': ['TSV Hartberg'],
            'Hypo No Amstetten': ['SG VCA Amstetten No'],

            }

        for team in response.xpath("(//table)[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 7)
        # results = Calculative.compare(response, 1, 7)
        # print(results)

    def parse_Volleyball_French_Ligue_A_Women(self, response):
        ladder=[]
        teams={
            'Rocheville Le Cannet W': ['Volero Le Cannet'],
            'Evreux W': ['Evreux Vb'],
            'Saint Raphael W': ['Saint-Raphael Var Volley-Ball'],
            'Beziers W': ['Beziers Volley'],
            'Mulhouse W': ['Asptt Mulhouse Volley-Ball'],
            'Marcq Baroeul W': ['Volley Club Marcq Baroeul'],
            'France Avenir 2024 W': ['France Avenir 2024'],
            'Cannes W': ['Racing Club de Cannes'],
            'Paris St-Cloud W': ['S F Paris Saint-Cloud'],
            'Chamalierois W': ['VBC Chamalieres'],
            'Terville W': ['Terville Florange'],
            'Nantes W': ['VB Nantes'],
            'Vandoeuvre Nancy W': ['Vandoeuvre Nancy Volley Ball'],
            'Pays d Aix Venelles W': ["Pays D'Aix Venelles Volley-Ball"],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 12)
        # results = Calculative.compare(response, 2, 12)
        # print(results)

    def parse_Volleyball_Brazilian_Superliga_Men(self, response):
        ladder=[]
        teams={
            'Volei Brasil Kirin': ['Brasilia Volei'],
            'Goias': ['Goias EC'],
            'Uberlandia': ['Academia do Volei Uberlandia'],
            'Funvic': ['EMS Taubate Funvic','Volei Funvic Natal'],
            'Sada Cruzeiro Volei': ['Sada Cruzeiro'],
            'Guarulhos': ['Volei Guarulhos'],
            'Sao Jose dos Campos': ['Sao Jose Dos Campos'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Volleyball_Polish_League_Men(self, response):
        ladder=[]
        teams={
            'Slepsk Suwalki': ['MKS Slepsk Suwalki'],
            'Asseco Resovia Rzeszow': ['Resovia Rzeszow'],
            'Lotos Trefl Gdansk': ['Trefl Gdansk'],
            'Indykpol Olsztyn': ['AZS Olsztyn'],
            'Cuprum Lubin': ['Cuprum Lubin SA'],
            'PGE Skra Belchatow': ['Skra Belchatow'],
            'Stal AZS PWSZ Nysa': ['Stal Nysa SA'],
            'Warszawa': ['Projekt Warsaw'],
            'Cerrad Czarni Radom': ['Wks Czarni Radom'],
            'Jastrzebski': ['Jastrzebski Wegiel'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 12)
        # results = Calculative.compare(response, 2, 12)
        # print(results)

    def parse_Volleyball_German_Bundesliga_Men(self, response):
        ladder=[]
        teams={
            'Herrsching': ['Wwk Volleys Herrsching'],
            'Luneburg': ['Svg Luneburg'],
            'Berlin Recycling': ['Berlin RV'],
            'VFB Friedrichshafen': ['VfB Friedrichshafen'],
            'Giesen/Hildesheim': ['TSV Giesen Grizzlys'],
            'TSV Unterhaching II': ['TSV Unterhaching'],
            'Netzhoppers': ['Netzhoppers KW Bestensee'],
            'Duren': ['SWD Powervolleys Duren'],
            }

        for team in response.xpath("(//table)[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 8)
        # results = Calculative.compare(response, 1, 8)
        # print(results)

    def parse_Volleyball_Polish_League_Women(self, response):
        ladder=[]
        teams={
            'Budowlani Lodz W': ['Budowlani Lodz'],
            'Chemik Police W': ['Chemik Police'],
            'Joker Swiecie W': ['Joker Swiecie'],
            'Opole W': ['Uni Opole'],
            'Legionowo W': ['Legionovia Legionowo'],
            'Radom W': ['Radomka Radom'],
            'Rzeszow W': ['KS Rzeszow'],
            'Commercecon Lodz W': ['LKS Lodz'],
            'Wroclaw W': ['Volley Wroclaw'],
            'Bydgoszcz W': ['KS Palac Bydgoszcz'],
            'Bielsko-Biała W': ['Bks Bielsko-Biala'],
            'MKS Kalisz W': ['MKS Kalisz'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Volleyball_Turkish_League_Men(self, response):
        ladder=[]
        teams={
            'Altekma': ['TFL Altekma'],
            'Fenerbahce Istanbul': ['Fenerbahce SK Istanbul'],
            'Sorgun Bld': ['Sorgun BLD'],
            'Belediye Plevne': ['Tokat Belediye'],
            'Afyon Karahisar Bld': ['Afyon Belediye Yuntas'],
            'Ziraat Bankasi': ['Ziraat Bankasi Ankara'],
            'Halk Bankasi': ['Halkbank Ankara'],
            'Kiziltepe': ['Yeni Kiziltepe Spor'],
            'Arkas Spor': ['Arkas Izmir'],
            'Galatasaray': ['Galatasaray Istanbul'],
            'Spor Toto': ['Spor Toto SK Ankara'],
            'Bursa B.Sehir Bld': ['Bursa B.sehir Bld'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 12)
        # results = Calculative.compare(response, 2, 12)
        # print(results)

    def parse_Volleyball_Korean_League_Women(self, response):
        ladder=[]
        teams={
            'Hyundai Greenfox W': ['Suwon Hillstate'],
            'Hungkuk Pinkspiders W': ['Incheon Pink Spiders'],
            'IBK W': ['IBK Altos'],
            'Daejeon KGC W': ['Daejeon Pro VC'],
            'GS Caltex W': ['Seoul KIXX'],
            'Expressway Co W': ['Gimcheon Hi-Pass'],
            'Gwangju AI Peppers W': ['Gwangju Ai Peppers'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 0, 6)
        # results = Calculative.compare(response, 0, 6)
        # print(results)

    def parse_Volleyball_Serbian_League_Men(self, response):
        ladder=[]
        teams={
            '': [''],
            '': [''],
            '': [''],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 8)
        # results = Calculative.compare(response, 1, 8)
        # print(results)

    def parse_Volleyball_Italian_Serie_A2_Men(self, response):
        ladder=[]
        teams={
            'Siena': ['Volley Siena'],
            'Mondovi': ['VBC Mondovi'],
            'Cuneo': ['Cuneo Volley'],
            'BCC-NEP Castellana': ['New Mater Volley Castellana Grotte'],
            'Ortona': ['Ortona Volley'],
            'Brescia': ['Atlantide Pallavolo Brescia'],
            'Porto Viro': ['Volley Porto Viro'],
            'HRK Motta di Livenza': ['Asd Pallavolo Motta 1969'],
            'Lagonegro': ['Rinascita Lagonegro'],
            'Reggio Emilia': ['Reggio Emilia Volley'],
            'Cantu': ['Cassa Rurale Cantu'],
            'Santa Croce': ['Lupi Santa Croce'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 11)
        # results = Calculative.compare(response, 2, 11)
        # print(results)

    def parse_Volleyball_Italian_Serie_A2_Women(self, response):
        # Watch for this one on how it results
        ladder=[]
        teams={
            'Marsala W': ['Volley Marsala'],
            'Talmassons W': ['Volley Talmassons'],
            'Futura Volley Giovani W': ['Futura Volley Giovani Busto Arsizio'],
            'Aragona W': ['Volley Aragona'],
            'Montecchio W': ['Volley Montecchio'],
            'Albese W': ['Volley Como'],
            'Soverato W': ['Volley Soverato'],
            'Pallavolo Sicilia Catania W': ['Pallavolo Sicilia Catania'],
            'PVT Modica W': ['Pvt Modica'],
            'Club Italia W': ['Club Italia Volley'],
            'Mondovi W': ['Volley Mondovi'],
            'Altino W': ['Altino Volley'],
            'Martignacco W': ['VC Martignacco'],
            'Olbia W': ['Volley Hermaea Olbia'],
            'Sara Pinerolo W': ['Volley Pinerolo'],
            'Brescia W': ['Millenium Brescia'],
            'Sassuolo W': ['Volley Sassuolo ASD'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.group_split(response, 1, 9, first='Group 1', second='Group 2')
        # results = Calculative.group_split(response, 1, 9, first='Group 1', second='Group 2')
        # print(results)

    def parse_Volleyball_Italian_Serie_A1_Women(self, response):
        ladder=[]
        teams={
            'Perugia W': ['Perugia Volley'],
            'Casalmaggiore W': ['Casalmaggiore'],
            'Novara W': ['Agil Volley Novara'],
            'Chieri W': ['Chieri 76 Volleyball'],
            'Scandicci W': ['Pallavolo Scandicci'],
            'Trentino W': ['Trentino Rosa'],
            'Busto Arsizio W': ['Busto Arsizio Volley'],
            'Monza W': ['Volley Monza'],
            'Bergamo W': ['Volley Bergamo'],
            'Cuneo W': ['Cuneo Granda Volley'],
            'Conegliano W': ['Volley Conegliano'],
            'Roma W': ['Roma Volley Club'],
            'Vallefoglia W': ['Volley Vallefoglia'],
            'Firenze W': ['Azzurra Volley San Casciano'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 12)
        # results = Calculative.compare(response, 2, 12)
        # print(results)

    def parse_Volleyball_Finnish_Mestaruusliiga_Men(self, response):
        ladder=[]
        teams={
            'Loimu': ['Raision Loimu'],
            'Valepa': ['Valepa Sastamala'],
            'Hurrikaani': ['Hurrikaani Loimaa'],
            'Savo Volley Kuopio': ['Savo Volley'],
            'Turun Toverit': ['TUTO Volley'],
            'Lakkapaa': ['Team Lakkapaa'],
            'Akaa': ['Akaa Volley'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 9)
        # results = Calculative.compare(response, 1, 9)
        # print(results)

    def parse_Volleyball_French_Ligue_A_Men(self, response):
        ladder=[]
        teams={
            'Poitiers': ['Stade Poitevin Poitiers'],
            'Chaumont': ['Chaumont 52'],
            'Nice': ['Nice Volley Ball'],
            'Cannes': ['AS Cannes Volley-Ball'],
            'Tourcoing': ['Tourcoing Lille Metropole'],
            'Cambrai': ['Volley Club de Cambrai'],
            'Montpellier': ['Montpellier Volley UC'],
            'Toulouse': ['Spacers Toulouse Volley'],
            'Plessis Robinson VB': ['Plessis Robinson'],
            'Sete': ['Arago de Sete'],
            'Nantes-Reze': ['Nantes Reze Metropole Volley'],
            'Grand Nancy Metropole Hb': ['Grand Nancy Metropole HB'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 12)
        # results = Calculative.compare(response, 2, 12)
        # print(results)

    def parse_Volleyball_Finnish_Mestaruusliiga_Women(self, response):
        ladder=[]
        teams={
            'LiigaPloki W': ['Liigaploki'],
            'Puijo W': ['Puijo Wolley'],
            'Orpo W': ['Orpo'],
            'Nurmon Jymy W': ['Jymy Volley'],
            'Helsinki W': ['Helsinki Volley'],
            'Vampula W': ['LP Vampula'],
            'WoVo W': ['WoVo Rovaniemi'],
            'Polkky Kuusamo W': ['Polkky Kuusamo'],
            'LP Kangasala W': ['LP Kangasala'],
            'Hameenlinna W': ['Hameenlinna'],
            'LP Viesti W': ['Salon Viesti'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 1, 10)
        # results = Calculative.compare(response, 1, 10)
        # print(results)

    def parse_Volleyball_Russian_Superleague_Men(self, response):
        ladder=[]
        teams={
            'Nizhny Novgorod': ['ASK Nizhny Novgorod'],
            'Zenit Kazan': ['VC Zenit-Kazan'],
            'Fakel Novyi Urengoy': ['Fakel Novy Urengoy'],
            'Yugra-Samotlor Nizhnevartovsk': ['Yugra Samotlor'],
            'Enisey Krasnoyarsk': ['VC Yenisey Krasnoyarsk'],
            'Gazprom': ['Gazprom-Ugra Surgut'],
            'Ural Ufa': ['UFA Ural'],
            'Orenburg': ['Neftyanik Orenburg'],
            'Dynamo Leningrad': ['Dinamo-Lo'],
            'Perm': ['Permskie Medvedi'],
            'Kaustik': ['HC Kaustik Volgograd'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 12)
        # results = Calculative.compare(response, 2, 12)
        # print(results)

    def parse_Volleyball_Greek_League_Women(self, response):
        ladder=[]
        teams={
            'Evosmou W': ['Aias Euosmou'],
            'PAOK W': ['Paok','PAOK'],
            'Ilisiakos W': ['AO Ilisiakos'],
            'Thiras W': ['AO Thiras'],
            'Thetis W': ['Asp Thetis'],
            'AON Pannaxiakos W': ['AON Panaxiakos'],
            'Porfiras W': ['AO Porfiras'],
            'Amazonas W': ['AON Amazones'],
            'Olympiacos W': ['Olympiacos Piraeus'],
            'AEK W': ['AEK Athens'],
            'Lamia W': ['AO Lamias 2013'],
            'Aris W': ['Aris Thessaloniki'],
            'Markopoulo W': ['AO Markopoulou'],
            'Panathinaikos W': ['Panathinaikos Athens'],
            }

        for team in response.xpath("//table[1]/tbody/tr/td/div/div/div/a/text()").getall():
            if team in teams.keys():
                ladder.append(teams[team])
            else:
                ladder.append([team])

        response.request.meta['ladder']=ladder
        Calculative.compare(response, 2, 12)
        # results = Calculative.compare(response, 2, 12)
        # print(results)

    

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
