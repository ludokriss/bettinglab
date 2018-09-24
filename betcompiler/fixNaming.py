#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Aug  2 17:35:23 2017
    
    @author: kristofferbjerkelund
    """
import re
def fixNaming(matchnames):
    for i in range(len(matchnames)):
        F=0;
        while F==0:
            if re.search('  ',matchnames[i]):
                matchnames[i]=re.sub('  ',' ',matchnames[i]);
            elif re.search(' vs ',matchnames[i]):
                matchnames[i]=re.sub(' vs ',' - ',matchnames[i]);
            elif re.search(' v ',matchnames[i]):
                matchnames[i]=re.sub(' v ',' - ',matchnames[i]);
            elif re.search(' vs. ',matchnames[i]):
                matchnames[i]=re.sub(' vs. ',' - ',matchnames[i]);
            elif re.search('Rep of Ireland',matchnames[i]):
                matchnames[i]=re.sub('Rep of Ireland','Ireland',matchnames[i]);
            elif re.search('Republic of Ireland',matchnames[i]):
                matchnames[i]=re.sub('Republic of Ireland','Ireland',matchnames[i]);
            elif re.search('West Bromwich Albion',matchnames[i]):
                matchnames[i]=re.sub('West Bromwich Albion','West Brom',matchnames[i]);
            elif re.search('W.B.A',matchnames[i]):
                matchnames[i]=re.sub('W.B.A','West Brom',matchnames[i]);
            elif re.search('Man Utd',matchnames[i]):
                matchnames[i]=re.sub('Man Utd','Manchester United',matchnames[i]);
            elif re.search('C Palace',matchnames[i]):
                matchnames[i]=re.sub('C Palace','Crystal Palace',matchnames[i]);
            elif re.search('Man City',matchnames[i]):
                matchnames[i]=re.sub('Man City','Manchester City',matchnames[i]);
            elif re.search('Bournemouth AFC',matchnames[i]):
                matchnames[i]=re.sub('Bournemouth AFC','Bournemouth',matchnames[i]);
            elif re.search('AFC Bournemouth',matchnames[i]):
                matchnames[i]=re.sub('AFC Bournemouth','Bournemouth',matchnames[i]);
            elif re.search('Hull City',matchnames[i]):
                matchnames[i]=re.sub('Hull City','Hull',matchnames[i]);
            elif re.search('West Ham United',matchnames[i]):
                matchnames[i]=re.sub('West Ham United','West Ham',matchnames[i]);
            elif re.search('Leicester City',matchnames[i]):
                matchnames[i]=re.sub('Leicester City','Leicester',matchnames[i]);
            elif re.search('Brighton &amp; Hove Albion',matchnames[i]):
                matchnames[i]=re.sub('Brighton &amp; Hove Albion','Brighton',matchnames[i]);
            elif re.search('Stoke City',matchnames[i]):
                matchnames[i]=re.sub('Stoke City','Stoke',matchnames[i]);
            elif re.search('Swansea City',matchnames[i]):
                matchnames[i]=re.sub('Swansea City','Swansea',matchnames[i]);
            elif re.search('Tottenham Hotspur',matchnames[i]):
                matchnames[i]=re.sub('Tottenham Hotspur','Tottenham',matchnames[i]);
            elif re.search('Man United',matchnames[i]):
                matchnames[i]=re.sub('Man United','Manchester United',matchnames[i]);
            elif re.search('FC Barcelona',matchnames[i]):
                matchnames[i]=re.sub('FC Barcelona','Barcelona',matchnames[i]);
            elif re.search('FC Basel',matchnames[i]):
                matchnames[i]=re.sub('FC Basel','Basel',matchnames[i]);
            elif re.search('FC Bayern',matchnames[i]):
                matchnames[i]=re.sub('FC Bayern','Bayern',matchnames[i]);
            elif re.search('FC Porto',matchnames[i]):
                matchnames[i]=re.sub('FC Porto','Porto',matchnames[i]);
            elif re.search('Bayer 04 Leverkusen',matchnames[i]):
                matchnames[i]=re.sub('Bayer 04 Leverkusen','Bayer Leverkusen',matchnames[i]);
            elif re.search('Atlético Madrid',matchnames[i]):
                matchnames[i]=re.sub('Atlético Madrid','Atletico Madrid',matchnames[i]);
            elif re.search('Sporting Lisbon',matchnames[i]):
                matchnames[i]=re.sub('Sporting Lisbon','Sporting CP',matchnames[i]);
            elif re.search('FK Rostov',matchnames[i]):
                matchnames[i]=re.sub('FK Rostov','Rostov',matchnames[i]);
            elif re.search('FC Rostov',matchnames[i]):
                matchnames[i]=re.sub('FC Rostov','Rostov',matchnames[i]);
            elif re.search('Paris Saint-Germain',matchnames[i]):
                matchnames[i]=re.sub('Paris Saint-Germain','Paris SG',matchnames[i]);
            elif re.search('Ludogorets Razgrad',matchnames[i]):
                matchnames[i]=re.sub('Ludogorets Razgrad','Ludogorets',matchnames[i]);
            elif re.search('PFC Ludogorets',matchnames[i]):
                matchnames[i]=re.sub('PFC Ludogorets','Ludogorets',matchnames[i]);
            elif re.search('CSKA Moskva',matchnames[i]):
                matchnames[i]=re.sub('CSKA Moskva','CSKA Moscow',matchnames[i]);
            elif re.search('AS Monaco',matchnames[i]):
                matchnames[i]=re.sub('AS Monaco','Monaco',matchnames[i]);
            elif re.search('Dynamo Kyiv',matchnames[i]):
                matchnames[i]=re.sub('Dynamo Kyiv','Dynamo Kiev',matchnames[i]);
            elif re.search('Be.ikta. A.?.',matchnames[i]):
                matchnames[i]=re.sub('Be.ikta. A.?..','Besictas FC',matchnames[i]);
            elif re.search('Be.ikta. JK',matchnames[i]):
                matchnames[i]=re.sub('Besiktas JK','Besictas FC',matchnames[i]);
            elif re.search('Be.ikta.',matchnames[i]):
                matchnames[i]=re.sub('Be.ikta.','Besictas FC',matchnames[i]);
            elif re.search('FC Copenhagen',matchnames[i]):
                matchnames[i]=re.sub('FC Copenhagen','FC København',matchnames[i]);
            elif re.search('Olympique Lyonnais',matchnames[i]):
                matchnames[i]=re.sub('Olympique Lyonnais','Lyon',matchnames[i]);
            elif re.search('Republic of Ireland',matchnames[i]):
                matchnames[i]=re.sub('Republic of Ireland','Ireland',matchnames[i]);
            elif re.search('West Bromwich Albion',matchnames[i]):
                matchnames[i]=re.sub('West Bromwich Albion','West Brom',matchnames[i]);
            elif re.search('W.B.A',matchnames[i]):
                matchnames[i]=re.sub('W.B.A','West Brom',matchnames[i]);
            elif re.search('Man Utd',matchnames[i]):
                matchnames[i]=re.sub('Man Utd','Manchester United',matchnames[i]);
            elif re.search('Man City',matchnames[i]):
                matchnames[i]=re.sub('Man City','Manchester City',matchnames[i]);
            elif re.search('Bournemouth AFC',matchnames[i]):
                matchnames[i]=re.sub('Bournemouth AFC','Bournemouth',matchnames[i]);
            elif re.search('AFC Bournemouth',matchnames[i]):
                matchnames[i]=re.sub('AFC Bournemouth','Bournemouth',matchnames[i]);
            elif re.search('Hull City',matchnames[i]):
                matchnames[i]=re.sub('Hull City','Hull',matchnames[i]);
            elif re.search('West Ham United',matchnames[i]):
                matchnames[i]=re.sub('West Ham United','West Ham',matchnames[i]);
            elif re.search('Leicester City',matchnames[i]):
                matchnames[i]=re.sub('Leicester City','Leicester',matchnames[i]);
            elif re.search('Stoke City',matchnames[i]):
                matchnames[i]=re.sub('Stoke City','Stoke',matchnames[i]);
            elif re.search('Swansea City',matchnames[i]):
                matchnames[i]=re.sub('Swansea City','Swansea',matchnames[i]);
            elif re.search('Tottenham Hotspur',matchnames[i]):
                matchnames[i]=re.sub('Tottenham Hotspur','Tottenham',matchnames[i]);
            elif re.search('Man United',matchnames[i]):
                matchnames[i]=re.sub('Man United','Manchester United',matchnames[i]);
            # Europa League
            elif re.search('FK Qarabag',matchnames[i]):
                matchnames[i]=re.sub('FK Qarabag','FC Quarabag',matchnames[i]);
            elif re.search('FK Qabala',matchnames[i]):
                matchnames[i]=re.sub('FK Qabala','Gabala',matchnames[i]);
            elif re.search('FC Slovan Liberec',matchnames[i]):
                matchnames[i]=re.sub('FC Slovan Liberec','Slovan Liberec',matchnames[i]);
            elif re.search('Sporting de Braga',matchnames[i]):
                matchnames[i]=re.sub('Sporting de Braga','Sporting Braga',matchnames[i]);
            elif re.search('Steaua Bucuresti',matchnames[i]):
                matchnames[i]=re.sub('Steaua Bucuresti','Steaua',matchnames[i]);
            elif re.search('1. FSV Mainz 05',matchnames[i]):
                matchnames[i]=re.sub('1. FSV Mainz 05','Mainz',matchnames[i]);
            elif re.search('Zenit Saint-Petersburg',matchnames[i]):
                matchnames[i]=re.sub('Zenit Saint-Petersburg','Zenit',matchnames[i]);
            elif re.search('Saint-Etienne',matchnames[i]):
                matchnames[i]=re.sub('Saint-Etienne','Saint Etienne',matchnames[i]);
            elif re.search('AS Roma',matchnames[i]):
                matchnames[i]=re.sub('AS Roma','Roma',matchnames[i]);
            elif re.search('BSC Young Boys',matchnames[i]):
                matchnames[i]=re.sub('BSC Young Boys','Young Boys',matchnames[i]);
            elif re.search('KAA Gent',matchnames[i]):
                matchnames[i]=re.sub('KAA Gent','Gent',matchnames[i]);
            elif re.search('RC Genk',matchnames[i]):
                matchnames[i]=re.sub('RC Genk','Genk',matchnames[i]);
            elif re.search('FC Viktoria Plzen',matchnames[i]):
                matchnames[i]=re.sub('FC Viktoria Plzen','Victoria Plzen',matchnames[i]);
            elif re.search('FK Austria Wien',matchnames[i]):
                matchnames[i]=re.sub('FK Austria Wien','Austria Wien',matchnames[i]);
            elif re.search('FC Astana',matchnames[i]):
                matchnames[i]=re.sub('FC Astana','Astana',matchnames[i]);
            elif re.search('Fenerbah.e SK',matchnames[i]):
                matchnames[i]=re.sub('Fenerbah.e SK','Fenerbahçe',matchnames[i]);
            elif re.search('SK Rapid Wien',matchnames[i]):
                matchnames[i]=re.sub('SK Rapid Wien','Rapid Wien',matchnames[i]);
            elif re.search('Racing Genk',matchnames[i]):
                matchnames[i]=re.sub('Racing Genk','Genk',matchnames[i]);
            elif re.search('Zorya Luhansk',matchnames[i]):
                matchnames[i]=re.sub('Zorya Luhansk','Zorya',matchnames[i]);
            elif re.search('Racing Genk',matchnames[i]):
                matchnames[i]=re.sub('Racing Genk','Genk',matchnames[i]);
            elif re.search('FC Schalke 04',matchnames[i]):
                matchnames[i]=re.sub('FC Schalke 04','Schalke 04',matchnames[i]);
            elif re.search('Internazionale',matchnames[i]):
                matchnames[i]=re.sub('Internazionale','Inter',matchnames[i]);
            elif re.search('AC Sparta Praha',matchnames[i]):
                matchnames[i]=re.sub('AC Sparta Praha','Sparta Praha',matchnames[i]);
            elif re.search('OGC Nice',matchnames[i]):
                matchnames[i]=re.sub('OGC Nice','Nice',matchnames[i]);
            elif re.search('FK Krasnodar',matchnames[i]):
                matchnames[i]=re.sub('FK Krasnodar','Krasnodar',matchnames[i]);
            elif re.search('Celta de Vigo',matchnames[i]):
                matchnames[i]=re.sub('Celta de Vigo','Celta',matchnames[i]);
            elif re.search('Hapoel Be''er Sheva',matchnames[i]):
                matchnames[i]=re.sub('Hapoel Be''er Sheva','Hapoel',matchnames[i]);
            elif re.search('FK Krasnodar',matchnames[i]):
                matchnames[i]=re.sub('FK Krasnodar','Krasnodar',matchnames[i]);
            elif re.search('Celta de Vigo',matchnames[i]):
                matchnames[i]=re.sub('Celta de Vigo','Celta Vigo',matchnames[i]);
            elif re.search('Osmanlispor',matchnames[i]):
                matchnames[i]=re.sub('Osmanlispor','Osmanliispor',matchnames[i]);
            elif re.search('FC Red Bull Salzburg',matchnames[i]):
                matchnames[i]=re.sub('FC Red Bull Salzburg','Red Bull Salzburg',matchnames[i]);
            elif re.search('FC Z.rich',matchnames[i]):
                matchnames[i]=re.sub('FC Z.rich','Zürich',matchnames[i]);
            # Ligue 1
            elif re.search('Girondins de Bordeaux',matchnames[i]):
                matchnames[i]=re.sub('Girondins de Bordeaux','Bordeaux',matchnames[i]);
            elif re.search('AS Nancy',matchnames[i]):
                matchnames[i]=re.sub('AS Nancy','Nancy',matchnames[i]);
            elif re.search('SM Caen',matchnames[i]):
                matchnames[i]=re.sub('SM Caen','Caen',matchnames[i]);
            elif re.search('Dijon FCO',matchnames[i]):
                matchnames[i]=re.sub('Dijon FCO','Dijon',matchnames[i]);
            elif re.search('Toulouse FC',matchnames[i]):
                matchnames[i]=re.sub('Toulouse FC','Toulouse',matchnames[i]);
            elif re.search('FC Metz',matchnames[i]):
                matchnames[i]=re.sub('FC Metz','Metz',matchnames[i]);
            elif re.search('En Avant Guingamp',matchnames[i]):
                matchnames[i]=re.sub('En Avant Guingamp','Guingamp',matchnames[i]);
            elif re.search('FC Nantes',matchnames[i]):
                matchnames[i]=re.sub('FC Nantes','Nantes',matchnames[i]);
            elif re.search('Montpellier HSC',matchnames[i]):
                matchnames[i]=re.sub('Montpellier HSC','Montpellier',matchnames[i]);
            elif re.search('Angers SCO',matchnames[i]):
                matchnames[i]=re.sub('Angers SCO','Angers',matchnames[i]);
            elif re.search('Lille OSC',matchnames[i]):
                matchnames[i]=re.sub('Lille OSC','Lille',matchnames[i]);
            elif re.search('Stade Rennais',matchnames[i]):
                matchnames[i]=re.sub('Stade Rennais','Rennes',matchnames[i]);
            elif re.search('SC Bastia',matchnames[i]):
                matchnames[i]=re.sub('SC Bastia','Bastia',matchnames[i]);
            elif re.search('Olympique Marseille',matchnames[i]):
                matchnames[i]=re.sub('Olympique Marseille','Marseille',matchnames[i]);
            elif re.search('FC Lorient',matchnames[i]):
                matchnames[i]=re.sub('FC Lorient','Lorient',matchnames[i]);
            elif re.search('Amiens SC',matchnames[i]):
                matchnames[i]=re.sub('Amiens SC','Amiens',matchnames[i]);
            elif re.search('St Etienne',matchnames[i]):
                matchnames[i]=re.sub('St Etienne','Saint Etienne',matchnames[i]);
            # Fa Cup
            elif re.search('Accrington Stanley',matchnames[i]):
                matchnames[i]=re.sub('Accrington Stanley','Accrington',matchnames[i]);
            elif re.search('Luton Town',matchnames[i]):
                matchnames[i]=re.sub('Luton Town','Luton',matchnames[i]);
            elif re.search('Birmingham City',matchnames[i]):
                matchnames[i]=re.sub('Birmingham City','Birmingham',matchnames[i]);
            elif re.search('Newcastle United',matchnames[i]):
                matchnames[i]=re.sub('Newcastle United','Newcastle',matchnames[i]);
            elif re.search('Brighton & Hove Albion',matchnames[i]):
                matchnames[i]=re.sub('Brighton & Hove Albion','Brighton',matchnames[i]);
            elif re.search('Brighton & Hove Al',matchnames[i]):
                matchnames[i]=re.sub('Brighton & Hove Al','Brighton',matchnames[i]);
            elif re.search('Milton Keynes Dons',matchnames[i]):
                matchnames[i]=re.sub('Milton Keynes Dons','Milton Keynes',matchnames[i]);
            elif re.search('Fleetwood Town',matchnames[i]):
                matchnames[i]=re.sub('Fleetwood Town','Fleetwood',matchnames[i]);
            elif re.search('Huddersfield Town',matchnames[i]):
                matchnames[i]=re.sub('Huddersfield Town','Huddersfield',matchnames[i]);
            elif re.search('Ipswich Town',matchnames[i]):
                matchnames[i]=re.sub('Ipswich Town','Ipswich',matchnames[i]);
            elif re.search('Lincoln City',matchnames[i]):
                matchnames[i]=re.sub('Lincoln City','Lincoln',matchnames[i]);
            elif re.search('Ipswich Town',matchnames[i]):
                matchnames[i]=re.sub('Ipswich Town','Ipswich',matchnames[i]);
            elif re.search('Bolton Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Bolton Wanderers','Bolton',matchnames[i]);
            elif re.search('Cardiff City',matchnames[i]):
                matchnames[i]=re.sub('Cardiff City','Cardiff',matchnames[i]);
            elif re.search('Sheffield Wednesday',matchnames[i]):
                matchnames[i]=re.sub('Sheffield Wednesday','Sheffield Wed',matchnames[i]);
            elif re.search('Norwich City',matchnames[i]):
                matchnames[i]=re.sub('Norwich City','Norwich',matchnames[i]);
            elif re.search('Preston North End',matchnames[i]):
                matchnames[i]=re.sub('Preston North End','Preston',matchnames[i]);
            elif re.search('Queens Park Rangers',matchnames[i]):
                matchnames[i]=re.sub('Queens Park Rangers','QPR',matchnames[i]);
            elif re.search('Blackburn Rovers',matchnames[i]):
                matchnames[i]=re.sub('Blackburn Rovers','Blackburn',matchnames[i]);
            elif re.search('Rotherham United',matchnames[i]):
                matchnames[i]=re.sub('Rotherham United','Rotherham',matchnames[i]);
            elif re.search('Oxford United',matchnames[i]):
                matchnames[i]=re.sub('Oxford United','Oxford Utd',matchnames[i]);
            elif re.search('Wolverhampton Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Wolverhampton Wanderers','Wolves',matchnames[i]);
            elif re.search('Wolverhampton',matchnames[i]):
                matchnames[i]=re.sub('Wolverhampton','Wolves',matchnames[i]); 
            elif re.search('Wigan Athletic',matchnames[i]):
                matchnames[i]=re.sub('Wigan Athletic','Wigan',matchnames[i]);
            elif re.search('Wycombe Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Wycombe Wanderers','Wycombe',matchnames[i]);
            elif re.search('Plymouth Argyle',matchnames[i]):
                matchnames[i]=re.sub('Plymouth Argyle','Plymouth',matchnames[i]);
            elif re.search('Peterborough United',matchnames[i]):
                matchnames[i]=re.sub('Peterborough United','Peterborough',matchnames[i]);
            elif re.search('Cambridge United',matchnames[i]):
                matchnames[i]=re.sub('Cambridge United','Cambridge',matchnames[i]);
            elif re.search('Leeds United',matchnames[i]):
                matchnames[i]=re.sub('Leeds United','Leeds',matchnames[i]);
            # Bundesliga
            elif re.search('FC Ingolstadt 04',matchnames[i]):
                matchnames[i]=re.sub('FC Ingolstadt 04','FC Ingolstadt',matchnames[i]);
            elif re.search('1899 Hoffenheim',matchnames[i]):
                matchnames[i]=re.sub('1899 Hoffenheim','Hoffenheim',matchnames[i]);
            elif re.search('FC Augsburg',matchnames[i]):
                matchnames[i]=re.sub('FC Augsburg','Augsburg',matchnames[i]);
            elif re.search('Hertha BSC Berlin',matchnames[i]):
                matchnames[i]=re.sub('Hertha BSC Berlin','Hertha Berlin',matchnames[i]);
            elif re.search('Hertha BSC',matchnames[i]):
                matchnames[i]=re.sub('Hertha BSC','Hertha Berlin',matchnames[i]);
            elif re.search('SV Darmstadt 98',matchnames[i]):
                matchnames[i]=re.sub('SV Darmstadt 98','Darmstadt 98',matchnames[i]);
            elif re.search('Sport-Club Freiburg',matchnames[i]):
                matchnames[i]=re.sub('Sport-Club Freiburg','Freiburg',matchnames[i]);
            elif re.search('Borussia Monchengladbach',matchnames[i]):
                matchnames[i]=re.sub('Borussia Monchengladbach','Borussia Mönchengladbach',matchnames[i]);
            elif re.search('Borussia Monchengladbach',matchnames[i]):
                matchnames[i]=re.sub('Borussia Monchengladbach','Borussia Mönchengladbach',matchnames[i]);
            elif re.search('B Mönchengladbach',matchnames[i]):
                matchnames[i]=re.sub('B Mönchengladbach','Borussia Mönchengladbach',matchnames[i]);
            elif re.search('Mgladbach',matchnames[i]):
                matchnames[i]=re.sub('Mgladbach','Borussia Mönchengladbach',matchnames[i]);
            elif re.search('1. Mainz',matchnames[i]):
                matchnames[i]=re.sub('1. Mainz','Mainz',matchnames[i]);
            elif re.search('SC Freiburg',matchnames[i]):
                matchnames[i]=re.sub('SC Freiburg','Freiburg',matchnames[i]);
            elif re.search('VfL Wolfsburg',matchnames[i]):
                matchnames[i]=re.sub('VfL Wolfsburg','Wolfsburg',matchnames[i]);
            elif re.search('Ingolstadt 04',matchnames[i]):
                matchnames[i]=re.sub('Ingolstadt 04','FC Ingolstadt',matchnames[i]);
            elif re.search('VfB Stuttgart',matchnames[i]):
                matchnames[i]=re.sub('VfB Stuttgart','Stuttgart',matchnames[i]);
            elif re.search('Eintracht Frankfur ',matchnames[i]):
                matchnames[i]=re.sub('Eintracht Frankfur ','Eintracht Frankfurt ',matchnames[i]);
            # La Liga
            elif re.search('Deportivo de la Coruna',matchnames[i]):
                matchnames[i]=re.sub('Deportivo de la Coruna','Dep La Coruña',matchnames[i]);
            elif re.search('Deportivo La Coruna',matchnames[i]):
                matchnames[i]=re.sub('Deportivo La Coruna','Dep La Coruña',matchnames[i]);
            elif re.search('Deportivo La Coruña',matchnames[i]):
                matchnames[i]=re.sub('Deportivo La Coruña','Dep La Coruña',matchnames[i]);
            elif re.search('Granada CF',matchnames[i]):
                matchnames[i]=re.sub('Granada CF','Granada',matchnames[i]);
            elif re.search('Málaga',matchnames[i]):
                matchnames[i]=re.sub('Málaga','Malaga',matchnames[i]);
            elif re.search('UD Las Palmas',matchnames[i]):
                matchnames[i]=re.sub('UD Las Palmas','Las Palmas',matchnames[i]);
            elif re.search('Real Sporting de Gijon',matchnames[i]):
                matchnames[i]=re.sub('Real Sporting de Gijon','Sporting de Gijón',matchnames[i]);
            elif re.search('Sporting Gijon',matchnames[i]):
                matchnames[i]=re.sub('Sporting Gijon','Sporting de Gijón',matchnames[i]);
            elif re.search('Sporting Gijón',matchnames[i]):
                matchnames[i]=re.sub('Sporting Gijón','Sporting de Gijón',matchnames[i]);
            elif re.search('SD Eibar',matchnames[i]):
                matchnames[i]=re.sub('SD Eibar','Eibar',matchnames[i]);
            elif re.search('Deportivo Alaves',matchnames[i]):
                matchnames[i]=re.sub('Deportivo Alaves','Alavés',matchnames[i]);
            elif re.search('Alaves',matchnames[i]):
                matchnames[i]=re.sub('Alaves','Alavés',matchnames[i]);
            elif re.search('CD Alavés',matchnames[i]):
                matchnames[i]=re.sub('CD Alavés','Alavés',matchnames[i]);
            elif re.search('CD Leganés',matchnames[i]):
                matchnames[i]=re.sub('CD Leganés','Leganés',matchnames[i]);
            elif re.search('Deportivo La Corun',matchnames[i]):
                matchnames[i]=re.sub('Deportivo La Corun','Dep La Coruña',matchnames[i]);
            elif re.search('Real Betis',matchnames[i]):
                matchnames[i]=re.sub('Real Betis','Betis',matchnames[i]);
            elif re.search('SKA Saint Petersburg',matchnames[i]):
                matchnames[i]=re.sub('SKA Saint Petersburg','SKA St. Petersburg',matchnames[i]);
            # TL
            elif re.search('Viking FK',matchnames[i]):
                matchnames[i]=re.sub('Viking FK','Viking',matchnames[i]);
            elif re.search('Odds Ballklubb',matchnames[i]):
                matchnames[i]=re.sub('Odds Ballklubb','Odd',matchnames[i]);
            elif re.search('Aalesunds FK',matchnames[i]):
                matchnames[i]=re.sub('Aalesunds FK','Aalesund',matchnames[i]);
            elif re.search('Aalesunds',matchnames[i]):
                matchnames[i]=re.sub('Aalesunds','Aalesund',matchnames[i]);
            elif re.search('Lillestrøm SK',matchnames[i]):
                matchnames[i]=re.sub('Lillestrøm SK','Lillestrøm',matchnames[i]);
            elif re.search('Lillestroem SK',matchnames[i]):
                matchnames[i]=re.sub('Lillestroem SK','Lillestrøm',matchnames[i]);
            elif re.search('Sandefjord Fotball',matchnames[i]):
                matchnames[i]=re.sub('Sandefjord Fotball','Sandefjord',matchnames[i]);
            elif re.search('Kristiansund BK',matchnames[i]):
                matchnames[i]=re.sub('Kristiansund BK','Kristiansund',matchnames[i]);
            elif re.search('Rosenborg BK',matchnames[i]):
                matchnames[i]=re.sub('Rosenborg BK','Rosenborg',matchnames[i]);
            elif re.search('Rep of Ireland',matchnames[i]):
                matchnames[i]=re.sub('Rep of Ireland','Ireland',matchnames[i]);

            elif re.search('Republic of Ireland',matchnames[i]):
                matchnames[i]=re.sub('Republic of Ireland','Ireland',matchnames[i]);

            elif re.search('West Ham United',matchnames[i]):
                matchnames[i]=re.sub('West Ham United','West Ham',matchnames[i]);

            elif re.search('AFC Bournemouth',matchnames[i]):
                matchnames[i]=re.sub('AFC Bournemouth','Bournemouth',matchnames[i]);

            elif re.search('Hull City',matchnames[i]):
                matchnames[i]=re.sub('Hull City','Hull',matchnames[i]);

            elif re.search('Leicester City',matchnames[i]):
                matchnames[i]=re.sub('Leicester City','Leicester',matchnames[i]);

            elif re.search('Tottenham Hotspur',matchnames[i]):
                matchnames[i]=re.sub('Tottenham Hotspur','Tottenham',matchnames[i]);

            elif re.search('West Bromwich Albion',matchnames[i]):
                matchnames[i]=re.sub('West Bromwich Albion','West Brom',matchnames[i]);

            elif re.search('Stoke City',matchnames[i]):
                matchnames[i]=re.sub('Stoke City','Stoke',matchnames[i]);

            elif re.search('Swansea City',matchnames[i]):
                matchnames[i]=re.sub('Swansea City','Swansea',matchnames[i]);
            elif re.search('FC Barcelona',matchnames[i]):
                matchnames[i]=re.sub('FC Barcelona','Barcelona',matchnames[i]);
            elif re.search('FC Basel',matchnames[i]):
                matchnames[i]=re.sub('FC Basel','Basel',matchnames[i]);
            elif re.search('Bayern München',matchnames[i]):
                matchnames[i]=re.sub('Bayern München','Bayern Munich',matchnames[i]);
            elif re.search('1. FC Köln',matchnames[i]):
                matchnames[i]=re.sub('1. FC Köln','Koln',matchnames[i]);
            elif re.search('FC Köln',matchnames[i]):
                matchnames[i]=re.sub('FC Köln','Koln',matchnames[i]);
            elif re.search('1. Koln',matchnames[i]):
                matchnames[i]=re.sub('1. Koln','Koln',matchnames[i]);
            elif re.search('1 Koln',matchnames[i]):
                matchnames[i]=re.sub('1 Koln','Koln',matchnames[i]);
            elif re.search('RasenBallsport Leipzig',matchnames[i]):
                matchnames[i]=re.sub('RasenBallsport Leipzig','RB Leipzig',matchnames[i]);
            elif re.search('Hamburger SV',matchnames[i]):
                matchnames[i]=re.sub('Hamburger SV','Hamburger',matchnames[i]);
            elif re.search('FC Bayern',matchnames[i]):
                matchnames[i]=re.sub('FC Bayern','Bayern Munich',matchnames[i]);
            elif re.search('Bayern Munchen',matchnames[i]):
                matchnames[i]=re.sub('Bayern Munchen','Bayern Munich',matchnames[i]);
            elif re.search('FC Porto',matchnames[i]):
                matchnames[i]=re.sub('FC Porto','Porto',matchnames[i]);
            elif re.search('Bayer 04 Leverkusen',matchnames[i]):
                matchnames[i]=re.sub('Bayer 04 Leverkusen','Bayer Leverkusen',matchnames[i]);
            elif re.search('Atlético Madrid',matchnames[i]):
                matchnames[i]=re.sub('Atlético Madrid','Atletico Madrid',matchnames[i]);
            elif re.search('Atletico de Madrid',matchnames[i]):
                matchnames[i]=re.sub('Atletico de Madrid','Atletico Madrid',matchnames[i]);
            elif re.search('Sporting Lisbon',matchnames[i]):
                matchnames[i]=re.sub('Sporting Lisbon','Sporting CP',matchnames[i]);
            elif re.search('FK Rostov',matchnames[i]):
                matchnames[i]=re.sub('FK Rostov','Rostov',matchnames[i]);
            elif re.search('FC Rostov',matchnames[i]):
                matchnames[i]=re.sub('FC Rostov','Rostov',matchnames[i]);
            elif re.search('Paris Saint-Germain',matchnames[i]):
                matchnames[i]=re.sub('Paris Saint-Germain','Paris SG',matchnames[i]);
            elif re.search('Paris St-G',matchnames[i]):
                matchnames[i]=re.sub('Paris St-G','Paris SG',matchnames[i]);
            elif re.search('Ludogorets Razgrad',matchnames[i]):
                matchnames[i]=re.sub('Ludogorets Razgrad','Ludogorets',matchnames[i]);
            elif re.search('PFC Ludogorets',matchnames[i]):
                matchnames[i]=re.sub('PFC Ludogorets','Ludogorets',matchnames[i]);
            elif re.search('CSKA Moskva',matchnames[i]):
                matchnames[i]=re.sub('CSKA Moskva','CSKA Moscow',matchnames[i]);
            elif re.search('AS Monaco',matchnames[i]):
                matchnames[i]=re.sub('AS Monaco','Monaco',matchnames[i]);
            elif re.search('Dynamo Kyiv',matchnames[i]):
                matchnames[i]=re.sub('Dynamo Kyiv','Dynamo Kiev',matchnames[i]);
            elif re.search('Be.ikta. A.?.',matchnames[i]):
                matchnames[i]=re.sub('Be.ikta. A.?..','Besictas FC',matchnames[i]);
            elif re.search('Be.ikta. JK',matchnames[i]):
                matchnames[i]=re.sub('Besiktas JK','Besictas FC',matchnames[i]);
            elif re.search('Be.ikta.',matchnames[i]):
                matchnames[i]=re.sub('Be.ikta.','Besictas FC',matchnames[i]);
            elif re.search('FC Copenhagen',matchnames[i]):
                matchnames[i]=re.sub('FC Copenhagen','FC København',matchnames[i]);
            elif re.search('Olympique Lyonnais',matchnames[i]):
                matchnames[i]=re.sub('Olympique Lyonnais','Lyon',matchnames[i]);
            elif re.search('Club Brugge KV',matchnames[i]):
                matchnames[i]=re.sub('Club Brugge KV','Club Brugge',matchnames[i]);
            elif re.search('Troyes AC',matchnames[i]):
                matchnames[i]=re.sub('Troyes AC','Troyes',matchnames[i]);
            elif re.search('ESTAC Troyes',matchnames[i]):
                matchnames[i]=re.sub('ESTAC Troyes','Troyes',matchnames[i]);
            elif re.search('RC Strasbourg',matchnames[i]):
                matchnames[i]=re.sub('RC Strasbourg','Strasbourg',matchnames[i]);
            elif re.search('SC Amiens',matchnames[i]):
                matchnames[i]=re.sub('SC Amiens','Amiens',matchnames[i]);
            elif re.search('Racing Strasbourg',matchnames[i]):
                matchnames[i]=re.sub('Racing Strasbourg','Strasbourg',matchnames[i]);
            elif re.search('NK Maribor',matchnames[i]):
                matchnames[i]=re.sub('NK Maribor','Maribor',matchnames[i]);
            elif re.search('Spartak Moskva',matchnames[i]):
                matchnames[i]=re.sub('Spartak Moskva','Spartak Moscow',matchnames[i]);
            elif re.search('RSC Anderlecht',matchnames[i]):
                matchnames[i]=re.sub('RSC Anderlecht','Anderlecht',matchnames[i]);
            elif re.search('FC Shakhtar Donetsk',matchnames[i]):
                matchnames[i]=re.sub('FC Shakhtar Donetsk','Shakhtar Donetsk',matchnames[i]);
            elif re.search('Bate Borisov',matchnames[i]):
                matchnames[i]=re.sub('Bate Borisov','BATE Borisov',matchnames[i]);
            elif re.search('FC Koebenhavn',matchnames[i]):
                matchnames[i]=re.sub('FC Koebenhavn','FC København',matchnames[i]);
            elif re.search('FK Partizan',matchnames[i]):
                matchnames[i]=re.sub('FK Partizan','Partizan',matchnames[i]);
            elif re.search('Partizan Belgrade',matchnames[i]):
                matchnames[i]=re.sub('Partizan Belgrade','Partizan',matchnames[i]);
            elif re.search('Partizan Belgrad',matchnames[i]):
                matchnames[i]=re.sub('Partizan Belgrad','Partizan',matchnames[i]);
            elif re.search('Hapoel Be&#039;er Sheva',matchnames[i]):
                matchnames[i]=re.sub('Hapoel Be&#039;er Sheva','Hapoel Be''er Sheva',matchnames[i]);
            elif re.search('SK Slavia Praha',matchnames[i]):
                matchnames[i]=re.sub('SK Slavia Praha','Slavia Praha',matchnames[i]);
            elif re.search('Slavia Prag',matchnames[i]):
                matchnames[i]=re.sub('Slavia Prag','Slavia Praha',matchnames[i]);
            elif re.search('San Diego Chargers',matchnames[i]):
                matchnames[i]=re.sub('San Diego Chargers','Los Angeles Chargers',matchnames[i]);
            elif re.search('blabla',matchnames[i]):
                matchnames[i]=re.sub('blabla','blabla',matchnames[i]);
            elif re.search('blabla',matchnames[i]):
                matchnames[i]=re.sub('blabla','blabla',matchnames[i]);


            # Europa League
            elif re.search('FK Q.r.b.g',matchnames[i]):
                matchnames[i]=re.sub('FK Q.r.b.g','FC Quarabag',matchnames[i]);
            elif re.search('FK Karabakh',matchnames[i]):
                matchnames[i]=re.sub('FK Karabakh','FC Quarabag',matchnames[i]);
            elif re.search('Steaua Bucuresti',matchnames[i]):
                matchnames[i]=re.sub('Steaua Bucuresti','Steaua',matchnames[i]);
            elif re.search('FC Zarya Lugansk',matchnames[i]):
                matchnames[i]=re.sub('FC Zarya Lugansk','Zorya',matchnames[i]);
            elif re.search('AC Sparta Praha',matchnames[i]):
                matchnames[i]=re.sub('AC Sparta Praha','Sparta Praha',matchnames[i]);
            elif re.search('Hapoel Be er Sheva',matchnames[i]):
                matchnames[i]=re.sub('Hapoel Be er Sheva','Hapoel',matchnames[i]);
            elif re.search('PAOK Thessaloniki',matchnames[i]):
                matchnames[i]=re.sub('PAOK Thessaloniki','PAOK',matchnames[i]);
            elif re.search('FSV Mainz',matchnames[i]):
                matchnames[i]=re.sub('FSV Mainz','Mainz',matchnames[i]);
            elif re.search('Zenit St.Petersburg',matchnames[i]):
                matchnames[i]=re.sub('Zenit St.Petersburg','Zenit',matchnames[i]);
            elif re.search('KAA Gent',matchnames[i]):
                matchnames[i]=re.sub('KAA Gent','Gent',matchnames[i]);
            elif re.search('RC Genk',matchnames[i]):
                matchnames[i]=re.sub('RC Genk','Genk',matchnames[i]);
            elif re.search('Viktoria Plze.',matchnames[i]):
                matchnames[i]=re.sub('Viktoria Plze.','Victoria Plzen',matchnames[i]);
            elif re.search('FK Austria Wien',matchnames[i]):
                matchnames[i]=re.sub('FK Austria Wien','Austria Wien',matchnames[i]);
            elif re.search('Apoel Nicosia',matchnames[i]):
                matchnames[i]=re.sub('Apoel Nicosia','APOEL',matchnames[i]);
            elif re.search('Dundalk FC',matchnames[i]):
                matchnames[i]=re.sub('Dundalk FC','Dundalk',matchnames[i]);
            elif re.search('Osmanlispor',matchnames[i]):
                matchnames[i]=re.sub('Osmanlispor','Osmanliispor',matchnames[i]);
            elif re.search('Atletic Club Bilbao',matchnames[i]):
                matchnames[i]=re.sub('Atletic Club Bilbao','Atletic Bilbao',matchnames[i]);
            elif re.search('Olympiakos',matchnames[i]):
                matchnames[i]=re.sub('Olympiakos','Olympiacos',matchnames[i]);
            elif re.search('Athletic Club Bilbao',matchnames[i]):
                matchnames[i]=re.sub('Athletic Club Bilbao','Athletic Bilbao',matchnames[i]);
            elif re.search('Steaua Bucharest',matchnames[i]):
                matchnames[i]=re.sub('Steaua Bucharest','Steaua',matchnames[i]);
            elif re.search('FC Z.rich',matchnames[i]):
                matchnames[i]=re.sub('FC Z.rich','Zürich',matchnames[i]);
            #Fa cup
            elif re.search('Burton Albion',matchnames[i]):
                matchnames[i]=re.sub('Burton Albion','Burton',matchnames[i]);
            elif re.search('Accrington Stanley',matchnames[i]):
                matchnames[i]=re.sub('Accrington Stanley','Accrington',matchnames[i]);
            elif re.search('Luton Town',matchnames[i]):
                matchnames[i]=re.sub('Luton Town','Luton',matchnames[i]);
            elif re.search('Birmingham City',matchnames[i]):
                matchnames[i]=re.sub('Birmingham City','Birmingham',matchnames[i]);
            elif re.search('Newcastle United',matchnames[i]):
                matchnames[i]=re.sub('Newcastle United','Newcastle',matchnames[i]);
            elif re.search('Brighton & Hove Albion',matchnames[i]):
                matchnames[i]=re.sub('Brighton & Hove Albion','Brighton',matchnames[i]);
            elif re.search('Milton Keynes Dons',matchnames[i]):
                matchnames[i]=re.sub('Milton Keynes Dons','Milton Keynes',matchnames[i]);
            elif re.search('Fleetwood Town',matchnames[i]):
                matchnames[i]=re.sub('Fleetwood Town','Fleetwood',matchnames[i]);
            elif re.search('Huddersfield Town',matchnames[i]):
                matchnames[i]=re.sub('Huddersfield Town','Huddersfield',matchnames[i]);
            elif re.search('Ipswich Town',matchnames[i]):
                matchnames[i]=re.sub('Ipswich Town','Ipswich',matchnames[i]);
            elif re.search('Lincoln City',matchnames[i]):
                matchnames[i]=re.sub('Lincoln City','Lincoln',matchnames[i]);
            elif re.search('Ipswich Town',matchnames[i]):
                matchnames[i]=re.sub('Ipswich Town','Ipswich',matchnames[i]);
            elif re.search('Bolton Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Bolton Wanderers','Bolton',matchnames[i]);
            elif re.search('Cardiff City',matchnames[i]):
                matchnames[i]=re.sub('Cardiff City','Cardiff',matchnames[i]);
            elif re.search('Sheffield Wednesday',matchnames[i]):
                matchnames[i]=re.sub('Sheffield Wednesday','Sheffield Wed',matchnames[i]);
            elif re.search('Norwich City',matchnames[i]):
                matchnames[i]=re.sub('Norwich City','Norwich',matchnames[i]);
            elif re.search('Preston North End',matchnames[i]):
                matchnames[i]=re.sub('Preston North End','Preston',matchnames[i]);
            elif re.search('Queens Park Rangers',matchnames[i]):
                matchnames[i]=re.sub('Queens Park Rangers','QPR',matchnames[i]);
            elif re.search('Blackburn Rovers',matchnames[i]):
                matchnames[i]=re.sub('Blackburn Rovers','Blackburn',matchnames[i]);
            elif re.search('Rotherham United',matchnames[i]):
                matchnames[i]=re.sub('Rotherham United','Rotherham',matchnames[i]);
            elif re.search('Oxford United',matchnames[i]):
                matchnames[i]=re.sub('Oxford United','Oxford Utd',matchnames[i]);
            elif re.search('Wolverhampton Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Wolverhampton Wanderers','Wolves',matchnames[i]);
            elif re.search('Wigan Athletic',matchnames[i]):
                matchnames[i]=re.sub('Wigan Athletic','Wigan',matchnames[i]);
            elif re.search('Wycombe Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Wycombe Wanderers','Wycombe',matchnames[i]);
            elif re.search('St. Louis Blues',matchnames[i]):
                matchnames[i]=re.sub('St. Louis Blues','St Louis Blues',matchnames[i]);
            elif re.search('AS Roma',matchnames[i]):
                matchnames[i]=re.sub('AS Roma','Roma',matchnames[i]);
            # Bundesliga
            elif re.search('FC Augsburg',matchnames[i]):
                matchnames[i]=re.sub('FC Augsburg','Augsburg',matchnames[i]);
            elif re.search('FC Ingolstadt 04',matchnames[i]):
                matchnames[i]=re.sub('FC Ingolstadt 04','FC Ingolstadt',matchnames[i]);

            elif re.search('FC Augsburg',matchnames[i]):
                matchnames[i]=re.sub('FC Augsburg','Augsburg',matchnames[i]);
            elif re.search('TSG Hoffenheim',matchnames[i]):
                matchnames[i]=re.sub('TSG Hoffenheim','Hoffenheim',matchnames[i]);
            elif re.search('Leganes CD',matchnames[i]):
                matchnames[i]=re.sub('Leganes CD','Leganés',matchnames[i]);
            elif re.search('Leganes',matchnames[i]):
                matchnames[i]=re.sub('Leganes','Leganés',matchnames[i]);
            elif re.search('Celta Vigo',matchnames[i]):
                matchnames[i]=re.sub('Celta Vigo','Celta',matchnames[i]);
            elif re.search('Málaga',matchnames[i]):
                matchnames[i]=re.sub('Málaga','Malaga',matchnames[i]);
            elif re.search('Celta Vigo',matchnames[i]):
                matchnames[i]=re.sub('Celta Vigo','Celta',matchnames[i]);
            elif re.search('AK Bars Kazan',matchnames[i]):
                matchnames[i]=re.sub('AK Bars Kazan','Ak Bars Kazan',matchnames[i]);
            # TL
            elif re.search('Rosenborg BK',matchnames[i]):
                matchnames[i]=re.sub('Rosenborg BK','Rosenborg',matchnames[i]);
            elif re.search('FK Haugesund',matchnames[i]):
                matchnames[i]=re.sub('FK Haugesund','Haugesund',matchnames[i]);
            elif re.search('Kristiansund BK',matchnames[i]):
                matchnames[i]=re.sub('Kristiansund BK','Kristiansund',matchnames[i]);

            elif re.search('Republic of Ireland',matchnames[i]):
                matchnames[i]=re.sub('Republic of Ireland','Ireland',matchnames[i]);
            elif re.search('Hull City',matchnames[i]):
                matchnames[i]=re.sub('Hull City','Hull',matchnames[i]);
            elif re.search('Leicester City',matchnames[i]):
                matchnames[i]=re.sub('Leicester City','Leicester',matchnames[i]);
            elif re.search('Stoke City',matchnames[i]):
                matchnames[i]=re.sub('Stoke City','Stoke',matchnames[i]);
            elif re.search('Swansea City',matchnames[i]):
                matchnames[i]=re.sub('Swansea City','Swansea',matchnames[i]);
            elif re.search('West Bromwich',matchnames[i]):
                matchnames[i]=re.sub('West Bromwich','West Brom',matchnames[i]);
            elif re.search('FC Barcelona',matchnames[i]):
                matchnames[i]=re.sub('FC Barcelona','Barcelona',matchnames[i]);
            elif re.search('FC Basel',matchnames[i]):
                matchnames[i]=re.sub('FC Basel','Basel',matchnames[i]);
            elif re.search('FC Bayern',matchnames[i]):
                matchnames[i]=re.sub('FC Bayern','Bayern',matchnames[i]);
            elif re.search('FC Porto',matchnames[i]):
                matchnames[i]=re.sub('FC Porto','Porto',matchnames[i]);
            elif re.search('Bayer 04 Leverkusen',matchnames[i]):
                matchnames[i]=re.sub('Bayer 04 Leverkusen','Bayer Leverkusen',matchnames[i]);
            elif re.search('Atlético Madrid',matchnames[i]):
                matchnames[i]=re.sub('Atlético Madrid','Atletico Madrid',matchnames[i]);
            elif re.search('Sporting Lisbon',matchnames[i]):
                matchnames[i]=re.sub('Sporting Lisbon','Sporting CP',matchnames[i]);
            elif re.search('FK Rostov',matchnames[i]):
                matchnames[i]=re.sub('FK Rostov','Rostov',matchnames[i]);
            elif re.search('FC Rostov',matchnames[i]):
                matchnames[i]=re.sub('FC Rostov','Rostov',matchnames[i]);
            elif re.search('Paris Saint-Germain',matchnames[i]):
                matchnames[i]=re.sub('Paris Saint-Germain','Paris SG',matchnames[i]);
            elif re.search('Ludogorets Razgrad',matchnames[i]):
                matchnames[i]=re.sub('Ludogorets Razgrad','Ludogorets',matchnames[i]);
            elif re.search('PFC Ludogorets',matchnames[i]):
                matchnames[i]=re.sub('PFC Ludogorets','Ludogorets',matchnames[i]);
            elif re.search('CSKA Moskva',matchnames[i]):
                matchnames[i]=re.sub('CSKA Moskva','CSKA Moscow',matchnames[i]);
            elif re.search('AS Monaco',matchnames[i]):
                matchnames[i]=re.sub('AS Monaco','Monaco',matchnames[i]);
            elif re.search('Dynamo Kyiv',matchnames[i]):
                matchnames[i]=re.sub('Dynamo Kyiv','Dynamo Kiev',matchnames[i]);
            elif re.search('Be.ikta. A.?.',matchnames[i]):
                matchnames[i]=re.sub('Be.ikta. A.?..','Besictas FC',matchnames[i]);
            elif re.search('Be.ikta. JK',matchnames[i]):
                matchnames[i]=re.sub('Besiktas JK','Besictas FC',matchnames[i]);
            elif re.search('Be.ikta.',matchnames[i]):
                matchnames[i]=re.sub('Be.ikta.','Besictas FC',matchnames[i]);
            elif re.search('FC Copenhagen',matchnames[i]):
                matchnames[i]=re.sub('FC Copenhagen','FC København',matchnames[i]);
            elif re.search('Olympique Lyonnais',matchnames[i]):
                matchnames[i]=re.sub('Olympique Lyonnais','Lyon',matchnames[i]);
            # Europa League
            elif re.search('Qaraba.',matchnames[i]):
                matchnames[i]=re.sub('Qaraba.','FC Quarabag',matchnames[i]);
            elif re.search('Q.b.l.',matchnames[i]):
                matchnames[i]=re.sub('Q.b.l.','Gabala',matchnames[i]);
            elif re.search('FC Slovan Liberec',matchnames[i]):
                matchnames[i]=re.sub('FC Slovan Liberec','Slovan Liberec',matchnames[i]);
            elif re.search('S.C. Braga',matchnames[i]):
                matchnames[i]=re.sub('S.C. Braga','Sporting Braga',matchnames[i]);
            elif re.search('Steaua Bucure.ti',matchnames[i]):
                matchnames[i]=re.sub('Steaua Bucure.ti','Steaua',matchnames[i]);
            elif re.search('Mainz 05',matchnames[i]):
                matchnames[i]=re.sub('Mainz 05','Mainz',matchnames[i]);
            elif re.search('Zenit St Petersburg',matchnames[i]):
                matchnames[i]=re.sub('Zenit St Petersburg','Zenit',matchnames[i]);
            elif re.search('Saint-.tienne',matchnames[i]):
                matchnames[i]=re.sub('Saint-.tienne','Saint Etienne',matchnames[i]);
            elif re.search('AS Roma',matchnames[i]):
                matchnames[i]=re.sub('AS Roma','Roma',matchnames[i]);
            elif re.search('BSC Young Boys',matchnames[i]):
                matchnames[i]=re.sub('BSC Young Boys','Young Boys',matchnames[i]);
            elif re.search('KAA Gent',matchnames[i]):
                matchnames[i]=re.sub('KAA Gent','Gent',matchnames[i]);
            elif re.search('KRC Genk',matchnames[i]):
                matchnames[i]=re.sub('KRC Genk','Genk',matchnames[i]);
            elif re.search('Viktoria Plze.',matchnames[i]):
                matchnames[i]=re.sub('Viktoria Plze.','Victoria Plzen',matchnames[i]);
            elif re.search('FK Austria Wien',matchnames[i]):
                matchnames[i]=re.sub('FK Austria Wien','Austria Wien',matchnames[i]);
            elif re.search('FC Astana',matchnames[i]):
                matchnames[i]=re.sub('FC Astana','Astana',matchnames[i]);
            elif re.search('Fenerbah.e SK',matchnames[i]):
                matchnames[i]=re.sub('Fenerbah.e SK','Fenerbahçe',matchnames[i]);
            elif re.search('SK Rapid Wien',matchnames[i]):
                matchnames[i]=re.sub('SK Rapid Wien','Rapid Wien',matchnames[i]);
            elif re.search('Racing Genk',matchnames[i]):
                matchnames[i]=re.sub('Racing Genk','Genk',matchnames[i]);
            elif re.search('Zorya Luhansk',matchnames[i]):
                matchnames[i]=re.sub('Zorya Luhansk','Zorya',matchnames[i]);
            elif re.search('AA Gent',matchnames[i]):
                matchnames[i]=re.sub('AA Gent','Gent',matchnames[i]);
            elif re.search('FC Schalke 04',matchnames[i]):
                matchnames[i]=re.sub('FC Schalke 04','Schalke 04',matchnames[i]);
            elif re.search('Internazionale',matchnames[i]):
                matchnames[i]=re.sub('Internazionale','Inter',matchnames[i]);
            elif re.search('AC Sparta Praha',matchnames[i]):
                matchnames[i]=re.sub('AC Sparta Praha','Sparta Praha',matchnames[i]);
            elif re.search('OGC Nice',matchnames[i]):
                matchnames[i]=re.sub('OGC Nice','Nice',matchnames[i]);
            elif re.search('FC Krasnodar',matchnames[i]):
                matchnames[i]=re.sub('FC Krasnodar','Krasnodar',matchnames[i]);
            elif re.search('Celta de Vigo',matchnames[i]):
                matchnames[i]=re.sub('Celta de Vigo','Celta Vigo',matchnames[i]);
            elif re.search('Hapoel Be''er Sheva',matchnames[i]):
                matchnames[i]=re.sub('Hapoel Be''er Sheva','Hapoel',matchnames[i]);
            elif re.search('Apoel Nicosia',matchnames[i]):
                matchnames[i]=re.sub('Apoel Nicosia','APOEL',matchnames[i]);
            elif re.search('Olympiakos Piraeus',matchnames[i]):
                matchnames[i]=re.sub('Olympiakos Piraeus','Olympiacos',matchnames[i]);
            elif re.search('Osmanl.spor',matchnames[i]):
                matchnames[i]=re.sub('Osmanl.spor','Osmanliispor',matchnames[i]);
            elif re.search('PAOK Thessaloniki',matchnames[i]):
                matchnames[i]=re.sub('PAOK Thessaloniki','PAOK',matchnames[i]);
            elif re.search('Athletic Club Bilbao',matchnames[i]):
                matchnames[i]=re.sub('Athletic Club Bilbao','Athletic Bilbao',matchnames[i]);
            elif re.search('Hapoel Beer Sheva',matchnames[i]):
                matchnames[i]=re.sub('Hapoel Beer Sheva','Hapoel',matchnames[i]);
            elif re.search('FC Z.rich',matchnames[i]):
                matchnames[i]=re.sub('FC Z.rich','Zürich',matchnames[i]);
            #Serie A
            elif re.search('Chievo Verona',matchnames[i]):
                matchnames[i]=re.sub('Chievo Verona','Chievo',matchnames[i]);
            elif re.search('Hellas Verona',matchnames[i]):
                matchnames[i]=re.sub('Hellas Verona','Verona',matchnames[i]);
            elif re.search('Spal',matchnames[i]):
                matchnames[i]=re.sub('Spal','SPAL',matchnames[i]);
            elif re.search('SPAL 2013',matchnames[i]):
                matchnames[i]=re.sub('SPAL 2013','SPAL',matchnames[i]);
            elif re.search('ChievoVerona',matchnames[i]):
                matchnames[i]=re.sub('ChievoVerona','Chievo',matchnames[i]);
            elif re.search('Benevento Calcio',matchnames[i]):
                matchnames[i]=re.sub('Benevento Calcio','Benevento',matchnames[i]);
            elif re.search('AC Milan',matchnames[i]):
                matchnames[i]=re.sub('AC Milan','Milan',matchnames[i]);
            elif re.search('SSC Napoli',matchnames[i]):
                matchnames[i]=re.sub('SSC Napoli','Napoli',matchnames[i]);
            elif re.search('San José Sharks',matchnames[i]):
                matchnames[i]=re.sub('San José Sharks','San Jose Sharks',matchnames[i]);
            elif re.search('St. Louis Blues',matchnames[i]):
                matchnames[i]=re.sub('St. Louis Blues','St Louis Blues',matchnames[i]);
            # Fa Cup 
            elif re.search('Eastleigh FC',matchnames[i]):
                matchnames[i]=re.sub('Eastleigh FC','Eastleigh',matchnames[i]);
            elif re.search('Derby County',matchnames[i]):
                matchnames[i]=re.sub('Derby County','Derby',matchnames[i]);
            elif re.search('Burton Albion',matchnames[i]):
                matchnames[i]=re.sub('Burton Albion','Burton',matchnames[i]);
            elif re.search('Accrington Stanley',matchnames[i]):
                matchnames[i]=re.sub('Accrington Stanley','Accrington',matchnames[i]);
            elif re.search('Luton Town',matchnames[i]):
                matchnames[i]=re.sub('Luton Town','Luton',matchnames[i]);
            elif re.search('Birmingham City',matchnames[i]):
                matchnames[i]=re.sub('Birmingham City','Birmingham',matchnames[i]);
            elif re.search('Newcastle United',matchnames[i]):
                matchnames[i]=re.sub('Newcastle United','Newcastle',matchnames[i]);
            elif re.search('Brighton & Hove Albion',matchnames[i]):
                matchnames[i]=re.sub('Brighton & Hove Albion','Brighton',matchnames[i]);
            elif re.search('Milton Keynes Dons',matchnames[i]):
                matchnames[i]=re.sub('Milton Keynes Dons','Milton Keynes',matchnames[i]);
            elif re.search('Fleetwood Town',matchnames[i]):
                matchnames[i]=re.sub('Fleetwood Town','Fleetwood',matchnames[i]);
            elif re.search('Huddersfield Town',matchnames[i]):
                matchnames[i]=re.sub('Huddersfield Town','Huddersfield',matchnames[i]);
            elif re.search('Ipswich Town',matchnames[i]):
                matchnames[i]=re.sub('Ipswich Town','Ipswich',matchnames[i]);
            elif re.search('Lincoln City',matchnames[i]):
                matchnames[i]=re.sub('Lincoln City','Lincoln',matchnames[i]);
            elif re.search('Ipswich Town',matchnames[i]):
                matchnames[i]=re.sub('Ipswich Town','Ipswich',matchnames[i]);
            elif re.search('Bolton Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Bolton Wanderers','Bolton',matchnames[i]);
            elif re.search('Cardiff City',matchnames[i]):
                matchnames[i]=re.sub('Cardiff City','Cardiff',matchnames[i]);
            elif re.search('Sheffield Wednesday',matchnames[i]):
                matchnames[i]=re.sub('Sheffield Wednesday','Sheffield Wed',matchnames[i]);
            elif re.search('Norwich City',matchnames[i]):
                matchnames[i]=re.sub('Norwich City','Norwich',matchnames[i]);
            elif re.search('Preston North End',matchnames[i]):
                matchnames[i]=re.sub('Preston North End','Preston',matchnames[i]);
            elif re.search('Queens Park Rangers',matchnames[i]):
                matchnames[i]=re.sub('Queens Park Rangers','QPR',matchnames[i]);
            elif re.search('Blackburn Rovers',matchnames[i]):
                matchnames[i]=re.sub('Blackburn Rovers','Blackburn',matchnames[i]);
            elif re.search('Rotherham United',matchnames[i]):
                matchnames[i]=re.sub('Rotherham United','Rotherham',matchnames[i]);
            elif re.search('Oxford United',matchnames[i]):
                matchnames[i]=re.sub('Oxford United','Oxford Utd',matchnames[i]);
            elif re.search('Wolverhampton Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Wolverhampton Wanderers','Wolves',matchnames[i]);
            elif re.search('Wigan Athletic',matchnames[i]):
                matchnames[i]=re.sub('Wigan Athletic','Wigan',matchnames[i]);
            elif re.search('Wycombe Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Wycombe Wanderers','Wycombe',matchnames[i]);
            elif re.search('Plymouth Argyle',matchnames[i]):
                matchnames[i]=re.sub('Plymouth Argyle','Plymouth',matchnames[i]);
            elif re.search('Peterborough United',matchnames[i]):
                matchnames[i]=re.sub('Peterborough United','Peterborough',matchnames[i]);
            elif re.search('Cambridge United',matchnames[i]):
                matchnames[i]=re.sub('Cambridge United','Cambridge',matchnames[i]);
            elif re.search('Leeds United',matchnames[i]):
                matchnames[i]=re.sub('Leeds United','Leeds',matchnames[i]);
            elif re.search('Brighton and Hove Albion',matchnames[i]):
                matchnames[i]=re.sub('Brighton and Hove Albion','Brighton',matchnames[i]);
            #La Liga
            elif re.search('Celta Vigo',matchnames[i]):
                matchnames[i]=re.sub('Celta Vigo','Celta',matchnames[i]);
            elif re.search('Levante UD',matchnames[i]):
                matchnames[i]=re.sub('Levante UD','Levante',matchnames[i]);
            elif re.search('Deportivo La Coruña',matchnames[i]):
                matchnames[i]=re.sub('Deportivo La Coruña','Dep La Coruña',matchnames[i]);
            elif re.search('Deportivo de La Coruna',matchnames[i]):
                matchnames[i]=re.sub('Deportivo de La Coruna','Dep La Coruña',matchnames[i]);
            elif re.search('Granada CF',matchnames[i]):
                matchnames[i]=re.sub('Granada CF','Granada',matchnames[i]);
            elif re.search('Deportiva Las Palmas',matchnames[i]):
                matchnames[i]=re.sub('Deportiva Las Palmas','Las Palmas',matchnames[i]);
            elif re.search('Deportivo Alaves',matchnames[i]):
                matchnames[i]=re.sub('Deportivo Alaves','Alavés',matchnames[i]);
            elif re.search('Málaga',matchnames[i]):
                matchnames[i]=re.sub('Málaga','Malaga',matchnames[i]);
            # TL
            elif re.search('Sandefjord Fotball',matchnames[i]):
                matchnames[i]=re.sub('Sandefjord Fotball','Sandefjord',matchnames[i]);
            elif re.search('Odds Ballklubb',matchnames[i]):
                matchnames[i]=re.sub('Odds Ballklubb','Odd',matchnames[i]);
            elif re.search('Kristiansund BK',matchnames[i]):
                matchnames[i]=re.sub('Kristiansund BK','Kristiansund',matchnames[i]);
            elif re.search('Stroemsgodset',matchnames[i]):
                matchnames[i]=re.sub('Stroemsgodset','Strømsgodset',matchnames[i]);
            elif re.search('Stromsgodset',matchnames[i]):
                matchnames[i]=re.sub('Stromsgodset','Strømsgodset',matchnames[i]);
            elif re.search('Valerenga',matchnames[i]):
                matchnames[i]=re.sub('Valerenga','Vålerenga',matchnames[i]);
            elif re.search('Stabaek',matchnames[i]):
                matchnames[i]=re.sub('Stabaek','Stabæk',matchnames[i]);
            elif re.search('Lillestrom',matchnames[i]):
                matchnames[i]=re.sub('Lillestrom','Lillestrøm',matchnames[i]);
            elif re.search('Tromsoe',matchnames[i]):
                matchnames[i]=re.sub('Tromsoe','Tromsø',matchnames[i]);
            elif re.search('Tromso',matchnames[i]):
                matchnames[i]=re.sub('Tromso','Tromsø',matchnames[i]);
            elif re.search('Odd Grenland',matchnames[i]):
                matchnames[i]=re.sub('Odd Grenland','Odd',matchnames[i]);
            # Championship
            elif re.search('Queens Park Rangers',matchnames[i]):
                matchnames[i]=re.sub('Queens Park Rangers','QPR',matchnames[i]);
            elif re.search('Queens Park Range',matchnames[i]):
                matchnames[i]=re.sub('Queens Park Range','QPR',matchnames[i]);
            elif re.search('Burton Albion',matchnames[i]):
                matchnames[i]=re.sub('Burton Albion','Burton',matchnames[i]);
            elif re.search('Huddersfield Town',matchnames[i]):
                matchnames[i]=re.sub('Huddersfield Town','Huddersfield',matchnames[i]);
            elif re.search('Leeds United',matchnames[i]):
                matchnames[i]=re.sub('Leeds United','Leeds',matchnames[i]);
            elif re.search('Newcastle United',matchnames[i]):
                matchnames[i]=re.sub('Newcastle United','Newcastle',matchnames[i]);
            elif re.search('Preston North End',matchnames[i]):
                matchnames[i]=re.sub('Preston North End','Preston',matchnames[i]);
            elif re.search('Rotherham United',matchnames[i]):
                matchnames[i]=re.sub('Rotherham United','Rotherham',matchnames[i]);
            elif re.search('Sheffield Wednesday',matchnames[i]):
                matchnames[i]=re.sub('Sheffield Wednesday','Sheffield Wed',matchnames[i]);
            elif re.search('Sheffield Wednesd',matchnames[i]):
                matchnames[i]=re.sub('Sheffield Wednesd','Sheffield Wed',matchnames[i]);
            elif re.search('Sheffield Utd',matchnames[i]):
                matchnames[i]=re.sub('Sheffield Utd','Sheffield United',matchnames[i]);
            elif re.search('Derby County',matchnames[i]):
                matchnames[i]=re.sub('Derby County','Derby',matchnames[i]);
            elif re.search('Wigan Athletic',matchnames[i]):
                matchnames[i]=re.sub('Wigan Athletic','Wigan',matchnames[i]);
            elif re.search('Cardiff City',matchnames[i]):
                matchnames[i]=re.sub('Cardiff City','Cardiff',matchnames[i]);
            elif re.search('Wolverhampton Wanderers',matchnames[i]):
                matchnames[i]=re.sub('Wolverhampton Wanderers','Wolves',matchnames[i]);
            elif re.search('Blackburn Rovers',matchnames[i]):
                matchnames[i]=re.sub('Blackburn Rovers','Blackburn',matchnames[i]);
            # International Ice Hockey
            elif re.search('.u00F8',matchnames[i]):
                matchnames[i]=re.sub('.u00F8','ø',matchnames[i]);
            elif re.search('.u00F8',matchnames[i]):
                matchnames[i]=re.sub('.u00F8','ø',matchnames[i]);
            elif re.search('.u00F8',matchnames[i]):
                matchnames[i]=re.sub('.u00F8','ø',matchnames[i]);
            elif re.search('.u00F8',matchnames[i]):
                matchnames[i]=re.sub('.u00F8','ø',matchnames[i]);
            elif re.search('.u00F8',matchnames[i]):
                matchnames[i]=re.sub('.u00F8','ø',matchnames[i]);
            # Allsvenskan
            elif re.search('AFC Utd',matchnames[i]):
                matchnames[i]=re.sub('AFC Utd','Eskilstuna',matchnames[i]);
            elif re.search('Athletic Eskilstuna',matchnames[i]):
                matchnames[i]=re.sub('Athletic Eskilstuna','Eskilstuna',matchnames[i]);
            elif re.search('Jönköpings Södra IF',matchnames[i]):
                matchnames[i]=re.sub('Jönköpings Södra IF','Jonkopings Sodra',matchnames[i]);
            elif re.search('IFK Göteborg',matchnames[i]):
                matchnames[i]=re.sub('IFK Göteborg','Goteborg',matchnames[i]);
            elif re.search('AFC Eskilstuna',matchnames[i]):
                matchnames[i]=re.sub('AFC Eskilstuna','Eskilstuna',matchnames[i]);
            elif re.search('Malmö FF',matchnames[i]):
                matchnames[i]=re.sub('Malmö FF','Malmo',matchnames[i]);
            elif re.search('IFK Norrköping',matchnames[i]):
                matchnames[i]=re.sub('IFK Norrköping','Norrkoping',matchnames[i]);
            elif re.search('BK Häcken',matchnames[i]):
                matchnames[i]=re.sub('BK Häcken','Hacken',matchnames[i]);
            elif re.search('Häcken',matchnames[i]):
                matchnames[i]=re.sub('Häcken','Hacken',matchnames[i]);
            elif re.search('IK Sirius FK',matchnames[i]):
                matchnames[i]=re.sub('IK Sirius FK','Sirius',matchnames[i]);
            elif re.search('IK Sirius',matchnames[i]):
                matchnames[i]=re.sub('IK Sirius','Sirius',matchnames[i]);
            elif re.search('Sirius FK',matchnames[i]):
                matchnames[i]=re.sub('Sirius FK','Sirius',matchnames[i]);
            elif re.search('Örebro SK',matchnames[i]):
                matchnames[i]=re.sub('Örebro SK','Orebro',matchnames[i]);
            elif re.search('Djurgårdens IF',matchnames[i]):
                matchnames[i]=re.sub('Djurgårdens IF','Djurgarden',matchnames[i]);
            elif re.search('Djurgården',matchnames[i]):
                matchnames[i]=re.sub('Djurgården','Djurgarden',matchnames[i]);
            elif re.search('Östersunds FK',matchnames[i]):
                matchnames[i]=re.sub('Östersunds FK','Ostersund',matchnames[i]);
            elif re.search('IF Elfsborg',matchnames[i]):
                matchnames[i]=re.sub('IF Elfsborg','Elfsborg',matchnames[i]);
            elif re.search('IFK Norrkoping',matchnames[i]):
                matchnames[i]=re.sub('IFK Norrkoping','Norrkoping',matchnames[i]);
            elif re.search('Djurgardens IF',matchnames[i]):
                matchnames[i]=re.sub('Djurgardens IF','Djurgarden',matchnames[i]);
            elif re.search('Halmstads BK',matchnames[i]):
                matchnames[i]=re.sub('Halmstads BK','Halmstad',matchnames[i]);
            elif re.search('GIF Sundsvall',matchnames[i]):
                matchnames[i]=re.sub('GIF Sundsvall','Sundsvall',matchnames[i]);
            elif re.search('IFK Goteborg',matchnames[i]):
                matchnames[i]=re.sub('IFK Goteborg','Goteborg',matchnames[i]);
            elif re.search('Ostersunds FK',matchnames[i]):
                matchnames[i]=re.sub('Ostersunds FK','Ostersund',matchnames[i]);
            elif re.search('Malmo FF',matchnames[i]):
                matchnames[i]=re.sub('Malmo FF','Malmo',matchnames[i]);
            elif re.search('Kalmar FF',matchnames[i]):
                matchnames[i]=re.sub('Kalmar FF','Kalmar',matchnames[i]);
            elif re.search('Hammarby IF',matchnames[i]):
                matchnames[i]=re.sub('Hammarby IF','Hammarby',matchnames[i]);
            elif re.search('Jönköpings Södra',matchnames[i]):
                matchnames[i]=re.sub('Jönköpings Södra','Jonkoping',matchnames[i]);
            elif re.search('Jonkopings Sodra',matchnames[i]):
                matchnames[i]=re.sub('Jonkopings Sodra','Jonkoping',matchnames[i]);
            elif re.search('BK Hacken',matchnames[i]):
                matchnames[i]=re.sub('BK Hacken','Hacken',matchnames[i]);
            elif re.search('Orebro SK',matchnames[i]):
                matchnames[i]=re.sub('Orebro SK','Orebro',matchnames[i]);
            # NM
            elif re.search('Florø SK',matchnames[i]):
                matchnames[i]=re.sub('Florø SK','Florø',matchnames[i]);
            elif re.search('KFUM Oslo',matchnames[i]):
                matchnames[i]=re.sub('KFUM Oslo','KFUM',matchnames[i]);
            elif re.search('Kråkerøy IL',matchnames[i]):
                matchnames[i]=re.sub('Kråkerøy IL','Kråkerøy',matchnames[i]);
            elif re.search('Kvik Halden FK',matchnames[i]):
                matchnames[i]=re.sub('Kvik Halden FK','Kvik Halden',matchnames[i]);
            elif re.search('Skeid Fotball',matchnames[i]):
                matchnames[i]=re.sub('Skeid Fotball','Skeid',matchnames[i]);
            elif re.search('Ullensaker/Kisa',matchnames[i]):
                matchnames[i]=re.sub('Ullensaker/Kisa','Ull/Kisa',matchnames[i]);
            elif re.search('Byåsen TF',matchnames[i]):
                matchnames[i]=re.sub('Byåsen TF','Byåsen',matchnames[i]);
            elif re.search('Byasen',matchnames[i]):
                matchnames[i]=re.sub('Byasen','Byåsen',matchnames[i]);
            elif re.search('Flekkeroey IL',matchnames[i]):
                matchnames[i]=re.sub('Flekkeroey IL','Flekkerøy',matchnames[i]);
            elif re.search('Floeya',matchnames[i]):
                matchnames[i]=re.sub('Floeya','Fløya',matchnames[i]);
            elif re.search('Floroe',matchnames[i]):
                matchnames[i]=re.sub('Floroe','Florø',matchnames[i]);
            elif re.search('Hoedd',matchnames[i]):
                matchnames[i]=re.sub('Hoedd','Hødd',matchnames[i]);
            elif re.search('Baerum',matchnames[i]):
                matchnames[i]=re.sub('Baerum','Bærum',matchnames[i]);
            elif re.search('Krakeroey IL',matchnames[i]):
                matchnames[i]=re.sub('Krakeroey IL','Kråkerøy',matchnames[i]);
            elif re.search('Mjoendalen',matchnames[i]):
                matchnames[i]=re.sub('Mjoendalen','Mjøndalen',matchnames[i]);
            elif re.search('Mosjoeen',matchnames[i]):
                matchnames[i]=re.sub('Mosjoeen','Mosjøen',matchnames[i]);
            elif re.search('Nybergsund IL-Trysil',matchnames[i]):
                matchnames[i]=re.sub('Nybergsund IL-Trysil','Nybergsund',matchnames[i]);
            elif re.search('Nybergsund IL Trysil',matchnames[i]):
                matchnames[i]=re.sub('Nybergsund IL Trysil','Nybergsund',matchnames[i]);
            elif re.search('Kongsvinger IL',matchnames[i]):
                matchnames[i]=re.sub('Kongsvinger IL','Kongsvinger',matchnames[i]);
            elif re.search('OErn Horten',matchnames[i]):
                matchnames[i]=re.sub('OErn Horten','Ørn-Horten',matchnames[i]);
            elif re.search('Stjoerdals-Blink IL',matchnames[i]):
                matchnames[i]=re.sub('Stjoerdals-Blink IL','Stjørdals/Blink',matchnames[i]);
            elif re.search('Bodoe..Glimt',matchnames[i]):
                matchnames[i]=re.sub('Bodoe..Glimt','Bodø/Glimt',matchnames[i]);
            elif re.search('Stroemmen',matchnames[i]):
                matchnames[i]=re.sub('Stroemmen','Strømmen',matchnames[i]);
            elif re.search('Kjelsas',matchnames[i]):
                matchnames[i]=re.sub('Kjelsas','Kjelsås',matchnames[i]);
            elif re.search('Ullensaker..Kisa',matchnames[i]):
                matchnames[i]=re.sub('Ullensaker..Kisa','Ull/Kisa',matchnames[i]);
            elif re.search('Asane',matchnames[i]):
                matchnames[i]=re.sub('Asane','Åsane',matchnames[i]);
            elif re.search('Levanger FK',matchnames[i]):
                matchnames[i]=re.sub('Levanger FK','Levanger',matchnames[i]);
            elif re.search('Flekkerøy IL',matchnames[i]):
                matchnames[i]=re.sub('Flekkerøy IL','Flekkerøy',matchnames[i]);
            elif re.search('Stjørdals-Blink IL',matchnames[i]):
                matchnames[i]=re.sub('Stjørdals-Blink IL','Stjørdals/Blink',matchnames[i]);
            elif re.search('Ørn Horten',matchnames[i]):
                matchnames[i]=re.sub('Ørn Horten','Ørn-Horten',matchnames[i]);
            # MLS
            elif re.search('D.C. United',matchnames[i]):
                matchnames[i]=re.sub('D.C. United','DC United',matchnames[i]);
            # Europe
            elif re.search('FYR Macedonia',matchnames[i]):
                matchnames[i]=re.sub('FYR Macedonia','Macedonia',matchnames[i]);
            elif re.search('Bosnia-Herzegovina',matchnames[i]):
                matchnames[i]=re.sub('Bosnia-Herzegovina','Bosnia & Herzegovina',matchnames[i]);
            elif re.search('Bosnia and Herzegovina',matchnames[i]):
                matchnames[i]=re.sub('Bosnia and Herzegovina','Bosnia & Herzegovina',matchnames[i]);
            elif re.search('Ireland Republic',matchnames[i]):
                matchnames[i]=re.sub('Ireland Republic','Ireland',matchnames[i]);
            # Tennis
            elif re.search('Haider-Maurer, Mario',matchnames[i]):
                matchnames[i]=re.sub('Haider-Maurer, Mario','Haider-Maurer, M',matchnames[i]);
            elif re.search('Kuznetsov, Andrey',matchnames[i]):
                matchnames[i]=re.sub('Kuznetsov, Andrey','Kuznetsov, A',matchnames[i]);
            elif re.search('Bautista-Agut, Roberto',matchnames[i]):
                matchnames[i]=re.sub('Bautista-Agut, Roberto','Bautista Agut, R',matchnames[i]);
            elif re.search('Klizan, Martin',matchnames[i]):
                matchnames[i]=re.sub('Klizan, Martin','Klizan, M',matchnames[i]);
            elif re.search('Djokovic, Novak',matchnames[i]):
                matchnames[i]=re.sub('Djokovic, Novak','Djokovic, N',matchnames[i]);
            elif re.search('Jaziri, Malek',matchnames[i]):
                matchnames[i]=re.sub('Jaziri, Malek','Jaziri, M',matchnames[i]);
            elif re.search('Pouille, Lucas',matchnames[i]):
                matchnames[i]=re.sub('Pouille, Lucas','Pouille, L',matchnames[i]);
            elif re.search('Edmund, Kyle',matchnames[i]):
                matchnames[i]=re.sub('Edmund, Kyle','Edmund, K',matchnames[i]);
            elif re.search('Ward, Alexander',matchnames[i]):
                matchnames[i]=re.sub('Ward, Alexander','Ward, A',matchnames[i]);
            elif re.search('Murray, Andy',matchnames[i]):
                matchnames[i]=re.sub('Murray, Andy','Murray, A',matchnames[i]);
            elif re.search('Bublik, Alexander',matchnames[i]):
                matchnames[i]=re.sub('Bublik, Alexander','Bublik, A',matchnames[i]);
            elif re.search('Tsonga, Jo-Wilfried',matchnames[i]):
                matchnames[i]=re.sub('Tsonga, Jo-Wilfried','Tsonga, JW',matchnames[i]);
            elif re.search('Norrie, Cameron',matchnames[i]):
                matchnames[i]=re.sub('Norrie, Cameron','Norrie, C',matchnames[i]);
            elif re.search('Nadal, Rafael',matchnames[i]):
                matchnames[i]=re.sub('Nadal, Rafael','Nadal, R',matchnames[i]);
            elif re.search('Millman, John',matchnames[i]):
                matchnames[i]=re.sub('Millman, John','Millman, J',matchnames[i]);
            elif re.search('Dutra Silva, Rogerio',matchnames[i]):
                matchnames[i]=re.sub('Dutra Silva, Rogerio','Dutra Silva, R',matchnames[i]);
            elif re.search('Paire, Benoit',matchnames[i]):
                matchnames[i]=re.sub('Paire, Benoit','Paire, B',matchnames[i]);
            elif re.search('Kyrgios, Nick',matchnames[i]):
                matchnames[i]=re.sub('Kyrgios, Nick','Kyrgios, N',matchnames[i]);
            elif re.search('Herbert, Pierre-Hugues',matchnames[i]):
                matchnames[i]=re.sub('Herbert, Pierre-Hugues','Herbert, PH',matchnames[i]);
            elif re.search('Dolgopolov, Alexandr',matchnames[i]):
                matchnames[i]=re.sub('Dolgopolov, Alexandr','Dolgopolov, A',matchnames[i]);
            elif re.search('Federer, Roger',matchnames[i]):
                matchnames[i]=re.sub('Federer, Roger','Federer, R',matchnames[i]);
            elif re.search('Raonic, Milos',matchnames[i]):
                matchnames[i]=re.sub('Raonic, Milos','Raonic, M',matchnames[i]);
            elif re.search('Struff, Jan-Lennard',matchnames[i]):
                matchnames[i]=re.sub('Struff, Jan-Lennard','Struff, JL',matchnames[i]);
            elif re.search('Sock, Jack',matchnames[i]):
                matchnames[i]=re.sub('Sock, Jack','Sock, J',matchnames[i]);
            elif re.search('Garin, Christian',matchnames[i]):
                matchnames[i]=re.sub('Garin, Christian','Garin, C',matchnames[i]);
            elif re.search('Kohlschreiber, Philipp',matchnames[i]):
                matchnames[i]=re.sub('Kohlschreiber, Philipp','Kohlschreiber, P',matchnames[i]);
            elif re.search('Cilic, Marin',matchnames[i]):
                matchnames[i]=re.sub('Cilic, Marin','Cilic, M',matchnames[i]);
            elif re.search('Fucsovics, Marton',matchnames[i]):
                matchnames[i]=re.sub('Fucsovics, Marton','Fucsovics, M',matchnames[i]);
            elif re.search('Muller, Gilles',matchnames[i]):
                matchnames[i]=re.sub('Muller, Gilles','Muller, G',matchnames[i]);
            elif re.search('Donskoy, Evgeny',matchnames[i]):
                matchnames[i]=re.sub('Donskoy, Evgeny','Donskoy, E',matchnames[i]);
            elif re.search('Bagnis, Facundo',matchnames[i]):
                matchnames[i]=re.sub('Bagnis, Facundo','Bagnis, F',matchnames[i]);
            elif re.search('Albot, Radu ',matchnames[i]):
                matchnames[i]=re.sub('Albot, Radu ','Albot, R',matchnames[i]);
            elif re.search('Albot, Radu',matchnames[i]):
                matchnames[i]=re.sub('Albot, Radu','Albot, R',matchnames[i]);
            elif re.search('Dimitrov, Grigor',matchnames[i]):
                matchnames[i]=re.sub('Dimitrov, Grigor','Dimitrov, G',matchnames[i]);
            elif re.search('Schwartzman, Diego Sebastian',matchnames[i]):
                matchnames[i]=re.sub('Schwartzman, Diego Sebastian','Schwartzman, DS',matchnames[i]);
            elif re.search('Gasquet, Richard ',matchnames[i]):
                matchnames[i]=re.sub('Gasquet, Richard ','Gasquet, R',matchnames[i]);
            elif re.search('Gasquet, Richard',matchnames[i]):
                matchnames[i]=re.sub('Gasquet, Richard','Gasquet, R',matchnames[i]);
            elif re.search('Ferrer, David',matchnames[i]):
                matchnames[i]=re.sub('Ferrer, David','Ferrer, D',matchnames[i]);
            elif re.search('Tursunov, Dmitry',matchnames[i]):
                matchnames[i]=re.sub('Tursunov, Dmitry','Tursunov, D',matchnames[i]);
            elif re.search('Fognini, Fabio',matchnames[i]):
                matchnames[i]=re.sub('Fognini, Fabio','Fognini, F',matchnames[i]);
            elif re.search('Fabbiano, Thomas',matchnames[i]):
                matchnames[i]=re.sub('Fabbiano, Thomas','Fabbiano, T',matchnames[i]);
            elif re.search('Querrey, Sam',matchnames[i]):
                matchnames[i]=re.sub('Querrey, Sam','Querrey, S',matchnames[i]);
            elif re.search('Sugita, Yuichi',matchnames[i]):
                matchnames[i]=re.sub('Sugita, Yuichi','Sugita, Y',matchnames[i]);
            elif re.search('Klein, Brydan',matchnames[i]):
                matchnames[i]=re.sub('Klein, Brydan','Klein, B',matchnames[i]);
            elif re.search('Monteiro, Thiago',matchnames[i]):
                matchnames[i]=re.sub('Monteiro, Thiago','Monteiro, T',matchnames[i]);
            elif re.search('Whittington, Andrew',matchnames[i]):
                matchnames[i]=re.sub('Whittington, Andrew','Whittington, A',matchnames[i]);
            elif re.search('Ward, James',matchnames[i]):
                matchnames[i]=re.sub('Ward, James','Ward, J',matchnames[i]);
            elif re.search('Baghdatis, Marcos',matchnames[i]):
                matchnames[i]=re.sub('Baghdatis, Marcos','Baghdatis, M',matchnames[i]);
            elif re.search('Rublev, Andrey',matchnames[i]):
                matchnames[i]=re.sub('Rublev, Andrey','Rublev, A',matchnames[i]);
            elif re.search('Travaglia, Stefano',matchnames[i]):
                matchnames[i]=re.sub('Travaglia, Stefano','Travaglia, S',matchnames[i]);
            elif re.search('Darcis, Steve',matchnames[i]):
                matchnames[i]=re.sub('Darcis, Steve','Darcis, S',matchnames[i]);
            elif re.search('Berankis, Ricardas',matchnames[i]):
                matchnames[i]=re.sub('Berankis, Ricardas','Berankis, R',matchnames[i]);
            elif re.search('Haider-Maurer, Andreas',matchnames[i]):
                matchnames[i]=re.sub('Haider-Maurer, Andreas','Haider-Maurer, A',matchnames[i]);
            elif re.search('Bautista-Agut, Roberto',matchnames[i]):
                matchnames[i]=re.sub('Bautista-Agut, Roberto','Bautista Agut, R',matchnames[i]);
            elif re.search('Rosol, Lukas',matchnames[i]):
                matchnames[i]=re.sub('Rosol, Lukas','Rosol, L',matchnames[i]);
            elif re.search('Laaksonen, Henri',matchnames[i]):
                matchnames[i]=re.sub('Laaksonen, Henri','Laaksonen, H',matchnames[i]);
            elif re.search('Sela, Dudi',matchnames[i]):
                matchnames[i]=re.sub('Sela, Dudi','Sela, D',matchnames[i]);
            elif re.search('Granollers, Marcel',matchnames[i]):
                matchnames[i]=re.sub('Granollers, Marcel','Granollers, M',matchnames[i]);
            elif re.search('Bellucci, Thomaz',matchnames[i]):
                matchnames[i]=re.sub('Bellucci, Thomaz','Bellucci, T',matchnames[i]);
            elif re.search('Ofner, Sebastian',matchnames[i]):
                matchnames[i]=re.sub('Ofner, Sebastian','Ofner, S',matchnames[i]);
            elif re.search('Chardy, Jeremy',matchnames[i]):
                matchnames[i]=re.sub('Chardy, Jeremy','Chardy, J',matchnames[i]);
            elif re.search('Berdych, Tomas',matchnames[i]):
                matchnames[i]=re.sub('Berdych, Tomas','Berdych, T',matchnames[i]);
            elif re.search('Kukushkin, Mikhail',matchnames[i]):
                matchnames[i]=re.sub('Kukushkin, Mikhail','Kukushkin, M',matchnames[i]);
            elif re.search('Daniel, Taro',matchnames[i]):
                matchnames[i]=re.sub('Daniel, Taro','Daniel, T',matchnames[i]);
            elif re.search('Dzumhur, Damir',matchnames[i]):
                matchnames[i]=re.sub('Dzumhur, Damir','Dzumhur, D',matchnames[i]);
            elif re.search('Olivo, Renzo',matchnames[i]):
                matchnames[i]=re.sub('Olivo, Renzo','Olivo, R',matchnames[i]);
            elif re.search('Thiem, Dominic',matchnames[i]):
                matchnames[i]=re.sub('Thiem, Dominic','Thiem, D',matchnames[i]);
            elif re.search('Pospisil, Vasek',matchnames[i]):
                matchnames[i]=re.sub('Pospisil, Vasek','Pospisil, V',matchnames[i]);
            elif re.search('Tipsarevic, Janko',matchnames[i]):
                matchnames[i]=re.sub('Tipsarevic, Janko','Tipsarevic, J',matchnames[i]);
            elif re.search('Donaldson, Jared',matchnames[i]):
                matchnames[i]=re.sub('Donaldson, Jared','Donaldson, J',matchnames[i]);
            elif re.search('Gombos, Norbert',matchnames[i]):
                matchnames[i]=re.sub('Gombos, Norbert','Gombos, N',matchnames[i]);
            elif re.search('Seppi, Andreas',matchnames[i]):
                matchnames[i]=re.sub('Seppi, Andreas','Seppi, A',matchnames[i]);
            elif re.search('Mannarino, Adrian',matchnames[i]):
                matchnames[i]=re.sub('Mannarino, Adrian','Mannarino, A',matchnames[i]);
            elif re.search('Lopez, Feliciano',matchnames[i]):
                matchnames[i]=re.sub('Lopez, Feliciano','Lopez, F',matchnames[i]);
            elif re.search('Simon, Gilles',matchnames[i]):
                matchnames[i]=re.sub('Simon, Gilles','Simon, G',matchnames[i]);
            elif re.search('Jarry, Nicolas',matchnames[i]):
                matchnames[i]=re.sub('Jarry, Nicolas','Jarry, N',matchnames[i]);
            elif re.search('Zverev, Mischa',matchnames[i]):
                matchnames[i]=re.sub('Zverev, Mischa','Zverev, M',matchnames[i]);
            elif re.search('Tomic, Bernard',matchnames[i]):
                matchnames[i]=re.sub('Tomic, Bernard','Tomic, B',matchnames[i]);
            elif re.search('Medvedev, Daniil',matchnames[i]):
                matchnames[i]=re.sub('Medvedev, Daniil','Medvedev, D',matchnames[i]);
            elif re.search('Wawrinka, Stanislas',matchnames[i]):
                matchnames[i]=re.sub('Wawrinka, Stanislas','Wawrinka, S',matchnames[i]);
            elif re.search('Benneteau, Julien',matchnames[i]):
                matchnames[i]=re.sub('Benneteau, Julien','Benneteau, J',matchnames[i]);
            elif re.search('Stakhovsky, Sergiy',matchnames[i]):
                matchnames[i]=re.sub('Stakhovsky, Sergiy','Stakhovsky, S',matchnames[i]);
            elif re.search('Gojowczyk, Peter',matchnames[i]):
                matchnames[i]=re.sub('Gojowczyk, Peter','Gojowczyk, P',matchnames[i]);
            elif re.search('Copil, Marius',matchnames[i]):
                matchnames[i]=re.sub('Copil, Marius','Copil, M',matchnames[i]);
            elif re.search('Verdasco, Fernando',matchnames[i]):
                matchnames[i]=re.sub('Verdasco, Fernando','Verdasco, F',matchnames[i]);
            elif re.search('Anderson, Kevin',matchnames[i]):
                matchnames[i]=re.sub('Anderson, Kevin','Anderson, K',matchnames[i]);
            elif re.search('Bolelli, Simone',matchnames[i]):
                matchnames[i]=re.sub('Bolelli, Simone','Bolelli, S',matchnames[i]);
            elif re.search('Yen-Hsun Lu',matchnames[i]):
                matchnames[i]=re.sub('Yen-Hsun Lu','Lu, Y-H',matchnames[i]);
            elif re.search('Shapovalov, Denis',matchnames[i]):
                matchnames[i]=re.sub('Shapovalov, Denis','Shapovalov, D',matchnames[i]);
            elif re.search('Janowicz, Jerzy',matchnames[i]):
                matchnames[i]=re.sub('Janowicz, Jerzy','Janowicz, J',matchnames[i]);
            elif re.search('Troicki, Viktor',matchnames[i]):
                matchnames[i]=re.sub('Troicki, Viktor','Troicki, V',matchnames[i]);
            elif re.search('Mayer, Florian',matchnames[i]):
                matchnames[i]=re.sub('Mayer, Florian','Mayer, F',matchnames[i]);
            elif re.search('Young, Donald',matchnames[i]):
                matchnames[i]=re.sub('Young, Donald','Young, D',matchnames[i]);
            elif re.search('Istomin, Denis',matchnames[i]):
                matchnames[i]=re.sub('Istomin, Denis','Istomin, D',matchnames[i]);
            elif re.search('Thompson, Jordan',matchnames[i]):
                matchnames[i]=re.sub('Thompson, Jordan','Thompson, J',matchnames[i]);
            elif re.search('Ramos-Viñolas, Albert',matchnames[i]):
                matchnames[i]=re.sub('Ramos-Viñolas, Albert','Ramos Vinolas, A',matchnames[i]);
            elif re.search('Del Potro, Juan Martin',matchnames[i]):
                matchnames[i]=re.sub('Del Potro, Juan Martin','Del Potro, JM',matchnames[i]);
            elif re.search('Kokkinakis, Thanasi',matchnames[i]):
                matchnames[i]=re.sub('Kokkinakis, Thanasi','Kokkinakis, T',matchnames[i]);
            elif re.search('Khachanov, Karen',matchnames[i]):
                matchnames[i]=re.sub('Khachanov, Karen','Khachanov, K',matchnames[i]);
            elif re.search('Brands, Daniel',matchnames[i]):
                matchnames[i]=re.sub('Brands, Daniel','Brands, D',matchnames[i]);
            elif re.search('Monfils, Gael',matchnames[i]):
                matchnames[i]=re.sub('Monfils, Gael','Monfils, G',matchnames[i]);
            elif re.search('Berlocq, Carlos',matchnames[i]):
                matchnames[i]=re.sub('Berlocq, Carlos','Berlocq, C',matchnames[i]);
            elif re.search('Basilashvili, Nikoloz',matchnames[i]):
                matchnames[i]=re.sub('Basilashvili, Nikoloz','Basilashvili, N',matchnames[i]);
            elif re.search('Coric, Borna',matchnames[i]):
                matchnames[i]=re.sub('Coric, Borna','Coric, B',matchnames[i]);
            elif re.search('Harrison, Ryan',matchnames[i]):
                matchnames[i]=re.sub('Harrison, Ryan','Harrison, R',matchnames[i]);
            elif re.search('Gulbis, Ernests',matchnames[i]):
                matchnames[i]=re.sub('Gulbis, Ernests','Gulbis, E',matchnames[i]);
            elif re.search('Estrella Burgos, Victor',matchnames[i]):
                matchnames[i]=re.sub('Estrella Burgos, Victor','Estrella, V',matchnames[i]);
            elif re.search('Haas, Tommy',matchnames[i]):
                matchnames[i]=re.sub('Haas, Tommy','Haas, T',matchnames[i]);
            elif re.search('Bemelmans, Ruben',matchnames[i]):
                matchnames[i]=re.sub('Bemelmans, Ruben','Bemelmans, R',matchnames[i]);
            elif re.search('Pavlasek, Adam',matchnames[i]):
                matchnames[i]=re.sub('Pavlasek, Adam','Pavlasek, A',matchnames[i]);
            elif re.search('Escobedo, Ernesto',matchnames[i]):
                matchnames[i]=re.sub('Escobedo, Ernesto','Escobedo, E',matchnames[i]);
            elif re.search('Sousa, Joao',matchnames[i]):
                matchnames[i]=re.sub('Sousa, Joao','Sousa, J',matchnames[i]);
            elif re.search('Brown, Dustin',matchnames[i]):
                matchnames[i]=re.sub('Brown, Dustin','Brown, D',matchnames[i]);
            elif re.search('Tsitsipas, Stefanos',matchnames[i]):
                matchnames[i]=re.sub('Tsitsipas, Stefanos','Tsitsipas, S',matchnames[i]);
            elif re.search('Lajovic, Dusan',matchnames[i]):
                matchnames[i]=re.sub('Lajovic, Dusan','Lajovic, D',matchnames[i]);
            elif re.search('Vesely, Jiri',matchnames[i]):
                matchnames[i]=re.sub('Vesely, Jiri','Vesely, J',matchnames[i]);
            elif re.search('Marchenko, Illya',matchnames[i]):
                matchnames[i]=re.sub('Marchenko, Illya','Marchenko, I',matchnames[i]);
            elif re.search('Youzhny, Mikhail',matchnames[i]):
                matchnames[i]=re.sub('Youzhny, Mikhail','Youzhny, M',matchnames[i]);
            elif re.search('Mahut, Nicolas',matchnames[i]):
                matchnames[i]=re.sub('Mahut, Nicolas','Mahut, N',matchnames[i]);
            elif re.search('Zeballos, Horacio',matchnames[i]):
                matchnames[i]=re.sub('Zeballos, Horacio','Zeballos, H',matchnames[i]);
            elif re.search('Lorenzi, Paolo',matchnames[i]):
                matchnames[i]=re.sub('Lorenzi, Paolo','Lorenzi, P',matchnames[i]);
            elif re.search('Zverev, Alexander',matchnames[i]):
                matchnames[i]=re.sub('Zverev, Alexander','Zverev, A',matchnames[i]);
            elif re.search('Fritz, Taylor',matchnames[i]):
                matchnames[i]=re.sub('Fritz, Taylor','Fritz, T',matchnames[i]);
            elif re.search('Isner, John',matchnames[i]):
                matchnames[i]=re.sub('Isner, John','Isner, J',matchnames[i]);
            elif re.search('Haase, Robin',matchnames[i]):
                matchnames[i]=re.sub('Haase, Robin','Haase, R',matchnames[i]);
            elif re.search('Tiafoe, Frances',matchnames[i]):
                matchnames[i]=re.sub('Tiafoe, Frances','Tiafoe, F',matchnames[i]);
            elif re.search('Karlovic, Ivo',matchnames[i]):
                matchnames[i]=re.sub('Karlovic, Ivo','Karlovic, I',matchnames[i]);
            elif re.search('Bedene, Alja.',matchnames[i]):
                matchnames[i]=re.sub('Bedene, Alja.','Bedene, A',matchnames[i]);
            elif re.search('Andy Murray',matchnames[i]):
                matchnames[i]=re.sub('Andy Murray','Murray, A',matchnames[i]);
            elif re.search('Alexander Bublik',matchnames[i]):
                matchnames[i]=re.sub('Alexander Bublik','Bublik, A',matchnames[i]);
            elif re.search('Joao Sousa',matchnames[i]):
                matchnames[i]=re.sub('Joao Sousa','Sousa, J',matchnames[i]);
            elif re.search('Dustin Brown',matchnames[i]):
                matchnames[i]=re.sub('Dustin Brown','Brown, D',matchnames[i]);
            elif re.search('Jiri Vesely',matchnames[i]):
                matchnames[i]=re.sub('Jiri Vesely','Vesely, J',matchnames[i]);
            elif re.search('Illya Marchenko',matchnames[i]):
                matchnames[i]=re.sub('Illya Marchenko','Marchenko, I',matchnames[i]);
            elif re.search('Dmitry Tursunov',matchnames[i]):
                matchnames[i]=re.sub('Dmitry Tursunov','Tursunov, D',matchnames[i]);
            elif re.search('Fabio Fognini',matchnames[i]):
                matchnames[i]=re.sub('Fabio Fognini','Fognini, F',matchnames[i]);
            elif re.search('Nick Kyrgios',matchnames[i]):
                matchnames[i]=re.sub('Nick Kyrgios','Kyrgios, N',matchnames[i]);
            elif re.search('Pierre-Hugues Herbert',matchnames[i]):
                matchnames[i]=re.sub('Pierre-Hugues Herbert','Herbert, PH',matchnames[i]);
            elif re.search('Rogério Dutra Silva',matchnames[i]):
                matchnames[i]=re.sub('Rogério Dutra Silva','Dutra Silva, R',matchnames[i]);
            elif re.search('Benoit Paire',matchnames[i]):
                matchnames[i]=re.sub('Benoit Paire','Paire, B',matchnames[i]);
            elif re.search('Denis Shapovalov',matchnames[i]):
                matchnames[i]=re.sub('Denis Shapovalov','Shapovalov, D',matchnames[i]);
            elif re.search('Jerzy Janowicz',matchnames[i]):
                matchnames[i]=re.sub('Jerzy Janowicz','Janowicz, J',matchnames[i]);
            elif re.search('Malek Jaziri',matchnames[i]):
                matchnames[i]=re.sub('Malek Jaziri','Jaziri, M',matchnames[i]);
            elif re.search('Lucas Pouille',matchnames[i]):
                matchnames[i]=re.sub('Lucas Pouille','Pouille, L',matchnames[i]);
            elif re.search('Jo Wilfried Tsonga',matchnames[i]):
                matchnames[i]=re.sub('Jo Wilfried Tsonga','Tsonga, JW',matchnames[i]);
            elif re.search('Cameron Norrie',matchnames[i]):
                matchnames[i]=re.sub('Cameron Norrie','Norrie, C',matchnames[i]);
            elif re.search('Carlos Berlocq',matchnames[i]):
                matchnames[i]=re.sub('Carlos Berlocq','Berlocq, C',matchnames[i]);
            elif re.search('Nikoloz Basilashvili',matchnames[i]):
                matchnames[i]=re.sub('Nikoloz Basilashvili','Basilashvili, N',matchnames[i]);
            elif re.search('Thomas Fabbiano',matchnames[i]):
                matchnames[i]=re.sub('Thomas Fabbiano','Fabbiano, T',matchnames[i]);
            elif re.search('Sam Querrey',matchnames[i]):
                matchnames[i]=re.sub('Sam Querrey','Querrey, S',matchnames[i]);
            elif re.search('Fernando Verdasco',matchnames[i]):
                matchnames[i]=re.sub('Fernando Verdasco','Verdasco, F',matchnames[i]);
            elif re.search('Kevin Anderson',matchnames[i]):
                matchnames[i]=re.sub('Kevin Anderson','Anderson, K',matchnames[i]);
            elif re.search('Norbert Gombos',matchnames[i]):
                matchnames[i]=re.sub('Norbert Gombos','Gombos, N',matchnames[i]);
            elif re.search('Andreas Seppi',matchnames[i]):
                matchnames[i]=re.sub('Andreas Seppi','Seppi, A',matchnames[i]);
            elif re.search('Tommy Haas',matchnames[i]):
                matchnames[i]=re.sub('Tommy Haas','Haas, T',matchnames[i]);
            elif re.search('Ruben Bemelmans',matchnames[i]):
                matchnames[i]=re.sub('Ruben Bemelmans','Bemelmans, R',matchnames[i]);
            elif re.search('Daniil Medvedev',matchnames[i]):
                matchnames[i]=re.sub('Daniil Medvedev','Medvedev, D',matchnames[i]);
            elif re.search('Stanislas Wawrinka',matchnames[i]):
                matchnames[i]=re.sub('Stanislas Wawrinka','Wawrinka, S',matchnames[i]);
            elif re.search('Rafael Nadal',matchnames[i]):
                matchnames[i]=re.sub('Rafael Nadal','Nadal, R',matchnames[i]);
            elif re.search('John Millman',matchnames[i]):
                matchnames[i]=re.sub('John Millman','Millman, J',matchnames[i]);
            elif re.search('Donald Young',matchnames[i]):
                matchnames[i]=    re.sub('Donald Young','Young, D',matchnames[i]);
            elif re.search('Denis Istomin',matchnames[i]):
                matchnames[i]=    re.sub('Denis Istomin','Istomin, D',matchnames[i]);
            elif re.search('Thiago Moura Monteiro',matchnames[i]):
                matchnames[i]=    re.sub('Thiago Moura Monteiro','Monteiro, T',matchnames[i]);
            elif re.search('Andrew Whittington',matchnames[i]):
                matchnames[i]=    re.sub('Andrew Whittington','Whittington, A',matchnames[i]);
            elif re.search('Andrey Kuznetsov',matchnames[i]):
                matchnames[i]=    re.sub('Andrey Kuznetsov','Kuznetsov, A',matchnames[i]);
            elif re.search('Karen Khachanov',matchnames[i]):
                matchnames[i]=    re.sub('Karen Khachanov','Khachanov, K',matchnames[i]);
            elif re.search('Ivo Karlovic',matchnames[i]):
                matchnames[i]=    re.sub('Ivo Karlovic','Karlovic, I',matchnames[i]);
            elif re.search('Aljaz Bedene',matchnames[i]):
                matchnames[i]=    re.sub('Aljaz Bedene','Bedene, A',matchnames[i]);
            elif re.search('Damir Dzumhur',matchnames[i]):
                matchnames[i]=    re.sub('Damir Dzumhur','Dzumhur, D',matchnames[i]);
            elif re.search('Renzo Olivo',matchnames[i]):
                matchnames[i]=    re.sub('Renzo Olivo','Olivo, R',matchnames[i]);
            elif re.search('Lukas Rosol',matchnames[i]):
                matchnames[i]=    re.sub('Lukas Rosol','Rosol, L',matchnames[i]);
            elif re.search('Henri Laaksonen',matchnames[i]):
                matchnames[i]=    re.sub('Henri Laaksonen','Laaksonen, H',matchnames[i]);
            elif re.search('Marton Fucsovics',matchnames[i]):
                matchnames[i]=    re.sub('Marton Fucsovics','Fucsovics, M',matchnames[i]);
            elif re.search('Gilles Muller',matchnames[i]):
                matchnames[i]=    re.sub('Gilles Muller','Muller, G',matchnames[i]);
            elif re.search('Kei Nishikori',matchnames[i]):
                matchnames[i]=    re.sub('Kei Nishikori','Nishikori, K',matchnames[i]);
            elif re.search('Marco Cecchinato',matchnames[i]):
                matchnames[i]=    re.sub('Marco Cecchinato','Cecchinato, M',matchnames[i]);
            elif re.search('Julien Benneteau',matchnames[i]):
                matchnames[i]=    re.sub('Julien Benneteau','Benneteau, J',matchnames[i]);
            elif re.search('Sergiy Stakhovsky',matchnames[i]):
                matchnames[i]=    re.sub('Sergiy Stakhovsky','Stakhovsky, S',matchnames[i]);
            elif re.search('Peter Gojowczyk',matchnames[i]):
                matchnames[i]=    re.sub('Peter Gojowczyk','Gojowczyk, P',matchnames[i]);
            elif re.search('Marius Copil',matchnames[i]):
                matchnames[i]=    re.sub('Marius Copil','Copil, M',matchnames[i]);
            elif re.search('Andreas Haider-Maurer',matchnames[i]):
                matchnames[i]=    re.sub('Andreas Haider-Maurer','Haider-Maurer, M',matchnames[i]);
            elif re.search('Roberto Bautista-Agut',matchnames[i]):
                matchnames[i]=    re.sub('Roberto Bautista-Agut','Bautista Agut, R',matchnames[i]);
            elif re.search('Steve Johnson',matchnames[i]):
                matchnames[i]=    re.sub('Steve Johnson','Johnson, S',matchnames[i]);
            elif re.search('Nicolas Kicker',matchnames[i]):
                matchnames[i]=    re.sub('Nicolas Kicker','Kicker, N',matchnames[i]);
            elif re.search('Facundo Bagnis',matchnames[i]):
                matchnames[i]=    re.sub('Facundo Bagnis','Bagnis, F',matchnames[i]);
            elif re.search('Radu Albot',matchnames[i]):
                matchnames[i]=    re.sub('Radu Albot','Albot, R',matchnames[i]);
            elif re.search('Victor Troicki',matchnames[i]):
                matchnames[i]=    re.sub('Victor Troicki','Troicki, V',matchnames[i]);
            elif re.search('Florian Mayer',matchnames[i]):
                matchnames[i]=    re.sub('Florian Mayer','Mayer, F',matchnames[i]);
            elif re.search('Philipp Kohlschreiber',matchnames[i]):
                matchnames[i]=    re.sub('Philipp Kohlschreiber','Kohlschreiber, P',matchnames[i]);
            elif re.search('Marin Cilic',matchnames[i]):
                matchnames[i]=    re.sub('Marin Cilic','Cilic, M',matchnames[i]);
            elif re.search('Milos Raonic',matchnames[i]):
                matchnames[i]=    re.sub('Milos Raonic','Raonic, M',matchnames[i]);
            elif re.search('Jan-Lennard Struff',matchnames[i]):
                matchnames[i]=    re.sub('Jan-Lennard Struff','Struff, JL',matchnames[i]);
            elif re.search('Mikhail Youzhny',matchnames[i]):
                matchnames[i]=    re.sub('Mikhail Youzhny','Youzhny, M',matchnames[i]);
            elif re.search('Nicolas Mahut',matchnames[i]):
                matchnames[i]=    re.sub('Nicolas Mahut','Mahut, N',matchnames[i]);
            elif re.search('Andrey Rublev',matchnames[i]):
                matchnames[i]=    re.sub('Andrey Rublev','Rublev, A',matchnames[i]);
            elif re.search('Stefano Travaglia',matchnames[i]):
                matchnames[i]=    re.sub('Stefano Travaglia','Travaglia, S',matchnames[i]);
            elif re.search('Jordan Thompson',matchnames[i]):
                matchnames[i]=    re.sub('Jordan Thompson','Thompson, J',matchnames[i]);
            elif re.search('Albert Ramos-Vinolas',matchnames[i]):
                matchnames[i]=    re.sub('Albert Ramos-Vinolas','Ramos Vinolas, A',matchnames[i]);
            elif re.search('Jack Sock',matchnames[i]):
                matchnames[i]=    re.sub('Jack Sock','Sock, J',matchnames[i]);
            elif re.search('Christian Garin',matchnames[i]):
                matchnames[i]=    re.sub('Christian Garin','Garin, C',matchnames[i]);
            elif re.search('Thomaz Bellucci',matchnames[i]):
                matchnames[i]=    re.sub('Thomaz Bellucci','Bellucci, T',matchnames[i]);
            elif re.search('Sebastian Ofner',matchnames[i]):
                matchnames[i]=    re.sub('Sebastian Ofner','Ofner, S',matchnames[i]);
            elif re.search('Robin Haase',matchnames[i]):
                matchnames[i]=    re.sub('Robin Haase','Haase, R',matchnames[i]);
            elif re.search('Francis Tiafoe',matchnames[i]):
                matchnames[i]=    re.sub('Francis Tiafoe','Tiafoe, F',matchnames[i]);
            elif re.search('Evgeny Donskoy',matchnames[i]):
                matchnames[i]=    re.sub('Evgeny Donskoy','Donskoy, E',matchnames[i]);
            elif re.search('Alexander Zverev',matchnames[i]):
                matchnames[i]=    re.sub('Alexander Zverev','Zverev, A',matchnames[i]);
            elif re.search('Grigor Dimitrov',matchnames[i]):
                matchnames[i]=    re.sub('Grigor Dimitrov','Dimitrov, G',matchnames[i]);
            elif re.search('Diego Schwartzman',matchnames[i]):
                matchnames[i]=    re.sub('Diego Schwartzman','Schwartzman, DS',matchnames[i]);
            elif re.search('James Ward',matchnames[i]):
                matchnames[i]=    re.sub('James Ward','Ward, J',matchnames[i]);
            elif re.search('Marcos Baghdatis',matchnames[i]):
                matchnames[i]=    re.sub('Marcos Baghdatis','Baghdatis, M',matchnames[i]);
            elif re.search('Dudi Sela',matchnames[i]):
                matchnames[i]=    re.sub('Dudi Sela','Sela, D',matchnames[i]);
            elif re.search('Marcel Granollers',matchnames[i]):
                matchnames[i]=    re.sub('Marcel Granollers','Granollers, M',matchnames[i]);
            elif re.search('Taylor Harry Fritz',matchnames[i]):
                matchnames[i]=    re.sub('Taylor Harry Fritz','Harry, T',matchnames[i]);
            elif re.search('John Isner',matchnames[i]):
                matchnames[i]=    re.sub('John Isner','Isner, J',matchnames[i]);
            elif re.search('Mischa Zverev',matchnames[i]):
                matchnames[i]=    re.sub('Mischa Zverev','Zverev, M',matchnames[i]);
            elif re.search('Bernard Tomic',matchnames[i]):
                matchnames[i]=    re.sub('Bernard Tomic','Tomic, B',matchnames[i]);
            elif re.search('Mikhail Kukushkin',matchnames[i]):
                matchnames[i]=    re.sub('Mikhail Kukushkin','Kukushkin, M',matchnames[i]);
            elif re.search('Taro Daniel',matchnames[i]):
                matchnames[i]=    re.sub('Taro Daniel','Daniel, T',matchnames[i]);
            elif re.search('Stefanos Tsitsipas',matchnames[i]):
                matchnames[i]=    re.sub('Stefanos Tsitsipas','Tsitsipas, S',matchnames[i]);
            elif re.search('Dusan Lajovic',matchnames[i]):
                matchnames[i]=    re.sub('Dusan Lajovic','Lajovic, D',matchnames[i]);
            elif re.search('Alexandr Dolgopolov',matchnames[i]):
                matchnames[i]=    re.sub('Alexandr Dolgopolov','Dolgopolov, A',matchnames[i]);
            elif re.search('Roger Federer',matchnames[i]):
                matchnames[i]=    re.sub('Roger Federer','Federer, R',matchnames[i]);
            elif re.search('Dominic Thiem',matchnames[i]):
                matchnames[i]=    re.sub('Dominic Thiem','Thiem, D',matchnames[i]);
            elif re.search('Vasek Pospisil',matchnames[i]):
                matchnames[i]=    re.sub('Vasek Pospisil','Pospisil, V',matchnames[i]);
            elif re.search('Gilles Simon',matchnames[i]):
                matchnames[i]=    re.sub('Gilles Simon','Simon, G',matchnames[i]);
            elif re.search('Nicolas Jarry',matchnames[i]):
                matchnames[i]=    re.sub('Nicolas Jarry','Jarry, N',matchnames[i]);
            elif re.search('Janko Tipsarevic',matchnames[i]):
                matchnames[i]=    re.sub('Janko Tipsarevic','Tipsarevic, J',matchnames[i]);
            elif re.search('Jared Donaldson',matchnames[i]):
                matchnames[i]=    re.sub('Jared Donaldson','Donaldson, J',matchnames[i]);
            # WTA
            elif re.search('Giorgi, Camila',matchnames[i]):
                matchnames[i]=    re.sub('Giorgi, Camila','Giorgi, C',matchnames[i]);
            elif re.search('Cornet, Alizé',matchnames[i]):
                matchnames[i]=    re.sub('Cornet, Alizé','Cornet, A',matchnames[i]);
            elif re.search('Hibino, Nao',matchnames[i]):
                matchnames[i]=    re.sub('Hibino, Nao','Hibino, N',matchnames[i]);
            elif re.search('Keys, Madison',matchnames[i]):
                matchnames[i]=    re.sub('Keys, Madison','Keys, M',matchnames[i]);
            elif re.search('Haddad Maia, Beatriz',matchnames[i]):
                matchnames[i]=    re.sub('Haddad Maia, Beatriz','Haddad Maia, B',matchnames[i]);
            elif re.search('Robson, Laura',matchnames[i]):
                matchnames[i]=    re.sub('Robson, Laura','Robson, L',matchnames[i]);
            elif re.search('Barty, Ashleigh',matchnames[i]):
                matchnames[i]=    re.sub('Barty, Ashleigh','Barty, A',matchnames[i]);
            elif re.search('Svitolina, Elina',matchnames[i]):
                matchnames[i]=    re.sub('Svitolina, Elina','Svitolina, E',matchnames[i]);
            elif re.search('Erakovic, Marina',matchnames[i]):
                matchnames[i]=    re.sub('Erakovic, Marina','Erakovic, M',matchnames[i]);
            elif re.search('Halep, Simona',matchnames[i]):
                matchnames[i]=    re.sub('Halep, Simona','Halep, S',matchnames[i]);
            elif re.search('Pliskova, Kristyna',matchnames[i]):
                matchnames[i]=    re.sub('Pliskova, Kristyna','Pliskova, K',matchnames[i]);
            elif re.search('Vinci, Roberta',matchnames[i]):
                matchnames[i]=    re.sub('Vinci, Roberta','Vinci, R',matchnames[i]);
            elif re.search('Mertens, Elise',matchnames[i]):
                matchnames[i]=    re.sub('Mertens, Elise','Mertens, E',matchnames[i]);
            elif re.search('Williams, Venus',matchnames[i]):
                matchnames[i]=    re.sub('Williams, Venus','Williams, V',matchnames[i]);
            elif re.search('Cibulkova, Dominika',matchnames[i]):
                matchnames[i]=    re.sub('Cibulkova, Dominika','Cibulkova, D',matchnames[i]);
            elif re.search('Petkovic, Andrea',matchnames[i]):
                matchnames[i]=    re.sub('Petkovic, Andrea','Petkovic, A',matchnames[i]);
            elif re.search('Broady, Naomi',matchnames[i]):
                matchnames[i]=    re.sub('Broady, Naomi','Broady, N',matchnames[i]);
            elif re.search('Begu, Irina-Camelia',matchnames[i]):
                matchnames[i]=    re.sub('Begu, Irina-Camelia','Begu, IC',matchnames[i]);
            elif re.search('Siniakova, Katerina',matchnames[i]):
                matchnames[i]=    re.sub('Siniakova, Katerina','Siniakova, K',matchnames[i]);
            elif re.search('Sakkari, Maria',matchnames[i]):
                matchnames[i]=    re.sub('Sakkari, Maria','Sakkari, M',matchnames[i]);
            elif re.search('Garcia, Caroline',matchnames[i]):
                matchnames[i]=    re.sub('Garcia, Caroline','Garcia, C',matchnames[i]);
            elif re.search('Cepelova, Jana',matchnames[i]):
                matchnames[i]=    re.sub('Cepelova, Jana','Cepelova, J',matchnames[i]);
            elif re.search('Brengle, Madison',matchnames[i]):
                matchnames[i]=    re.sub('Brengle, Madison','Brengle, M',matchnames[i]);
            elif re.search('Hogenkamp, Richel',matchnames[i]):
                matchnames[i]=    re.sub('Hogenkamp, Richel','Hogenkamp, R',matchnames[i]);
            elif re.search('Larsson, Johanna',matchnames[i]):
                matchnames[i]=    re.sub('Larsson, Johanna','Larsson, J',matchnames[i]);
            elif re.search('Kvitova, Petra',matchnames[i]):
                matchnames[i]=    re.sub('Kvitova, Petra','Kvitova, P',matchnames[i]);
            elif re.search('Lisicki, Sabine',matchnames[i]):
                matchnames[i]=    re.sub('Lisicki, Sabine','Lisicki, S',matchnames[i]);
            elif re.search('Konjuh, Ana',matchnames[i]):
                matchnames[i]=    re.sub('Konjuh, Ana','Konjuh, A',matchnames[i]);
            elif re.search('Ostapenko, Jelena',matchnames[i]):
                matchnames[i]=    re.sub('Ostapenko, Jelena','Ostapenko, J',matchnames[i]);
            elif re.search('Sasnovich, Aliaksandra',matchnames[i]):
                matchnames[i]=    re.sub('Sasnovich, Aliaksandra','Sasnovich, A',matchnames[i]);
            elif re.search('Vekic, Donna',matchnames[i]):
                matchnames[i]=    re.sub('Vekic, Donna','Vekic, D',matchnames[i]);
            elif re.search('Vikhlyantseva, Natalia',matchnames[i]):
                matchnames[i]=    re.sub('Vikhlyantseva, Natalia','Vikhlyantseva, N',matchnames[i]);
            elif re.search('Vesnina, Elena',matchnames[i]):
                matchnames[i]=    re.sub('Vesnina, Elena','Vesnina, E',matchnames[i]);
            elif re.search('Blinkova, Anna',matchnames[i]):
                matchnames[i]=    re.sub('Blinkova, Anna','Blinkova, A',matchnames[i]);
            elif re.search('Zanevska, Maryna',matchnames[i]):
                matchnames[i]=    re.sub('Zanevska, Maryna','Zanevska, M',matchnames[i]);
            elif re.search('Watson, Heather',matchnames[i]):
                matchnames[i]=    re.sub('Watson, Heather','Watson, H',matchnames[i]);
            elif re.search('Abanda, Francoise',matchnames[i]):
                matchnames[i]=    re.sub('Abanda, Francoise','Abanda, F',matchnames[i]);
            elif re.search('Nara, Kurumi',matchnames[i]):
                matchnames[i]=    re.sub('Nara, Kurumi','Nara, K',matchnames[i]);
            elif re.search('Vondrousova, Marketa',matchnames[i]):
                matchnames[i]=    re.sub('Vondrousova, Marketa','Vondrousova, M',matchnames[i]);
            elif re.search('Brady, Jennifer',matchnames[i]):
                matchnames[i]=    re.sub('Brady, Jennifer','Brady, J',matchnames[i]);
            elif re.search('Kovinic, Danka',matchnames[i]):
                matchnames[i]=    re.sub('Kovinic, Danka','Kovinic, D',matchnames[i]);
            elif re.search('Konta, Johanna',matchnames[i]):
                matchnames[i]=    re.sub('Konta, Johanna','Konta, J',matchnames[i]);
            elif re.search('Putintseva, Yulia',matchnames[i]):
                matchnames[i]=    re.sub('Putintseva, Yulia','Putintseva, Y',matchnames[i]);
            elif re.search('Sevastova, Anastasija',matchnames[i]):
                matchnames[i]=    re.sub('Sevastova, Anastasija','Sevastova, A',matchnames[i]);
            elif re.search('Azarenka, Victoria',matchnames[i]):
                matchnames[i]=    re.sub('Azarenka, Victoria','Azarenka, V',matchnames[i]);
            elif re.search('Bellis, Catherine',matchnames[i]):
                matchnames[i]=    re.sub('Bellis, Catherine','Bellis, C',matchnames[i]);
            elif re.search('Suarez Navarro, Carla',matchnames[i]):
                matchnames[i]=    re.sub('Suarez Navarro, Carla','Suarez Navarro, C',matchnames[i]);
            elif re.search('Bouchard, Eugenie',matchnames[i]):
                matchnames[i]=    re.sub('Bouchard, Eugenie','Bouchard, E',matchnames[i]);
            elif re.search('Shelby Rogers',matchnames[i]):
                matchnames[i]=    re.sub('Shelby Rogers','Rogers, S',matchnames[i]);
            elif re.search('Julia Boserup',matchnames[i]):
                matchnames[i]=    re.sub('Julia Boserup','Boserup, J',matchnames[i]);
            elif re.search('Kai-Chen Chang',matchnames[i]):
                matchnames[i]=    re.sub('Kai-Chen Chang','Chang, K-C',matchnames[i]);
            elif re.search('Qiang Wang',matchnames[i]):
                matchnames[i]=    re.sub('Qiang Wang','Wang, Q',matchnames[i]);
            elif re.search('Camila Giorgi',matchnames[i]):
                matchnames[i]=    re.sub('Camila Giorgi','Giorgi, C',matchnames[i]);
            elif re.search('Alize Cornet',matchnames[i]):
                matchnames[i]=    re.sub('Alize Cornet','Cornet, A',matchnames[i]);
            elif re.search('Nao Hibino',matchnames[i]):
                matchnames[i]=    re.sub('Nao Hibino','Hibino, N',matchnames[i]);
            elif re.search('Madison Keys',matchnames[i]):
                matchnames[i]=    re.sub('Madison Keys','Keys, M',matchnames[i]);
            elif re.search('Beatriz Haddad Maia',matchnames[i]):
                matchnames[i]=    re.sub('Beatriz Haddad Maia','Haddad Maia, B',matchnames[i]);
            elif re.search('Laura Robson',matchnames[i]):
                matchnames[i]=    re.sub('Laura Robson','Robson, L',matchnames[i]);
            elif re.search('Aryna Sabalenka',matchnames[i]):
                matchnames[i]=    re.sub('Aryna Sabalenka','Sabalenka, A',matchnames[i]);
            elif re.search('Irina Khromacheva',matchnames[i]):
                matchnames[i]=    re.sub('Irina Khromacheva','Khromacheva, I',matchnames[i]);
            elif re.search('Elise Mertens',matchnames[i]):
                matchnames[i]=    re.sub('Elise Mertens','Mertens, E',matchnames[i]);
            elif re.search('Venus Williams',matchnames[i]):
                matchnames[i]=    re.sub('Venus Williams','Williams, V',matchnames[i]);
            elif re.search('Barbora Strycova',matchnames[i]):
                matchnames[i]=    re.sub('Barbora Strycova','Strycova, B',matchnames[i]);
            elif re.search('Strycova, Barbora',matchnames[i]):
                matchnames[i]=    re.sub('Strycova, Barbora','Strycova, B',matchnames[i]);
            elif re.search('Veronica Cepede Royg',matchnames[i]):
                matchnames[i]=    re.sub('Veronica Cepede Royg','Cepede Royg, V',matchnames[i]);
            elif re.search('Cepede Royg, Veronica',matchnames[i]):
                matchnames[i]=    re.sub('Cepede Royg, Veronica','Cepede Royg, V',matchnames[i]);
            elif re.search('Osaka, Naomi',matchnames[i]):
                matchnames[i]=    re.sub('Osaka, Naomi','Osaka, N',matchnames[i]);
            elif re.search('Sara Sorribes Tormo',matchnames[i]):
                matchnames[i]=    re.sub('Sara Sorribes Tormo','Sorribes Tormo, S',matchnames[i]);
            elif re.search('Sorribes Tormo, Sara',matchnames[i]):
                matchnames[i]=    re.sub('Sorribes Tormo, Sara','Sorribes Tormo, S',matchnames[i]);
            elif re.search('Naomi Osaka',matchnames[i]):
                matchnames[i]=    re.sub('Naomi Osaka','Osaka, N',matchnames[i]);
            elif re.search('Mirjana Lucic-Baroni',matchnames[i]):
                matchnames[i]=    re.sub('Mirjana Lucic-Baroni','Lucic-Baroni, M',matchnames[i]);
            elif re.search('Carina Witthoeft',matchnames[i]):
                matchnames[i]=    re.sub('Carina Witthoeft','Witthoeft, C',matchnames[i]);
            elif re.search('Francesca Schiavone',matchnames[i]):
                matchnames[i]=    re.sub('Francesca Schiavone','Schiavone, F',matchnames[i]);
            elif re.search('Mandy Minella',matchnames[i]):
                matchnames[i]=    re.sub('Mandy Minella','Minella, M',matchnames[i]);
            elif re.search('Ashleigh Barty',matchnames[i]):
                matchnames[i]=    re.sub('Ashleigh Barty','Barty, A',matchnames[i]);
            elif re.search('Elina Svitolina',matchnames[i]):
                matchnames[i]=    re.sub('Elina Svitolina','Svitolina, E',matchnames[i]);
            elif re.search('Kristyna Pliskova',matchnames[i]):
                matchnames[i]=    re.sub('Kristyna Pliskova','Pliskova, K',matchnames[i]);
            elif re.search('Roberta Vinci',matchnames[i]):
                matchnames[i]=    re.sub('Roberta Vinci','Vinci, R',matchnames[i]);
            elif re.search('Marina Erakovic',matchnames[i]):
                matchnames[i]=    re.sub('Marina Erakovic','Erakovic, M',matchnames[i]);
            elif re.search('Simona Halep',matchnames[i]):
                matchnames[i]=    re.sub('Simona Halep','Halep, S',matchnames[i]);
            elif re.search('Katerina Siniakova',matchnames[i]):
                matchnames[i]=    re.sub('Katerina Siniakova','Siniakova, K',matchnames[i]);
            elif re.search('Maria Sakkari',matchnames[i]):
                matchnames[i]=    re.sub('Maria Sakkari','Sakkari, M',matchnames[i]);
            elif re.search('Dominika Cibulková',matchnames[i]):
                matchnames[i]=    re.sub('Dominika Cibulková','Cibulkova, D',matchnames[i]);
            elif re.search('Andrea Petkovic',matchnames[i]):
                matchnames[i]=    re.sub('Andrea Petkovic','Petkovic, A',matchnames[i]);
            elif re.search('Caroline Garcia',matchnames[i]):
                matchnames[i]=    re.sub('Caroline Garcia','Garcia, C',matchnames[i]);
            elif re.search('Jana Cepelova',matchnames[i]):
                matchnames[i]=    re.sub('Jana Cepelova','Cepelova, J',matchnames[i]);
            elif re.search('Johanna Larsson',matchnames[i]):
                matchnames[i]=    re.sub('Johanna Larsson','Larsson, J',matchnames[i]);
            elif re.search('Petra Kvitova',matchnames[i]):
                matchnames[i]=    re.sub('Petra Kvitova','Kvitova, P',matchnames[i]);
            elif re.search('Naomi Broady',matchnames[i]):
                matchnames[i]=    re.sub('Naomi Broady','Broady, N',matchnames[i]);
            elif re.search('Irina-Camelia Begu',matchnames[i]):
                matchnames[i]=    re.sub('Irina-Camelia Begu','Begu, I',matchnames[i]);
            elif re.search('Jennifer Brady',matchnames[i]):
                matchnames[i]=    re.sub('Jennifer Brady','Brady, J',matchnames[i]);
            elif re.search('Danka Kovinic',matchnames[i]):
                matchnames[i]=    re.sub('Danka Kovinic','Kovinic, D',matchnames[i]);
            elif re.search('Ying-Ying Duan',matchnames[i]):
                matchnames[i]=    re.sub('Ying-Ying Duan','Duan, Y-Y',matchnames[i]);
            elif re.search('Ana Bogdan',matchnames[i]):
                matchnames[i]=    re.sub('Ana Bogdan','Bogdan, A',matchnames[i]);
            elif re.search('Bogdan, Ana',matchnames[i]):
                matchnames[i]=    re.sub('Bogdan, Ana','Bogdan, A',matchnames[i]);
            elif re.search('Madison Brengle',matchnames[i]):
                matchnames[i]=    re.sub('Madison Brengle','Brengle, M',matchnames[i]);
            elif re.search('Richel Hogenkamp',matchnames[i]):
                matchnames[i]=    re.sub('Richel Hogenkamp','Hogenkamp, R',matchnames[i]);
            elif re.search('Johanna Konta',matchnames[i]):
                matchnames[i]=    re.sub('Johanna Konta','Konta, J',matchnames[i]);
            elif re.search('Su-Wei Hsieh',matchnames[i]):
                matchnames[i]=    re.sub('Su-Wei Hsieh','Hsieh, Su-Wei',matchnames[i]);
            elif re.search('Victoria Azarenka',matchnames[i]):
                matchnames[i]=    re.sub('Victoria Azarenka','Azarenka, V',matchnames[i]);
            elif re.search('Catherine Cartan Bellis',matchnames[i]):
                matchnames[i]=    re.sub('Catherine Cartan Bellis','Bellis, C',matchnames[i]);
            elif re.search('Carla Suarez-Navarro',matchnames[i]):
                matchnames[i]=    re.sub('Carla Suarez-Navarro','Suarez Navarro, C',matchnames[i]);
            elif re.search('Eugenie Bouchard',matchnames[i]):
                matchnames[i]=    re.sub('Eugenie Bouchard','Bouchard, E',matchnames[i]);
            elif re.search('Sabine Lisicki',matchnames[i]):
                matchnames[i]=    re.sub('Sabine Lisicki','Lisicki, S',matchnames[i]);
            elif re.search('Peng, Shuai',matchnames[i]):
                matchnames[i]=    re.sub('Peng, Shuai','Peng, S',matchnames[i]);
            elif re.search('Lucic-Baroni, Mirjana',matchnames[i]):
                matchnames[i]=    re.sub('Lucic-Baroni, Mirjana','Lucic-Baroni, M',matchnames[i]);
            elif re.search('Ana Konjuh',matchnames[i]):
                matchnames[i]=    re.sub('Ana Konjuh','Konjuh, A',matchnames[i]);
            elif re.search('Yulia Putintseva',matchnames[i]):
                matchnames[i]=    re.sub('Yulia Putintseva','Putintseva, Y',matchnames[i]);
            elif re.search('Anastasija Sevastova',matchnames[i]):
                matchnames[i]=    re.sub('Anastasija Sevastova','Sevastova, A',matchnames[i]);
            elif re.search('Elena Vesnina',matchnames[i]):
                matchnames[i]=    re.sub('Elena Vesnina','Vesnina, E',matchnames[i]);
            elif re.search('Anna Blinkova',matchnames[i]):
                matchnames[i]=    re.sub('Anna Blinkova','Blinkova, A',matchnames[i]);
            elif re.search('Jelena Ostapenko',matchnames[i]):
                matchnames[i]=    re.sub('Jelena Ostapenko','Ostapenko, J',matchnames[i]);
            elif re.search('Aliaksandra Sasnovich',matchnames[i]):
                matchnames[i]=    re.sub('Aliaksandra Sasnovich','Sasnovich, A',matchnames[i]);
            elif re.search('Donna Vekic',matchnames[i]):
                matchnames[i]=    re.sub('Donna Vekic','Vekic, D',matchnames[i]);
            elif re.search('Natalia Vikhlyantseva',matchnames[i]):
                matchnames[i]=    re.sub('Natalia Vikhlyantseva','Vikhlyantseva, N',matchnames[i]);
            elif re.search('Maryna Zanevska',matchnames[i]):
                matchnames[i]=    re.sub('Maryna Zanevska','Zanevska, M',matchnames[i]);
            elif re.search('Heather Watson',matchnames[i]):
                matchnames[i]=    re.sub('Heather Watson','Watson, H',matchnames[i]);
            elif re.search('Marketa Vondrousova',matchnames[i]):
                matchnames[i]=    re.sub('Marketa Vondrousova','Vondrousova, M',matchnames[i]);
            elif re.search('Shuai Peng',matchnames[i]):
                matchnames[i]=    re.sub('Shuai Peng','Peng, S',matchnames[i]);
            elif re.search('Francoise Abanda',matchnames[i]):
                matchnames[i]=    re.sub('Francoise Abanda','Abanda, F',matchnames[i]);
            elif re.search('Kurumi Nara',matchnames[i]):
                matchnames[i]=    re.sub('Kurumi Nara','Nara, K',matchnames[i]);
            elif re.search('Angelique Kerber',matchnames[i]):
                matchnames[i]=    re.sub('Angelique Kerber','Kerber, A',matchnames[i]);
            elif re.search('Irina Falconi',matchnames[i]):
                matchnames[i]=    re.sub('Irina Falconi','Falconi, I',matchnames[i]);
            elif re.search('Kirsten Flipkens',matchnames[i]):
                matchnames[i]=    re.sub('Kirsten Flipkens','Flipkens, K',matchnames[i]);
            elif re.search('Misaki Doi',matchnames[i]):
                matchnames[i]=    re.sub('Misaki Doi','Doi, M',matchnames[i]);
            elif re.search('Oceane Dodin',matchnames[i]):
                matchnames[i]=    re.sub('Oceane Dodin','Dodin, O',matchnames[i]);
            elif re.search('Lucie Safarova',matchnames[i]):
                matchnames[i]=    re.sub('Lucie Safarova','Safarova, L',matchnames[i]);
            elif re.search('Kiki Bertens',matchnames[i]):
                matchnames[i]=    re.sub('Kiki Bertens','Bertens, K',matchnames[i]);
            elif re.search('Sorana Cirstea',matchnames[i]):
                matchnames[i]=    re.sub('Sorana Cirstea','Cirstea, S',matchnames[i]);
            elif re.search('Magda Linette',matchnames[i]):
                matchnames[i]=    re.sub('Magda Linette','Linette, M',matchnames[i]);
            elif re.search('Bethanie Mattek-Sands',matchnames[i]):
                matchnames[i]=    re.sub('Bethanie Mattek-Sands','Mattek-Sands, B',matchnames[i]);
            elif re.search('Yanina Wickmayer',matchnames[i]):
                matchnames[i]=    re.sub('Yanina Wickmayer','Wickmayer, Y',matchnames[i]);
            elif re.search('Kateryna Bondarenko',matchnames[i]):
                matchnames[i]=    re.sub('Kateryna Bondarenko','Bondarenko, K',matchnames[i]);
            elif re.search('Ekaterina Alexandrova',matchnames[i]):
                matchnames[i]=    re.sub('Ekaterina Alexandrova','Alexandrova, E',matchnames[i]);
            elif re.search('Garbine Muguruza',matchnames[i]):
                matchnames[i]=    re.sub('Garbine Muguruza','Muguruza, G',matchnames[i]);
            elif re.search('Agnieszka Radwanska',matchnames[i]):
                matchnames[i]=    re.sub('Agnieszka Radwanska','Radwanska, A',matchnames[i]);
            elif re.search('Jelena Jankovic',matchnames[i]):
                matchnames[i]=    re.sub('Jelena Jankovic','Jankovic, J',matchnames[i]);
            elif re.search('Katie Boulter',matchnames[i]):
                matchnames[i]=    re.sub('Katie Boulter','Boulter, K',matchnames[i]);
            elif re.search('Christina McHale',matchnames[i]):
                matchnames[i]=    re.sub('Christina McHale','McHale, C',matchnames[i]);
            elif re.search('Kristina Kucova',matchnames[i]):
                matchnames[i]=    re.sub('Kristina Kucova','Kucova, K',matchnames[i]);
            elif re.search('Bianca Andreescu',matchnames[i]):
                matchnames[i]=    re.sub('Bianca Andreescu','Andreescu, B',matchnames[i]);
            elif re.search('Monica Puig',matchnames[i]):
                matchnames[i]=    re.sub('Monica Puig','Puig, M',matchnames[i]);
            elif re.search('Timea Bacsinszky',matchnames[i]):
                matchnames[i]=    re.sub('Timea Bacsinszky','Bacsinszky, T',matchnames[i]);
            elif re.search('Lauren Davis',matchnames[i]):
                matchnames[i]=    re.sub('Lauren Davis','Davis, L',matchnames[i]);
            elif re.search('Varvara Lepchenko',matchnames[i]):
                matchnames[i]=    re.sub('Varvara Lepchenko','Lepchenko, V',matchnames[i]);
            elif re.search('Polona Hercog',matchnames[i]):
                matchnames[i]=    re.sub('Polona Hercog','Hercog, P',matchnames[i]);
            elif re.search('Annika Beck',matchnames[i]):
                matchnames[i]=    re.sub('Annika Beck','Beck, A',matchnames[i]);
            elif re.search('Beck, Annika',matchnames[i]):
                matchnames[i]=    re.sub('Beck, Annika','Beck, A',matchnames[i]);
            elif re.search('Ekaterina Makarova',matchnames[i]):
                matchnames[i]=    re.sub('Ekaterina Makarova','Makarova, E',matchnames[i]);
            elif re.search('Alison Van Uytvanck',matchnames[i]):
                matchnames[i]=    re.sub('Alison Van Uytvanck','Van Uytvanck, A',matchnames[i]);
            elif re.search('Ons Jabeur',matchnames[i]):
                matchnames[i]=    re.sub('Ons Jabeur','Jabeur, O',matchnames[i]);
            elif re.search('Svetlana Kuznetsova',matchnames[i]):
                matchnames[i]=    re.sub('Svetlana Kuznetsova','Kuznetsova, S',matchnames[i]);
            elif re.search('Karolina Pliskova',matchnames[i]):
                matchnames[i]=    re.sub('Karolina Pliskova','Pliskova, K',matchnames[i]);
            elif re.search('Pliskova, Karolina',matchnames[i]):
                matchnames[i]=    re.sub('Pliskova, Karolina','Pliskova, K',matchnames[i]);
            elif re.search('Evgeniya Rodina',matchnames[i]):
                matchnames[i]=    re.sub('Evgeniya Rodina','Rodina, E',matchnames[i]);
            elif re.search('Monica Niculescu',matchnames[i]):
                matchnames[i]=    re.sub('Monica Niculescu','Niculescu, M',matchnames[i]);
            elif re.search('Magdalena Rybarikova',matchnames[i]):
                matchnames[i]=    re.sub('Magdalena Rybarikova','Rybarikova, M',matchnames[i]);
            elif re.search('Schiavone, Francesca',matchnames[i]):
                matchnames[i]=    re.sub('Schiavone, Francesca','Schiavone, F',matchnames[i]);
            elif re.search('Minella, Mandy',matchnames[i]):
                matchnames[i]=    re.sub('Minella, Mandy','Minella, M',matchnames[i]);
            elif re.search('Alexandrova, Ekaterina',matchnames[i]):
                matchnames[i]=    re.sub('Alexandrova, Ekaterina','Alexandrova, E',matchnames[i]);
            elif re.search('Muguruza, Garbiñe',matchnames[i]):
                matchnames[i]=    re.sub('Muguruza, Garbiñe','Muguruza, G',matchnames[i]);
            elif re.search('Alison Riske',matchnames[i]):
                matchnames[i]=    re.sub('Alison Riske','Riske, A',matchnames[i]);
            elif re.search('Sloane Stephens',matchnames[i]):
                matchnames[i]=    re.sub('Sloane Stephens','Stephens, S',matchnames[i]);
            elif re.search('Allertova, Denisa',matchnames[i]):
                matchnames[i]=    re.sub('Allertova, Denisa','Allertova, D',matchnames[i]);
            elif re.search('Ozaki, Risa',matchnames[i]):
                matchnames[i]=    re.sub('Ozaki, Risa','Ozaki, R',matchnames[i]);
            elif re.search('Arina Rodionova',matchnames[i]):
                matchnames[i]=    re.sub('Arina Rodionova','Rodionova, A',matchnames[i]);
            elif re.search('Anastasia Pavlyuchenkova',matchnames[i]):
                matchnames[i]=    re.sub('Anastasia Pavlyuchenkova','Pavlyuchenkova, A',matchnames[i]);
            elif re.search('Arruabarrena, Lara',matchnames[i]):
                matchnames[i]=    re.sub('Arruabarrena, Lara','Arruabarrena-Vecino, L',matchnames[i]);
            elif re.search('Kontaveit, Anett',matchnames[i]):
                matchnames[i]=    re.sub('Kontaveit, Anett','Kontaveit, A',matchnames[i]);
            elif re.search('Babos, Timea',matchnames[i]):
                matchnames[i]=    re.sub('Babos, Timea','Babos, T',matchnames[i]);
            elif re.search('Wozniacki, Caroline',matchnames[i]):
                matchnames[i]=    re.sub('Wozniacki, Caroline','Wozniacki, C',matchnames[i]);
            elif re.search('Barthel, Mona',matchnames[i]):
                matchnames[i]=    re.sub('Barthel, Mona','Barthel, M',matchnames[i]);
            elif re.search('Vandeweghe, Coco',matchnames[i]):
                matchnames[i]=    re.sub('Vandeweghe, Coco','Vandeweghe, C',matchnames[i]);
            elif re.search('Bertens, Kiki',matchnames[i]):
                matchnames[i]=    re.sub('Bertens, Kiki','Bertens, K',matchnames[i]);
            elif re.search('Cirstea, Sorana',matchnames[i]):
                matchnames[i]=    re.sub('Cirstea, Sorana','Cirstea, S',matchnames[i]);
            elif re.search('Boulter, Katie',matchnames[i]):
                matchnames[i]=    re.sub('Boulter, Katie','Boulter, K',matchnames[i]);
            elif re.search('McHale, Christina',matchnames[i]):
                matchnames[i]=    re.sub('McHale, Christina','McHale, C',matchnames[i]);
            elif re.search('Daria Gavrilova',matchnames[i]):
                matchnames[i]=    re.sub('Daria Gavrilova','Gavrilova, D',matchnames[i]);
            elif re.search('Petra Martic',matchnames[i]):
                matchnames[i]=    re.sub('Petra Martic','Martic, P',matchnames[i]);
            elif re.search('Mona Barthel',matchnames[i]):
                matchnames[i]=    re.sub('Mona Barthel','Barthel, M',matchnames[i]);
            elif re.search('Coco Vandeweghe',matchnames[i]):
                matchnames[i]=    re.sub('Coco Vandeweghe','Vandeweghe, C',matchnames[i]);
            elif re.search('Rodina, Evgeniya',matchnames[i]):
                matchnames[i]=    re.sub('Rodina, Evgeniya','Rodina, E',matchnames[i]);
            elif re.search('Timea Babos',matchnames[i]):
                matchnames[i]=    re.sub('Timea Babos','Babos, T',matchnames[i]);
            elif re.search('Caroline Wozniacki',matchnames[i]):
                matchnames[i]=    re.sub('Caroline Wozniacki','Wozniacki, C',matchnames[i]);
            elif re.search('Lesya Tsurenko',matchnames[i]):
                matchnames[i]=    re.sub('Lesya Tsurenko','Tsurenko, L',matchnames[i]);
            elif re.search('Julia Goerges',matchnames[i]):
                matchnames[i]=    re.sub('Julia Goerges','Goerges, J',matchnames[i]);
            elif re.search('Rodionova, Arina',matchnames[i]):
                matchnames[i]=    re.sub('Rodionova, Arina','Rodionova, A',matchnames[i]);
            elif re.search('Pavlyuchenkova, Anastasia',matchnames[i]):
                matchnames[i]=    re.sub('Pavlyuchenkova, Anastasia','Pavlyuchenkova, A',matchnames[i]);
            elif re.search('Tsurenko, Lesia',matchnames[i]):
                matchnames[i]=    re.sub('Tsurenko, Lesia','Tsurenko, L',matchnames[i]);
            elif re.search('Goerges, Julia',matchnames[i]):
                matchnames[i]=    re.sub('Goerges, Julia','Goerges, J',matchnames[i]);
            elif re.search('Wickmayer, Yanina',matchnames[i]):
                matchnames[i]=    re.sub('Wickmayer, Yanina','Wickmayer, Y',matchnames[i]);
            elif re.search('Bondarenko, Kateryna',matchnames[i]):
                matchnames[i]=    re.sub('Bondarenko, Kateryna','Bondarenko, K',matchnames[i]);
            elif re.search('Kristina Mladenovic',matchnames[i]):
                matchnames[i]=    re.sub('Kristina Mladenovic','Mladenovic, K',matchnames[i]);
            elif re.search('Pauline Parmentier',matchnames[i]):
                matchnames[i]=    re.sub('Pauline Parmentier','Parmentier, P',matchnames[i]);
            elif re.search('Lara Arruabarrena',matchnames[i]):
                matchnames[i]=    re.sub('Lara Arruabarrena','Arruabarrena-Vecino, L',matchnames[i]);
            elif re.search('Anett Kontaveit',matchnames[i]):
                matchnames[i]=    re.sub('Anett Kontaveit','Kontaveit, A',matchnames[i]);
            elif re.search('Tatjana Maria',matchnames[i]):
                matchnames[i]=    re.sub('Tatjana Maria','Maria, T',matchnames[i]);
            elif re.search('Anastasia Potapova',matchnames[i]):
                matchnames[i]=    re.sub('Anastasia Potapova','Potapova, A',matchnames[i]);
            elif re.search('Tsvetana Pironkova',matchnames[i]):
                matchnames[i]=    re.sub('Tsvetana Pironkova','Pironkova, T',matchnames[i]);
            elif re.search('Sara Errani',matchnames[i]):
                matchnames[i]=    re.sub('Sara Errani','Errani, S',matchnames[i]);
            elif re.search('Viktorija Golubic',matchnames[i]):
                matchnames[i]=    re.sub('Viktorija Golubic','Golubic, V',matchnames[i]);
            elif re.search('Shuai Zhang',matchnames[i]):
                matchnames[i]=    re.sub('Shuai Zhang','Zhang, S',matchnames[i]);
            elif re.search('Zarina Diyas',matchnames[i]):
                matchnames[i]=    re.sub('Zarina Diyas','Diyas, Z',matchnames[i]);
            elif re.search('Adam Pavlasek',matchnames[i]):
                matchnames[i]=    re.sub('Adam Pavlasek','Pavlasek, A',matchnames[i]);
            elif re.search('Ernesto Escobedo',matchnames[i]):
                matchnames[i]=    re.sub('Ernesto Escobedo','Escobedo, E',matchnames[i]);
            elif re.search('Adrian Mannarino',matchnames[i]):
                matchnames[i]=    re.sub('Adrian Mannarino','Mannarino, A',matchnames[i]);
            elif re.search('Feliciano Lopez',matchnames[i]):
                matchnames[i]=    re.sub('Feliciano Lopez','Lopez, F',matchnames[i]);
            elif re.search('Ernest Gulbis',matchnames[i]):
                matchnames[i]=    re.sub('Ernest Gulbis','Gulbis, E',matchnames[i]);
            elif re.search('Victor Estrella Burgos',matchnames[i]):
                matchnames[i]=    re.sub('Victor Estrella Burgos','Estrella, V',matchnames[i]);
            elif re.search('Gael Monfils',matchnames[i]):
                matchnames[i]=    re.sub('Gael Monfils','Monfils, G',matchnames[i]);
            elif re.search('Daniel Brands',matchnames[i]):
                matchnames[i]=    re.sub('Daniel Brands','Brands, D',matchnames[i]);
            elif re.search('Horacio Zeballos',matchnames[i]):
                matchnames[i]=    re.sub('Horacio Zeballos','Zeballos, H',matchnames[i]);
            elif re.search('Paolo Lorenzi',matchnames[i]):
                matchnames[i]=    re.sub('Paolo Lorenzi','Lorenzi, P',matchnames[i]);
            elif re.search('Jeremy Chardy',matchnames[i]):
                matchnames[i]=    re.sub('Jeremy Chardy','Chardy, J',matchnames[i]);
            elif re.search('Tomas Berdych',matchnames[i]):
                matchnames[i]=    re.sub('Tomas Berdych','Berdych, T',matchnames[i]);
            elif re.search('Juan Martin Del Potro',matchnames[i]):
                matchnames[i]=    re.sub('Juan Martin Del Potro','Del Potro, JM',matchnames[i]);
            elif re.search('Thanasi Kokkinakis',matchnames[i]):
                matchnames[i]=    re.sub('Thanasi Kokkinakis','Kokkinakis, T',matchnames[i]);
            elif re.search('Kyle Edmund',matchnames[i]):
                matchnames[i]=    re.sub('Kyle Edmund','Edmund, K',matchnames[i]);
            elif re.search('Alexander Ward',matchnames[i]):
                matchnames[i]=    re.sub('Alexander Ward','Ward, A',matchnames[i]);
            elif re.search('Martin Klizan',matchnames[i]):
                matchnames[i]=    re.sub('Martin Klizan','Klizan, M',matchnames[i]);
            elif re.search('Novak Djokovic',matchnames[i]):
                matchnames[i]=    re.sub('Novak Djokovic','Djokovic, N',matchnames[i]);
            elif re.search('Richard Gasquet',matchnames[i]):
                matchnames[i]=    re.sub('Richard Gasquet','Gasquet, R',matchnames[i]);
            elif re.search('David Ferrer',matchnames[i]):
                matchnames[i]=    re.sub('David Ferrer','Ferrer, D',matchnames[i]);
            elif re.search('Steve Darcis',matchnames[i]):
                matchnames[i]=    re.sub('Steve Darcis','Darcis, S',matchnames[i]);
            elif re.search('Ricardas Berankis',matchnames[i]):
                matchnames[i]=    re.sub('Ricardas Berankis','Berankis, R',matchnames[i]);
            elif re.search('Simone Bolelli',matchnames[i]):
                matchnames[i]=    re.sub('Simone Bolelli','Bolelli, S',matchnames[i]);
            elif re.search('Borna ?ori?',matchnames[i]):
                matchnames[i]=    re.sub('Borna ?ori?','Coric, B',matchnames[i]);
            elif re.search('Ryan Harrison',matchnames[i]):
                matchnames[i]=    re.sub('Ryan Harrison','Harrison, R',matchnames[i]);
            elif re.search('Yuichi Sugita',matchnames[i]):
                matchnames[i]=    re.sub('Yuichi Sugita','Sugita, Y',matchnames[i]);
            elif re.search('Brydan Klein',matchnames[i]):
                matchnames[i]=    re.sub('Brydan Klein','Klein, B',matchnames[i]);
            elif re.search('Rogers, Shelby',matchnames[i]):
                matchnames[i]=    re.sub('Rogers, Shelby','Rogers, S',matchnames[i]);
            elif re.search('Boserup, Julia',matchnames[i]):
                matchnames[i]=    re.sub('Boserup, Julia','Boserup, J',matchnames[i]);
            elif re.search('Riske, Alison',matchnames[i]):
                matchnames[i]=    re.sub('Riske, Alison','Riske, A',matchnames[i]);
            elif re.search('Stephens, Sloane',matchnames[i]):
                matchnames[i]=    re.sub('Stephens, Sloane','Stephens, S',matchnames[i]);
            elif re.search('Radwanska, Agnieszka',matchnames[i]):
                matchnames[i]=    re.sub('Radwanska, Agnieszka','Radwanska, A',matchnames[i]);
            elif re.search('Jankovic, Jelena',matchnames[i]):
                matchnames[i]=    re.sub('Jankovic, Jelena','Jankovic, J',matchnames[i]);
            elif re.search('Puig, Monica',matchnames[i]):
                matchnames[i]=    re.sub('Puig, Monica','Puig, M',matchnames[i]);
            elif re.search('Bacsinszky, Timea',matchnames[i]):
                matchnames[i]=    re.sub('Bacsinszky, Timea','Bacsinszky, T',matchnames[i]);
            elif re.search('Pironkova, Tsvetana',matchnames[i]):
                matchnames[i]=    re.sub('Pironkova, Tsvetana','Pironkova, T',matchnames[i]);
            elif re.search('Errani, Sara',matchnames[i]):
                matchnames[i]=    re.sub('Errani, Sara','Errani, S',matchnames[i]);
            elif re.search('Niculescu, Monica',matchnames[i]):
                matchnames[i]=    re.sub('Niculescu, Monica','Niculescu, M',matchnames[i]);
            elif re.search('Rybarikova, Magdalena',matchnames[i]):
                matchnames[i]=    re.sub('Rybarikova, Magdalena','Rybarikova, M',matchnames[i]);
            elif re.search('Maria, Tatjana',matchnames[i]):
                matchnames[i]=    re.sub('Maria, Tatjana','Maria, T',matchnames[i]);
            elif re.search('Potapova, Anastasia',matchnames[i]):
                matchnames[i]=    re.sub('Potapova, Anastasia','Potapova, A',matchnames[i]);
            elif re.search('Makarova, Ekaterina',matchnames[i]):
                matchnames[i]=    re.sub('Makarova, Ekaterina','Makarova, E',matchnames[i]);
            elif re.search('Van Uytvanck, Alison',matchnames[i]):
                matchnames[i]=    re.sub('Van Uytvanck, Alison','Van Uytvanck, A',matchnames[i]);
            elif re.search('Linette, Magda',matchnames[i]):
                matchnames[i]=    re.sub('Linette, Magda','Linette, M',matchnames[i]);
            elif re.search('Mattek-Sands, Bethanie',matchnames[i]):
                matchnames[i]=    re.sub('Mattek-Sands, Bethanie','Mattek-Sands, B',matchnames[i]);
            elif re.search('Kucova, Kristina',matchnames[i]):
                matchnames[i]=    re.sub('Kucova, Kristina','Kucova, K',matchnames[i]);
            elif re.search('Andreescu, Bianca Vanessa',matchnames[i]):
                matchnames[i]=    re.sub('Andreescu, Bianca Vanessa','Andreescu, B',matchnames[i]);
            elif re.search('Kerber, Angelique',matchnames[i]):
                matchnames[i]=    re.sub('Kerber, Angelique','Kerber, A',matchnames[i]);
            elif re.search('Falconi, Irina',matchnames[i]):
                matchnames[i]=    re.sub('Falconi, Irina','Falconi, I',matchnames[i]);
            elif re.search('Kasatkina, Daria',matchnames[i]):
                matchnames[i]=    re.sub('Kasatkina, Daria','Kasatkina, D',matchnames[i]);
            elif re.search('Saisai Zheng',matchnames[i]):
                matchnames[i]=    re.sub('Saisai Zheng','Zheng, S',matchnames[i]);
            elif re.search('Jabeur, Ons',matchnames[i]):
                matchnames[i]=    re.sub('Jabeur, Ons','Jabeur, O',matchnames[i]);
            elif re.search('Kuznetsova, Svetlana',matchnames[i]):
                matchnames[i]=    re.sub('Kuznetsova, Svetlana','Kuznetsova, S',matchnames[i]);
            elif re.search('Hercog, Polona',matchnames[i]):
                matchnames[i]=    re.sub('Hercog, Polona','Hercog, P',matchnames[i]);
            elif re.search('Golubic, Viktorija',matchnames[i]):
                matchnames[i]=    re.sub('Golubic, Viktorija','Golubic, V',matchnames[i]);
            elif re.search('Gavrilova, Daria',matchnames[i]):
                matchnames[i]=    re.sub('Gavrilova, Daria','Gavrilova, D',matchnames[i]);
            elif re.search('Martic, Petra',matchnames[i]):
                matchnames[i]=    re.sub('Martic, Petra','Martic, P',matchnames[i]);
            elif re.search('Flipkens, Kirsten',matchnames[i]):
                matchnames[i]=    re.sub('Flipkens, Kirsten','Flipkens, K',matchnames[i]);
            elif re.search('Doi, Misaki',matchnames[i]):
                matchnames[i]=    re.sub('Doi, Misaki','Doi, M',matchnames[i]);
            elif re.search('Dodin, Oceane',matchnames[i]):
                matchnames[i]=    re.sub('Dodin, Oceane','Dodin, O',matchnames[i]);
            elif re.search('Safarova, Lucie',matchnames[i]):
                matchnames[i]=    re.sub('Safarova, Lucie','Safarova, L',matchnames[i]);
            elif re.search('Denisa Allertova',matchnames[i]):
                matchnames[i]=    re.sub('Denisa Allertova','Allertova, D',matchnames[i]);
            elif re.search('Risa Ozaki',matchnames[i]):
                matchnames[i]=    re.sub('Risa Ozaki','Ozaki, R',matchnames[i]);
            elif re.search('Davis, Lauren',matchnames[i]):
                matchnames[i]=    re.sub('Davis, Lauren','Davis, L',matchnames[i]);
            elif re.search('Lepchenko, Varvara',matchnames[i]):
                matchnames[i]=    re.sub('Lepchenko, Varvara','Lepchenko, V',matchnames[i]);
            elif re.search('Darya Kasatkina',matchnames[i]):
                matchnames[i]=    re.sub('Darya Kasatkina','Kasatkina, D',matchnames[i]);
            elif re.search('Saisai Zheng',matchnames[i]):
                matchnames[i]=    re.sub('Saisai Zheng','Zheng, S',matchnames[i]);
            elif re.search('Alexios Halebian',matchnames[i]):
                matchnames[i]=    re.sub('Alexios Halebian','Halebian, A',matchnames[i]);
            elif re.search('Lukas Lacko',matchnames[i]):
                matchnames[i]=    re.sub('Lukas Lacko','Lacko, L',matchnames[i]);
            elif re.search('Go Soeda',matchnames[i]):
                matchnames[i]=    re.sub('Go Soeda','Soeda, G',matchnames[i]);
            elif re.search('Tennys Sandgren',matchnames[i]):
                matchnames[i]=    re.sub('Tennys Sandgren','Sandgren, T',matchnames[i]);
            elif re.search('Halebian, Alexios',matchnames[i]):
                matchnames[i]=    re.sub('Halebian, Alexios','Halebian, A',matchnames[i]);
            elif re.search('Lacko, Lukas',matchnames[i]):
                matchnames[i]=    re.sub('Lacko, Lukas','Lacko, L',matchnames[i]);
            elif re.search('Alessandro Bega',matchnames[i]):
                matchnames[i]=    re.sub('Alessandro Bega','Bega, A',matchnames[i]);
            elif re.search('Bega, Alessandro',matchnames[i]):
                matchnames[i]=    re.sub('Bega, Alessandro','Bega, A',matchnames[i]);
            elif re.search('Kozlov, Stefan',matchnames[i]):
                matchnames[i]=    re.sub('Kozlov, Stefan','Kozlov, S',matchnames[i]);
            elif re.search('Bhambri, Yuki',matchnames[i]):
                matchnames[i]=    re.sub('Bhambri, Yuki','Bhambri, Y',matchnames[i]);
            elif re.search('Leshem, Edan',matchnames[i]):
                matchnames[i]=    re.sub('Leshem, Edan','Leshem, E',matchnames[i]);
            elif re.search('Opelka, Reilly',matchnames[i]):
                matchnames[i]=    re.sub('Opelka, Reilly','Opelka, R',matchnames[i]);
            elif re.search('Reilly Opelka',matchnames[i]):
                matchnames[i]=    re.sub('Reilly Opelka','Opelka, R',matchnames[i]);
            elif re.search('Paul, Tommy',matchnames[i]):
                matchnames[i]=    re.sub('Paul, Tommy','Paul, T',matchnames[i]);
            elif re.search('Ruud, Casper',matchnames[i]):
                matchnames[i]=    re.sub('Ruud, Casper','Ruud, C',matchnames[i]);
            elif re.search('Ramanathan, Ramkumar',matchnames[i]):
                matchnames[i]=    re.sub('Ramanathan, Ramkumar','Ramanathan, R',matchnames[i]);
            elif re.search('Pella, Guido',matchnames[i]):
                matchnames[i]=    re.sub('Pella, Guido','Pella, G',matchnames[i]);
            elif re.search('Ramkumar Ramanathan',matchnames[i]):
                matchnames[i]=    re.sub('Ramkumar Ramanathan','Ramanathan, R',matchnames[i]);
            elif re.search('Guido Pella',matchnames[i]):
                matchnames[i]=    re.sub('Guido Pella','Pella, G',matchnames[i]);
            elif re.search('Sekou Bangoura',matchnames[i]):
                matchnames[i]=    re.sub('Sekou Bangoura','Bangoura, S',matchnames[i]);
            elif re.search('Smyczek, Tim',matchnames[i]):
                matchnames[i]=    re.sub('Smyczek, Tim','Smyczek, T',matchnames[i]);
            elif re.search('Soeda, Go',matchnames[i]):
                matchnames[i]=    re.sub('Soeda, Go','Soeda, G',matchnames[i]);
            elif re.search('Sandgren, Tennys',matchnames[i]):
                matchnames[i]=    re.sub('Sandgren, Tennys','Sandgren, T',matchnames[i]);
            elif re.search('Stefan Kozlov',matchnames[i]):
                matchnames[i]=    re.sub('Stefan Kozlov','Kozlov, S',matchnames[i]);
            elif re.search('Yuki Bhambri',matchnames[i]):
                matchnames[i]=    re.sub('Yuki Bhambri','Bhambri, Y',matchnames[i]);
            elif re.search('Tim Smyczek',matchnames[i]):
                matchnames[i]=    re.sub('Tim Smyczek','Smyczek, T',matchnames[i]);
            elif re.search('Tommy Paul',matchnames[i]):
                matchnames[i]=    re.sub('Tommy Paul','Paul, T',matchnames[i]);
            elif re.search('Casper Ruud',matchnames[i]):
                matchnames[i]=    re.sub('Casper Ruud','Ruud, C',matchnames[i]);
            elif re.search('Krueger, Mitchell',matchnames[i]):
                matchnames[i]=    re.sub('Krueger, Mitchell','Krueger, M',matchnames[i]);
            elif re.search('Mitchell Krueger',matchnames[i]):
                matchnames[i]=    re.sub('Mitchell Krueger','Krueger, M',matchnames[i]);
            elif re.search('Edan Leshem',matchnames[i]):
                matchnames[i]=    re.sub('Edan Leshem','Leshem, E',matchnames[i]);
            elif re.search('Chirico, Louisa',matchnames[i]):
                matchnames[i]=    re.sub('Chirico, Louisa','Chirico, L',matchnames[i]);
            elif re.search('Jamie Loeb',matchnames[i]):
                matchnames[i]=    re.sub('Jamie Loeb','Loeb, J',matchnames[i]);
            elif re.search('Grammatikopoulou, Valentini',matchnames[i]):
                matchnames[i]=    re.sub('Grammatikopoulou, Valentini','Grammatikopoulou, V',matchnames[i]);
            elif re.search('Valentini Grammatikopoulou',matchnames[i]):
                matchnames[i]=    re.sub('Valentini Grammatikopoulou','Grammatikopoulou, V',matchnames[i]);
            elif re.search('Loeb, Jamie',matchnames[i]):
                matchnames[i]=    re.sub('Loeb, Jamie','Loeb, J',matchnames[i]);
            elif re.search('Louisa Chirico',matchnames[i]):
                matchnames[i]=    re.sub('Louisa Chirico','Chirico, L',matchnames[i]);
            elif re.search('Mladenovic, Kristina',matchnames[i]):
                matchnames[i]=    re.sub('Mladenovic, Kristina','Mladenovic, K',matchnames[i]);
            elif re.search('Patricia Maria Tig',matchnames[i]):
                matchnames[i]=    re.sub('Patricia Maria Tig','Tig, PM',matchnames[i]);
            elif re.search('Tig, Patricia Maria',matchnames[i]):
                matchnames[i]=    re.sub('Tig, Patricia Maria','Tig, PM',matchnames[i]);
            elif re.search('Marc Polmans',matchnames[i]):
                matchnames[i]=    re.sub('Marc Polmans','Polmans, M',matchnames[i]);
            elif re.search('Hyeon Chung',matchnames[i]):
                matchnames[i]=    re.sub('Hyeon Chung','Chung, H',matchnames[i]);
            elif re.search('Chung, Hyeon',matchnames[i]):
                matchnames[i]=    re.sub('Chung, Hyeon','Chung, H',matchnames[i]);
            elif re.search('Nishikori, Kei',matchnames[i]):
                matchnames[i]=    re.sub('Nishikori, Kei','Nishikori, K',matchnames[i]);
            elif re.search('Polmans, Marc',matchnames[i]):
                matchnames[i]=    re.sub('Polmans, Marc','Polmans, M',matchnames[i]);
            elif re.search('Johnson, Steve',matchnames[i]):
                matchnames[i]=    re.sub('Johnson, Steve','Johnson, S',matchnames[i]);
            elif re.search('Kanepi, Kaia',matchnames[i]):
                matchnames[i]=    re.sub('Kanepi, Kaia','Kanepi, K',matchnames[i]);
            elif re.search('Kaia Kanepi',matchnames[i]):
                matchnames[i]=    re.sub('Kaia Kanepi','Kanepi, K',matchnames[i]);
            elif re.search('Carreno Busta, Pablo',matchnames[i]):
                matchnames[i]=    re.sub('Carreno Busta, Pablo','Carreno Busta, P',matchnames[i]);
            elif re.search('Pablo Carreño Busta',matchnames[i]):
                matchnames[i]=    re.sub('Pablo Carreño Busta','Carreno Busta, P',matchnames[i]);
            elif re.search('HC Kunlun Red Star',matchnames[i]):
                matchnames[i]=    re.sub('HC Kunlun Red Star','HC Red Star Kunlun',matchnames[i]);
            elif re.search('Avtomobilist Ekaterinburg',matchnames[i]):
                matchnames[i]=    re.sub('Avtomobilist Ekaterinburg','Avtomobilist Yekaterinburg',matchnames[i]);
            elif re.search('Dynamo Riga',matchnames[i]):
                matchnames[i]=    re.sub('Dynamo Riga','Dinamo Riga',matchnames[i]);
            elif re.search('Dynamo Moscow',matchnames[i]):
                matchnames[i]=    re.sub('Dynamo Moscow','Dinamo Moscow',matchnames[i]);
            elif re.search('Dynamo Moskva',matchnames[i]):
                matchnames[i]=    re.sub('Dynamo Moskva','Dinamo Moscow',matchnames[i]);
            elif re.search('HC Dinamo Minsk',matchnames[i]):
                matchnames[i]=    re.sub('HC Dinamo Minsk','Dinamo Minsk',matchnames[i]);
            elif re.search('Yugra Khanty-Mansiysk',matchnames[i]):
                matchnames[i]=    re.sub('Yugra Khanty-Mansiysk','Ugra Khanty-Mansiysk',matchnames[i]);
            elif re.search('Salavat Yulaev Ufa',matchnames[i]):
                matchnames[i]=    re.sub('Salavat Yulaev Ufa','Salavat Ulaev Ufa',matchnames[i]);
            elif re.search('Severstal Cherepovec',matchnames[i]):
                matchnames[i]=    re.sub('Severstal Cherepovec','Severstal Cherepovets',matchnames[i]);
            elif re.search('HC Sochi',matchnames[i]):
                matchnames[i]=    re.sub('HC Sochi','Sochi',matchnames[i]);
            elif re.search(' Women ',matchnames[i]): 
                matchnames[i]=    re.sub(' Women','',matchnames[i]);
            elif re.search(' \([^\(\)]*\)',matchnames[i]):
                matchnames[i]=    re.sub(' \([^\(\)]*\)','',matchnames[i]);
            # Letters
            elif re.search('.u00F8',matchnames[i]):
                matchnames[i]=re.sub('.u00F8','ø',matchnames[i]);
            elif re.search('.u00E6',matchnames[i]):
                matchnames[i]=re.sub('.u00E6','æ',matchnames[i]);
            elif re.search('.u00E5',matchnames[i]):
                matchnames[i]=re.sub('.u00E5','å',matchnames[i]);
            elif re.search('.u00F3',matchnames[i]):
                matchnames[i]=re.sub('.u00F3','o',matchnames[i]);
            elif re.search('.u00F1',matchnames[i]):
                matchnames[i]=re.sub('.u00F1','ñ',matchnames[i]);
            elif re.search(' FC',matchnames[i]):
                matchnames[i]=re.sub(' FC','',matchnames[i]);
            elif re.search(' AFC',matchnames[i]):
                matchnames[i]=re.sub(' AFC','',matchnames[i]);
            elif re.search('  ',matchnames[i]):
                matchnames[i]=re.sub('  ',' ',matchnames[i]);
            else:
                matchnames[i]=matchnames[i];
                F=1;


    return matchnames
