#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:24:45 2017

@author: kristofferbjerkelund
"""
import requests
import numpy
import datetime
from betcompiler import fixNaming
import pandas as pd
 
def parseUnibet(comp) :
    
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}
    df=pd.DataFrame(columns=['name','matchtime','home','draw','away'])

    if comp==2: #TL
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/football/norway/eliteserien.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503558120523&categoryGroup=COMBINED&displayDefault=true';
    elif comp==3: #La Liga
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/football/spain/laliga.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503558156971&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==4: #Serie A
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/football/italy/serie_a.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503558193171&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==5: #Ligue 1
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/football/france/ligue_1.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503558281774&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==6: #Bundesliga
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/football/germany/bundesliga.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503558235857&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==7: #Championship
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/football/england/the_championship.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503558325841&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==1: # PL
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ubuk/listView/football/england/premier_league.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1503521419022&categoryGroup=COMBINED&displayDefault=true';
    elif comp==8: #NHL
        url='https://e3-api.kambi.com/offering/api/v3/ub/listView/ice_hockey/nhl.json?lang=en_GB&market=ZZ&client_id=2&channel_id=1&ncid=1482450021775&categoryGroup=COMBINED&displayDefault=true';
    elif comp==9: #FA Cup
        url='https://e3-api.kambi.com/offering/api/v3/ubuk/listView/football/england/fa_cup.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1483687135632&categoryGroup=COMBINED&displayDefault=true';
    elif comp==10: #Europa League
        url='https://e4-api.kambi.com/offering/api/v3/ubuk/listView/football/europa_league.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1481185693162&categoryGroup=COMBINED&displayDefault=true';
    elif comp==11: #Champions League
        url='https://e3-api.kambi.com/offering/api/v3/ub/listView/football/champions_league.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1505050337845&categoryGroup=COMBINED&displayDefault=true'
    elif comp==12: #KHL
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/ice_hockey/khl.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503558379604&categoryGroup=COMBINED&displayDefault=true';
    elif comp==13: #WC Qualification Europe
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ubuk/listView/football/world_cup_qualifying_-_europe.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1489712503403&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==14: #WC Hockey
        url='https://e4-api.kambi.com/offering/api/v3/ubuk/listView/ice_hockey/world_championship.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1494003009981&categoryGroup=COMBINED&displayDefault=true';
    elif comp==15: #Allsvenskan
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ubuk/listView/football/sweden/allsvenskan.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1494969936607&categoryGroup=COMBINED&displayDefault=true';
    elif comp==16: #U20 VM
        url='https://e3-api.kambi.com/offering/api/v3/ubuk/listView/football/fifa_world_cup_u20.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1495479807010&categoryGroup=COMBINED&displayDefault=true';
    elif comp==17: #NM
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/football/norway/nm_cupen.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503558418380&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==18: #MLS
        url='https://e3-api.kambi.com/offering/api/v3/ub/listView/football/usa/mls.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1495901462871&categoryGroup=COMBINED&displayDefault=true';
    elif comp==19:
        url='https://e4-api.kambi.com/offering/api/v3/ubuk/listView/football/uefa_championship_u21.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1497560040655&categoryGroup=COMBINED&displayDefault=true';
    elif comp==20:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ubuk/listView/football/fifa_confederations_cup.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1497561687098&categoryGroup=COMBINED&displayDefault=true';
    elif comp==21:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ubuk/listView/tennis/grand_slam/wimbledon.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1498862322746&categoryGroup=COMBINED&displayDefault=true';
    elif comp==22:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ubuk/listView/tennis/grand_slam/wimbledon_women.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1499013475233&categoryGroup=COMBINED&displayDefault=true';
    elif comp==23:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ubuk/listView/football/uefa_womens_euro.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1500198440372&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==24:
        url='https://e3-api.kambi.com/offering/api/v3/ubuk/listView/football/club_tournaments/international_champions_cup.json?lang=en_GB&market=GB&client_id=2&channel_id=1&ncid=1500362589664&categoryGroup=COMBINED&displayDefault=true';
    elif comp==25:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/football/norway/obos-ligaen.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503558473950&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==26:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/tennis/atp/washington.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1501499363793&categoryGroup=COMBINED&displayDefault=true';
    elif comp==27:
        url='https://e3-api.kambi.com/offering/api/v3/ub/listView/baseball/mlb.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1501493795360&categoryGroup=COMBINED&displayDefault=true';
    elif comp==28:
        url='https://e4-api.kambi.com/offering/api/v3/ub/listView/tennis/wta/washington.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1501572774893&categoryGroup=COMBINED&displayDefault=true';
    elif comp==29:
        url='https://e3-api.kambi.com/offering/api/v3/ub/listView/football/club_tournaments/audi_cup.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1501584939749&categoryGroup=COMBINED&displayDefault=true'
    elif comp==31:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/football/england/efl_cup.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503311064536&categoryGroup=COMBINED&displayDefault=true'
    elif comp==32:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/ice_hockey/champions_hockey_league.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503575918860&categoryGroup=COMBINED&displayDefault=true&category=Match';
    elif comp==33:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/tennis/grand_slam/us_open.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503729034293&categoryGroup=COMBINED&displayDefault=true';
    elif comp==34:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/tennis/grand_slam/us_open_women.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1503729137308&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==35:
        url='https://e4-api.kambi.com/offering/api/v3/ub/listView/american_football/nfl.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1505034411972&categoryGroup=COMBINED&displayDefault=true'
    elif comp==36:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/basketball/nba.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1508599214509&categoryGroup=COMBINED&displayDefault=true&category=match';
    elif comp==37:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/ice_hockey/norway/get-ligaen.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1514319717366&categoryGroup=COMBINED&displayDefault=true'
    elif comp==38:
        url='https://e4-api.kambi.com/offering/api/v3/ub/listView/handball/european_championship.json?lang=en_GB&market=ZZ&client_id=2&channel_id=1&ncid=1515694247184&categoryGroup=COMBINED&displayDefault=true'
    elif comp==39:
        url='https://e4-api.kambi.com/offering/api/v3/ub/listView/tennis/grand_slam/australian_open.json?lang=en_GB&market=ZZ&client_id=2&channel_id=1&ncid=1516044722910&categoryGroup=COMBINED&displayDefault=true&category=match'
    elif comp==40:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/tennis/grand_slam/australian_open_women.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1516376613510&categoryGroup=COMBINED&displayDefault=true&category=match'
    elif comp==41:
        url='https://e1-api.aws.kambicdn.com/offering/api/v3/ub/listView/tennis/atp/miami.json?lang=no_NO&market=NO&client_id=2&channel_id=1&ncid=1521656107787&categoryGroup=COMBINED&displayDefault=true'       
    elif comp==42:
        url='https://e4-api.kambi.com/offering/api/v3/ub/listView/tennis/grand_slam/french_open.json?lang=en_GB&market=ZZ&client_id=2&channel_id=1&ncid=1527413592461&categoryGroup=COMBINED&displayDefault=true&category=match'
    elif comp==43:
        url='https://api.aws.kambicdn.com/offering/api/v3/ub/listView/football/world_cup_2018.json?lang=en_GB&market=NO&client_id=2&channel_id=1&ncid=1528636372531&categoryGroup=COMBINED&displayDefault=true'
    
    tmp=requests.get(url,headers=header)
    Unibettmp=tmp.json()
    # Lag en egen Marius-fil
    #cwd= os.getcwd()
    #os.system("curl '%s' > %s/cmp.json" %(url, cwd))
    #with open('cmp.json') as data_file:    
    #    Unibettmp = json.load(data_file)
    failed=0    
    
    for i in range(len(Unibettmp['events'])):
        try:
            if type(Unibettmp['events']) is dict:
                Matches['events'][i]['name']=Unibettmp['events'][i]['event']['name']
                df.loc[i,'name']=Unibettmp['events'][i]['event']['name']
                Matches['events'][i]['matchtime']=datetime.datetime.fromtimestamp(Unibettmp['events'][i]['event']['start']/1000, datetime.timezone.utc)
                df.loc[i,'matchtime']=datetime.datetime.fromtimestamp(Unibettmp['events'][i]['event']['start']/1000, datetime.timezone.utc)

            else:
                Matches['events']['name'][i]=Unibettmp['events'][i]['event']['name']
                df.loc[i,'name']=Unibettmp['events'][i]['event']['name']
                Matches['events']['matchtime'][i]=datetime.datetime.fromtimestamp(Unibettmp['events'][i]['event']['start']/1000, datetime.timezone.utc)
                df.loc[i,'matchtime']=datetime.datetime.fromtimestamp(Unibettmp['events'][i]['event']['start']/1000, datetime.timezone.utc)
                tmpvals=numpy.empty((1,len(Unibettmp['events'][i]['betOffers'][0]['outcomes'])))
                if type(Unibettmp['events'][i]['betOffers']) is list:
                    for j in range(len(Unibettmp['events'][i]['betOffers'][0]['outcomes'])):
                        tmpvals[0][j]=Unibettmp['events'][i]['betOffers'][0]['outcomes'][j]['odds']/1000
                        df.iloc[i,j+2]=Unibettmp['events'][i]['betOffers'][0]['outcomes'][j]['odds']/1000
                else:
                    for j in range(len(Unibettmp['events'][i]['betOffers']['outcomes'])):
                        tmpvals[0][j]=Unibettmp['events'][i]['betOffers'][0]['outcomes'][j]['odds']/1000
                        df.iloc[i,j+2]=Unibettmp['events'][i]['betOffers'][0]['outcomes'][j]['odds']/1000
                Matches['events']['odds'][i]=tmpvals
            
        except:
            failed=failed+1
    
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name'])
    df.name=fixNaming.fixNaming(df.name)
    return Matches,df