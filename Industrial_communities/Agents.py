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


### To DO
 ## Drop out of the community should consider the return on investment (a percentage of how much money I received based on how much money I putted back)
 ## trade certificates --> how many cenrtificates a community generates during the simulation
 ## Drop out rule needs to be well designed --> ROI 


##Variables
#General variables
park_limit = 15 #Size of the park grid layout (15 x 15 squares)
wind_threshold = 5000 #in KW, minimum value to make it a possibility for wind energy production - https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2019/May/IRENA_Renewable-Power-Generations-Costs-in-2018.pdf?la=en&hash=99683CDDBC40A729A5F51C20DA7B6C297F794C5D
pareto = 1 
margin = 0.2 #Pareto 80% principle
depreciation_period= 20 #years
pool_financial_investments = ["feed-in-tariff", "tax-incentive", "tradable-certificates"]
pool_countries = ["AUS", "BRA", "IRA", "JPN", "NLD", "USA"]

#General Variables
financial_investment = "tax-incentive"
country = "BRA"
decision_style = Data.BRADecision_style_mean 
decision_rule = Data.BRADecision_rule_mean

#Interaction functions
def askforInvestment(com, member): #for project execution ask for investment to shareholders
    stakeholder_input = 0
    if com.request < member.wealth:
        stakeholder_input = stakeholder_input + com.request
    else:
        pass         
    com.wealth = com.wealth + stakeholder_input
    return com.wealth


def cbaCalc(me, peer = None): #CBA calculation
    me.CBAp = 0
    if peer != None:
        demand = (me.energy + peer.energy) * 12 #yearly
    else:
        demand = me.energy * 12 #yearly   
    solar_implement_Costs = Data.BRA_solarCosts
    wind_implement_Costs = Data.BRA_windCosts
    gridtariff = Data.BRA_gridtariff
    discount_rate = Data.BRA_discount_rate
    solar_OM = Data.BRA_solar_OM
    wind_OM = Data.BRA_wind_OM
   
    #baseline
    NPV_baseline = 0
    for i in range(depreciation_period):
        NPV_baseline = NPV_baseline + ((demand * gridtariff)/(1+discount_rate)**(i*12))
        
    #renewable energy 
    coef = demand/wind_threshold
    #Scenario 1 = Strategy 0, solar energy
    if coef < 1:
        wind_energy_s1 = 0
        wind_tariff_s1 = 0
        wind_OM_s1 = 0
         
        solar_energy_s1 = demand
        investment_solar_s1 = solar_energy_s1 * solar_implement_Costs
    
        if financial_investment == "tax-incentive":
            solar_implement_Costs = solar_implement_Costs * 0.6
            wind_implement_Costs = wind_implement_Costs * 0.6
   
        solar_tariff_s1 = investment_solar_s1/(solar_energy_s1 * depreciation_period)
        solar_OM_s1 = solar_OM * solar_tariff_s1
        
        NPV_investment = 0
        for i in range(depreciation_period):
            NPV_investment = NPV_investment + ((wind_energy_s1 * (wind_tariff_s1) - wind_OM_s1) + 
                                             (solar_energy_s1 * (solar_tariff_s1 - solar_OM_s1))) /((1+discount_rate)**(i*12))
        
    #Scenario 2 = Strategy 0, mixed energy
    if coef > 1:
        wind_energy_s2 = int(demand/wind_threshold)*wind_threshold
        investment_wind_s2 = wind_energy_s2 * wind_implement_Costs
    
        solar_energy_s2 = demand % wind_threshold
        investment_solar_s2 = solar_energy_s2 * solar_implement_Costs 
    
        if financial_investment == "tax-incentive":
            solar_implement_Costs = solar_implement_Costs * 0.6
            wind_implement_Costs = wind_implement_Costs * 0.6
    
        wind_tariff_s2 = (investment_wind_s2/(wind_energy_s2 * depreciation_period))
        solar_tariff_s2 =  (investment_solar_s2/(solar_energy_s2 * depreciation_period))
        wind_OM_s2 = wind_OM * wind_energy_s2
        solar_OM_s2 = solar_OM * solar_tariff_s2
    
        NPV_investment = -(solar_implement_Costs + wind_implement_Costs)
        for i in range(depreciation_period):
            NPV_investment = NPV_investment + ((wind_energy_s2 * (wind_tariff_s2) - wind_OM_s2) + 
                                             (solar_energy_s2 * (solar_tariff_s2 - solar_OM_s2))) /((1+discount_rate)**(i*12))
            
    if (NPV_baseline / NPV_investment) > 1:
        me.CBA = "favorable"
    elif (NPV_baseline / NPV_investment) < 1 - margin:
        me.CBA = "unfavorable"
    else:
        me.CBA = "approximate"
    #print(NPV_baseline / NPV_investment)
    return me.CBA


