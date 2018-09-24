#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 22:31:15 2017

@author: kristofferbjerkelund
"""
from betcompiler import parseCoolbet
from betcompiler import parseNordicbet
from betcompiler import parseUnibet
from betcompiler import parseOlybet
from betcompiler import parseBetsson
import numpy
from betcompiler import parseOdds
import pandas as pd

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
    return start;

class vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)() # retain local pointer to value
        return value                     # faster to return than dict lookup
    
def init_db(cur):
    cur.execute('''CREATE TABLE overview (
        Row INTEGER,
        Name TEXT,
        matchtime timestamp,
        home float,
        X float
        away float)''')
    
class oddsmatrix():
    def __init__(self):
        self.last=[]
        self.best=[]
        self.df=pd.DataFrame()
        self.df=pd.DataFrame()
    def compileOdds(self,comp):
        d={}
        d['name']={}
        d['odds']=vividict()
        d['matchtime']={}
        self.df=pd.DataFrame()
        
        try:
            Coolbet,df=parseCoolbet.parseCoolbet(comp)
            d['name']=list(set(list(Coolbet['events']['name'].values())+list(d['name'])))
            df['provider']='Coolbet'
            self.df=self.df.append(df)
        except:
            print("Coolbet failed")  
        try:
            Nordicbet,df=parseNordicbet.parseNordicbet(comp)
            d['name']=list(set(list(Nordicbet['events']['name'].values())+list(d['name'])))
            df['provider']='Nordicbet'
            self.df=self.df.append(df)
        except:
            print("Nordicbet failed")
            Nordicbet=[]
        try:
            Betsson,df=parseBetsson.parseBetsson(comp)
            d['name']=list(set(list(Betsson['events']['name'].values())+list(d['name'])))
            df['provider']='Betsson'
            self.df=self.df.append(df)
        except:
            print("Betsson failed")
        try:
            Unibet,df=parseUnibet.parseUnibet(comp)
            d['name']=list(set(list(Unibet['events']['name'].values())+list(d['name'])))
            df['provider']='Unibet'
            self.df=self.df.append(df)
        except:
            print("Unibet failed")
        try:
            Olybet,df=parseOlybet.parseOlybet(comp)
            d['name']=list(set(list(Olybet['events']['name'].values())+list(d['name'])))
            df['provider']='Olybet'
            self.df=self.df.append(df)
        except:
            print("Olybet failed")
            
        try:
            NT,df=parseOdds.parseNT(comp)
            d['name']=list(set(list(NT['events']['name'].values())+list(d['name'])))
            df['provider']='NT'
            self.df=self.df.append(df)
        except:
            print("NT failed")
    
        try:
            Expekt,df=parseOdds.parseExpekt(comp)
            d['name']=list(set(list(Expekt['events']['name'].values())+list(d['name'])))
            df['provider']='Expekt'
            self.df=self.df.append(df)
        except:
            print("Expekt failed")

        try:
            for i in range(len(Coolbet['events']['name'])):
                idx=d['name'].index(Coolbet['events']['name'][i])
                d['odds'][idx]['Coolbet']=Coolbet['events']['odds'][i]
                d['matchtime'][idx]=Coolbet['events']['matchtime'][i]
        except:
            print("Coolbet failed")
        try:
            for i in range(len(Nordicbet['events']['name'])):
                idx=d['name'].index(Nordicbet['events']['name'][i])
                d['odds'][idx]['Nordicbet']=Nordicbet['events']['odds'][i]
                d['matchtime'][idx]=Nordicbet['events']['matchtime'][i]
        except:
            print("Nordicbet failed")
            
        try:
            for i in range(len(Betsson['events']['name'])):
                idx=d['name'].index(Betsson['events']['name'][i])
                d['odds'][idx]['Betsson']=Betsson['events']['odds'][i]
                d['matchtime'][idx]=Betsson['events']['matchtime'][i]
        except:
            print("Betsson failed")    
        try:
            for i in range(len(Unibet['events']['name'])):
                idx=d['name'].index(Unibet['events']['name'][i])
                d['odds'][idx]['Unibet']=Unibet['events']['odds'][i]
                d['matchtime'][idx]=Unibet['events']['matchtime'][i]
        except:
            print("Unibet failed")
        try:
            for i in range(len(Olybet['events']['name'])):
                idx=d['name'].index(Olybet['events']['name'][i])
                d['odds'][idx]['Olybet']=Olybet['events']['odds'][i]
                d['matchtime'][idx]=Olybet['events']['matchtime'][i]
        except:
            print("Olybet failed")
    
        try:
            for i in range(len(NT['events']['name'])):
                idx=d['name'].index(NT['events']['name'][i])
                d['odds'][idx]['NT']=NT['events']['odds'][i]
                d['matchtime'][idx]=NT['events']['matchtime'][i]
        except:
            print("NT failed")

        try:
            for i in range(len(Expekt['events']['name'])):
                idx=d['name'].index(Expekt['events']['name'][i])
                d['odds'][idx]['Expekt']=Expekt['events']['odds'][i]
        except:
            print("Expekt failed")
    
    
            
        self.maxodds=self.df.groupby('name')['home','draw','away'].max()
        self.maxodds['safe']=1-1/(1/self.maxodds['home']+1/self.maxodds['draw']+1/self.maxodds['away'])
        self.maxodds=self.maxodds.reset_index()
        
        self.maxodds['provider1']=self.maxodds.apply(lambda row: list(self.df[(self.df.name.str.contains(row['name'])) & (self.df.home==row['home'])].provider.values),axis=1)
        self.maxodds['providerX']=self.maxodds.apply(lambda row: list(self.df[(self.df.name.str.contains(row['name'])) & (self.df.draw==row['draw'])].provider.values),axis=1)
        self.maxodds['provider2']=self.maxodds.apply(lambda row: list(self.df[(self.df.name.str.contains(row['name'])) & (self.df.away==row['away'])].provider.values),axis=1)
        
        self.last=self.bestodds(d)
        
    
    def bestodds(self,d):
        best={}
        best['name']=d['name']
        best['matchtime']=d['matchtime']
        best['odds']={}
        best['provider']={}
        best['safe']={}
        for i in range(len(d['name'])):
            ks=list(d['odds'][i].keys())

                    
            best['odds'][i]={}
            best['provider'][i]={}
            try:
                nodds=nodds=d['odds'][i][ks[0]].size
                for j in range(nodds):
                    best['odds'][i][j]=0
                    best['provider'][i][j]=''
                    for k in range(len(ks)):
                        if best['odds'][i][j]<d['odds'][i][ks[k]][0,j]:
                            best['odds'][i][j]=d['odds'][i][ks[k]][0,j]
                            best['provider'][i][j]=ks[k]
                        elif best['odds'][i][j]==d['odds'][i][ks[k]][0,j]:
                            best['provider'][i][j]=ks[k]+ ', ' + best['provider'][i][j]
            except:
                a=0
            try:
                best['safe'][i]=1/sum(1./numpy.array(list(best['odds'][i].values())))-1
            except:
                best['safe'][i]=-1
                    
        return best
        
    def show_arbitrage(self):
        for i in self.last['safe']:
            if self.last['safe'][i]>=0:
                print(self.last['name'][i],self.last['safe'][i],self.last['odds'][i],self.last['provider'][i],'\n')
    def compileExchanges(self,comp):
        d={}
        d['name']={}
        d['odds']=vividict()
        d['matchtime']={}
        try:
            Betfair=parseOdds.parseBetfairExchange(comp)
            d['name']=list(set(list(Betfair['events']['name'].values())+list(d['name'])))
        except:
            print("Betfair failed")
        try:
            Smarkets=parseOdds.parseSmarkets(comp)
            d['name']=list(set(list(Smarkets['events']['name'].values())+list(d['name'])))
        except:
            print("Smarkets failed")
        try:
            Matchbook=parseOdds.parseMatchbook(comp)
            d['name']=list(set(list(Matchbook['events']['name'].values())+list(d['name'])))
        except:
            print("Matchbook failed")
        try:
            for i in range(len(Betfair['events']['name'])):
                idx=d['name'].index(Betfair['events']['name'][i])
                d['odds'][idx]['Betfair']=Betfair['events']['odds'][i]
                d['matchtime'][idx]=Betfair['events']['matchtime'][i]
        except:
            print("Betfair failed")
        try:
            for i in range(len(Smarkets['events']['name'])):
                idx=d['name'].index(Smarkets['events']['name'][i])
                d['odds'][idx]['Smarkets']=Smarkets['events']['odds'][i]
                d['matchtime'][idx]=Smarkets['events']['matchtime'][i]
        except:
            print("Smarkets failed")
        try:
            for i in range(len(Matchbook['events']['name'])):
                idx=d['name'].index(Matchbook['events']['name'][i])
                d['odds'][idx]['Matchbook']=Matchbook['events']['odds'][i]
                d['matchtime'][idx]=Matchbook['events']['matchtime'][i]
        except:
            print("Matchbook failed")
        self.last=self.bestodds(d)
        
a=0