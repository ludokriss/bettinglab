#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 21:22:55 2017

@author: kristofferbjerkelund
"""
import requests
from dateutil.parser import parse
import numpy
from betcompiler import main
from betcompiler import fixNaming
import pandas as pd

def parseOlybet(comp): 
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}
    df=pd.DataFrame(columns=['name','matchtime','home','draw','away'])

    if comp==1: #PL
        url='https://olybet.eu/bet/parents/14321';
    elif comp==2: #TL
        url='https://olybet.eu/bet/parents/13885';
    elif comp==3: #La Liga
        url='https://olybet.eu/bet/parents/14090';
    elif comp==4: #Serie A
        url='https://olybet.eu/bet/parents/14025';
    elif comp==5: #Ligue 1
        url='https://olybet.eu/bet/parents/14160';
    elif comp==6: #Bundesliga
        url='https://olybet.eu/bet/parents/14172';
    elif comp==7: #Championship
        url='https://olybet.eu/bet/parents/14322';
    elif comp==8: #NHL
        url='https://olybet.eu/bet/parents/15182';
    elif comp==9: #FA Cup
        url='https://www.olybet.eu/bet/parents/14326'
    elif comp==10: #Europa League
        url='https://olybet.eu/bet/parents/13191';
    elif comp==11: #Champions League
        url='https://olybet.eu/bet/parents/13213';
    elif comp==12: #KHL
        url='https://olybet.eu/bet/parents/15170'
    elif comp==13: #WC Qualification Europe
        url='https://olybet.eu/bet/parents/19107';
    elif comp==14: #WC Hockey
        url='https://olybet.eu/bet/parents/15155';
    elif comp==15: #Allsvenskan
        url='https://olybet.eu/bet/parents/13983';
    elif comp==16: #U20 VM
        url='https://olybet.eu/bet/parents/13074';
    elif comp==17: #NM
        url='https://olybet.eu/bet/parents/13897';
    elif comp==18: #MLS
        url='https://olybet.eu/bet/parents/13365';
    elif comp==19: #U21 EM
        url='https://olybet.eu/bet/parents/13172';
    elif comp==20: #Confederations cup
        url='https://olybet.eu/bet/parents/13088';
    elif comp==21: #ATP Wimbledon
        url='https://olybet.eu/bet/parents/16257';
    elif comp==22: #WTA Wimbledon
        url='https://olybet.eu/bet/parents/16258';
    elif comp==23: #EURO Women
        url='https://olybet.eu/bet/parents/17199';
    elif comp==24:
        url='https://olybet.eu/bet/parents/13099';
    elif comp==25:
        url='https://olybet.eu/bet/parents/13863';
    elif comp==26:
        url='https://olybet.eu/bet/parents/15627';
    elif comp==27:
        url='https://olybet.eu/bet/parents/15134';
    elif comp==28:
        url='https://olybet.eu/bet/parents/15618';
    elif comp==29:
        url='https://olybet.eu/bet/parents/13084';
    elif comp==31:
        url='https://olybet.eu/bet/parents/14375'
    elif comp==32:
        url='https://olybet.eu/bet/parents/15173';
    elif comp==33:
        url='https://olybet.eu/bet/parents/15626';
    elif comp==34:
        url='https://olybet.eu/bet/parents/15635';
    elif comp==35:
        url='https://www.olybet.eu/bet/parents/15114'
    elif comp==36:
        url='https://www.olybet.eu/bet/parents/16628'
    elif comp==37:
        url='https://www.olybet.eu/bet/parents/15216'
    elif comp==38:
        url='https://www.olybet.eu/bet/parents/14521'
    elif comp==39:
        url='https://www.olybet.eu/bet/parents/16197'
    elif comp==40:
        url='https://www.olybet.eu/bet/parents/16194'
    elif comp==41:
        url='https://www.olybet.eu/bet/parents/15632'
    elif comp==42:
        url='https://www.olybet.eu/bet/parents/16095'
    elif comp==43:
        url='https://www.olybet.eu/bet/parents/13076'
        
        
    tmp=requests.get(url,headers=header)
    matchtmp=tmp.json()
    string=matchtmp['data'];
    starttag='Minimalt antall kombinerte';
    idstart=string.rfind(starttag);
    if idstart<0:
        string=string
    else:
        string=string[idstart:len(string)];
    
    nametag=';name&quot;:&quot;';
    endnametag='&quot;,&quot;alt_name&quot;:&quot;';
    oddstag='&quot;,&quot;coef&quot;:&quot;';
    endoddstag='&quot;,&quot;option&quot;:&quot;';
    timetag='<span class="event-sport-and-time"> <span class="datetime" title="';
    timeids=list(main.find_all(string,timetag))
    nameids=list(main.find_all(string,nametag))
    endnameids=list(main.find_all(string,endnametag))
    oddsids=list(main.find_all(string,oddstag))
    endoddsids=list(main.find_all(string,endoddstag))
    # calculate how many outcomes there are per game.
    mnames={}
    for i in range(len(nameids)):
        mnames[i]=string[nameids[i]+len(nametag):endnameids[i]];
    
    temp=set( val for dic in mnames for val in mnames.values())
    N_outcomes=int(len(oddsids)/len(temp));
    
    for i in range(len(timeids)):
        Matches['events']['name'][i]=string[nameids[i*N_outcomes]+len(nametag):endnameids[i*N_outcomes]];
        df.loc[i,'name']=string[nameids[i*N_outcomes]+len(nametag):endnameids[i*N_outcomes]]
        Matches['events']['matchtime'][i]=parse(string[timeids[i]+len(timetag):timeids[i]+len(timetag)+16] + ' UTC');
        df.loc[i,'matchtime']=parse(string[timeids[i]+len(timetag):timeids[i]+len(timetag)+16] + ' UTC')
        tmpvals=numpy.empty((1,N_outcomes))
        for j in range(N_outcomes):
            tmpvals[0][j]=float(string[oddsids[i*N_outcomes+j]+len(oddstag):endoddsids[i*N_outcomes+j]])
            df.iloc[i,j+2]=float(string[oddsids[i*N_outcomes+j]+len(oddstag):endoddsids[i*N_outcomes+j]])
        Matches['events']['odds'][i]=tmpvals
        
    
    
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name']);
    df.name=fixNaming.fixNaming(df.name)
    return Matches,df