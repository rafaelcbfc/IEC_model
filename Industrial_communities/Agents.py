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
from scipy.stats import uniform
import Data
import networkx as nx

### To DO
 ## Drop out of the community should consider the return on investment (a percentage of how much money I received based on how much money I putted back)
 ## Build a small world network -->  Adjust based on the networkx library
 ## Interest rates added to the CBA calculation for considering if joining a community or not
 ## trade certificates --> how many cenrtificates a community generates during the simulation
 ## Drop out rule needs to be well designed --> ROI 


##Variables
#General variables
park_limit = 15 #Size of the park grid layout (15 x 15 squares)
strategy = ["energy generation", "profit increase"] #Energy strategy for industries and communities
energy_demand = uniform.rvs(size=10000, loc = 20, scale=30000) #uniform distribution from 20KWh till 30MWh

def country():
    country.country_selection = "BRA"


#General Variables
country()
if country.country_selection == "AUS":
    gridtariff = Data.AUS_gridtariff #Price paid for KWh for energy from the grid
    solarCosts = random.choice(Data.AUS_solarCosts) #Cost of installation for solar generation
    windCosts = random.choice(Data.AUS_windCosts) #Cost for installation for wind generation

if country.country_selection == "BRA":
    gridtariff = Data.BRA_gridtariff
    solarCosts = random.choice(Data.BRA_solarCosts)
    windCosts = random.choice(Data.BRA_windCosts)

if country.country_selection == "IRA":
    gridtariff = Data.IRA_gridtariff
    solarCosts = random.choice(Data.IRA_solarCosts)
    windCosts = random.choice(Data.IRA_windCosts)

if country.country_selection == "JPN":
    gridtariff = Data.JPN_gridtariff
    solarCosts = random.choice(Data.JPN_solarCosts)
    windCosts = random.choice(Data.JPN_windCosts)

if country.country_selection == "NLD":
    gridtariff = Data.NLD_gridtariff
    solarCosts = random.choice(Data.NLD_solarCosts)
    windCosts = random.choice(Data.NLD_windCosts)

if country.country_selection == "USA":
    gridtariff = Data.USA_gridtariff
    solarCosts = random.choice(Data.USA_solarCosts)
    windCosts = random.choice(Data.USA_windCosts)



#CBA Calculations 
solartariff = 10 #Calculated tariff when producing solar energy
windtariff = 10 #Calculated tariff when producing wind energy
WindThreshold = 5000 #in KW, minimum value to make it a possibility for wind energy production - https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D


#Interaction functions
def askforInvestment(com, member): #for project execution ask for investment to shareholders
    stakeholder_input = 0
    if com.request < member.wealth:
        stakeholder_input = stakeholder_input + com.request
    else:
        pass         
    com.wealth = com.wealth + stakeholder_input
    return com.wealth


def cbaPeer(me, peer): #Peer CBA calculation
    #comb_amount = me.energy_amount + peer.energy_amount
    #me.CBAp = (comb_amount + peer.energy_amount * energy_cost) / (comb_amount * RE_energy_cost + RE_Investment_costs)
    me.CBAp = random.uniform(0.7, 1.2)
    return me.CBAp


def communityName(ind, com): #Assign a member to a community
        ind.which_community = com.name
        return ind.which_community

    
def voting(com, member): #Voting process during meetings
    if com.strategy == member.strategy and com.business_plan == "Feasible":
        member.vote = 1
    else:
        member.vote = -1
    com.voting_result = com.voting_result + member.vote



##Industry
class Industry(Agent): #Industry agent propoerties
    def __init__(self, name, pos, model):
        super().__init__(name, model)
        self.breed = "ind"
        self.CBAi = 0
        self.CBAp = 0
        self.community_loyalty = 0
        self.decision_style = "a"
        self.energy_evaluation_time = 12
        self.energy_time_check = list(range(0,240,self.energy_evaluation_time))
        self.engaged = "not engaged" # not engaged/ engaged / RE installation / Grid energy
        self.eng_lvl = 0
        self.id = name 
        self.i_energy = np.random.choice(energy_demand)  #randomly picks one value from the uniform distribution
        self.motivated_friends = 0
        self.partners = []
        self.period = int(0)
        self.pos = pos
        self.ROI = 0
        self.smallworld_eng = []
        self.strategy = strategy[random.randrange(0,2)] #0 - Increase energy consumption / 1 - reduce costs
        #self.strategy = strategy[0] #0 - Increase energy consumption / 1 - reduce costs 
        self.vote = 0
        self.wealth = 100000000
        self.which_community = 0 
        
        
