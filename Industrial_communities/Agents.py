#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rafael

@Address: https://github.com/rafaelcbfc/InCES_model/blob/master/Industrial_communities/Agents.py

"""
###Model agents
##Imports
import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities")
import random
import numpy as np
from mesa import Agent

 ## Drop out of the community should consider the return on investment (a percentage of how much money I received based on how much money I putted back)
 ## Build a small world network --> See virus simulation --> neighbours influence on decision to join community
 ## Number of industries & capacity of members are important to initiate a community. High capacity investment to start a community.
 ## Initial investment =! 0 
 ## Explicit assumption on the grid already existing
 ## Interest rates added to the CBA calculation for considering if joining a community or not
 ## Cost per MWh


##Variables
#General variables
#park_limit = np.random.choice(range(10,20,1))
park_limit = 15
strategy = ["energy", "costs", "A", "B"]
counter = 0
n_industries = 10
n_communities = 10
#General Variables
#energy_cost = random.randrange(100, 270, 5) #Random range, to be based on country
#RE_energy_cost = random.randrange(80, 200, 5) #Based on countries
#RE_costs = random.randrange(10000, 50000, 100)

#Game Theory
#Decision style = for each country, normal distribution with center on countries valueRafa!

#Agents functions
def CBA():
    #    self.cb = (self.i_energy * energy_cost) / (self.i_energy * RE_energy_cost + RE_costs)
    CBA = random.uniform(0.4, 1.2)
    return CBA


def CBA_peer(me, peer): #Peer CBA calculation
    #comb_amount = me.energy_amount + peer.energy_amount
    #me.CBAp = (comb_amount + peer.energy_amount * energy_cost) / (comb_amount * RE_energy_cost + RE_costs)
    me.CBAp = random.uniform(0.7, 1.2)
    return me.CBAp


def community_name(me, peer):
        me.which_community = peer.name
        return me.which_community

    
def voting(com, member):
    pass


##Industry
class Industry(Agent):
    def __init__(self, name, pos, model):
        super().__init__(name, model)
        self.id = name
        self.pos = pos
        self.breed = "ind"
        self.i_energy =  np.random.choice(range(100, 210, 10))  #Use random range see Mesa literature -- to be updated every period
        #self.strategy = strategy[0] #0 - Increase energy consumption / 1 - reduce costs
        self.strategy = strategy[random.randrange(0,4)] #0 - Increase energy consumption / 1 - reduce costs
        self.engaged = "not engaged" # not engaged/ engaged / RE installation / Grid energy
        self.eng_lvl = 0
        self.which_community = 0
        self.community_loyalty = 0
        self.period = int(0)
        self.energy_evaluation_time = 2
        self.energy_time_check = list(range(0,240,self.energy_evaluation_time))
        self.CBAi = 0
        self.CBAp = 0
        self.decision_style = "a"
        self.motivated_friends = 0
        self.smallworld_eng = []
        self.partners = []
            
    #Industry functions
     #tick actions 
    def step(self):
        self.update_neighbors()
        self.engagementlevel()
        self.createcommunity()
        self.period = self.period + 1
        #print("I " + str(self.id) + " " + str(self.i_energy) + " " + "C" + str(self.which_community))
        
        
    def update_neighbors(self): #create a list of neighbors in the Industrial Park
            global c_neighbors, i_neighbors
            self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=10)
            self.neighbors = self.model.grid.get_cell_list_contents(self.neighborhood)
            self.c_neighbors = [x for x in self.neighbors if type(x) is Community]
            self.i_neighbors = [x for x in self.neighbors if type(x) is Industry]
            
    
    def industrynetwork(self):
        self.small_network = self.model.grid.get_neighborhood(self.pos, moore=True, radius=5)
        self.smallworld = self.model.grid.get_cell_list_contents(self.small_network)
        self.ind_smallworld = [x for x in self.smallworld if type(x) is Industry]
        for f in self.ind_smallworld:
              self.smallworld_eng.append(f.eng_lvl)   
              if f.eng_lvl == 5 and f.engaged != "engaged":
                  self.partners.append(f)
                  self.motivated_friends =+ 1
            
            
    def CBA_calc(self): #Individial CBA calculation
        self.CBAi = CBA()
        return self.CBAi
        
    
    def engagementlevel(self): #Define engagement level
        if self.eng_lvl != 99:
            self.CBA_calc()
            beta = 0.8 #Pareto 80% principle
            if self.CBAi < (beta-0.3):
                self.eng_lvl = 1
                self.engaged = "Grid Energy"
            elif self.CBAi > (beta+0.3):
                self.eng_lvl = 3
                self.engaged = "RE installation"
            elif self.CBAi > (beta-0.3) and self.CBAi < (beta+0.3):
                #Check if there is a community nearby
                for c in self.c_neighbors:
                    if c.active == "No":
                        pass
                    if c.active == "Yes":
                        if c.strategy == self.strategy:
                            CBA_peer(self, c)
                            if self.CBAp > (beta+0.1):
                                self.eng_lvl = 10
                                self.engaged = "engaged"
                                community_name(self, c)
                                break
                            
                #If no communities exists, look for industries
                for i in self.i_neighbors:
                    if self.engaged != "not engaged":
                        pass
                    if self.engaged == "not engaged":
                        CBA_peer(self, i)
                        if i.CBAi < (beta+0.1) and i.CBAi > (beta-0.1):
                            if self.CBAp < (beta-0.3):
                                self.eng_lvl = 2
                                self.engaged == "not engaged"
                            if self.CBAp > (beta - 0.3) and self.CBAp < (beta + 0.3):
                                self.eng_lvl = 4
                                self.engaged == "not engaged"
                            if self.CBAp > (beta+0.3):
                                self.eng_lvl = 5
                                self.engaged = "enthusiast"
      
        
    def createcommunity(self): #create a community
        if self.period in self.energy_time_check:
             self.industrynetwork()
             if self.eng_lvl != 99:
                if self.motivated_friends/len(self.smallworld_eng) >0.5: #Link to scharpf decision style
                  self.eng_lvl = 99
                  for f in self.partners:
                      f.eng_lvl = 99
             if self.which_community == 0: 
                  vicinity_c = self.c_neighbors
                  com = None
                  for com in (x for x in vicinity_c if x.active == "No"): break
             com.active = "Yes"
             self.which_community = com.name
             for f in self.partners:
                 f.which_community = com.name
        else:
            pass
      
        
    def community_member_role(self): #interact with Community
        voting()
 
 
##Community
class Community(Agent):
    def __init__(self, name, pos, model):
        super().__init__(name, model)
        self.pos = pos
        self.breed = "com"
        self.wealth = 0
        self.c_energy = 0
        #self.strategy = strategy[0]
        self.strategy = strategy[random.randrange(0,3)] #0 - Increase energy consumption / 1 - reduce costs
        self.active = "No"
        self.name = name
        self.CBAc = 0
        self.members = 0
        self.memberlist = []
        
#Community functions   
    def step(self):
        self.CBA_calc()
        self.meeting_schedule()
        self.ask_revenue()
        self.businessPlan()
        self.executePlan()
        self.PolicyEntrepeneur()
    
     
    def CBA_calc(self): #Individial CBA calculation
        self.CBAc = CBA()
        return self.CBAc
    
    
    def meeting_schedule(self): #Schedule a meeting with its members
         self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=10)
         self.neighbors = self.model.grid.get_cell_list_contents(self.neighborhood)
         self.neighb = [x for x in self.neighbors if type(x) is Industry]
         self.members = [x for x in self.neighb if x.which_community == self.name]
         
         for x in self.members:
             voting(self, x)
     
        
    def ask_revenue(self): #Ask for revenue if wealth is below 0
        if self.wealth < 0:
            for x in self.members:
                pass
    
    
    def businessPlan(self):
        #Insert Sum of energy demand by its members
        for x in self.members:
            self.c_energy = self.c_energy + x.i_energy      

    
    def executePlan(self): #Execute the business plan having profit or loss
        pass
    
    
    def PolicyEntrepeneur(self): #report to government how each period was compared to the past one
        pass
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        