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
import Data
import random
import numpy as np
from mesa import Agent
from scipy.stats import uniform


##Variables
#General variables
gridtariff = float(random.choice(Data.gridtariff))
decision_style = Data.decision_style 
decision_rule = Data.decision_rule


## Interaction functions
def askforInvestment(com, member): #for project execution ask for investment to shareholders
    com.moeny = com.money + com.request
    member.invested = member.invested + com.request
    member.loyalty = member.loyalty - 1
 
       
def voting(com, member): #Voting process during meetings
    if com.strategy == 0:
        if com.project_tariff0 < gridtariff and com.business_plan == "Feasible":
            member.vote = 1
        else: member.vote = 0
    
    elif com.strategy == 1:
        if com.project_margin >= member.expected_return and com.business_plan == "Feasible":
            member.vote = 1
        else: member.vote = 0
    
    com.voting_result  = com.voting_result + member.vote
    member.community_vote = com.voting_result / len(com.members)   
    
    
##Industry
class Industry(Agent): #Industry agent propoerties
    def __init__(self, name, pos, model):
        super().__init__(name, model)
        self.aff = []
        self.cba_lvl = 0
        self.cba_lvlc = 0
        self.cba_lvlp = 0
        self.com_premium = 0
        self.community_vote = 0
        self.decision_style = random.choice(decision_style)
        self.decision_rule = random.choice(decision_rule)
        self.energy = 0
        self.eng_lvl = 0
        self.exit = 0
        self.expected_return = random.uniform(0, 0.05) # -------> Check value
        self.friends = []
        self.id = name 
        self.invested = 0
        self.LCOE = 0
        self.loyalty = 0
        self.max_re = 0
        self.payment = 0
        self.period = 0
        self.pos = pos
        self.ROI = 0
        self.retrn = 0
        self.energy_rtn = 0
        self.smallworld = []
        self.strategy = random.randrange(0,2) #0 - "energy generation" / 1 - "profit increase"
        self.threshold = 12
        self.vote = 0
        self.which_community = 0 
       
        