#Industry functions
#tick actions 
    def step(self):
        self.updateNeighbors()
        self.engagementLevel()
        self.createCommunity()
        self.period = self.period + 1
        #print("I " + str(self.id) + " " + str(self.i_energy) + " " + "C" + str(self.which_community))
        
     
    def cbaCalc(self): #Individial CBA calculation
        #    self.cb = (self.i_energy * energy_cost) / (self.i_energy * RE_energy_cost + RE_Investment_costs)
        self.CBAi = random.uniform(0.4, 1.2)
        return self.CBAi  
    
    
    def createCommunity(self): #create a community
        if self.period in self.energy_time_check:
             self.industryNetwork()
             if self.eng_lvl != 99:
                if self.motivated_friends/len(self.smallworld_eng) >0.5: #Link to scharpf decision style
                  self.eng_lvl = 99
                  for f in self.partners:
                      f.eng_lvl = 99
             if self.which_community == 0: 
                  vicinity_c = self.c_neighbors
                  com = None
                  for com in (com for com in vicinity_c if com.active == "No"): break
                  com.active = "Yes"
                  self.which_community = com.name
                  for f in self.partners:
                      f.which_community = com.name
                        ##Pay for entering community
        else:
            pass
        
    
    def engagementLevel(self): #Define engagement level
        if self.eng_lvl != 99:
            self.cbaCalc()
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
                            cbaPeer(self, c)
                            if self.CBAp > (beta+0.1):
                                self.eng_lvl = 10
                                self.engaged = "engaged"
                                communityName(self, c)
                                ##Pay for entering community
                                break
                            
                #If no communities exists, look for industries
                for i in self.i_neighbors:
                    if self.engaged != "not engaged":
                        pass
                    if self.engaged == "not engaged":
                        cbaPeer(self, i)
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





    def industryNetwork(self): #Small-network definition --to be updated    
                self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=15)
                neighbors_nodes = self.model.grid.get_cell_list_contents(self.neighborhood)
                print(neighbors_nodes)
                vicinity = self.model.G.neighbors(self.id)
                smallworld = [agent for agent in vicinity if type(agent) is Industry]
                for f in smallworld:
                      self.smallworld_eng.append(f.eng_lvl)   
                      if f.eng_lvl == 5 and f.engaged != "engaged":
                          self.partners.append(f)
                          self.motivated_friends =+ 1

           
                  
    def retunofInvestment(self): #Return of Investment function used on voting
        self.ROI = (self.profit -self.investment)/self.investment
    
    
    def updateNeighbors(self): #create a list of neighbors in the Industrial Park
                global c_neighbors, i_neighbors
                self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=10)
                self.neighbors = self.model.grid.get_cell_list_contents(self.neighborhood)
                self.c_neighbors = [x for x in self.neighbors if type(x) is Community]
                self.i_neighbors = [x for x in self.neighbors if type(x) is Industry]
 

##Community
class Community(Agent):
    def __init__(self, name, pos, active, model):
        super().__init__(name, model)
        self.active = active
        self.breed = "com"
        self.business_plan = "" 
        self.c_energy = 0
        self.energy_evaluation_time = 12
        self.energy_time_check = list(range(0,240,self.energy_evaluation_time))
        self.generation = 0
        self.investment = 0
        self.members = 0
        self.name = name
        self.period = 0
        self.plan = 0
        self.pos = pos
        self.project_cost= 0 
        self.plan_execution = "" 
        self.request = 0
        self.solar_energy = 0
        self.stakeholder_input = 0
        self.strategy = strategy[random.randrange(0,2)] #0 - Increase energy consumption / 1 - reduce costs
        self.technology = 0 
        self.voting_result = 0
        self.wealth = 0 
        self.wind_energy = 0
        
        