def communityName(ind, com): #Assign a member to a community
        ind.which_community = com.name
        
    
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
        self.cb = 0
        self.CBA = 0
        self.community_loyalty = 0
        self.decision_style = decision_style
        self.decision_rule = decision_rule
        self.energy = np.random.choice(uniform.rvs(size=10000, loc = 20, scale=3000)) #value in KWh from a distribution between 20KWh and 6MWh
        self.energy_evaluation_time = 12
        self.energy_time_check = list(range(0,240,self.energy_evaluation_time))
        self.engaged = "not_engaged" # not engaged/ engaged / RE installation / Grid energy
        self.eng_lvl = 0
        self.id = name 
        self.motivated_friends = 0
        self.partners = []
        self.period = int(0)
        self.pos = pos
        self.ROI = 0
        self.smallworld = []
        self.strategy = random.randrange(0,2) #0 - "energy generation" / 1 - "profit increase"
        self.vote = 0
        self.wealth = 100000000
        self.which_community = 0 
        
        
#Industry functions
#tick actions 
    def step(self): #Action per tick
        self.updateNeighbors()
        self.engagementLevel()
        self.createCommunity()
        self.joinCommunity()
        self.period = self.period + 1
       
    
    def createCommunity(self): #create a community
        if self.period in self.energy_time_check and self.eng_lvl == 5:
            self.industryNetwork()
            if self.eng_lvl == 99 and self.which_community == 0: 
                for com in [x for x in self.c_neighbors if x.active == "No"]: break
                com.active = "Yes"
                self.which_community = com.name
                for f in self.smallworld:
                    if f.id in self.partners:
                        f.which_community = com.name
                       ##Pay for entering community
        
    
    def engagementLevel(self): #Define engagement level of each industry
        if self.period in self.energy_time_check:
            if self.eng_lvl in [0, 1, 2, 3, 4, 5]:
                cbaCalc(self)
                if self.CBA == "unfavorable":
                    self.eng_lvl = 1
                    self.engaged = "Grid_Energy"
                elif self.CBA == "favorable":
                    self.eng_lvl = 3
                    self.engaged = "RE installation" 
                elif self.CBA == "approximate":
                    #Check if there is a community to join
                        for c in self.c_neighbors:
                            if self.eng_lvl not in [10, 99]:
                                if c.active == "No":
                                    pass
                                if c.active == "Yes":
                                    if c.strategy == self.strategy:
                                        cbaCalc(self, c)
                                        if self.CBA == "favorable":
                                            self.eng_lvl = 10
                                            self.engaged = "member"
                                            self.which_community == c.name
                                            self.wealth = self.wealth - (c.fee * self.energy)
                                            c.wealth = c.wealth + (c.fee * self.energy)
                                            break
                        
                        #If no communities exists, look for industries
                        for i in self.i_neighbors:
                            if self.eng_lvl not in [1, 10, 99]:
                                cbaCalc(self, i)
                                if self.CBA == "unfavorable":
                                    self.eng_lvl = 2
                                    self.engaged == "not_engaged"
                                if self.CBA == "favorable" or "approximate":
                                    self.eng_lvl = 5
                                    self.engaged = "enthusiast"
            print(" id " + str(self.id) + " eng_lvl " + str(self.eng_lvl))

    def joinCommunity(self):
            pass
                #print("3 id2 " + str(self.id) + " eng_lvl " + str(self.eng_lvl) + " com " + str(self.which_community))
            #pay to enter
            #calculate a ROI
                

            
    def industryNetwork(self): 
        self.smallworld = []    
        neighbors = [agent for agent in self.i_neighbors if type(agent) == Industry]
        vicinity = list(self.model.G.neighbors(self.id))
        self.smallworld = [agent for agent in neighbors if agent.id in vicinity]
        for f in self.smallworld:
            if f.engaged == "enthusiast":
                self.partners.append(f.id)
        if len(self.partners) > 0 and len(self.partners)/len(self.smallworld) >= 0.5: 
            self.eng_lvl = 99
            for f in self.smallworld:
                if f.id in self.partners:
                    f.eng_lvl = 99

                  
    def retunofInvestment(self): #Return of Investment function used on voting
        self.ROI = (self.profit -self.investment)/self.investment
        ## how to deal with dividends
    
    def updateNeighbors(self): #create a list of neighbors in the Industrial Park
        global c_neighbors, i_neighbors
        self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=20)
        self.neighbors = self.model.grid.get_cell_list_contents(self.neighborhood)
        self.c_neighbors = [x for x in self.neighbors if type(x) is Community]
        self.i_neighbors = [x for x in self.neighbors if type(x) is Industry]
 

