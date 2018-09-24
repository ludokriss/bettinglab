#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:01:54 2017

@author: kristofferbjerkelund
"""

import requests
from dateutil.parser import parse
import numpy
from betcompiler import fixNaming
import json
import datetime
from bs4 import BeautifulSoup
import pandas as pd

def parseNT(comp):
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0',
            'GET':'/api-langoddsen/getGameInformation.json?categories=true&filter=ligue HTTP/1.1',
            'Host':'www.norsk-tipping.no',
            'Referer':'https://www.norsk-tipping.no/sport/langoddsen',
            'Connection':'keep-alive'}
    
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}
    df=pd.DataFrame(columns=['name','matchtime','home','draw','away'])
    
    eventnameid=1
    if comp==1:
        NTcomp=1;
    elif comp==2:
        NTcomp=5;
    elif comp==3:
        NTcomp=36;
    elif comp==4:
        NTcomp=33;
    elif comp==5:
        NTcomp=4;
    elif comp==6:
        NTcomp=42;
    elif comp==7:
        NTcomp=2;
    elif comp==8:
        NTcomp=142
        eventnameid=0
        
    elif comp==10:
        NTcomp=10909
    elif comp==11:
        NTcomp=23
    elif comp==12:
        NTcomp=673
    elif comp==15:
        NTcomp=24
    elif comp==17:
        NTcomp=6;
    elif comp==15:
        NTcomp=24;
    elif comp==25:
        NTcomp=6;
    elif comp==37:
        NTcomp=120
    elif comp==39:
        NTcomp=100016613
    
    tmp=requests.get('https://www.norsk-tipping.no/api-langoddsen/getGameInformation.json?categories=true&filter=ligue',headers=header);
    nt=json.loads(tmp.text[19:len(tmp.text)-6])
    j=0
    for i in range(len(nt['events'])):
        if nt['events'][i]['eventDetails'][1]==NTcomp and  len(nt['events'][i]['eventDetails'][6])>0:
            Matches['events']['name'][j]=nt['events'][i]['eventDetails'][2][eventnameid]
            df.loc[j,'name']=nt['events'][i]['eventDetails'][2][eventnameid]
            Matches['events']['matchtime'][j]=datetime.datetime.fromtimestamp(nt['events'][i]['eventDetails'][4]/1000, datetime.timezone.utc)
            df.loc[j,'matchtime']=datetime.datetime.fromtimestamp(nt['events'][i]['eventDetails'][4]/1000, datetime.timezone.utc)
            tmpvals=numpy.empty((1,len(nt['events'][i]['eventDetails'][6][0][3][2])))
            for k in range(len(nt['events'][i]['eventDetails'][6][0][3][2])):
                tmpvals[0][k]=nt['events'][i]['eventDetails'][6][0][3][2][k]/100
                df.iloc[j,k+2]=nt['events'][i]['eventDetails'][6][0][3][2][k]/100
            Matches['events']['odds'][j]=tmpvals
            j=j+1
            
    df.name=fixNaming.fixNaming(df.name)
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name']);
    return Matches,df
    
def parseBetfairExchange(comp):
    header={'host':'strands.betfair.com',
    'X-Application':'nzIFcwyWhrlwYMrh',
    'Accept':'application/json, text/plain, */*',
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Content-Type':'application/json'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['eventId']={}
    Matches['events']['odds']={}
    Matches['events']['marketId']={}
    
    if comp==1:
        competitionId=10932509;
    elif comp==2:
        competitionId=11068551;
    elif comp==3:
        competitionId=117;
    elif comp==4:
        competitionId=81;
    elif comp==5:
        competitionId=55;
    elif comp==6:
        competitionId=59;
    elif comp==15:
        competitionId=129;
    
    url='https://strands.betfair.com/api/eds/navigation-aggregator/v1?competitionId='+str(competitionId);
    
    tmp=requests.get(url,headers=header)
    matchtmp=tmp.json()
    flds=list(matchtmp['fixtures'].keys())
    posturl='https://strands.betfair.com/api/eds/coupon/v1';
    postbody='{"search":{"type":"COMPETITION","ids":[' +str(competitionId) +']},"filters":{"selectBy":"TIME","timeFrame":"ALL","marketType":"MATCH_ODDS"},"limits":{"maxEventTypes":5,"maxEventsPerEventType":50,"maxCompetitions":5}}'
    tmp2=requests.post(posturl,postbody,headers=header);
    tmpevent=tmp2.json()
    k=0;
    for i in range(len(flds)):
        for j in range(len(matchtmp['fixtures'][flds[i]])):
            
            Matches['events']['name'][k]=matchtmp['fixtures'][flds[i]][j]['name']
            Matches['events']['matchtime'][k]=parse(matchtmp['fixtures'][flds[i]][j]['openDate'])
            Matches['events']['eventId'][k]=matchtmp['fixtures'][flds[i]][j]['eventId']
            k=k+1;
            
    for i in range(len(tmpevent[0]['competitions'][0]['events'])):
        try:
            idEvent=list(Matches['events']['eventId'].values()).index(tmpevent[0]['competitions'][0]['events'][i]['eventId'])
            Matches['events']['marketId'][idEvent]=tmpevent[0]['competitions'][0]['events'][i]['marketId']
            marketUrl='https://www.betfair.com/www/sports/exchange/readonly/v1/bymarket?alt=json&currencyCode=NOK&locale=no&marketIds='+str(tmpevent[0]['competitions'][0]['events'][i]['marketId'])+'&rollupLimit=100&rollupModel=STAKE&types=MARKET_STATE,MARKET_RATES,MARKET_DESCRIPTION,EVENT,RUNNER_DESCRIPTION,RUNNER_STATE,RUNNER_EXCHANGE_PRICES_BEST,RUNNER_METADATA,MARKET_LICENCE'
            tmpdata=requests.get(marketUrl,headers=header);
            data=tmpdata.json()
            tmpvals=numpy.empty((1,len(data['eventTypes'][0]['eventNodes'][0]['marketNodes'][0]['runners'])))
            for j in range(len(data['eventTypes'][0]['eventNodes'][0]['marketNodes'][0]['runners'])):
                if j==0:
                    outcome=0;
                elif j==1:
                    outcome=2;
                elif j==2:
                    outcome=1;
                
                try:
                    tmpvals[0][outcome]=data['eventTypes'][0]['eventNodes'][0]['marketNodes'][0]['runners'][j]['exchange']['availableToBack'][0]['price']
                except:
                    a=0
            Matches['events']['odds'][idEvent]=tmpvals
        except:
            a=0
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name'])
    
    return Matches

def parseSmarkets(comp):
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}
    if comp==1:
        url="https://smarkets.com/v0/listings/slug/sport/football/premier-league-2017-2018/"
    
    tmp=requests.get(url,headers=header)
    data=tmp.json()
    
    events=str([int(data['event_ids'][i]) for i in range(len(data['event_ids']))])[1:-1].replace(" ","")
    url2="https://smarkets.com/v0/events/ids/"+events+"/live/"
    tmp2=requests.get(url2,headers=header)
    data2=tmp2.json()
    
    i=0
    for key in data['events']:
        Matches['events']['name'][i]=data['events'][key]['name']
        Matches['events']['matchtime'][i]=parse(data['events'][key]['start_datetime'])
        contracts=data['events'][key]['primary_contracts_ids']
        tmpvals=numpy.empty((1,len(contracts)))
        for j in range(len(contracts)):
            if j==0:
                idx=0
            elif j==1:
                idx=2
            elif j==2:
                idx=1
            try:
                tmpvals[0][idx]=1/(data2['quotes'][contracts[j]]['offers'][0]['price']/10000)
            except:
                tmpvals[0][idx]=1.
        Matches['events']['odds'][i]=tmpvals
        i+=1
    
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name'])
    return Matches


def parseMatchbook(comp):
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}

    if comp==1:
        url="https://www.matchbook.com/edge/rest/events?language=en&currency=USD&exchange-type=back-lay&odds-type=DECIMAL&price-depth=6&price-order=price%20desc&include-event-participants=true&offset=0&per-page=18&tag-url-names=soccer%2Cengland%2Cpremier-league"
    tmp=requests.get(url,headers=header)
    data=tmp.json()
    
    for i in range(len(data['events'])):
        Matches['events']['name'][i]=data['events'][i]['name']
        Matches['events']['matchtime'][i]=parse(data['events'][i]['start'])

        url2="https://www.matchbook.com/edge/rest/events/"+str(data['events'][i]['id'])+"?language=en&currency=USD&exchange-type=back-lay&odds-type=DECIMAL&include-markets=true&include-prices=true&include-runners=true&market-per-page=500&price-depth=6&price-order=price%20desc&include-event-participants=true"
        tmp2=requests.get(url2,headers=header)
        data2=tmp2.json()
        tmpvals=numpy.empty((1,len(data2['markets'][0]['runners'])))
        for j in range(len(data2['markets'][0]['runners'])):
            if j==0:
                idx=0
            elif j==1:
                idx=2
            elif j==2:
                idx=1
            try:
                tmpvals[0][idx]=data2['markets'][0]['runners'][j]['prices'][0]['odds']
            except:
                tmpvals[0][idx]=1.
        Matches['events']['odds'][i]=tmpvals
        
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name'])

    return Matches

def parseComeon(comp):
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0',
            ':path:':'/pagemethods.aspx/GetGroupViewForLeagueViewResponsive?isInitialLoad=true&leagueId=40253',
            'requesttarget':'AJAXService'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}

    
    
    if comp==1:
        url="https://m.comeon.com/pagemethods.aspx/GetGroupViewForLeagueViewResponsive?isInitialLoad=true&leagueId=40253"
    
    tmp=requests.get(url, headers=header)
    data=tmp.json()
    
def parseExpekt(comp=1):
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}
    df=pd.DataFrame(columns=['name','matchtime','home','draw','away'])
    
    i=0
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
    if comp==1:
        tmp=requests.get('https://en.expekt.com/fotball/eng-premier-league-3',headers=header)
    elif comp==2:
        tmp=requests.get('https://en.expekt.com/fotball/nor-eliteserien-156',headers=header)
    elif comp==3:
        tmp=requests.get('https://no.expekt.com/fotball/spa-primera-division-7',headers=header)
    elif comp==8:
        tmp=requests.get('https://no.expekt.com/ishockey/nhl-83',headers=header)
    elif comp==11: 
        tmp=requests.get('https://no.expekt.com/fotball/champions-league-8',headers=header)
    elif comp==43:
        tmp=requests.get('https://en.expekt.com/football/world-cup-1',headers=header)
        
    soup=BeautifulSoup(tmp.content,"lxml")
    for tr in soup.find_all("div",{"class":"match-entry"}):
        Matches['events']['name'][i]=tr.attrs['data-track-event-name']
        df.loc[i,'name']=tr.attrs['data-track-event-name']
        j=0
        tmpvals=numpy.empty((1,3))
        for td in tr.find_all("span",{"class":"oddValue"}):
            tmpvals[0][j]=td.text.replace(',','.')
            df.iloc[i,j+2]=float(td.text.replace(',','.'))
            j+=1
        Matches['events']['odds'][i]=tmpvals
        i+=1
    df.name=fixNaming.fixNaming(df.name)
    Matches['events']['name']=fixNaming.fixNaming(Matches['events']['name'])
    return Matches,df