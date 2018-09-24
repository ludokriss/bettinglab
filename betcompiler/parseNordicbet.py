#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:11:56 2017

@author: kristofferbjerkelund
"""
from betcompiler import fixNaming
import requests
from dateutil.parser import parse
import numpy
import pandas as pd

def parseNordicbet(comp):
    
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}
    df=pd.DataFrame(columns=['name','matchtime','home','draw','away'])
    
    if comp==1: #PL
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=3';
    elif comp==2: #TL
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=128';
    elif comp==3: #La Liga
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=12';
    elif comp==4: #Serie A
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=9';
    elif comp==5: #Ligue 1
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=13&subCategoryIds=19';
    elif comp==6: #Bundesliga
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=15';
    elif comp==7: #Championship
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/904/no/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=4';
    elif comp==8: #NHL
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/904/no/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=50';
    elif comp==9: #FA Cup
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=11&subCategoryIds=7';
    elif comp==10: #Europa League
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=2612';
    elif comp==11: #Champions League
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=6134';
    elif comp==12: #KHL
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=3207';
    elif comp==13: #WC Qualification Europe
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=1609';
    elif comp==14: #WC hockey
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=444';
    elif comp==15: #Allsvenskan
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=1';
    elif comp==16: #U20 VM
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=1163';
    elif comp==17: #NM
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=134';
    elif comp==18: #MLS
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=250';
    elif comp==19: #U21 EM
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&marketCount=50&page=1&subCategoryIds=563';
    elif comp==20:
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&eventSortBy=2&marketCount=50&page=1&subCategoryIds=257';
    elif comp==21:
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&eventSortBy=2&marketCount=50&page=1&subCategoryIds=577';
    elif comp==22:
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&eventSortBy=2&marketCount=50&page=1&subCategoryIds=578';
    elif comp==23:
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/901/en/event?betgroupgroupingids=36&eventPhase=1&eventSortBy=2&marketCount=50&page=1&subCategoryIds=4830';
    elif comp==25:
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/904/no/event?betgroupgroupingids=36&eventPhase=1&eventSortBy=2&marketCount=50&page=1&subCategoryIds=129';
    elif comp==31:
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/904/no/event?betgroupgroupingids=36&eventPhase=1&eventSortBy=2&marketCount=50&page=1&subCategoryIds=148'
    elif comp==32:
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/904/no/event?betgroupgroupingids=36&eventPhase=1&eventSortBy=2&marketCount=50&page=1&subCategoryIds=2079';
    elif comp==42:
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/904/no/event?betgroupgroupingids=36&eventPhase=1&eventSortBy=2&marketCount=50&page=1&subCategoryIds=548'
    elif comp==43:
        url='https://sbsitefacade2.bpsgameserver.com/isa/v2/904/no/event?betgroupgroupingids=36&eventPhase=1&eventSortBy=2&marketCount=50&page=1&subCategoryIds=3505'
    
    tmp=requests.get(url,headers=header)
    Nordicbettmp=tmp.json();
    for i in range(len(Nordicbettmp['el'])):
        Matches['events']['name'][i]=Nordicbettmp['el'][i]['en'];
        df.loc[i,'name']=Nordicbettmp['el'][i]['en']
        Matches['events']['matchtime'][i]=parse(Nordicbettmp['el'][i]['sd'])
        df.loc[i,'matchtime']=parse(Nordicbettmp['el'][i]['sd'])
        tmpvals=numpy.empty((1,len(Nordicbettmp['el'][i]['ml'][0]['msl'])))
        for j in range(len(Nordicbettmp['el'][i]['ml'][0]['msl'])):
            tmpvals[0][j]=Nordicbettmp['el'][i]['ml'][0]['msl'][j]['msp']
            df.iloc[i,j+2]=Nordicbettmp['el'][i]['ml'][0]['msl'][j]['msp']
        Matches['events']['odds'][i]=tmpvals
    
    df.name=fixNaming.fixNaming(df.name)
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name']);
    return Matches,df