##Community
class Community(Agent):
    def __init__(self, name, pos, activity, model):
        super().__init__(name, model)
        self.active = activity
        self.breed = "com"
        self.business_plan = "" 
        self.energy = 0
        self.energy_evaluation_time = 12
        self.energy_time_check = list(range(0,240,self.energy_evaluation_time))
        self.fee = 0
        self.generation = 0
        self.invested_capital = 0
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
        self.strategy = random.randrange(0,2) # 0 - "energy generation" / 1 - "profit increase"
        self.technology = 0 
        self.voting_result = 0
        self.wealth = 0 
        self.wind_energy = 0
        
        
#Community functions   
    def step(self):
         if self.active == "Yes":
            self.membersList()
            self.initialInvestment()
            self.totalDemand()
            self.technologySelector()
            self.businessPlan()
            self.meetings()
            self.planExecution()
            self.policyEntrepeneur()
            self.project_cost = 0
            self.newMemberFee()
            self.period = self.period + 1 
         else:
            pass
            
       
    def newMemberFee(self):
        self.fee = self.invested_capital / self.energy
    
    
    def membersList(self): #update every tick the member list
        self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=15)
        self.neighbors = self.model.grid.get_cell_list_contents(self.neighborhood)
        self.neighb = [x for x in self.neighbors if type(x) is Industry]
        self.members = [x for x in self.neighb if x.which_community == self.name]
        print(len(self.members))
        if len(self.members) == 0:
            self.active = "No" 

    
    def initialInvestment(self):#Initial investment by founders
        if self.active == 'Yes' and self.period == 0:
            self.totalDemand()
            self.technologySelector()
            self.invested_capital = self.project_cost/len(self.members)  
            for member in self.members:
                try:
                    member.wealth = member.wealth - self.invested_capital
                except:
                    print("no cash" + str(member.id))
                self.wealth = self.wealth + self.invested_capital
  
        
    def totalDemand(self): #Demand evaluation every tick
        for member in self.members:
           self.energy = (self.energy + member.energy) * 1.1
           print(self.energy)
 
   
    def technologySelector(self): #technology definition based on energy demand  ##--> adjust demand to already implemented energy
        coef = self.energy/wind_threshold
        solar_implement_Costs = Data.BRA_solarCosts
        wind_implement_Costs = Data.BRA_windCosts
        solar_OM = Data.BRA_solar_OM
        wind_OM = Data.BRA_solar_OM
        
        if financial_investment == "tax-incentive":
            solar_implement_Costs = solar_implement_Costs * 0.6
            wind_implement_Costs = wind_implement_Costs * 0.6
       
        if coef < 1:
            self.technology = "Solar"
            solar_energy = self.energy
            wind_energy = 0
        
        if coef > 1:
            if self.strategy == 0:
                self.technology = "Mixed"
                wind_energy = int(self.energy/wind_threshold)*wind_threshold
                solar_energy = self.energy % wind_threshold
            
            if self.strategy == 1:
                self.technology = "Mixed" 
                #Scenario 1 = all solar
                solar_s1 = self.energy
                pc_s1 = solar_s1 * solar_implement_Costs
                #Scenario 2 = Mixed
                wind_s2 = int(self.energy/wind_threshold)*wind_threshold
                solar_s2= self.energy % wind_threshold
                pc_s2 = wind_s2 * wind_implement_Costs + solar_s2 * solar_implement_Costs 
                pc = max(pc_s1, pc_s2)
                if pc == pc_s1:
                    wind_energy = 0
                    solar_energy = self.energy
                if pc == pc_s2:
                    wind_energy = int(self.energy/wind_threshold)*wind_threshold
                    solar_energy = self.energy % wind_threshold
       
        investment_wind = wind_energy * wind_implement_Costs
        investment_solar = solar_energy * solar_implement_Costs 
        wind_tariff = (investment_wind/(wind_energy * depreciation_period))
        solar_tariff =  (investment_solar/(solar_energy * depreciation_period))
        wind_OM = wind_OM * wind_energy
        solar_OM = solar_OM * solar_tariff
        
        self.project_cost = ((wind_energy * wind_tariff)- wind_OM + wind_implement_Costs) + ((solar_energy * (solar_tariff - solar_OM)) + solar_implement_Costs)    

        
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
            solar_revenue = self.solar_energy * 0.05
            wind_revenue = self.wind_energy * 0.11
            self.wealth = self.wealth + solar_revenue + wind_revenue
            self.invested_capital = self.invested_capital + self.project_cost
            print("A")    
        if self.plan_execution == "Rejected":
            print("B")
        
    
    def policyEntrepeneur(self): #report to government how each period was compared to the past one
        pass
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        