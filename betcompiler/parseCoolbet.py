#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 22:32:50 2017

@author: kristofferbjerkelund
"""
import requests
from dateutil.parser import parse
import numpy
from betcompiler import fixNaming
import pandas as pd

def parseCoolbet(Comp,version=1):
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}
    df=pd.DataFrame(columns=['name','matchtime','home','draw','away'])
    
    if Comp==2: #TL
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19050&is_mobile=0&lastCategoryId=0'
    elif Comp==3: #La Liga
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19104&is_mobile=0&lastCategoryId=0'
    elif Comp==4: #Serie A
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18994&is_mobile=0&lastCategoryId=0'
    elif Comp==5: #Ligue 1
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18849&is_mobile=0&lastCategoryId=0'
    elif Comp==6: #Bundesliga
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18986&is_mobile=0&lastCategoryId=0'
    elif Comp==7: #Championship
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18976&is_mobile=0&lastCategoryId=0'
    elif Comp==1: #PL
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18975&offset=0'
    elif Comp==8: #NHL
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18712&is_mobile=0&lastCategoryId=0'
    elif Comp==9: #FA Cup
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19076&is_mobile=0&lastCategoryId=0'
    elif Comp==10: #Europa League
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19129&is_mobile=0&lastCategoryId=0'
    elif Comp==11: #Champions League
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19128&is_mobile=0&lastCategoryId=0'
    elif Comp==12: #KHL
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18834&is_mobile=0&lastCategoryId=0'
    elif Comp==13: #WC Qualification Europe
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=20086&is_mobile=0&lastCategoryId=0'
    elif Comp==14: #WC Hockey
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19764&is_mobile=0&lastCategoryId=0'
    elif Comp==15: #Allsvenskan
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19111&is_mobile=0&lastCategoryId=0'
    elif Comp==16: #U20 VM
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=43069&is_mobile=0&lastCategoryId=0'
    elif Comp==17: #NM
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19052&is_mobile=0&lastCategoryId=0'
    elif Comp==18: #MLS
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19093&is_mobile=0&lastCategoryId=0'
    elif Comp==19: #U21 EM
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19931&is_mobile=0&lastCategoryId=0'
    elif Comp==20: #Confederation Cup
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=43073&is_mobile=0&lastCategoryId=0'
    elif Comp==21: #ATP Wimbledon
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=26402&is_mobile=0&lastCategoryId=0'
    elif Comp==22: #WTA Wimbledon
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=26403&is_mobile=0&lastCategoryId=0'
    elif Comp==23: #EURO Women
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19933&is_mobile=0&lastCategoryId=0'
    elif Comp==24: #International Champions Cup
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=20474&is_mobile=0&lastCategoryId=0'
    elif Comp==25: #OBOS-ligaen
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19051&is_mobile=0&lastCategoryId=0'
    elif Comp==26: #ATP Washington
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=26628&is_mobile=0&lastCategoryId=0'
    elif Comp==27: #MLB
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18708&is_mobile=0&lastCategoryId=0'
    elif Comp==28: #WTA Washington
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=26630&is_mobile=0&lastCategoryId=0'
    elif Comp==29: #Audi Cup
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=44968&is_mobile=0&lastCategoryId=0'
    elif Comp==31: #EFL Cup
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=28508&is_mobile=0&lastCategoryId=0'
    elif Comp==32: #CHL
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=28500&is_mobile=0&lastCategoryId=0'
    elif Comp==33: #US open
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=28666&is_mobile=0&lastCategoryId=0'
    elif Comp==34: #US open women
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=28667&is_mobile=0&lastCategoryId=0'
    elif Comp==35: #NFL
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19488&is_mobile=0&lastCategoryId=0'
    elif Comp==36: #NBA
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=19158&is_mobile=1&lastCategoryId=0'
    elif Comp==37: #GET-ligaen
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18841&is_mobile=0&lastCategoryId=0'
    elif Comp==38: #European championship handball
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18950&is_mobile=0&lastCategoryId=0'
    elif Comp==39: #Australian open
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=29671&is_mobile=0&lastCategoryId=0'
    elif Comp==40: #Australian open women
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=34460&is_mobile=0&lastCategoryId=0'
    elif Comp==41: #ATP Miami
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=18685&is_mobile=0&lastCategoryId=0'
    elif Comp==42: #French Open
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=25277&is_mobile=0&lastCategoryId=0'
    elif Comp==43: #VM
        url='https://www.coolbet.com/s/fixtures/fo-match-category/?categoryId=46801&is_mobile=0&lastCategoryId=0'

    tmp=requests.get(url,headers=header)
    matchtmp=tmp.json()
    field=tuple(matchtmp['matches_by_category'])
    field=field[0]
    failed=0
    idx=0
    for index in range(len(matchtmp['matches_by_category'][field])):
        try:
            if type(matchtmp['matches_by_category'][field][index]) is dict:
                idx=-1;
                if len(matchtmp['matches_by_category'][field][index]['markets'])>1:
                    k=0;
                    while k<len(matchtmp['matches_by_category'][field][index]['markets']) and idx<0:
                        if matchtmp['matches_by_category'][field][index]['markets'][k]['name'] == 'Match Result (1X2)':
                            idx=matchtmp['matches_by_category'][field][index]['markets'][k]['id']
                        elif matchtmp['matches_by_category'][field][index]['markets'][k]['name'] == 'Money Line':
                            idx=matchtmp['matches_by_category'][field][index]['markets'][k]['id']
                        elif matchtmp['matches_by_category'][field][index]['markets'][k]['name'] == 'Match Result':
                            idx=matchtmp['matches_by_category'][field][index]['markets'][k]['id']
                        
                        k=k+1;
                    
                else:
                    idx=matchtmp['matches_by_category'][field][index]['markets'][0]['id']
                
                tmp2=requests.get('https://www.coolbet.com/s/sb-odds/odds/current/fo/?where=%7B%22market_id%22:%7B%22in%22:%5B' + str(idx) + '%5D%7D%7D',headers=header)
                oddstmp=tmp2.json()
                Matches['events']['name'][index-failed]=matchtmp['matches_by_category'][field][index]['name']
                df.loc[index-failed,'name']=matchtmp['matches_by_category'][field][index]['name']
                Matches['events']['matchtime'][index-failed]=parse(matchtmp['matches_by_category'][field][index]['match_start'])
                df.loc[index-failed,'matchtime']=Matches['events']['matchtime'][index-failed]
                field2=sorted(tuple(oddstmp))
                tmpvals=numpy.empty((1,len(field2)))
                for index2 in range(len(field2)):
                    tmpvals[0][index2]=oddstmp[field2[index2]]['value'];
                    df.iloc[index-failed,index2+2]=oddstmp[field2[index2]]['value']
                Matches['events']['odds'][index-failed]=tmpvals
            else :
                if len(matchtmp['matches_by_category'][field][index]['markets'])>1:
                    idx=0;
                    k=1;
                    while k<len(matchtmp['matches_by_category'][field][index]['markets']) and idx<0:
                        if matchtmp['matches_by_category'][field][index]['markets'][k]['name'] == 'Match Result (1X2)':
                            idx=matchtmp['matches_by_category'][field][index]['markets'][k]['id']
                        elif matchtmp['matches_by_category'][field][index]['markets'][k]['name'] == 'Money Line':
                            idx=matchtmp['matches_by_category'][field][index]['markets'][k]['id']
                        elif matchtmp['matches_by_category'][field][index]['markets'][k]['name'] == 'Match Result':
                            idx=matchtmp['matches_by_category'][field][index]['markets'][k]['id']
                        
                        k=k+1;
                    
                else:
                    idx=matchtmp['matches_by_category'][field][index]['markets'][0]['id']
                
                tmp2=requests.get('https://www.coolbet.com/s/sb-odds/odds/current/fo/?where=%7B%22market_id%22:%7B%22in%22:%5B' + str(idx) + '%5D%7D%7D',headers=header)
                oddstmp=tmp2.json()
                Matches['events']['name'][index-failed]=matchtmp['matches_by_category'][field][index]['name'];
                Matches['events']['matchtime'][index-failed]=parse(matchtmp['matches_by_category'][field][index]['match_start'])
                field2=tuple(oddstmp)
                tmpvals=numpy.empty((1,len(field2)))
                for index2 in range(len(field2)):
                    tmpvals[0][index2]=oddstmp[field2[index2]]['value'];
                Matches['events']['odds'][index-failed]=tmpvals
            
        except:
            failed=failed+1;
        
    df.name=fixNaming.fixNaming(df.name)
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name'])
    return Matches,df
