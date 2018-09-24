#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 21:00:47 2017

@author: kristofferbjerkelund
"""

from betcompiler import fixNaming
import requests
from dateutil.parser import parse
import numpy
import pandas as pd

def parseBetsson(comp):

    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}
    df=pd.DataFrame(columns=['name','matchtime','home','draw','away'])
    
    if comp==1:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=11&subCategoryIds=3';
    elif comp==2: #TL
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=18&subCategoryIds=128';
    elif comp==3: #La Liga
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=25&subCategoryIds=12';
    elif comp==4: #Serie A
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=17&subCategoryIds=9';
    elif comp==5: #Ligue 1
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=13&subCategoryIds=19';
    elif comp==6: #Bundesliga
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=14&subCategoryIds=15'; 
    elif comp==14: # WC Hockey
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=6,31,32,410,8,66&categoryIds=2&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=129&subCategoryIds=444';
    elif comp==24:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=3&subCategoryIds=13334';
    elif comp==26: #ATP Washington
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=27,52,657,51,375,1919&categoryIds=11&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=38&subCategoryIds=4836';
    elif comp==27:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=99,100,56,398,399&categoryIds=19&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=125&subCategoryIds=388';
    elif comp==28:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=27,52,657,51,375,1919&categoryIds=11&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=39&subCategoryIds=4761';
    elif comp==29:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=1,5,4058,65,127&categoryIds=1&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=3&subCategoryIds=6049';
    elif comp==33:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=27,52,657,51,375,1919&categoryIds=11&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=38&subCategoryIds=668';
    elif comp==34:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=27,52,657,51,375,1919&categoryIds=11&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=39&subCategoryIds=669';
    elif comp==35:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=28,55,30,395,396&categoryIds=10&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=131&subCategoryIds=107'
    elif comp==36:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=15,54,36,465,466&categoryIds=4&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=118&subCategoryIds=87'
    elif comp==37:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=6,31,32,410,8,66&categoryIds=2&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=18&subCategoryIds=180'
    elif comp==38:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=10,34,14,68,33&categoryIds=3&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=1&subCategoryIds=208'
    elif comp==39: 
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=27,52,657,51,375,1919&categoryIds=11&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=38&subCategoryIds=106'
    elif comp==40:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/605/no/event?betGroupIds=27,52,657,51,375,1919&categoryIds=11&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=39&subCategoryIds=391'
    elif comp==41:
        url='https://bts-api-a.bpsgameserver.com/isa/v2/601/en/event?betGroupIds=27,52,657,51,375,1919&categoryIds=11&eventPhase=1&eventSortBy=1&ocb=1f6efdd0-d13f-44be-9a5a-ea6195cc885d&onlyEvenLineMarkets=false&regionIds=38&subCategoryIds=464'

    tmp=requests.get(url,headers=header)
    Betssontmp=tmp.json();
    for i in range(len(Betssontmp['el'])):
        Matches['events']['name'][i]=Betssontmp['el'][i]['en']
        df.loc[i,'name']=Betssontmp['el'][i]['en']
        Matches['events']['matchtime'][i]=parse(Betssontmp['el'][i]['sd'])
        df.loc[i,'matchtime']=parse(Betssontmp['el'][i]['sd'])
        tmpvals=numpy.empty((1,len(Betssontmp['el'][i]['ml'][0]['msl'])))
        for j in range(len(Betssontmp['el'][i]['ml'][0]['msl'])):
            tmpvals[0][j]=Betssontmp['el'][i]['ml'][0]['msl'][j]['msp']
            df.iloc[i,j+2]=Betssontmp['el'][i]['ml'][0]['msl'][j]['msp']
        Matches['events']['odds'][i]=tmpvals
    
    df.name=fixNaming.fixNaming(df.name)
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name']);
    
    return Matches,df