#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rafael Costa
@Addess: #https://github.com/rafaelcbfc/Thesis.git

"""
###Model creation
##Imports
import sys
sys.path.append('/Users/rafael/Google Drive/00 - Thesis/03 - Dataset/Python/Industrial_communities')
import itertools
from random import shuffle
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from Agents import Industry, Community

##Variables
#Model variables
width = 15
height = 15
max_ind_size = 100
max_com_size = 100
total = width * height
 
#Geographical locations 
x = [i for i in range(width)]
y = [i for i in range(height)]
geo = list(itertools.product(x,y))
shuffle(geo)
geo_i = geo[:max_ind_size]
geo_c = geo[max_ind_size:]
 

##Model functions
def countIndustry(model):
        n_ind =  sum([1 for a in model.schedule.agents if type(a) == Industry])
        return n_ind

def countCommunity(model):
        n_com =  sum([1 for a in model.schedule.agents if type(a) == Community])
        return n_com
    
def countActive(model):
        n_act =  sum([1 for a in model.schedule.agents if type(a) == Community and a.active == "Yes"])
        return n_act
    
##Model Definitions
class Modelrun(Model):
    def __init__(self, n_industries, n_communities, max_ticks = 240):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.n_industries = n_industries
        self.n_communities = n_communities
        self.width = width
        self.height = height
        self.grid = MultiGrid(self.width, self.height, torus=True)
        self.max_ticks = max_ticks
        self.model_reporters = {'Communities': lambda m: countCommunity(m),
                                'Active Communities': lambda m: countActive(m),
                                'Industries': lambda m: countIndustry(m)}
        self.agent_reporters = {'WhichCommunity': lambda i: getattr(i, "which_community", None)}        
        self.datacollector = DataCollector(model_reporters = self.model_reporters) #Not working as expected
        self.running = True
        self.datacollector.collect(self)
        self.tick = 0

        
        #Add industries        
        for i in range(self.n_industries):
            ind = Industry(i, geo_i[i], self)
            self.schedule.add(ind)
            self.grid.place_agent(ind, geo_i[i])
            
         #Add community       
        for c in range(self.n_communities):
            com = Community(c, geo_c[c], self)
            com.active = "No"
            self.schedule.add(com)
            self.grid.place_agent(com, geo_c[c])  
        self.datacollector.collect(self)
        
    def step(self): #what is done each step on the simulation
                self.datacollector.collect(self)
                self.schedule.step()
                self.tick += 1
                if self.tick >= self.max_ticks:
                    self.running = False


