#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rafael Costa
@Addess: #https://github.com/rafaelcbfc/InCES_model.git

"""
###Model creation
##Imports
import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import itertools
from random import shuffle
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from Agents import Industry, Community
import networkx as nx


##Variables
#Model variables
width = 15
height = 15
max_ind_size = 100
total = width * height
 

#Industrial Park geo-location
x = [i for i in range(width)]
y = [i for i in range(height)]
geo = list(itertools.product(x,y))
shuffle(geo)
geo_i = geo[:max_ind_size]
geo_c = geo[max_ind_size:]

##Evaluations metrics
def countIndustry(model): #Total number of industries
    n_ind =  [a for a in model.schedule.agents if type(a) == Industry]
    return len(n_ind)

def countCommunity(model): #Total communities placed on grid
    n_com =  [b for b in model.schedule.agents if type(b) == Community]
    return len(n_com)
    
def countActive(model): #Acitve communities per simulation run
    n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
    return len(n_act)

def countEntrepeneurrole(model): #Entrepreneur feedback to government
    n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
    n_policy = 0
    for c in n_act:
        n_policy = n_policy + int(c.policy_entrepreneur)
    return n_policy

def communityMembers(model): #Number of industries linked to the communities
    n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
    n_members = 0
    for c in n_act:
        n_members = n_members + int(len(c.members))
    return n_members

def totalEnergyProduced(model): #Total renewable energy produced by all communities
    n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
    n_energy = 0
    for c in n_act:
        n_energy = n_energy + int(c.energy_total_total)
    return n_energy

def solarEnergyProduced(model): #Total solar energy produced by all communities
    n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
    n_solar = 0
    for c in n_act:
        n_solar = n_solar + int(c.energy_total_solar)
    return n_solar

def windEnergyProduced(model): #Total wind energy produced by all communities
    n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
    n_wind = 0
    for c in n_act:
        n_wind = n_wind + int(c.energy_total_wind)
    return n_wind

def exitMembers(model): #Number of industries which exited a community
     n_ind =  [a for a in model.schedule.agents if type(a) == Industry]
     n_exit = 0
     for i in n_ind:
         n_exit = n_exit + int(i.exit)
     return n_exit

def investedCapital(model): #Total amount invested in renewable projects
     n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
     n_costs = 0
     for c in n_act:
         n_costs = n_costs + int(c.costs)
     return n_costs 

def investedCapitalInd(model): #Total amount invested by industries
     n_ind =  [a for a in model.schedule.agents if type(a) == Industry]
     n_invested = 0
     for i in n_ind:
         n_invested = n_invested + int(i.invested)
     return n_invested   

def incentiveFit(model): #Amount spent by government on FIT 
     n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
     n_fit = 0
     for c in n_act:
         n_fit = n_fit + int(c.incentive_fit)
     return n_fit 
 
def incentiveTax(model): #Amount spent by government on Tax incentives
     n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
     n_tax = 0
     for c in n_act:
         n_tax = n_tax + int(c.incentive_tax)
     return n_tax

def incentiveTGC(model):#Amount spent by government on TGC
     n_act =  [c for c in model.schedule.agents if type(c) == Community and c.active == 1]
     n_tgc = 0
     for c in n_act:
         n_tgc = n_tgc + int(c.incentive_tgc)
     return n_tgc
    
##Model Definitions
class Modelrun(Model):
    def __init__(self, n_communities, n_industries, max_ticks = 240):
        super().__init__()
        self.width = width
        self.height = height
        self.G = nx.watts_strogatz_graph(n_industries, 4, 0.2)
        self.grid = MultiGrid(self.width, self.height, torus = True)
        self.max_ticks = max_ticks        
        self.datacollector = DataCollector(model_reporters={
                                           "Communities": countCommunity,
                                           "ActiveCommunities": countActive,
                                           "Industries": countIndustry,
                                           "Community Members": communityMembers,
                                           "Total Energy communities": totalEnergyProduced,
                                           "Solar Energy": solarEnergyProduced,
                                           "Wind Energy": windEnergyProduced,
                                           "Member exit": exitMembers,
                                           "Community Invested":investedCapital,
                                           "Industry Investments": investedCapitalInd,
                                           "Governmental FIT incentive": incentiveFit,
                                           "Governmental TAX incentive": incentiveTax,
                                           "Governmental TGC incentive": incentiveTGC,
                                           "Policy Entrepreneur": countEntrepeneurrole})
        
        self.n_industries = n_industries
        self.n_communities = n_communities
        self.running = True
        self.schedule = RandomActivation(self)
        self.tick = 0    
        self.network = []
        
            
        #Add industries        
        for i in range(self.n_industries):
            ind = Industry(i, geo_i[i], self)
            self.schedule.add(ind)
            self.grid.place_agent(ind, geo_i[i])
            self.network.append(ind)
        
        #Add community       
        for c in range(self.n_communities):
            com = Community(c, geo_c[c], 0, self)
            self.schedule.add(com)
            self.grid.place_agent(com, geo_c[c])  

        
    def step(self): #what is done each step on the simulation
            self.datacollector.collect(self)
            self.schedule.step()
            self.tick += 1
            if self.tick >= self.max_ticks:
                self.running = False