#Industry functions
#tick actions 
    def step(self): #Action per tick
        self.updateNeighbors()
        self.energyLevel()
        self.engagementLevel()
        self.createCommunity()
        self.returnofInvestment()
        self.leaveCommunity()
        self.period = self.period + 1
        
 
    def updateNeighbors(self): #create a list of nglobal c_neighbors, i_neighbors
        self.neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=20)
        self.neighbors = self.model.grid.get_cell_list_contents(self.neighborhood)
        self.c_neighbors = [x for x in self.neighbors if type(x) is Community]
        self.i_neighbors = [x for x in self.neighbors if type(x) is Industry]      
        
    
    def energyLevel(self):  #value in KWh from a distribution between 200KWh and 30MWh
            self.energy = float(np.random.choice(uniform.rvs(size=10000, loc = 200, scale=30000)))     

    
    def engagementLevel(self): #Define engagement level of each industry
        if self.eng_lvl not in [3, 4, 5]:
                Data.cbaCalc(self)
                if self.cba_lvl in [1, 2, 3]:
                    if self.cba_lvl == 1:
                        self.eng_lvl = 1
                    if self.cba_lvl in [2,3]:
                            for community in self.c_neighbors: #Search for a community to join
                                if community.active == 1:
                                    Data.cbaCalcCom(self, community)
                                    if self.cba_lvlc == 1:
                                        self.eng_lvl = 4
                                        self.which_community = community.name
                                        community.members.append(self)
                                        self.joinCommunity()
                                        break
                                    
                    if self.eng_lvl not in [1, 4, 5]:
                            for neighbor in self.i_neighbors: #If no communities exists, look for industries
                                Data.cbaCalcPeer(self, neighbor)
                                if self.cba_lvlp == 1:
                                        self.eng_lvl = 2
                                if self.cba_lvlp == 2:
                                        self.eng_lvl = 3
                                        neighbor.eng_lvl = 3
                                        self.strategy = 0
                                        neighbor.strategy = 0
                                        break
                                if self.cba_lvlp == 3:
                                        self.eng_lvl = 3
                                        neighbor.eng_lvl = 3
                                        self.strategy = 1
                                        neighbor.strategy = 1
                                        break
        else:
            pass
        
            
    def createCommunity(self): #create a community
        if self.eng_lvl == 3:
            self.industryNetwork()
            if self.eng_lvl == 5 and self.which_community == 0: 
                for community in [x for x in self.c_neighbors if x.active == 0]: break
                self.which_community = community.name
                community.members.append(self)
                community.strategy = self.strategy
                community.active = 1
                for f in self.smallworld:
                    if f.eng_lvl == 5: 
                       f.which_community = community.name
                       community.members.append(f)
    
               
    def industryNetwork(self): #Define the strong network
        self.smallworld = []    
        neighbors = [agent for agent in self.i_neighbors if type(agent) == Industry]
        vicinity = list(self.model.G.neighbors(self.id))
        self.smallworld = [agent for agent in neighbors if agent.id in vicinity]
        for f in self.smallworld:
            if f.eng_lvl == 3:
                self.friends.append(f.id)
            if f.eng_lvl == 4:
                self.aff.append(f.id)
        if len(self.friends) > 0 and len(self.friends + self.aff)/len(self.smallworld) >= 0.5: 
            self.eng_lvl = 5
            for f in self.smallworld: # and f.which_community == 0:
                if f.id in self.friends:
                    f.eng_lvl = 5
    
        
    def joinCommunity(self): #Pay to join a community
        if self.com_premium == 0:
            self.invested = self.invested + self.energy * gridtariff
        else:
            self.invested =  self.invested + self.energy + self.com_premium
        
              
    def returnofInvestment(self): #Return of Investment function used on voting
        if self.which_community != 0:
            if self.com_premium == 0 or self.invested == 0: 
                pass
            else: self.ROI = self.retrn / self.invested 
        else: pass
 
    
    def decisionStyle(self): #Comparisson between what I voted with what the community members voted
        ratio = self.community_vote
        if self.decision_style <= 33: #Unanimity
            if ratio >=0.8:
                self.loyalty = self.loyalty + 1
            if ratio <= 0.2:
                self.loyalty = self.loyalty - 1
        elif self.decision_style > 33 and self.decision_style <= 66: #Majority
            if ratio >= 0.5:
                self.loyalty = self.loyalty + 1
            if ratio < 0.5:
                self.loyalty = self.loyalty - 1
        elif self.decision_style > 66: #Hierarchy
            if ratio < 0.5:
                self.loyalty = self.loyalty + 1
            if ratio > 0.5:
                self.loyalty = self.loyalty - 1
     
        
    def decisionRule(self): #Comparisson of my vote with what was decided in the community voting
        if self.decision_rule <= 33: #confrontation
            if self.vote == 1 and self.community_vote > 0: 
                self.loyalty = self.loyalty + 1
            else:
                self.loyalty = self.loyalty - 1
        if self.decision_rule > 33 and self.decision_rule <=66: #bargaining
            self.threshold = 24 #longer slack for tolerance
            if self.vote == 1 and self.community_vote > 0: 
                self.loyalty = self.loyalty + 1
            else:
                self.loyalty = self.loyalty - 1
        if self.decision_rule > 66: #Problem solving
            if self.vote ==1 and self.community_vote > 0: 
                self.loyalty = self.loyalty + 1
            else:
                self.loyalty = self.loyalty + 0


    def leaveCommunity(self): #leaving the community routine
        self.decisionStyle()
        self.decisionRule()
        if self.loyalty >= self.threshold:
                if self.ROI < 0.1:# -----> To be defined
                    self.which_community = 0
                    self.eng_lvl = 0
                    self.exit = 1


##Community
class Community(Agent): #Community agent propoerties
    def __init__(self, name, pos, activity, model):
        super().__init__(name, model)
        self.active = activity #0 - No / 1 - Yes
        self.business_plan = 0 
        self.costs = 0
        self.energy = 0
        self.energy_solar = 0
        self.energy_wind = 0
        self.energy_total_total = 0
        self.energy_total_solar = 0
        self.energy_total_wind = 0
        self.gov_fit = 0
        self.gov_tax = 0
        self.gov_tgc = 0
        self.incentive_fit = 0
        self.incentive_tax = 0
        self.incentive_tgc = 0
        self.investment = 0
        self.members = []
        self.name = name
        self.period = 0
        self.pos = pos
        self.policy_entrepreneur = 0
        self.premium = 0
        self.project_cba = 0
        self.project_cost = 0 
        self.project_margin = 0
        self.project_tariff0 = 0
        self.project_tariff1 = 0
        self.plan_execution = "" 
        self.request = 0
        self.revenue = 0
        self.sale0 = 0
        self.sale1 = 0
        self.strategy = 0
        self.voting_result = 0
        self.money = 0    
        
      
