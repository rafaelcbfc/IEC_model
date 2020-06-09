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
import Alpha, Beta, Gamma, Delta, Epsilon, Zeta


Alphacolor = '#3498db' 
Betacolor = '#27ae60' 
Gammacolor = '#7f8c8d'
Deltacolor = '#e74c3c'
Epsiloncolor = '#e67e22'
Zetacolor = '#40739e'
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
##Country specific - Alpha
######################################        
#Communities
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.C_S0, color = Alphacolor)
plt.plot(t, Alpha.C_S1, color = Betacolor)
plt.plot(t, Alpha.C_S2, color = Gammacolor)
plt.plot(t, Alpha.C_S3, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Alpha')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.savefig('01 - Alpha-Communities.png')
plt.show()  
      
#Members Exit
fig, ax = plt.subplots()
t = np.arange(20)
bar1 = ax.bar(t, Alpha.E_S0, color = Alphacolor, align='center')
bar2 = ax.bar(t, Alpha.E_S1, color = Betacolor, align='center', bottom = np.array(Alpha.E_S0))
bar3 = ax.bar(t, Alpha.E_S2, color = Gammacolor, align='center', bottom = np.array(Alpha.E_S1) + np.array(Alpha.E_S0))
bar4 = ax.bar(t, Alpha.E_S3, color = Deltacolor, align='center', bottom = np.array(Alpha.E_S2) + np.array(Alpha.E_S1) + np.array(Alpha.E_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Alpha')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('02 - Alpha-Quitters.png')
plt.show()

#Governmental Investment
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, Alpha.G_S1, color = FITcolor)
plt.plot(t, Alpha.G_S2, color = TAXcolor)
plt.plot(t, Alpha.G_S3, color = TGCcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government funding ($)')
plt.title('Alpha - Government investment by scenario')
ax.legend(["FIT", "TAX", "TGC"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.tight_layout()
plt.savefig('03 - Alpha-GovInvestment.png')
plt.show()

#Community Investment
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, Alpha.I_S0, color = Alphacolor)
plt.plot(t, Alpha.I_S1, color = Betacolor)
plt.plot(t, Alpha.I_S2, color = Gammacolor)
plt.plot(t, Alpha.I_S3, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE  Generation (10M$)')
plt.title('Alpha - Community Investment by scenario')
ax.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('04 - Alpha-IndInvestment.png')
plt.show()

#Members in community
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, Alpha.M_S0, color = Alphacolor, align='center')
ax.bar(t, Alpha.M_S1, color = Betacolor, align='center', bottom = np.array(Alpha.M_S0))
ax.bar(t, Alpha.M_S2, color = Gammacolor, align='center', bottom = np.array(Alpha.M_S1) + np.array(Alpha.M_S0))
ax.bar(t, Alpha.M_S3, color = Deltacolor, align='center', bottom = np.array(Alpha.M_S2) + np.array(Alpha.M_S1) + np.array(Alpha.M_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Alpha')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('05 - Alpha-Members.png')
plt.show()


#Policy Entrepreneur
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.P_S0, color = Alphacolor)
plt.plot(t, Alpha.P_S1, color = Betacolor)
plt.plot(t, Alpha.P_S2, color = Gammacolor)
plt.plot(t, Alpha.P_S3, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur flags')
plt.title('Alpha')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('06 - Alpha-Policy.png')
plt.show()

#Total Energy
ffig, ax = plt.subplots()
A = [sum(x) for x in zip(*[Alpha.S_S0, Alpha.W_S0])]
B = [sum(x) for x in zip(*[Alpha.S_S1, Alpha.W_S1])]
I = [sum(x) for x in zip(*[Alpha.S_S2, Alpha.W_S2])]
J = [sum(x) for x in zip(*[Alpha.S_S3, Alpha.W_S3])]
t = list(range(0,20))
plt.plot(t, A, color = Alphacolor)
plt.plot(t, B, color = Betacolor)
plt.plot(t, I, color = Gammacolor)
plt.plot(t, J, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Alpha - Total Energy Production by scenario')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('07 - Alpha-TotalEnerg.png')
plt.show()  
     
                
######################################
##Country specific - Epsilon
######################################        
#Communities
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Epsilon.C_S0, color = Alphacolor)
plt.plot(t, Epsilon.C_S1, color = Betacolor)
plt.plot(t, Epsilon.C_S2, color = Gammacolor)
plt.plot(t, Epsilon.C_S3, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Epsilon')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.savefig('08 - Epsilon-Communities.png')
plt.show()  
      
#Members Exit
fig, ax = plt.subplots()
t = np.arange(20)
bar1 = ax.bar(t, Epsilon.E_S0, color = Alphacolor, align='center')
bar2 = ax.bar(t, Epsilon.E_S1, color = Betacolor, align='center', bottom = np.array(Epsilon.E_S0))
bar3 = ax.bar(t, Epsilon.E_S2, color = Gammacolor, align='center', bottom = np.array(Epsilon.E_S1) + np.array(Epsilon.E_S0))
bar4 = ax.bar(t, Epsilon.E_S3, color = Deltacolor, align='center', bottom = np.array(Epsilon.E_S2) + np.array(Epsilon.E_S1) + np.array(Epsilon.E_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Epsilon')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('09 - Epsilon-Quitters.png')
plt.show()

#Governmental Investment
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, Epsilon.G_S1, color = FITcolor)
plt.plot(t, Epsilon.G_S2, color = TAXcolor)
plt.plot(t, Epsilon.G_S3, color = TGCcolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government funding ($)')
plt.title('Epsilon - Government investment by scenario')
ax.legend(["FIT", "TAX", "TGC"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('10 - Epsilon-GovInvestment.png')
plt.show()

#Community Investment
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, Epsilon.I_S0, color = Alphacolor)
plt.plot(t, Epsilon.I_S1, color = Betacolor)
plt.plot(t, Epsilon.I_S2, color = Gammacolor)
plt.plot(t, Epsilon.I_S3, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE  Generation (10M$)')
plt.title('Epsilon - Community Investment by scenario')
ax.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.tight_layout()
plt.savefig('11 - Epsilon-IndInvestment.png')
plt.show()

#Members in community
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, Epsilon.M_S0, color = Alphacolor, align='center')
ax.bar(t, Epsilon.M_S1, color = Betacolor, align='center', bottom = np.array(Epsilon.M_S0))
ax.bar(t, Epsilon.M_S2, color = Gammacolor, align='center', bottom = np.array(Epsilon.M_S1) + np.array(Epsilon.M_S0))
ax.bar(t, Epsilon.M_S3, color = Deltacolor, align='center', bottom = np.array(Epsilon.M_S2) + np.array(Epsilon.M_S1) + np.array(Epsilon.M_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Epsilon')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('12 - Epsilon-Members.png')
plt.show()


#Policy Entrepreneur
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Epsilon.P_S0, color = Alphacolor)
plt.plot(t, Epsilon.P_S1, color = Betacolor)
plt.plot(t, Epsilon.P_S2, color = Gammacolor)
plt.plot(t, Epsilon.P_S3, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur flags')
plt.title('Epsilon')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('13 - Epsilon-Policy.png')
plt.show()

#Total Energy
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[Epsilon.S_S0, Epsilon.W_S0])]
B = [sum(x) for x in zip(*[Epsilon.S_S1, Epsilon.W_S1])]
I = [sum(x) for x in zip(*[Epsilon.S_S2, Epsilon.W_S2])]
J = [sum(x) for x in zip(*[Epsilon.S_S3, Epsilon.W_S3])]
t = list(range(0,20))
plt.plot(t, A, color = Alphacolor)
plt.plot(t, B, color = Betacolor)
plt.plot(t, I, color = Gammacolor)
plt.plot(t, J, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Epsilon')
plt.legend(["Scenario 0", "Scenario 1", "Scenario 2", "Scenario 3"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('14 - Epsilon-TotalEnergy.png')
plt.show()  
     
        
######################################
##Communities
######################################
#Scenario 0
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.C_S0, color = Alphacolor)
plt.plot(t, Beta.C_S0, color = Betacolor)
plt.plot(t, Gamma.C_S0, color = Gammacolor)
plt.plot(t, Delta.C_S0, color = Deltacolor)
plt.plot(t, Epsilon.C_S0, color = Epsiloncolor)
plt.plot(t, Zeta.C_S0, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('15 - Communities_S0.png')
plt.show()


#Scenario 1
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.C_S1, color = Alphacolor)
plt.plot(t, Beta.C_S1, color = Betacolor)
plt.plot(t, Gamma.C_S1, color = Gammacolor)
plt.plot(t, Delta.C_S1, color = Deltacolor)
plt.plot(t, Epsilon.C_S1, color = Epsiloncolor)
plt.plot(t, Zeta.C_S1, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('16 - Communities_S1.png')
plt.show()


#Scenario 2
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.C_S2, color = Alphacolor)
plt.plot(t, Beta.C_S2, color = Betacolor)
plt.plot(t, Gamma.C_S2, color = Gammacolor)
plt.plot(t, Delta.C_S2, color = Deltacolor)
plt.plot(t, Epsilon.C_S2, color = Epsiloncolor)
plt.plot(t, Zeta.C_S2, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('17 - Communities_S2.png')
plt.show()


#Scenario 3
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.C_S3, color = Alphacolor)
plt.plot(t, Beta.C_S3, color = Betacolor)
plt.plot(t, Gamma.C_S3, color = Gammacolor)
plt.plot(t, Delta.C_S3, color = Deltacolor)
plt.plot(t, Epsilon.C_S3, color = Epsiloncolor)
plt.plot(t, Zeta.C_S3, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Communities')
plt.title('Scenario 3')
plt.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='lower right', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('18 - Communities_S3.png')
plt.show()


######################################
##Members Exit
######################################
#Scenario 0
fig, ax = plt.subplots()
t = np.arange(20)
bar1 = ax.bar(t, Alpha.E_S0, color = Alphacolor, align='center')
bar2 = ax.bar(t, Beta.E_S0, color = Betacolor, align='center', bottom = np.array(Alpha.E_S0))
bar3 = ax.bar(t, Gamma.E_S0, color = Gammacolor, align='center', bottom = np.array(Alpha.E_S0) + np.array(Beta.E_S0))
bar4 = ax.bar(t, Delta.E_S0, color = Deltacolor, align='center', bottom = np.array(Alpha.E_S0) + np.array(Beta.E_S0) + np.array(Gamma.E_S0))
bar5 = ax.bar(t, Epsilon.E_S0, color = Epsiloncolor, align='center', bottom = np.array(Alpha.E_S0) + np.array(Beta.E_S0) + np.array(Gamma.E_S0) + np.array(Delta.E_S0))
bar6 = ax.bar(t, Zeta.E_S0, color = Zetacolor, align='center', bottom = np.array(Alpha.E_S0) + np.array(Beta.E_S0) + np.array(Gamma.E_S0) + np.array(Delta.E_S0) + np.array(Epsilon.E_S0))
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('19 - Quitters_S0.png')
plt.show()

#Scenario 1
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, Alpha.E_S1, color = Alphacolor, align='center')
ax.bar(t, Beta.E_S1, color = Betacolor, align='center', bottom = np.array(Alpha.E_S1))
ax.bar(t, Gamma.E_S1, color = Gammacolor, align='center', bottom = np.array(Alpha.E_S1) + np.array(Beta.E_S1))
ax.bar(t, Delta.E_S1, color = Deltacolor, align='center', bottom = np.array(Alpha.E_S1) + np.array(Beta.E_S1) + np.array(Gamma.E_S1))
ax.bar(t, Epsilon.E_S1, color = Epsiloncolor, align='center', bottom = np.array(Alpha.E_S1) + np.array(Beta.E_S1) + np.array(Gamma.E_S1) + np.array(Delta.E_S1))
ax.bar(t, Zeta.E_S1, color = Zetacolor, align='center', bottom = np.array(Alpha.E_S1) + np.array(Beta.E_S1) + np.array(Gamma.E_S1) + np.array(Delta.E_S1) + np.array(Epsilon.E_S1))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('20 - Quitters_S1.png')
plt.show()

#Scenario 2
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, Alpha.E_S2, color = Alphacolor, align='center')
ax.bar(t, Beta.E_S2, color = Betacolor, align='center', bottom = np.array(Alpha.E_S2))
ax.bar(t, Gamma.E_S2, color = Gammacolor, align='center', bottom = np.array(Alpha.E_S2) + np.array(Beta.E_S2))
ax.bar(t, Delta.E_S2, color = Deltacolor, align='center', bottom = np.array(Alpha.E_S2) + np.array(Beta.E_S2) + np.array(Gamma.E_S2))
ax.bar(t, Epsilon.E_S2, color = Epsiloncolor, align='center', bottom = np.array(Alpha.E_S2) + np.array(Beta.E_S2) + np.array(Gamma.E_S2) + np.array(Delta.E_S2))
ax.bar(t, Zeta.E_S2, color = Zetacolor, align='center', bottom = np.array(Alpha.E_S2) + np.array(Beta.E_S2) + np.array(Gamma.E_S2) + np.array(Delta.E_S2) + np.array(Epsilon.E_S2))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('21 - Quitters_S2.png')
plt.show()

#Scenario 3
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, Alpha.E_S3, color = Alphacolor, align='center')
ax.bar(t, Beta.E_S3, color = Betacolor, align='center', bottom = np.array(Alpha.E_S3))
ax.bar(t, Gamma.E_S3, color = Gammacolor, align='center', bottom = np.array(Alpha.E_S3) + np.array(Beta.E_S3))
ax.bar(t, Delta.E_S3, color = Deltacolor, align='center', bottom = np.array(Alpha.E_S3) + np.array(Beta.E_S3) + np.array(Gamma.E_S3))
ax.bar(t, Epsilon.E_S3, color = Epsiloncolor, align='center', bottom = np.array(Alpha.E_S3) + np.array(Beta.E_S3) + np.array(Gamma.E_S3) + np.array(Delta.E_S3))
ax.bar(t, Zeta.E_S3, color = Zetacolor, align='center', bottom = np.array(Alpha.E_S3) + np.array(Beta.E_S3) + np.array(Gamma.E_S3) + np.array(Delta.E_S3) + np.array(Epsilon.E_S3))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members Exit')
plt.title('Scenario 3')
plt.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('22 - Quitters_S3.png')
plt.show()


######################################
##Governmental Investment
######################################
#Scenario 1 - FIT
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.G_S1, color = Alphacolor)
plt.plot(t, Beta.G_S1, color = Betacolor)
plt.plot(t, Gamma.G_S1, color = Gammacolor)
plt.plot(t, Delta.G_S1, color = Deltacolor)
plt.plot(t, Epsilon.G_S1, color = Epsiloncolor)
plt.plot(t, Zeta.G_S1, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government investment ($)')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('23 - GovInvestment_S1.png')
plt.show()


#Scenario 2 - TAX
ig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.G_S2, color = Alphacolor)
plt.plot(t, Beta.G_S2, color = Betacolor)
plt.plot(t, Gamma.G_S2, color = Gammacolor)
plt.plot(t, Delta.G_S2, color = Deltacolor)
plt.plot(t, Epsilon.G_S2, color = Epsiloncolor)
plt.plot(t, Zeta.G_S2, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government investment ($)')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('24 - GovInvestment_S2.png')
plt.show()

#Scenario 3 - TGC
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.G_S3, color = Alphacolor)
plt.plot(t, Beta.G_S3, color = Betacolor)
plt.plot(t, Gamma.G_S3, color = Gammacolor)
plt.plot(t, Delta.G_S3, color = Deltacolor)
plt.plot(t, Epsilon.G_S3, color = Epsiloncolor)
plt.plot(t, Zeta.G_S3, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government investment ($)')
plt.title('Scenario 3')
ax.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.tight_layout()
plt.savefig('25 - GovInvestment_S3.png')
plt.show()

#Total Investment
list_fit = [Alpha.G_S1, Beta.G_S1, Gamma.G_S1, Delta.G_S1, Epsilon.G_S1, Zeta.G_S1]
list_tax = [Alpha.G_S2, Beta.G_S2, Gamma.G_S2, Delta.G_S2, Epsilon.G_S2, Zeta.G_S2]
list_tgc = [Alpha.G_S3, Beta.G_S3, Gamma.G_S3, Delta.G_S3, Epsilon.G_S3, Zeta.G_S3]
FIT = [sum(x) for x in zip(*list_fit)]
TAX = [sum(x) for x in zip(*list_tax)]
TGC = [sum(x) for x in zip(*list_tgc)]

ig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, FIT, color = FITcolor)
plt.plot(t, TAX, color = TAXcolor)
plt.plot(t, TGC, color = TGCcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Government investment ($)')
plt.title('Total yield')
plt.legend(["FIT", "TAX", "TGC"], loc='lower right')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('26 - GovInvestment_Total.png')
plt.show()


######################################
##Investment in RE Generation
######################################
#Scenario 0
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.I_S0, color = Alphacolor)
plt.plot(t, Beta.I_S0, color = Betacolor)
plt.plot(t, Gamma.I_S0, color = Gammacolor)
plt.plot(t, Delta.I_S0, color = Deltacolor)
plt.plot(t, Epsilon.I_S0, color = Epsiloncolor)
plt.plot(t, Zeta.I_S0, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE Generarion (10M$)')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('27 - IndInvestment_S0.png')
plt.show()

#Scenario 1 - FIT
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, Alpha.I_S1, color = Alphacolor)
plt.plot(t, Beta.I_S1, color = Betacolor)
plt.plot(t, Gamma.I_S1, color = Gammacolor)
plt.plot(t, Delta.I_S1, color = Deltacolor)
plt.plot(t, Epsilon.I_S1, color = Epsiloncolor)
plt.plot(t, Zeta.I_S1, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE Generation ($)')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.tight_layout()
plt.savefig('28 - IndInvestment_S1.png')
plt.show()

#Scenario 2 - TAX
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, Alpha.I_S2, color = Alphacolor)
plt.plot(t, Beta.I_S2, color = Betacolor)
plt.plot(t, Gamma.I_S2, color = Gammacolor)
plt.plot(t, Delta.I_S2, color = Deltacolor)
plt.plot(t, Epsilon.I_S2, color = Epsiloncolor)
plt.plot(t, Zeta.I_S2, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE Generation ($)')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.tight_layout()
plt.savefig('29 - IndInvestment_S2.png')
plt.show()

#Scenario 3 - TGC
fig, ax = plt.subplots()
t = np.arange(20)
plt.plot(t, Alpha.I_S3, color = Alphacolor)
plt.plot(t, Beta.I_S3, color = Betacolor)
plt.plot(t, Gamma.I_S3, color = Gammacolor)
plt.plot(t, Delta.I_S3, color = Deltacolor)
plt.plot(t, Epsilon.I_S3, color = Epsiloncolor)
plt.plot(t, Zeta.I_S3, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Invested Capital in RE  Generation (10M$)')
plt.title('Scenario 3')
ax.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('30 - IndInvestment_S3.png')
plt.show()


#Total Investment
list_noi = [Alpha.I_S0, Beta.I_S0, Gamma.I_S0, Delta.I_S0, Epsilon.I_S0, Zeta.I_S0]
list_fit = [Alpha.I_S1, Beta.I_S1, Gamma.I_S1, Delta.I_S1, Epsilon.I_S1, Zeta.I_S1]
list_tax = [Alpha.I_S2, Beta.I_S2, Gamma.I_S2, Delta.I_S2, Epsilon.I_S2, Zeta.I_S2]
list_tgc = [Alpha.I_S3, Beta.I_S3, Gamma.I_S3, Delta.I_S3, Epsilon.I_S3, Zeta.I_S3]
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
plt.savefig('31 - IndInvestment_Total.png')
plt.show()


######################################
##Members
######################################
#Scenario 0
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, Alpha.M_S0, color = Alphacolor, align='center')
ax.bar(t, Beta.M_S0, color = Betacolor, align='center', bottom = np.array(Alpha.M_S0))
ax.bar(t, Gamma.M_S0, color = Gammacolor, align='center', bottom = np.array(Alpha.M_S0) + np.array(Beta.M_S0))
ax.bar(t, Delta.M_S0, color = Deltacolor, align='center', bottom = np.array(Alpha.M_S0) + np.array(Beta.M_S0) + np.array(Gamma.M_S0))
ax.bar(t, Epsilon.M_S0, color = Epsiloncolor, align='center', bottom = np.array(Alpha.M_S0) + np.array(Beta.M_S0) + np.array(Gamma.M_S0) + np.array(Delta.M_S0))
ax.bar(t, Zeta.M_S0, color = Zetacolor, align='center', bottom = np.array(Alpha.M_S0) + np.array(Beta.M_S0) + np.array(Gamma.M_S0) + np.array(Delta.M_S0) + np.array(Epsilon.M_S0))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('32 - Members_S0.png')
plt.show()

#Scenario 1
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, Alpha.M_S1, color = Alphacolor, align='center')
ax.bar(t, Beta.M_S1, color = Betacolor, align='center', bottom = np.array(Alpha.M_S1))
ax.bar(t, Gamma.M_S1, color = Gammacolor, align='center', bottom = np.array(Alpha.M_S1) + np.array(Beta.M_S1))
ax.bar(t, Delta.M_S1, color = Deltacolor, align='center', bottom = np.array(Alpha.M_S1) + np.array(Beta.M_S1) + np.array(Gamma.M_S1))
ax.bar(t, Epsilon.M_S1, color = Epsiloncolor, align='center', bottom = np.array(Alpha.M_S1) + np.array(Beta.M_S1) + np.array(Gamma.M_S1) + np.array(Delta.M_S1))
ax.bar(t, Zeta.M_S1, color = Zetacolor, align='center', bottom = np.array(Alpha.M_S1) + np.array(Beta.M_S1) + np.array(Gamma.M_S1) + np.array(Delta.M_S1) + np.array(Epsilon.M_S1))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('33 - Members_S1.png')
plt.show()

#Scenario 2
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, Alpha.M_S2, color = Alphacolor, align='center')
ax.bar(t, Beta.M_S2, color = Betacolor, align='center', bottom = np.array(Alpha.M_S2))
ax.bar(t, Gamma.M_S2, color = Gammacolor, align='center', bottom = np.array(Alpha.M_S2) + np.array(Beta.M_S2))
ax.bar(t, Delta.M_S2, color = Deltacolor, align='center', bottom = np.array(Alpha.M_S2) + np.array(Beta.M_S2) + np.array(Gamma.M_S2))
ax.bar(t, Epsilon.M_S2, color = Epsiloncolor, align='center', bottom = np.array(Alpha.M_S2) + np.array(Beta.M_S2) + np.array(Gamma.M_S2) + np.array(Delta.M_S2))
ax.bar(t, Zeta.M_S2, color = Zetacolor, align='center', bottom = np.array(Alpha.M_S2) + np.array(Beta.M_S2) + np.array(Gamma.M_S2) + np.array(Delta.M_S2) + np.array(Epsilon.M_S2))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('34 - Members_S2.png')
plt.show()

#Scenario 3
fig, ax = plt.subplots()
t = np.arange(20)
ax.bar(t, Alpha.M_S3, color = Alphacolor, align='center')
ax.bar(t, Beta.M_S3, color = Betacolor, align='center', bottom = np.array(Alpha.M_S3))
ax.bar(t, Gamma.M_S3, color = Gammacolor, align='center', bottom = np.array(Alpha.M_S3) + np.array(Beta.M_S3))
ax.bar(t, Delta.M_S3, color = Deltacolor, align='center', bottom = np.array(Alpha.M_S3) + np.array(Beta.M_S3) + np.array(Gamma.M_S3))
ax.bar(t, Epsilon.M_S3, color = Epsiloncolor, align='center', bottom = np.array(Alpha.M_S3) + np.array(Beta.M_S3) + np.array(Gamma.M_S3) + np.array(Delta.M_S3))
ax.bar(t, Zeta.M_S3, color = Zetacolor, align='center', bottom = np.array(Alpha.M_S3) + np.array(Beta.M_S3) + np.array(Gamma.M_S3) + np.array(Delta.M_S3) + np.array(Epsilon.M_S3))

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('# of Members in communitites')
plt.title('Scenario 3')
plt.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='lower right', bbox_to_anchor=(+1.1, +0.2), fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('35 - Members_S3.png')
plt.show()


######################################
##Policy Entrepreneur
######################################
#Scenario 0
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.P_S0, color = Alphacolor)
plt.plot(t, Beta.P_S0, color = Betacolor)
plt.plot(t, Gamma.P_S0, color = Gammacolor)
plt.plot(t, Delta.P_S0, color = Deltacolor)
plt.plot(t, Epsilon.P_S0, color = Epsiloncolor)
plt.plot(t, Zeta.P_S0, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur indicator')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('36 - Policy_S0.png')
plt.show()

#Scenario 1
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.P_S1, color = Alphacolor)
plt.plot(t, Beta.P_S1, color = Betacolor)
plt.plot(t, Gamma.P_S1, color = Gammacolor)
plt.plot(t, Delta.P_S1, color = Deltacolor)
plt.plot(t, Epsilon.P_S1, color = Epsiloncolor)
plt.plot(t, Zeta.P_S1, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur indicator')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('37 - Policy_S1.png')
plt.show()

#Scenario 2
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.P_S2, color = Alphacolor)
plt.plot(t, Beta.P_S2, color = Betacolor)
plt.plot(t, Gamma.P_S2, color = Gammacolor)
plt.plot(t, Delta.P_S2, color = Deltacolor)
plt.plot(t, Epsilon.P_S2, color = Epsiloncolor)
plt.plot(t, Zeta.P_S2, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur indicator')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('38 - Policy_S2.png')
plt.show()

#Scenario 3
fig, ax = plt.subplots()
t = list(range(0,20))
plt.plot(t, Alpha.P_S3, color = Alphacolor)
plt.plot(t, Beta.P_S3, color = Betacolor)
plt.plot(t, Gamma.P_S3, color = Gammacolor)
plt.plot(t, Delta.P_S3, color = Deltacolor)
plt.plot(t, Epsilon.P_S3, color = Epsiloncolor)
plt.plot(t, Zeta.P_S3, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Policy Entrepreneur indicator')
plt.title('Scenario 3')
plt.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('39 - Policy_S3.png')
plt.show()


######################################
##Total Energy
######################################
#Total
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[Alpha.S_S1, Alpha.W_S1, Alpha.S_S2, Alpha.W_S2, Alpha.S_S3, Alpha.W_S3])]
B = [sum(x) for x in zip(*[Beta.S_S1, Beta.W_S1, Beta.S_S2, Beta.W_S2, Beta.S_S3, Beta.W_S3])]
I = [sum(x) for x in zip(*[Gamma.S_S1, Gamma.W_S1, Gamma.S_S2, Gamma.W_S2, Gamma.S_S3, Gamma.W_S3])]
J = [sum(x) for x in zip(*[Delta.S_S1, Delta.W_S1, Delta.S_S2, Delta.W_S2, Delta.S_S3, Delta.W_S3])]
N = [sum(x) for x in zip(*[Epsilon.S_S1, Epsilon.W_S1, Epsilon.S_S2, Epsilon.W_S2, Epsilon.S_S3, Epsilon.W_S3])]
U = [sum(x) for x in zip(*[Zeta.S_S1, Zeta.W_S1, Zeta.S_S2, Zeta.W_S2, Zeta.S_S3, Zeta.W_S3])]

t = list(range(0,20))
plt.plot(t, A, color = Alphacolor)
plt.plot(t, B, color = Betacolor)
plt.plot(t, I, color = Gammacolor)
plt.plot(t, J, color = Deltacolor)
plt.plot(t, N, color = Epsiloncolor)
plt.plot(t, U, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenarios 1, 2 and 3')
plt.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.tight_layout()
plt.savefig('40 - TotalEnergy_Total.png')
plt.show()

#Total Solar
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[Alpha.S_S1,  Alpha.S_S2,  Alpha.S_S3])]
B = [sum(x) for x in zip(*[Beta.S_S1,  Beta.S_S2,  Beta.S_S3])]
I = [sum(x) for x in zip(*[Gamma.S_S1,  Gamma.S_S2,  Gamma.S_S3])]
J = [sum(x) for x in zip(*[Delta.S_S1,  Delta.S_S2,  Delta.S_S3])]
N = [sum(x) for x in zip(*[Epsilon.S_S1,  Epsilon.S_S2,  Epsilon.S_S3])]
U = [sum(x) for x in zip(*[Zeta.S_S1,  Zeta.S_S2,  Zeta.S_S3])]
t = list(range(0,20))
plt.plot(t, A, color = Alphacolor)
plt.plot(t, B, color = Betacolor)
plt.plot(t, I, color = Gammacolor)
plt.plot(t, J, color = Deltacolor)
plt.plot(t, N, color = Epsiloncolor)
plt.plot(t, U, color = Zetacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Solar Energy All Scenarios')
plt.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('41 - TotalEnergy_Solar.png')
plt.show()


#Total Wind
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[ Alpha.W_S1,  Alpha.W_S2,  Alpha.W_S3])]
B = [sum(x) for x in zip(*[Beta.W_S1,  Beta.W_S2,  Beta.W_S3])]
I = [sum(x) for x in zip(*[Gamma.W_S1,  Gamma.W_S2,  Gamma.W_S3])]
J = [sum(x) for x in zip(*[Delta.W_S1,  Delta.W_S2,  Delta.W_S3])]
N = [sum(x) for x in zip(*[Epsilon.W_S1,  Epsilon.W_S2,  Epsilon.W_S3])]
U = [sum(x) for x in zip(*[Zeta.W_S1,  Zeta.W_S2,  Zeta.W_S3])]
t = list(range(0,20))
plt.plot(t, A, color = Alphacolor)
plt.plot(t, B, color = Betacolor)
plt.plot(t, I, color = Gammacolor)
plt.plot(t, J, color = Deltacolor)
plt.plot(t, N, color = Epsiloncolor)
plt.plot(t, U, color = Zetacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Wind Energy All Scenarios')
plt.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('42 - TotalEnergy_Wind.png')
plt.show()

#Scenario 0
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[Alpha.S_S0, Alpha.W_S0])]
B = [sum(x) for x in zip(*[Beta.S_S0, Beta.W_S0])]
I = [sum(x) for x in zip(*[Gamma.S_S0, Gamma.W_S0])]
J = [sum(x) for x in zip(*[Delta.S_S0, Delta.W_S0])]
N = [sum(x) for x in zip(*[Epsilon.S_S0, Epsilon.W_S0])]
U = [sum(x) for x in zip(*[Zeta.S_S0, Zeta.W_S0])]

t = list(range(0,20))
plt.plot(t, A, color = Alphacolor)
plt.plot(t, B, color = Betacolor)
plt.plot(t, I, color = Gammacolor)
plt.plot(t, J, color = Deltacolor)
plt.plot(t, N, color = Epsiloncolor)
plt.plot(t, U, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenario 0')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('43 - TotalEnergy_S0.png')
plt.show()

#Scenario 1
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[Alpha.S_S1, Alpha.W_S1])]
B = [sum(x) for x in zip(*[Beta.S_S1, Beta.W_S1])]
I = [sum(x) for x in zip(*[Gamma.S_S1, Gamma.W_S1])]
J = [sum(x) for x in zip(*[Delta.S_S1, Delta.W_S1])]
N = [sum(x) for x in zip(*[Epsilon.S_S1, Epsilon.W_S1])]
U = [sum(x) for x in zip(*[Zeta.S_S1, Zeta.W_S1])]

t = list(range(0,20))
plt.plot(t, A, color = Alphacolor)
plt.plot(t, B, color = Betacolor)
plt.plot(t, I, color = Gammacolor)
plt.plot(t, J, color = Deltacolor)
plt.plot(t, N, color = Epsiloncolor)
plt.plot(t, U, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenario 1')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('44 - TotalEnergy_S1.png')
plt.show()

#Scenario 2
fig, ax = plt.subplots()
A = [sum(x) for x in zip(*[Alpha.S_S2, Alpha.W_S2])]
B = [sum(x) for x in zip(*[Beta.S_S2, Beta.W_S2])]
I = [sum(x) for x in zip(*[Gamma.S_S2, Gamma.W_S2])]
J = [sum(x) for x in zip(*[Delta.S_S2, Delta.W_S2])]
N = [sum(x) for x in zip(*[Epsilon.S_S2, Epsilon.W_S2])]
U = [sum(x) for x in zip(*[Zeta.S_S2, Zeta.W_S2])]

t = list(range(0,20))
plt.plot(t, A, color = Alphacolor)
plt.plot(t, B, color = Betacolor)
plt.plot(t, I, color = Gammacolor)
plt.plot(t, J, color = Deltacolor)
plt.plot(t, N, color = Epsiloncolor)
plt.plot(t, U, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenario 2')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('45 - TotalEnergy_S2.png')
plt.show()


#Scenario 3
ffig, ax = plt.subplots()
A = [sum(x) for x in zip(*[Alpha.S_S3, Alpha.W_S3])]
B = [sum(x) for x in zip(*[Beta.S_S3, Beta.W_S3])]
I = [sum(x) for x in zip(*[Gamma.S_S3, Gamma.W_S3])]
J = [sum(x) for x in zip(*[Delta.S_S3, Delta.W_S3])]
N = [sum(x) for x in zip(*[Epsilon.S_S3, Epsilon.W_S3])]
U = [sum(x) for x in zip(*[Zeta.S_S3, Zeta.W_S3])]

t = list(range(0,20))
plt.plot(t, A, color = Alphacolor)
plt.plot(t, B, color = Betacolor)
plt.plot(t, I, color = Gammacolor)
plt.plot(t, J, color = Deltacolor)
plt.plot(t, N, color = Epsiloncolor)
plt.plot(t, U, color = Zetacolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Scenario 3')
plt.legend(["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('46 - TotalEnergy_S3.png')
plt.show()


######################################
##Energy By Country
######################################
#Alpha
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Alpha.S_S1, Alpha.S_S2, Alpha.S_S3])]
w1 = [sum(x) for x in zip(*[Alpha.W_S1, Alpha.W_S2, Alpha.W_S3])]
solar1 = ax.plot(t, s1, color = Zetacolor)
Wind = ax.plot(t, w1, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Alpha - Total energy')
plt.legend(["Solar", "Wind"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('47 - AlphaEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Alpha.S_S1])]
s2 = [sum(x) for x in zip(*[Alpha.S_S2])]
s3 = [sum(x) for x in zip(*[Alpha.S_S3])]
st = [sum(x) for x in zip(*[Alpha.S_S1, Alpha.S_S2, Alpha.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('Alpha - Solar energy generation')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('47a - AlphaEnergy-solar.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[Alpha.W_S1])]
w2 = [sum(x) for x in zip(*[Alpha.W_S2])]
w3 = [sum(x) for x in zip(*[Alpha.W_S3])]
wt = [sum(x) for x in zip(*[Alpha.W_S1, Alpha.W_S2, Alpha.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('Alpha - Wind energy generation')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.tight_layout()
plt.savefig('47b - AlphaEnergy-wind.png')
plt.show()


#Beta
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Beta.S_S1, Beta.S_S2, Beta.S_S3])]
w1 = [sum(x) for x in zip(*[Beta.W_S1, Beta.W_S2, Beta.W_S3])]
solar1 = ax.plot(t, s1, color = Zetacolor)
Wind = ax.plot(t, w1, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Beta - Total energy')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('48 - BetaEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Beta.S_S1])]
s2 = [sum(x) for x in zip(*[Beta.S_S2])]
s3 = [sum(x) for x in zip(*[Beta.S_S3])]
st = [sum(x) for x in zip(*[Beta.S_S1, Beta.S_S2, Beta.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('Beta - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('48a - BetaEnergy - solar.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[Beta.W_S1])]
w2 = [sum(x) for x in zip(*[Beta.W_S2])]
w3 = [sum(x) for x in zip(*[Beta.W_S3])]
wt = [sum(x) for x in zip(*[Beta.W_S1, Beta.W_S2, Beta.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('Beta - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('48b - BetaEnergy - wind.png')
plt.show()

#Gamma
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Gamma.S_S1, Gamma.S_S2, Gamma.S_S3])]
w1 = [sum(x) for x in zip(*[Gamma.W_S1, Gamma.W_S2, Gamma.W_S3])]
solar1 = ax.plot(t, s1, color = Zetacolor)
Wind = ax.plot(t, w1, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Gamma - Total energy')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('49 - GammaEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Gamma.S_S1])]
s2 = [sum(x) for x in zip(*[Gamma.S_S2])]
s3 = [sum(x) for x in zip(*[Gamma.S_S3])]
st = [sum(x) for x in zip(*[Gamma.S_S1, Gamma.S_S2, Gamma.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('Gamma - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('49a - GammaEnergy - solar.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[Gamma.W_S1])]
w2 = [sum(x) for x in zip(*[Gamma.W_S2])]
w3 = [sum(x) for x in zip(*[Gamma.W_S3])]
wt = [sum(x) for x in zip(*[Gamma.W_S1, Gamma.W_S2, Gamma.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('Gamma - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.tight_layout()
plt.savefig('49b - GammaEnergy - wind.png')
plt.show()

#Delta
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Delta.S_S1, Delta.S_S2, Delta.S_S3])]
w1 = [sum(x) for x in zip(*[Delta.W_S1, Delta.W_S2, Delta.W_S3])]
solar1 = ax.plot(t, s1, color = Zetacolor)
Wind = ax.plot(t, w1, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Delta - Total energy')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('50 - DeltaEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Delta.S_S1])]
s2 = [sum(x) for x in zip(*[Delta.S_S2])]
s3 = [sum(x) for x in zip(*[Delta.S_S3])]
st = [sum(x) for x in zip(*[Delta.S_S1, Delta.S_S2, Delta.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('Delta - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('50a - DeltaEnergy - solar.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[Delta.W_S1])]
w2 = [sum(x) for x in zip(*[Delta.W_S2])]
w3 = [sum(x) for x in zip(*[Delta.W_S3])]
wt = [sum(x) for x in zip(*[Delta.W_S1, Delta.W_S2, Delta.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)


plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('Delta - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('50b - DeltaEnergy - wind.png')
plt.show()

#Epsilon
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Epsilon.S_S1, Epsilon.S_S2, Epsilon.S_S3])]
w1 = [sum(x) for x in zip(*[Epsilon.W_S1, Epsilon.W_S2, Epsilon.W_S3])]
solar1 = ax.plot(t, s1, color = Zetacolor)
Wind = ax.plot(t, w1, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Epsilon - Total energy')
plt.legend(["Solar", "Wind"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('51.1 - EpsilonEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Epsilon.S_S1, Epsilon.S_S2, Epsilon.S_S3])]
w1 = [sum(x) for x in zip(*[Epsilon.W_S1, Epsilon.W_S2, Epsilon.W_S3])]
solar1 = ax.plot(t, s1, color = Zetacolor)
Wind = ax.plot(t, w1, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Epsilon - Total energy')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('51.2 - EpsilonEnergy.png')
plt.show()


fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Epsilon.S_S1])]
s2 = [sum(x) for x in zip(*[Epsilon.S_S2])]
s3 = [sum(x) for x in zip(*[Epsilon.S_S3])]
st = [sum(x) for x in zip(*[Epsilon.S_S1, Epsilon.S_S2, Epsilon.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('Epsilon - Solar energy generation')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('51a - EpsilonEnergy - solar.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[Epsilon.W_S1])]
w2 = [sum(x) for x in zip(*[Epsilon.W_S2])]
w3 = [sum(x) for x in zip(*[Epsilon.W_S3])]
wt = [sum(x) for x in zip(*[Epsilon.W_S1, Epsilon.W_S2, Epsilon.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('Epsilon - Wind energy generation')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('51b - EpsilonEnergy - wind.png')
plt.show()


#Zeta
fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Zeta.S_S1, Zeta.S_S2, Zeta.S_S3])]
w1 = [sum(x) for x in zip(*[Zeta.W_S1, Zeta.W_S2, Zeta.W_S3])]
solar1 = ax.plot(t, s1, color = Zetacolor)
Wind = ax.plot(t, w1, color = Deltacolor)
plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Energy Production (100MWh)')
plt.title('Zeta - Total energy')
plt.legend(["Solar", "Wind"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('52 - ZetaEnergy.png')
plt.show()

fig, ax = plt.subplots()
t = list(range(0,20))
s1 = [sum(x) for x in zip(*[Zeta.S_S1])]
s2 = [sum(x) for x in zip(*[Zeta.S_S2])]
s3 = [sum(x) for x in zip(*[Zeta.S_S3])]
st = [sum(x) for x in zip(*[Zeta.S_S1, Zeta.S_S2, Zeta.S_S3])]
solar1 = ax.plot(t, s1, color = FITcolor)
solar2 = ax.plot(t, s2, color = TAXcolor)
solar3 = ax.plot(t, s3, color = TGCcolor)
solar = ax.plot(t, st, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Solar Energy Production (100MWh)')
plt.title('Zeta - Solar')
plt.legend(["solar FIT", "Solar TAX", "Solar TGC", "Solar Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('52a - ZetaEnergy - solar.png')
plt.show()

fig, ax = plt.subplots()
w1 = [sum(x) for x in zip(*[Zeta.W_S1])]
w2 = [sum(x) for x in zip(*[Zeta.W_S2])]
w3 = [sum(x) for x in zip(*[Zeta.W_S3])]
wt = [sum(x) for x in zip(*[Zeta.W_S1, Zeta.W_S2, Zeta.W_S3])]
wind1 = ax.plot(t, w1, color = FITcolor)
wind2 = ax.plot(t, w2, color = TAXcolor)
wind3 = ax.plot(t, w3, color = TGCcolor)
wind = plt.plot(t, wt, '--', color = TOTALcolor)

plt.xlabel('Years')
plt.xticks(list(range(1,21)))
plt.ylabel('Total Wind Energy Production (KWh)')
plt.title('Zeta - Wind')
plt.legend(["Wind FIT", "Wind TAX", "Wind TGC", "Wind Total"], loc='upper left', fancybox=True, shadow=True)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.savefig('52b - ZetaEnergy - wind.png')
plt.show()


######################################
###Ratio By Country
#####################################
##TOTAL
ft_I = Alpha.RFIT_I + Beta.RFIT_I + Gamma.RFIT_I + Delta.RFIT_I + Epsilon.RFIT_I + Zeta.RFIT_I
tx_I = Alpha.RTAX_I + Beta.RTAX_I + Gamma.RTAX_I + Delta.RTAX_I + Epsilon.RTAX_I + Zeta.RTAX_I
tc_I = Alpha.RTGC_I + Beta.RTGC_I + Gamma.RTGC_I + Delta.RTGC_I + Epsilon.RTGC_I + Zeta.RTGC_I

ft_En = Alpha.RFIT_En + Beta.RFIT_En + Gamma.RFIT_En + Delta.RFIT_En + Epsilon.RFIT_En + Zeta.RFIT_En
tx_En = Alpha.RTAX_En + Beta.RTAX_En + Gamma.RTAX_En + Delta.RTAX_En + Epsilon.RTAX_En + Zeta.RTAX_En
tc_En = Alpha.RTGC_En + Beta.RTGC_En + Gamma.RTGC_En + Delta.RTGC_En + Epsilon.RTGC_En + Zeta.RTGC_En

RFIT = ft_I/ft_En
RTAX = tx_I/tx_En
RTGC = tc_I/tc_En

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
#plt.legend(labels, loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for each incentive in Total')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.tight_layout()
plt.savefig('53 - RATIO_Total.png')
plt.show()

##Alpha - Com + Gov
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [Alpha.RFIT, Alpha.RTAX, Alpha.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
plt.title('LCOE for incentives in Alpha - Total Investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('54 - RATIO_Alpha.png')
plt.show()

##Alpha - Com
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [(Alpha.RFITIC/Alpha.RFIT_En), (Alpha.RTAXIC/Alpha.RTAX_En), (Alpha.RTGCIC/Alpha.RTGC_En)]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(labels, loc='upper right', bbox_to_anchor=(+1, +0.3), fancybox=True, shadow=True)
plt.title('LCOE for incentives in Alpha - Only community investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('55 - RATIO_Alpha_com.png')
plt.show()

##Beta - Com + Gov
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [Beta.RFIT, Beta.RTAX, Beta.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(labels, loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for incentives in Beta - Total Investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('56 - RATIO_Beta.png')
plt.show()

##Beta - Com
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [(Beta.RFITIC/Beta.RFIT_En), (Beta.RTAXIC/Beta.RTAX_En), (Beta.RTGCIC/Beta.RTGC_En)]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(labels, loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for incentives in Beta - Only community investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('57 - RATIO_Beta_com.png')
plt.show()

##Gamma - Com + Gov
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [Gamma.RFIT, Gamma.RTAX, Gamma.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(['FIT','TAX', 'TGC'], loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for incentives in Gamma - Total Investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('58- RATIO_Gamma.png')
plt.show()


##Gamma - Com
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [(Gamma.RFITIC/Gamma.RFIT_En), (Gamma.RTAXIC/Gamma.RTAX_En), (Gamma.RTGCIC/Gamma.RTGC_En)]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(['FIT','TAX', 'TGC'], loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for incentives in Gamma - Only community investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('59 - RATIO_Gamma_com.png')
plt.show()

##Delta - Com + Gov
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [Delta.RFIT, Delta.RTAX, Delta.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(['FIT','TAX', 'TGC'], loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for incentives in Delta - Total Investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('60 - RATIO_Delta.png')
plt.show()

##Delta - Com
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [(Delta.RFITIC/Delta.RFIT_En), (Delta.RTAXIC/Delta.RTAX_En), (Delta.RTGCIC/Delta.RTGC_En)]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(['FIT','TAX', 'TGC'], loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for incentive in Delta - Only community investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('61 - RATIO_Delta_com.png')
plt.show()


#Epsilon - Com + Gov
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [Epsilon.RFIT, Epsilon.RTAX, Epsilon.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(['FIT','TAX', 'TGC'], loc='upper right', bbox_to_anchor=(+1, +0.3), fancybox=True, shadow=True)
plt.title('LCOE for incentives in Epsilon - Total Investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('62 - RATIO_Epsilon.png')
plt.show()

#Epsilon - Com
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [(Epsilon.RFITIC/Epsilon.RFIT_En), (Epsilon.RTAXIC/Epsilon.RTAX_En), (Epsilon.RTGCIC/Epsilon.RTGC_En)]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(['FIT','TAX', 'TGC'], loc='upper right', bbox_to_anchor=(+1, +0.3), fancybox=True, shadow=True)
plt.title('LCOE for incentive in Epsilon - Only community investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('63 - RATIO_Epsilon_com.png')
plt.show()

#Zeta - Com + Gov
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [Zeta.RFIT, Zeta.RTAX, Zeta.RTGC]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(['FIT','TAX', 'TGC'], loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for incentives in Zeta - Total Investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('64 - RATIO_Zeta.png')
plt.show()

#Zeta - Com
fig, ax = plt.subplots()
labels = ['FIT', 'TAX', 'TGC']
x_pos = np.arange(len(labels))
sizes = [(Zeta.RFITIC/Zeta.RFIT_En), (Zeta.RTAXIC/Zeta.RTAX_En), (Zeta.RTGCIC/Zeta.RTGC_En)]
colors = ["Green", 'cyan', 'yellow']
bars1, = plt.bar(x_pos[0],sizes[0], color = FITcolor, align = 'center', alpha = 0.8)
bars2, = plt.bar(x_pos[1],sizes[1], color = TAXcolor, align = 'center', alpha = 0.8)
bars3, = plt.bar(x_pos[2],sizes[2], color = TGCcolor, align = 'center', alpha = 0.8)
plt.xticks(x_pos, labels)
plt.xlabel('Financial Incentive', fontsize=14)
plt.ylabel('USD/KWh', fontsize=14)
#plt.legend(['FIT','TAX', 'TGC'], loc='upper right', fancybox=True, shadow=True)
plt.title('LCOE for incentive in Zeta - Only community investment')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
bars = [bars1, bars2, bars3]
autolabel(bars)
plt.savefig('65 - RATIO_Zeta_com.png')
plt.show()


