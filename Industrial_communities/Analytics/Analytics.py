#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rafael
"""

###Imports
import sys
sys.path.append("/Users/rafael/Documents/GitHub/InCES-model/Industrial_communities/Analytics")
import matplotlib.pyplot as plt
import numpy as np
import AUS, BRA, IRA, JPN, NLD, USA


AUScolor = '#3498db' 
BRAcolor = '#27ae60' 
IRAcolor = '#7f8c8d'
JPNcolor = '#e74c3c'
NLDcolor = '#e67e22'
USAcolor = '#40739e'
FITcolor = '#16a085'
TAXcolor = '#f1c40f'
TGCcolor = '#2980b9'
NOIcolor = '#9b59b6' 
TOTALcolor = '#273746'

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.005*height,
                '%f' % float(height),
        ha='center', va='bottom')

 

###Plots
######################################
##Country specific - Australia
######################################        
#Communities
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.C_S0, color = AUScolor)
plt.plot(t, AUS.C_S1, color = BRAcolor)
plt.plot(t, AUS.C_S2, color = IRAcolor)
plt.plot(t, AUS.C_S3, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Australia')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.savefig('51 - AUS-Communities.png')
plt.show()  
      
#Members Exit
fig, ax = plt.subplots()
t = np.arange(20)
bar1 = ax.bar(t, AUS.E_S0, color = AUScolor, align='center')
bar2 = ax.bar(t, AUS.E_S1, color = BRAcolor, align='center', bottom = np.array(AUS.E_S0))
bar3 = ax.bar(t, AUS.E_S2, color = IRAcolor, align='center', bottom = np.array(AUS.E_S1) + np.array(AUS.E_S0))
bar4 = ax.bar(t, AUS.E_S3, color = JPNcolor, align='center', bottom = np.array(AUS.E_S2) + np.array(AUS.E_S1) + np.array(AUS.E_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Australia')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('52 - AUS-Quitters.png')
plt.show()

#Governmental Investment
fig, ax = plt.subplots()
t = np.arange(20)
y = np.vstack([AUS.G_S1, AUS.G_S2, AUS.G_S3]) 
colors = [FITcolor, TAXcolor, TGCcolor]
ax.stackplot(t, y, colors = colors, alpha=0.8)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government funding ($)')
plt.title('Australia')
ax.legend(["FIT", "TAX", "TGC"], loc='upper right', bbox_to_anchor=(+1, +0.9), fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('53 - AUS-GovInvestment.png')
plt.show()

#Community Investment
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, AUS.I_S0, color = AUScolor)
plt.plot(t, AUS.I_S1, color = BRAcolor)
plt.plot(t, AUS.I_S2, color = IRAcolor)
plt.plot(t, AUS.I_S3, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE  Generation (10M$)')
plt.title('Australia')
ax.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('54 - AUS-IndInvestment.png')
plt.show()

#Members in community
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, AUS.M_S0, color = AUScolor, align='center')
ax.bar(t, AUS.M_S1, color = BRAcolor, align='center', bottom = np.array(AUS.M_S0))
ax.bar(t, AUS.M_S2, color = IRAcolor, align='center', bottom = np.array(AUS.M_S1) + np.array(AUS.M_S0))
ax.bar(t, AUS.M_S3, color = JPNcolor, align='center', bottom = np.array(AUS.M_S2) + np.array(AUS.M_S1) + np.array(AUS.M_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Australia')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('55 - AUS-Members.png')
plt.show()


#Policy Entrepreneur
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.P_S0, color = AUScolor)
plt.plot(t, AUS.P_S1, color = BRAcolor)
plt.plot(t, AUS.P_S2, color = IRAcolor)
plt.plot(t, AUS.P_S3, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur flags')
plt.title('Australia')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('56 - AUS-Policy.png')
plt.show()

#Total Energy
ffig, ax = plt.subplots()
A = [sum(x) for x in zip(*[AUS.S_S0, AUS.W_S0])]
B = [sum(x) for x in zip(*[AUS.S_S1, AUS.W_S1])]
I = [sum(x) for x in zip(*[AUS.S_S2, AUS.W_S2])]
J = [sum(x) for x in zip(*[AUS.S_S3, AUS.W_S3])]
t = list(range(0,20))
plt.plot(t, A, color = AUScolor)
plt.plot(t, B, color = BRAcolor)
plt.plot(t, I, color = IRAcolor)
plt.plot(t, J, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Australia')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('57 - AUS-TotalEnerg.png')
plt.show()  
     
                
######################################
##Country specific - Netherlands
######################################        
#Communities
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, NLD.C_S0, color = AUScolor)
plt.plot(t, NLD.C_S1, color = BRAcolor)
plt.plot(t, NLD.C_S2, color = IRAcolor)
plt.plot(t, NLD.C_S3, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Netherlands')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.savefig('44 - NLD-Communities.png')
plt.show()  
      
#Members Exit
fig, ax = plt.subplots()
t = np.arange(20)
bar1 = ax.bar(t, NLD.E_S0, color = AUScolor, align='center')
bar2 = ax.bar(t, NLD.E_S1, color = BRAcolor, align='center', bottom = np.array(NLD.E_S0))
bar3 = ax.bar(t, NLD.E_S2, color = IRAcolor, align='center', bottom = np.array(NLD.E_S1) + np.array(NLD.E_S0))
bar4 = ax.bar(t, NLD.E_S3, color = JPNcolor, align='center', bottom = np.array(NLD.E_S2) + np.array(NLD.E_S1) + np.array(NLD.E_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Netherlands')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('45 - NLD-Quitters.png')
plt.show()

#Governmental Investment
fig, ax = plt.subplots()
t = np.arange(20)
y = np.vstack([NLD.G_S1, NLD.G_S2, NLD.G_S3]) 
colors = [FITcolor, TAXcolor, TGCcolor]
ax.stackplot(t, y, colors = colors, alpha=0.8)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government funding ($)')
plt.title('Netherlands')
ax.legend(["FIT", "TAX", "TGC"], loc='upper right', bbox_to_anchor=(+1, +0.9), fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('46 - NLD-GovInvestment.png')
plt.show()

#Community Investment
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, NLD.I_S0, color = AUScolor)
plt.plot(t, NLD.I_S1, color = BRAcolor)
plt.plot(t, NLD.I_S2, color = IRAcolor)
plt.plot(t, NLD.I_S3, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE  Generation (10M$)')
plt.title('Netherlands')
ax.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('47 - NLD-IndInvestment.png')
plt.show()

#Members in community
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, NLD.M_S0, color = AUScolor, align='center')
ax.bar(t, NLD.M_S1, color = BRAcolor, align='center', bottom = np.array(NLD.M_S0))
ax.bar(t, NLD.M_S2, color = IRAcolor, align='center', bottom = np.array(NLD.M_S1) + np.array(NLD.M_S0))
ax.bar(t, NLD.M_S3, color = JPNcolor, align='center', bottom = np.array(NLD.M_S2) + np.array(NLD.M_S1) + np.array(NLD.M_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Netherlands')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('48 - NLD-Members.png')
plt.show()


#Policy Entrepreneur
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, NLD.P_S0, color = AUScolor)
plt.plot(t, NLD.P_S1, color = BRAcolor)
plt.plot(t, NLD.P_S2, color = IRAcolor)
plt.plot(t, NLD.P_S3, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur flags')
plt.title('Netherlands')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('49 - NLD-Policy.png')
plt.show()

#Total Energy
ffig, ax = plt.subplots()
A = [sum(x) for x in zip(*[NLD.S_S0, NLD.W_S0])]
B = [sum(x) for x in zip(*[NLD.S_S1, NLD.W_S1])]
I = [sum(x) for x in zip(*[NLD.S_S2, NLD.W_S2])]
J = [sum(x) for x in zip(*[NLD.S_S3, NLD.W_S3])]
t = list(range(0,20))
plt.plot(t, A, color = AUScolor)
plt.plot(t, B, color = BRAcolor)
plt.plot(t, I, color = IRAcolor)
plt.plot(t, J, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Netherlands')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('50 - NLD-TotalEnergy.png')
plt.show()  
     
        
######################################
##Communities
######################################
#Scenario 0
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.C_S0, color = AUScolor)
plt.plot(t, BRA.C_S0, color = BRAcolor)
plt.plot(t, IRA.C_S0, color = IRAcolor)
plt.plot(t, JPN.C_S0, color = JPNcolor)
plt.plot(t, NLD.C_S0, color = NLDcolor)
plt.plot(t, USA.C_S0, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Scenario 0')
#plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
#plt.rcParams["figure.figsize"] = [15,10]
#plt.minorticks_on()
#plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('01 - Communities_S0.png')
plt.show()


#Scenario 1
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.C_S1, color = AUScolor)
plt.plot(t, BRA.C_S1, color = BRAcolor)
plt.plot(t, IRA.C_S1, color = IRAcolor)
plt.plot(t, JPN.C_S1, color = JPNcolor)
plt.plot(t, NLD.C_S1, color = NLDcolor)
plt.plot(t, USA.C_S1, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Scenario 1')
#plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('02 - Communities_S1.png')
plt.show()


#Scenario 2
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.C_S2, color = AUScolor)
plt.plot(t, BRA.C_S2, color = BRAcolor)
plt.plot(t, IRA.C_S2, color = IRAcolor)
plt.plot(t, JPN.C_S2, color = JPNcolor)
plt.plot(t, NLD.C_S2, color = NLDcolor)
plt.plot(t, USA.C_S2, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Scenario 2')
#plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('03 - Communities_S2.png')
plt.show()


#Scenario 3
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.C_S3, color = AUScolor)
plt.plot(t, BRA.C_S3, color = BRAcolor)
plt.plot(t, IRA.C_S3, color = IRAcolor)
plt.plot(t, JPN.C_S3, color = JPNcolor)
plt.plot(t, NLD.C_S3, color = NLDcolor)
plt.plot(t, USA.C_S3, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Scenario 3')
plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('04 - Communities_S3.png')
plt.show()


######################################
##Members Exit
######################################
#Scenario 0
fig, ax = plt.subplots()
t = np.arange(20)
bar1 = ax.bar(t, AUS.E_S0, color = AUScolor, align='center')
bar2 = ax.bar(t, BRA.E_S0, color = BRAcolor, align='center', bottom = np.array(AUS.E_S0))
bar3 = ax.bar(t, IRA.E_S0, color = IRAcolor, align='center', bottom = np.array(AUS.E_S0) + np.array(BRA.E_S0))
bar4 = ax.bar(t, JPN.E_S0, color = JPNcolor, align='center', bottom = np.array(AUS.E_S0) + np.array(BRA.E_S0) + np.array(IRA.E_S0))
bar5 = ax.bar(t, NLD.E_S0, color = NLDcolor, align='center', bottom = np.array(AUS.E_S0) + np.array(BRA.E_S0) + np.array(IRA.E_S0) + np.array(JPN.E_S0))
bar6 = ax.bar(t, USA.E_S0, color = USAcolor, align='center', bottom = np.array(AUS.E_S0) + np.array(BRA.E_S0) + np.array(IRA.E_S0) + np.array(JPN.E_S0) + np.array(NLD.E_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('05 - Quitters_S0.png')
plt.show()

#Scenario 1
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, AUS.E_S1, color = AUScolor, align='center')
ax.bar(t, BRA.E_S1, color = BRAcolor, align='center', bottom = np.array(AUS.E_S1))
ax.bar(t, IRA.E_S1, color = IRAcolor, align='center', bottom = np.array(AUS.E_S1) + np.array(BRA.E_S1))
ax.bar(t, JPN.E_S1, color = JPNcolor, align='center', bottom = np.array(AUS.E_S1) + np.array(BRA.E_S1) + np.array(IRA.E_S1))
ax.bar(t, NLD.E_S1, color = NLDcolor, align='center', bottom = np.array(AUS.E_S1) + np.array(BRA.E_S1) + np.array(IRA.E_S1) + np.array(JPN.E_S1))
ax.bar(t, USA.E_S1, color = USAcolor, align='center', bottom = np.array(AUS.E_S1) + np.array(BRA.E_S1) + np.array(IRA.E_S1) + np.array(JPN.E_S1) + np.array(NLD.E_S1))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('06 - Quitters_S1.png')
plt.show()

#Scenario 2
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, AUS.E_S2, color = AUScolor, align='center')
ax.bar(t, BRA.E_S2, color = BRAcolor, align='center', bottom = np.array(AUS.E_S2))
ax.bar(t, IRA.E_S2, color = IRAcolor, align='center', bottom = np.array(AUS.E_S2) + np.array(BRA.E_S2))
ax.bar(t, JPN.E_S2, color = JPNcolor, align='center', bottom = np.array(AUS.E_S2) + np.array(BRA.E_S2) + np.array(IRA.E_S2))
ax.bar(t, NLD.E_S2, color = NLDcolor, align='center', bottom = np.array(AUS.E_S2) + np.array(BRA.E_S2) + np.array(IRA.E_S2) + np.array(JPN.E_S2))
ax.bar(t, USA.E_S2, color = USAcolor, align='center', bottom = np.array(AUS.E_S2) + np.array(BRA.E_S2) + np.array(IRA.E_S2) + np.array(JPN.E_S2) + np.array(NLD.E_S2))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('07 - Quitters_S2.png')
plt.show()

#Scenario 3
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, AUS.E_S3, color = AUScolor, align='center')
ax.bar(t, BRA.E_S3, color = BRAcolor, align='center', bottom = np.array(AUS.E_S3))
ax.bar(t, IRA.E_S3, color = IRAcolor, align='center', bottom = np.array(AUS.E_S3) + np.array(BRA.E_S3))
ax.bar(t, JPN.E_S3, color = JPNcolor, align='center', bottom = np.array(AUS.E_S3) + np.array(BRA.E_S3) + np.array(IRA.E_S3))
ax.bar(t, NLD.E_S3, color = NLDcolor, align='center', bottom = np.array(AUS.E_S3) + np.array(BRA.E_S3) + np.array(IRA.E_S3) + np.array(JPN.E_S3))
ax.bar(t, USA.E_S3, color = USAcolor, align='center', bottom = np.array(AUS.E_S3) + np.array(BRA.E_S3) + np.array(IRA.E_S3) + np.array(JPN.E_S3) + np.array(NLD.E_S3))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Scenario 3')
plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('08 - Quitters_S3.png')
plt.show()


######################################
##Governmental Investment
######################################
#Scenario 1 - FIT
fig, ax = plt.subplots()
t = np.arange(20)
y = np.vstack([AUS.G_S1, BRA.G_S1, IRA.G_S1, JPN.G_S1, NLD.G_S1, USA.G_S1]) 
colors = [AUScolor, BRAcolor, IRAcolor, JPNcolor, NLDcolor, USAcolor]
ax.stackplot(t, y, colors = colors, alpha=0.8)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government funding ($)')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('09 - GovInvestment_S1.png')
plt.show()


#Scenario 2 - TAX
fig, ax = plt.subplots()
t = np.arange(20)
y = np.vstack([AUS.G_S2, BRA.G_S2, IRA.G_S2, JPN.G_S2, NLD.G_S2, USA.G_S2]) 
ccolors = [AUScolor, BRAcolor, IRAcolor, JPNcolor, NLDcolor, USAcolor]
ax.stackplot(t, y, colors = colors, alpha=0.8)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government funding ($)')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('10 - GovInvestment_S2.png')
plt.show()

#Scenario 3 - TGC
fig, ax = plt.subplots()
t = np.arange(20)
y = np.vstack([AUS.G_S3, BRA.G_S3, IRA.G_S3, JPN.G_S3, NLD.G_S3, USA.G_S3]) 
colors = [AUScolor, BRAcolor, IRAcolor, JPNcolor, NLDcolor, USAcolor]
ax.stackplot(t, y, colors = colors, alpha=0.8)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government funding ($)')
plt.title('Scenario 3')
ax.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper right', bbox_to_anchor=(+1.1, +0.9), fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('11 - GovInvestment_S3.png')
plt.show()

#Total Investment
list_fit = [AUS.G_S1, BRA.G_S1, IRA.G_S1, JPN.G_S1, NLD.G_S1, USA.G_S1]
list_tax = [AUS.G_S2, BRA.G_S2, IRA.G_S2, JPN.G_S2, NLD.G_S2, USA.G_S2]
list_tgc = [AUS.G_S3, BRA.G_S3, IRA.G_S3, JPN.G_S3, NLD.G_S3, USA.G_S3]
FIT = [sum(x) for x in zip(*list_fit)]
TAX = [sum(x) for x in zip(*list_tax)]
TGC = [sum(x) for x in zip(*list_tgc)]

fig, ax = plt.subplots()
t = list(range(0,20))
y = np.vstack([FIT, TAX, TGC]) 
colors = [FITcolor, TAXcolor, TGCcolor]
ax.stackplot(t, y, colors = colors, alpha=0.7)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government funding ($)')
plt.title('Total yield')
plt.legend(["FIT", "TAX", "TGC"], loc='lower right')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('12 - GovInvestment_Total.png')
plt.show()


######################################
##Investment in RE Generation
######################################
#Scenario 0
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.I_S0, color = AUScolor)
plt.plot(t, BRA.I_S0, color = BRAcolor)
plt.plot(t, IRA.I_S0, color = IRAcolor)
plt.plot(t, JPN.I_S0, color = JPNcolor)
plt.plot(t, NLD.I_S0, color = NLDcolor)
plt.plot(t, USA.I_S0, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE Generarion (10M$)')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('13 - IndInvestment_S0.png')
plt.show()

#Scenario 1 - FIT
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, AUS.I_S1, color = AUScolor)
plt.plot(t, BRA.I_S1, color = BRAcolor)
plt.plot(t, IRA.I_S1, color = IRAcolor)
plt.plot(t, JPN.I_S1, color = JPNcolor)
plt.plot(t, NLD.I_S1, color = NLDcolor)
plt.plot(t, USA.I_S1, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE Generation ($)')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('14 - IndInvestment_S1.png')
plt.show()

#Scenario 2 - TAX
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, AUS.I_S2, color = AUScolor)
plt.plot(t, BRA.I_S2, color = BRAcolor)
plt.plot(t, IRA.I_S2, color = IRAcolor)
plt.plot(t, JPN.I_S2, color = JPNcolor)
plt.plot(t, NLD.I_S2, color = NLDcolor)
plt.plot(t, USA.I_S2, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE Generation ($)')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('15 - IndInvestment_S2.png')
plt.show()

#Scenario 3 - TGC
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, AUS.I_S3, color = AUScolor)
plt.plot(t, BRA.I_S3, color = BRAcolor)
plt.plot(t, IRA.I_S3, color = IRAcolor)
plt.plot(t, JPN.I_S3, color = JPNcolor)
plt.plot(t, NLD.I_S3, color = NLDcolor)
plt.plot(t, USA.I_S3, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE  Generation (10M$)')
plt.title('Scenario 3')
ax.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('16 - IndInvestment_S3.png')
plt.show()


#Total Investment
list_noi = [AUS.I_S0, BRA.I_S0, IRA.I_S0, JPN.I_S0, NLD.I_S0, USA.I_S0]
list_fit = [AUS.I_S1, BRA.I_S1, IRA.I_S1, JPN.I_S1, NLD.I_S1, USA.I_S1]
list_tax = [AUS.I_S2, BRA.I_S2, IRA.I_S2, JPN.I_S2, NLD.I_S2, USA.I_S2]
list_tgc = [AUS.I_S3, BRA.I_S3, IRA.I_S3, JPN.I_S3, NLD.I_S3, USA.I_S3]
NOI = [sum(x) for x in zip(*list_noi)]
FIT = [sum(x) for x in zip(*list_fit)]
TAX = [sum(x) for x in zip(*list_tax)]
TGC = [sum(x) for x in zip(*list_tgc)]

fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, NOI, color = NOIcolor)
plt.plot(t, FIT, color = FITcolor)
plt.plot(t, TAX, color = TAXcolor)
plt.plot(t, TGC, color = TGCcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE Generation (10M$)')
plt.title('Total yield')
plt.legend(["NOI", "FIT", "TAX", "TGC"], loc='lower right')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('17 - IndInvestment_Total.png')
plt.show()


######################################
##Members
######################################
#Scenario 0
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, AUS.M_S0, color = AUScolor, align='center')
ax.bar(t, BRA.M_S0, color = BRAcolor, align='center', bottom = np.array(AUS.M_S0))
ax.bar(t, IRA.M_S0, color = IRAcolor, align='center', bottom = np.array(AUS.M_S0) + np.array(BRA.M_S0))
ax.bar(t, JPN.M_S0, color = JPNcolor, align='center', bottom = np.array(AUS.M_S0) + np.array(BRA.M_S0) + np.array(IRA.M_S0))
ax.bar(t, NLD.M_S0, color = NLDcolor, align='center', bottom = np.array(AUS.M_S0) + np.array(BRA.M_S0) + np.array(IRA.M_S0) + np.array(JPN.M_S0))
ax.bar(t, USA.M_S0, color = USAcolor, align='center', bottom = np.array(AUS.M_S0) + np.array(BRA.M_S0) + np.array(IRA.M_S0) + np.array(JPN.M_S0) + np.array(NLD.M_S0))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Scenario 0')
#plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('18 - Members_S0.png')
plt.show()

#Scenario 1
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, AUS.M_S1, color = AUScolor, align='center')
ax.bar(t, BRA.M_S1, color = BRAcolor, align='center', bottom = np.array(AUS.M_S1))
ax.bar(t, IRA.M_S1, color = IRAcolor, align='center', bottom = np.array(AUS.M_S1) + np.array(BRA.M_S1))
ax.bar(t, JPN.M_S1, color = JPNcolor, align='center', bottom = np.array(AUS.M_S1) + np.array(BRA.M_S1) + np.array(IRA.M_S1))
ax.bar(t, NLD.M_S1, color = NLDcolor, align='center', bottom = np.array(AUS.M_S1) + np.array(BRA.M_S1) + np.array(IRA.M_S1) + np.array(JPN.M_S1))
ax.bar(t, USA.M_S1, color = USAcolor, align='center', bottom = np.array(AUS.M_S1) + np.array(BRA.M_S1) + np.array(IRA.M_S1) + np.array(JPN.M_S1) + np.array(NLD.M_S1))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Scenario 1')
#plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('19 - Members_S1.png')
plt.show()

#Scenario 2
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, AUS.M_S2, color = AUScolor, align='center')
ax.bar(t, BRA.M_S2, color = BRAcolor, align='center', bottom = np.array(AUS.M_S2))
ax.bar(t, IRA.M_S2, color = IRAcolor, align='center', bottom = np.array(AUS.M_S2) + np.array(BRA.M_S2))
ax.bar(t, JPN.M_S2, color = JPNcolor, align='center', bottom = np.array(AUS.M_S2) + np.array(BRA.M_S2) + np.array(IRA.M_S2))
ax.bar(t, NLD.M_S2, color = NLDcolor, align='center', bottom = np.array(AUS.M_S2) + np.array(BRA.M_S2) + np.array(IRA.M_S2) + np.array(JPN.M_S2))
ax.bar(t, USA.M_S2, color = USAcolor, align='center', bottom = np.array(AUS.M_S2) + np.array(BRA.M_S2) + np.array(IRA.M_S2) + np.array(JPN.M_S2) + np.array(NLD.M_S2))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Scenario 2')
#plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('20 - Members_S2.png')
plt.show()

#Scenario 3
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, AUS.M_S3, color = AUScolor, align='center')
ax.bar(t, BRA.M_S3, color = BRAcolor, align='center', bottom = np.array(AUS.M_S3))
ax.bar(t, IRA.M_S3, color = IRAcolor, align='center', bottom = np.array(AUS.M_S3) + np.array(BRA.M_S3))
ax.bar(t, JPN.M_S3, color = JPNcolor, align='center', bottom = np.array(AUS.M_S3) + np.array(BRA.M_S3) + np.array(IRA.M_S3))
ax.bar(t, NLD.M_S3, color = NLDcolor, align='center', bottom = np.array(AUS.M_S3) + np.array(BRA.M_S3) + np.array(IRA.M_S3) + np.array(JPN.M_S3))
ax.bar(t, USA.M_S3, color = USAcolor, align='center', bottom = np.array(AUS.M_S3) + np.array(BRA.M_S3) + np.array(IRA.M_S3) + np.array(JPN.M_S3) + np.array(NLD.M_S3))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Scenario 3')
plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='lower right', bbox_to_anchor=(+1.1, +0.2), fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('21 - Members_S3.png')
plt.show()


######################################
##Policy Entrepreneur
######################################
#Scenario 0
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.P_S0, color = AUScolor)
plt.plot(t, BRA.P_S0, color = BRAcolor)
plt.plot(t, IRA.P_S0, color = IRAcolor)
plt.plot(t, JPN.P_S0, color = JPNcolor)
plt.plot(t, NLD.P_S0, color = NLDcolor)
plt.plot(t, USA.P_S0, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur flags')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('22 - Policy_S0.png')
plt.show()

#Scenario 1
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.P_S1, color = AUScolor)
plt.plot(t, BRA.P_S1, color = BRAcolor)
plt.plot(t, IRA.P_S1, color = IRAcolor)
plt.plot(t, JPN.P_S1, color = JPNcolor)
plt.plot(t, NLD.P_S1, color = NLDcolor)
plt.plot(t, USA.P_S1, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur flags')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('23 - Policy_S1.png')
plt.show()

#Scenario 2
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.P_S2, color = AUScolor)
plt.plot(t, BRA.P_S2, color = BRAcolor)
plt.plot(t, IRA.P_S2, color = IRAcolor)
plt.plot(t, JPN.P_S2, color = JPNcolor)
plt.plot(t, NLD.P_S2, color = NLDcolor)
plt.plot(t, USA.P_S2, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur flags')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('24 - Policy_S2.png')
plt.show()

#Scenario 3
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, AUS.P_S3, color = AUScolor)
plt.plot(t, BRA.P_S3, color = BRAcolor)
plt.plot(t, IRA.P_S3, color = IRAcolor)
plt.plot(t, JPN.P_S3, color = JPNcolor)
plt.plot(t, NLD.P_S3, color = NLDcolor)
plt.plot(t, USA.P_S3, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur flags')
plt.title('Scenario 3')
plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('25 - Policy_S3.png')
plt.show()


######################################
##Total Energy
######################################
#Total
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[AUS.S_S1, AUS.W_S1, AUS.S_S2, AUS.W_S2, AUS.S_S3, AUS.W_S3])]
B = [sum(x) for x in zip(*[BRA.S_S1, BRA.W_S1, BRA.S_S2, BRA.W_S2, BRA.S_S3, BRA.W_S3])]
I = [sum(x) for x in zip(*[IRA.S_S1, IRA.W_S1, IRA.S_S2, IRA.W_S2, IRA.S_S3, IRA.W_S3])]
J = [sum(x) for x in zip(*[JPN.S_S1, JPN.W_S1, JPN.S_S2, JPN.W_S2, JPN.S_S3, JPN.W_S3])]
N = [sum(x) for x in zip(*[NLD.S_S1, NLD.W_S1, NLD.S_S2, NLD.W_S2, NLD.S_S3, NLD.W_S3])]
U = [sum(x) for x in zip(*[USA.S_S1, USA.W_S1, USA.S_S2, USA.W_S2, USA.S_S3, USA.W_S3])]

t = list(range(0,20))
plt.plot(t, A, color = AUScolor)
plt.plot(t, B, color = BRAcolor)
plt.plot(t, I, color = IRAcolor)
plt.plot(t, J, color = JPNcolor)
plt.plot(t, N, color = NLDcolor)
plt.plot(t, U, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenarios 1, 2 and 3')
plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('26 - TotalEnergy_Total.png')
plt.show()

#Total Solar
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[AUS.S_S0,  AUS.S_S1,  AUS.S_S2,  AUS.S_S3])]
B = [sum(x) for x in zip(*[BRA.S_S0,  BRA.S_S1,  BRA.S_S2,  BRA.S_S3])]
I = [sum(x) for x in zip(*[IRA.S_S0,  IRA.S_S1,  IRA.S_S2,  IRA.S_S3])]
J = [sum(x) for x in zip(*[JPN.S_S0,  JPN.S_S1,  JPN.S_S2,  JPN.S_S3])]
N = [sum(x) for x in zip(*[NLD.S_S0,  NLD.S_S1,  NLD.S_S2,  NLD.S_S3])]
U = [sum(x) for x in zip(*[USA.S_S0,  USA.S_S1,  USA.S_S2,  USA.S_S3])]
t = list(range(0,20))
plt.plot(t, A, color = AUScolor)
plt.plot(t, B, color = BRAcolor)
plt.plot(t, I, color = IRAcolor)
plt.plot(t, J, color = JPNcolor)
plt.plot(t, N, color = NLDcolor)
plt.plot(t, U, color = USAcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Solar Energy All Scenarios')
plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('58 - TotalEnergy_Solar.png')
plt.show()


#Total Wind
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[AUS.W_S0,  AUS.W_S1,  AUS.W_S2,  AUS.W_S3])]
B = [sum(x) for x in zip(*[BRA.W_S0,  BRA.W_S1,  BRA.W_S2,  BRA.W_S3])]
I = [sum(x) for x in zip(*[IRA.W_S0,  IRA.W_S1,  IRA.W_S2,  IRA.W_S3])]
J = [sum(x) for x in zip(*[JPN.W_S0,  JPN.W_S1,  JPN.W_S2,  JPN.W_S3])]
N = [sum(x) for x in zip(*[NLD.W_S0,  NLD.W_S1,  NLD.W_S2,  NLD.W_S3])]
U = [sum(x) for x in zip(*[USA.W_S0,  USA.W_S1,  USA.W_S2,  USA.W_S3])]
t = list(range(0,20))
plt.plot(t, A, color = AUScolor)
plt.plot(t, B, color = BRAcolor)
plt.plot(t, I, color = IRAcolor)
plt.plot(t, J, color = JPNcolor)
plt.plot(t, N, color = NLDcolor)
plt.plot(t, U, color = USAcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Wind Energy All Scenarios')
plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('59 - TotalEnergy_Wind.png')
plt.show()

#Scenario 0
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[AUS.S_S0, AUS.W_S0])]
B = [sum(x) for x in zip(*[BRA.S_S0, BRA.W_S0])]
I = [sum(x) for x in zip(*[IRA.S_S0, IRA.W_S0])]
J = [sum(x) for x in zip(*[JPN.S_S0, JPN.W_S0])]
N = [sum(x) for x in zip(*[NLD.S_S0, NLD.W_S0])]
U = [sum(x) for x in zip(*[USA.S_S0, USA.W_S0])]

t = list(range(0,20))
plt.plot(t, A, color = AUScolor)
plt.plot(t, B, color = BRAcolor)
plt.plot(t, I, color = IRAcolor)
plt.plot(t, J, color = JPNcolor)
plt.plot(t, N, color = NLDcolor)
plt.plot(t, U, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('27 - TotalEnergy_S0.png')
plt.show()

#Scenario 1
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[AUS.S_S1, AUS.W_S1])]
B = [sum(x) for x in zip(*[BRA.S_S1, BRA.W_S1])]
I = [sum(x) for x in zip(*[IRA.S_S1, IRA.W_S1])]
J = [sum(x) for x in zip(*[JPN.S_S1, JPN.W_S1])]
N = [sum(x) for x in zip(*[NLD.S_S1, NLD.W_S1])]
U = [sum(x) for x in zip(*[USA.S_S1, USA.W_S1])]

t = list(range(0,20))
plt.plot(t, A, color = AUScolor)
plt.plot(t, B, color = BRAcolor)
plt.plot(t, I, color = IRAcolor)
plt.plot(t, J, color = JPNcolor)
plt.plot(t, N, color = NLDcolor)
plt.plot(t, U, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('28 - TotalEnergy_S1.png')
plt.show()

#Scenario 2
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[AUS.S_S2, AUS.W_S2])]
B = [sum(x) for x in zip(*[BRA.S_S2, BRA.W_S2])]
I = [sum(x) for x in zip(*[IRA.S_S2, IRA.W_S2])]
J = [sum(x) for x in zip(*[JPN.S_S2, JPN.W_S2])]
N = [sum(x) for x in zip(*[NLD.S_S2, NLD.W_S2])]
U = [sum(x) for x in zip(*[USA.S_S2, USA.W_S2])]

t = list(range(0,20))
plt.plot(t, A, color = AUScolor)
plt.plot(t, B, color = BRAcolor)
plt.plot(t, I, color = IRAcolor)
plt.plot(t, J, color = JPNcolor)
plt.plot(t, N, color = NLDcolor)
plt.plot(t, U, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('29 - TotalEnergy_S2.png')
plt.show()


#Scenario 3
ffig, ax = plt.subplots()
A = [sum(x) for x in zip(*[AUS.S_S3, AUS.W_S3])]
B = [sum(x) for x in zip(*[BRA.S_S3, BRA.W_S3])]
I = [sum(x) for x in zip(*[IRA.S_S3, IRA.W_S3])]
J = [sum(x) for x in zip(*[JPN.S_S3, JPN.W_S3])]
N = [sum(x) for x in zip(*[NLD.S_S3, NLD.W_S3])]
U = [sum(x) for x in zip(*[USA.S_S3, USA.W_S3])]

t = list(range(0,20))
plt.plot(t, A, color = AUScolor)
plt.plot(t, B, color = BRAcolor)
plt.plot(t, I, color = IRAcolor)
plt.plot(t, J, color = JPNcolor)
plt.plot(t, N, color = NLDcolor)
plt.plot(t, U, color = USAcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenario 3')
plt.legend(["Australia", "Brazil", "Iran", "Japan", "Netherlands", "USA"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('30 - TotalEnergy_S3.png')
plt.show()


######################################
##Energy By Country
######################################
#AUS
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[AUS.S_S0, AUS.S_S1, AUS.S_S2, AUS.S_S3])]
w1 = [sum(x) for x in zip(*[AUS.W_S0, AUS.W_S1, AUS.W_S2, AUS.W_S3])]
solar1 = ax.plot(t, s1, color = USAcolor)
Wind = ax.plot(t, w1, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('AUSTRALIA - Total energy')
plt.legend(["Solar", "Wind"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('31 - AUSEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[AUS.S_S1])]
s2 = [sum(x) for x in zip(*[AUS.S_S2])]
s3 = [sum(x) for x in zip(*[AUS.S_S3])]
st = [sum(x) for x in zip(*[AUS.S_S1, AUS.S_S2, AUS.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('AUSTRALIA - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('31a - AUSEnergy.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[AUS.W_S1])]
w2 = [sum(x) for x in zip(*[AUS.W_S2])]
w3 = [sum(x) for x in zip(*[AUS.W_S3])]
wt = [sum(x) for x in zip(*[AUS.W_S1, AUS.W_S2, AUS.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('AUSTRALIA - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('31b - AUSEnergy.png')
plt.show()


#BRA
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[BRA.S_S0, BRA.S_S1, BRA.S_S2, BRA.S_S3])]
w1 = [sum(x) for x in zip(*[BRA.W_S0, BRA.W_S1, BRA.W_S2, BRA.W_S3])]
solar1 = ax.plot(t, s1, color = USAcolor)
Wind = ax.plot(t, w1, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('BRAZIL - Total energy')
plt.legend(["Solar", "Wind"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('32 - BRAEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[BRA.S_S1])]
s2 = [sum(x) for x in zip(*[BRA.S_S2])]
s3 = [sum(x) for x in zip(*[BRA.S_S3])]
st = [sum(x) for x in zip(*[BRA.S_S1, BRA.S_S2, BRA.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('BRAZIL - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('32a - BRAEnergy.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[BRA.W_S1])]
w2 = [sum(x) for x in zip(*[BRA.W_S2])]
w3 = [sum(x) for x in zip(*[BRA.W_S3])]
wt = [sum(x) for x in zip(*[BRA.W_S1, BRA.W_S2, BRA.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('BRAZIL - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('32b - BRAEnergy.png')
plt.show()

#IRA
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[IRA.S_S0, IRA.S_S1, IRA.S_S2, IRA.S_S3])]
w1 = [sum(x) for x in zip(*[IRA.W_S0, IRA.W_S1, IRA.W_S2, IRA.W_S3])]
solar1 = ax.plot(t, s1, color = USAcolor)
Wind = ax.plot(t, w1, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('IRAN - Total energy')
plt.legend(["Solar", "Wind"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('33 - IRAEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[IRA.S_S1])]
s2 = [sum(x) for x in zip(*[IRA.S_S2])]
s3 = [sum(x) for x in zip(*[IRA.S_S3])]
st = [sum(x) for x in zip(*[IRA.S_S1, IRA.S_S2, IRA.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('IRAN - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('33a - IRAEnergy.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[IRA.W_S1])]
w2 = [sum(x) for x in zip(*[IRA.W_S2])]
w3 = [sum(x) for x in zip(*[IRA.W_S3])]
wt = [sum(x) for x in zip(*[IRA.W_S1, IRA.W_S2, IRA.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('IRAN - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('33b - IRAEnergy.png')
plt.show()

#JPN
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[JPN.S_S0, JPN.S_S1, JPN.S_S2, JPN.S_S3])]
w1 = [sum(x) for x in zip(*[JPN.W_S0, JPN.W_S1, JPN.W_S2, JPN.W_S3])]
solar1 = ax.plot(t, s1, color = USAcolor)
Wind = ax.plot(t, w1, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('JAPAN - Total energy')
plt.legend(["Solar", "Wind"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('34 - JPNEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[JPN.S_S1])]
s2 = [sum(x) for x in zip(*[JPN.S_S2])]
s3 = [sum(x) for x in zip(*[JPN.S_S3])]
st = [sum(x) for x in zip(*[JPN.S_S1, JPN.S_S2, JPN.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('JAPAN - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('34a - JPNEnergy.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[JPN.W_S1])]
w2 = [sum(x) for x in zip(*[JPN.W_S2])]
w3 = [sum(x) for x in zip(*[JPN.W_S3])]
wt = [sum(x) for x in zip(*[JPN.W_S1, JPN.W_S2, JPN.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)


plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('JAPAN - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('34b - JPNEnergy.png')
plt.show()

#NLD
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[NLD.S_S0, NLD.S_S1, NLD.S_S2, NLD.S_S3])]
w1 = [sum(x) for x in zip(*[NLD.W_S0, NLD.W_S1, NLD.W_S2, NLD.W_S3])]
solar1 = ax.plot(t, s1, color = USAcolor)
Wind = ax.plot(t, w1, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('NETHERLANDS - Total energy')
plt.legend(["Solar", "Wind"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('35 - NLDEnergy.png')
plt.show()


fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[NLD.S_S1])]
s2 = [sum(x) for x in zip(*[NLD.S_S2])]
s3 = [sum(x) for x in zip(*[NLD.S_S3])]
st = [sum(x) for x in zip(*[NLD.S_S1, NLD.S_S2, NLD.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('NETHERLANDS - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('35a - NLDEnergy.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[NLD.W_S1])]
w2 = [sum(x) for x in zip(*[NLD.W_S2])]
w3 = [sum(x) for x in zip(*[NLD.W_S3])]
wt = [sum(x) for x in zip(*[NLD.W_S1, NLD.W_S2, NLD.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('NETHERLANDS - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('35b - NLDEnergy.png')
plt.show()


#USA
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[USA.S_S0, USA.S_S1, USA.S_S2, USA.S_S3])]
w1 = [sum(x) for x in zip(*[USA.W_S0, USA.W_S1, USA.W_S2, USA.W_S3])]
solar1 = ax.plot(t, s1, color = USAcolor)
Wind = ax.plot(t, w1, color = JPNcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('UNITED STATES - Total energy')
plt.legend(["Solar", "Wind"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('36 - USAEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[USA.S_S1])]
s2 = [sum(x) for x in zip(*[USA.S_S2])]
s3 = [sum(x) for x in zip(*[USA.S_S3])]
st = [sum(x) for x in zip(*[USA.S_S1, USA.S_S2, USA.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('UNITED STATES - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('36a - USAEnergy.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[USA.W_S1])]
w2 = [sum(x) for x in zip(*[USA.W_S2])]
w3 = [sum(x) for x in zip(*[USA.W_S3])]
wt = [sum(x) for x in zip(*[USA.W_S1, USA.W_S2, USA.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('UNITED STATES - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('36b - USAEnergy.png')
plt.show()


######################################
###Ratio By Country
#####################################
##TOTAL
ft = AUS.RFIT + BRA.RFIT + IRA.RFIT + JPN.RFIT + NLD.RFIT + USA.RFIT
tx = AUS.RTAX + BRA.RTAX + IRA.RTAX + JPN.RTAX + NLD.RTAX + USA.RTAX
tc = AUS.RTGC + BRA.RTGC + IRA.RTGC + JPN.RTGC + NLD.RTGC + USA.RTGC

RFIT = ((AUS.RFIT * AUS.RFIT/ft) + (BRA.RFIT * BRA.RFIT/ft) + (IRA.RFIT * IRA.RFIT/ft) + (JPN.RFIT * JPN.RFIT/ft) + (NLD.RFIT * NLD.RFIT/ft) + (USA.RFIT * USA.RFIT/ft)) 
RTAX = ((AUS.RTAX * AUS.RTAX/tx) + (BRA.RTAX * BRA.RTAX/tx) + (IRA.RTAX * IRA.RTAX/tx) + (JPN.RTAX * JPN.RTAX/tx) + (NLD.RTAX * NLD.RTAX/tx) + (USA.RTAX * USA.RTAX/tx)) 
RTGC = ((AUS.RTGC * AUS.RTGC/tc) + (BRA.RTGC * BRA.RTGC/tc) + (IRA.RTGC * IRA.RTGC/tc) + (JPN.RTGC * JPN.RTGC/tc) + (NLD.RTGC * NLD.RTGC/tc) + (USA.RTGC * USA.RTGC/tc)) 

fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [RFIT, RTAX, RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=16)
plt.ylabel('USD/KWh', fontsize=16)
plt.legend(labels, loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for each incentive in Total')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('37 - RATIO_Total.png')
plt.show()

##AUS
fig, ax = plt.subplots()
w = AUS.RFIT + AUS.RTAX + AUS.RTGC
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [(AUS.RFIT * AUS.RFIT/w), (AUS.RTAX * AUS.RTAX/w) , (AUS.RTGC * AUS.RTGC/w)]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
plt.legend(labels, loc='upper right', bbox_to_anchor=(+1, +0.3), fancybox=True, shadow=True)
plt.title('LCOE for each incentive in Australia')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('38 - RATIO_aus.png')
plt.show()

##BRA
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [BRA.RFIT, BRA.RTAX, BRA.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
plt.legend(labels, loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for each incentive in Brazil')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('39 - RATIO_bra.png')
plt.show()

##IRA
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [IRA.RFIT, IRA.RTAX, IRA.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
plt.legend(['FIT','TAX', 'TGC'], loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for each incentive in Iran')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('40 - RATIO_ira.png')
plt.show()


##JPN
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [JPN.RFIT, JPN.RTAX, JPN.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
plt.legend(['FIT','TAX', 'TGC'], loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for each incentive in Japan')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('41 - RATIO_jpn.png')
plt.show()


#NLD
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [NLD.RFIT, NLD.RTAX, NLD.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
plt.legend(['FIT','TAX', 'TGC'], loc='upper right', bbox_to_anchor=(+1, +0.3), fancybox=True, shadow=True)
plt.title('LCOE for each incentive in the Netherlands')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('42 - RATIO_nld.png')
plt.show()


#USA
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [USA.RFIT, USA.RTAX, USA.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
plt.legend(['FIT','TAX', 'TGC'], loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for each incentive in the USA')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('43 - RATIO_usa.png')
plt.show()






#np.sum(np.sum(AUS.C_S1)/20 + np.sum(AUS.C_S2)/20 + np.sum(AUS.C_S3)/20 +  np.sum(BRA.C_S1)/20 + np.sum(BRA.C_S2)/20 + np.sum(BRA.C_S3)/20 + np.sum(IRA.C_S1)/20 + np.sum(IRA.C_S2)/20 + np.sum(IRA.C_S3)/20 + np.sum(JPN.C_S1)/20 + np.sum(JPN.C_S2)/20 + np.sum(JPN.C_S3)/20 + np.sum(NLD.C_S1)/20 + np.sum(NLD.C_S2)/20 + np.sum(NLD.C_S3)/20 + np.sum(USA.C_S1)/20 + np.sum(USA.C_S2)/20 + np.sum(USA.C_S3)/20)/18