#Community functions   
    def step(self):
        self.energy = 0
        self.plan_execution = 0
        self.request = 0
        self.sale = 0
        if self.active == 1:
           self.energyDemand()
           self.initialInvestment()
           self.projectDefinition()
           self.meetings()
           self.planExecution()
           self.policyEntrepeneur()
           self.newMemberFee()
           self.rtnFunc()
           self.memberExit()
           self.period = self.period + 1 
        
        if self.active == 0:
           pass
        
        
    def energyDemand(self): #update the member list
        if len(self.members) == 0:
            self.active = 0 
        else:
            for member in self.members:
                self.energy = self.energy + member.energy    
     
        
    def initialInvestment(self): #Initial investment by founders
        if self.active == 1 and self.period == 0:
            Data.projectSelector(self)
            invested_capital = float(((self.project_cost) * 1.2) /len(self.members)) 
            self.money = self.money + float(invested_capital * len(self.members))
            for member in self.members:
                member.invested = member.invested + invested_capital
    
    
    def projectDefinition(self): #Choose what type of project to be done: All solar, All wind or mixed sources
        if self.energy != 0: 
            Data.projectSelector(self)
            if self.project_margin <= 0:
                self.business_plan = "Unfeasible" 
                pass
            elif self.project_margin > 0:
                self.business_plan = "Feasible"    
                if self.project_cost >= self.money:
                    self.policy_entrepreneur = self.policy_entrepreneur - 1    
                    self.investment = self.project_cost - self.money
                    self.request = self.investment / len(self.members)
                    for member in self.members:
                       askforInvestment(self, member)
        else:
            None
    
    
    def meetings(self): #Schedule a meeting with members
        self.voting_result = 0
        for member in self.members:
             voting(self, member)
        if self.voting_result > len(self.members)/2:
            self.plan_execution = "Approved"
        else:
            self.plan_execution = "Rejected"
        
        
    def planExecution(self): #For approved plans, execute and generate revenue
        if self.plan_execution == "Approved":
            self.money = self.money - float(self.project_cost) #Pay for project
            self.energy_total_total  = self.energy_total_total + (self.energy_solar + self.energy_wind) #Increase generation park
            self.sale0 = ((self.energy_solar + self.energy_wind)) * self.project_tariff0 #Produce energy
            self.sale1 = self.project_tariff1 * (self.energy_solar + self.energy_wind)
            
            #Cummulative measures
            if self.strategy == 0:
                self.money = self.money + float(self.sale0)
                self.revenue = self.revenue + self.sale0
            if self.strategy == 1:
                self.money =  self.money + float(self.sale1)
                self.revenue = self.revenue + self.sale1
                
            self.costs = self.costs + self.project_cost 
            self.energy_total_solar = self.energy_total_solar + self.energy_solar
            self.energy_total_wind = self.energy_total_wind +  self.energy_wind
            self.gov_fit = self.gov_fit + self.incentive_fit
            self.gov_tax = self.gov_tax + self.incentive_tax
            self.gov_tgc = self.gov_tgc + self.incentive_tgc
        
        if self.plan_execution == "Rejected":
            self.money = self.money - float(self.energy * gridtariff)
            self.costs = self.costs + float(self.energy * gridtariff)
            for member in self.members:
                member.loyalty =  member.loyalty - 1
        else:
            pass
        
        
    def newMemberFee(self): #Calculate how much does it cost to a new member to join
        if self.energy_total_total != 0:
            ratios = self.energy_total_solar/self.energy_total_total
            ratiow = self.energy_total_wind/self.energy_total_total
        else:
            ratios = 0
            ratiow = 0
        
        if self.energy_total_wind == 0:
            LCOE_wind = 0
        else:
            LCOE_wind = (self.costs * ratiow)/(self.energy_total_wind)
        if self.energy_total_solar == 0:
            LCOE_solar = 0
        else:
            LCOE_solar = (self.costs * ratios)/(self.energy_total_solar)
        
        self.premium = (LCOE_solar * ratios) + (LCOE_wind * ratiow) 
        for member in self.members:
            member.com_premium = self.premium
        
    
    def rtnFunc(self): #return to members
        delta =  gridtariff - self.premium
        for member in self.members:
            if self.premium == 0:
                member.retrn = member.retrn + 0
            else:
                if self.strategy == 0:
                    member.retrn = member.retrn + float(delta * member.energy)
                    pass
                elif self.strategy == 1:
                    member.retrn = member.retrn + ((self.sale1 - self.project_cost) * 0.7)/len(self.members)
                    pass
        else:
            pass 
    
    
    def policyEntrepeneur(self): #reportt how each period was compared to the past one
            #Able to generate projects
            if self.plan_execution == "Approved":
                self.policy_entrepreneur = self.policy_entrepreneur + 1
            elif self.plan_execution == "Rejeceted":
                self.policy_entrepreneur = self.policy_entrepreneur + - 1     
            #Profitable
            try:
                if self.revenue/self.costs > 1:
                    self.policy_entrepreneur = self.policy_entrepreneur + 1   
                elif self.revenue/self.costs <= 1:
                    self.policy_entrepreneur = self.policy_entrepreneur - 1
            except: None
            

    def memberExit(self): #Member exit policy
        for member in self.members:
            if member.which_community == 0:
                self.members.remove(member)
               
        
  

   
        
        
        
        
        
        
        