#Community functions   
    def step(self):
         if self.active == "No":
            pass
         else:
            self.membersList()
            self.initialInvestment()
            self.totalDemand()
            self.technologySelector()
            self.businessPlan()
            self.meetings()
            self.planExecution()
            self.policyEntrepeneur()
            self.project_cost = 0
            self.period = self.period + 1 
            
       
    
    
    def membersList(self): #update every tick the member list
        self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=15)
        self.neighbors = self.model.grid.get_cell_list_contents(self.neighborhood)
        self.neighb = [x for x in self.neighbors if type(x) is Industry]
        self.members = [x for x in self.neighb if x.which_community == self.name]

    
    def initialInvestment(self):#Initial investment by founders
        if self.period == 0:
            self.c_energy = 0
            self.totalDemand()
            self.technologySelector()
            try:
                capital = self.project_cost/len(self.members)  
            except:
                pass
            for member in self.members:
                member.wealth = member.wealth - capital
                self.wealth = self.wealth + capital
     
        
    def totalDemand(self): #Demand evaluation every tick
       for member in self.members:
           self.c_energy = self.c_energy + member.i_energy
 
    
    def technologySelector(self): #technology definition based on energy demand
        coef = self.c_energy/WindThreshold
        if coef < 1:
            self.technology = "Solar"
            self.solar_energy = self.c_energy
            self.wind_energy = 0
        
        if coef > 1:
            if self.strategy == 0:
                self.technology = "Mixed"
                self.wind_energy = int(self.c_energy/WindThreshold)*WindThreshold
                self.solar_energy = self.c_energy % WindThreshold
            
            if self.strategy == 1:
                self.technology = "Mixed" 
                #Scenario 1 = all solar
                solar_s1 = self.c_energy
                pc_s1 = solar_s1 * solarCosts
                #Scenario 2 = Mixed
                wind_s2 = int(self.c_energy/WindThreshold)*WindThreshold
                solar_s2= self.c_energy % WindThreshold
                pc_s2 = wind_s2 * windCosts + solar_s2 * solarCosts 
                pc = max(pc_s1, pc_s2)
                if pc == pc_s1:
                    self.solar_energy = self.c_energy
                    self.wind_energy = 0
                if pc == pc_s2:
                    self.wind_energy = int(self.c_energy/WindThreshold)*WindThreshold
                    self.solar_energy = self.c_energy % WindThreshold
        
        self.project_cost = (self.wind_energy * windtariff + windCosts) + (self.solar_energy * solartariff + solarCosts)    

        
    def businessPlan(self):
        if self.project_cost < self.wealth:
            self.business_plan = "Feasible"
        if self.project_cost > self.wealth:
            self.investment = self.project_cost - self.wealth
            self.askRevenue()
            if self.wealth > self.project_cost: #Check if stakeholder investment approved the business plan
                self.business_plan = "Feasible"
            else:
                self.business_plan = "Unfeasible"   
     
        
    def askRevenue(self): #Ask for revenue if wealth is below 0
        try:
            self.request = self.investment / len(self.members)
        except:
            pass
            pass
        for member in self.members:
           askforInvestment(self, member)
        return self.wealth
    
        
    def meetings(self): #Schedule a meeting with its members
        self.volting_result = 0 
        for member in self.members:
             voting(self, member)
        if self.voting_result > 0:
            self.plan_execution = "Approved"
        else:
            self.plan_execution = "Rejected"
       
        
    def planExecution(self):
        if self.plan_execution == "Approved":
            self.wealth = self.wealth - self.project_cost
            solar_revenue = self.solar_energy * solartariff
            wind_revenue = self.wind_energy * windtariff
            self.wealth = self.wealth + solar_revenue + wind_revenue
            print("A")    
        if self.plan_execution == "Rejected":
            print("B")
        
    
    def policyEntrepeneur(self): #report to government how each period was compared to the past one
        pass
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        