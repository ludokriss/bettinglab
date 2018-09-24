#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:51:26 2017

@author: kristofferbjerkelund
"""

import requests
import numpy
import datetime
import fixNaming   
from dateutil.parser import parse

header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
url="https://www.matchbook.com/edge/rest/events?language=en&currency=USD&exchange-type=back-lay&odds-type=DECIMAL&price-depth=6&price-order=price%20desc&include-event-participants=true&offset=0&per-page=18&tag-url-names=soccer%2Cengland%2Cpremier-league"

tmp=requests.get(url,headers=header)

data=tmp.json()

for i in range(len(data['events'])):
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
        tmpvals[0][idx]=data2['markets'][0]['runners'][j]['prices'][0]['odds']
        
        
def parseSmarkets():
    header={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'}
    Matches={}
    Matches['events']={}
    Matches['events']['name']={}
    Matches['events']['matchtime']={}
    Matches['events']['odds']={}
    
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
        
    return Matches