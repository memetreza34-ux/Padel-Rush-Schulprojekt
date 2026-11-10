#!/usr/bin/env python3
"""Prüft die fiktiven Padel-Rush-Finanzzahlen der Schulpräsentation (kein echter Business-Case)."""
K=240000; APR=.07; N=96; VAT=1.19; FEE=.02; WEAR=.5; FIX=20500
ANN=K*(APR/12)/(1-(1+APR/12)**(-N))
OFFERS={
 "starter":(116,1.5,49),"academy":(90,1,37),"social":(144,3,21),
 "league":(2064,42,220),"tournament":(1120,16,280),"business":(599,6,195)
}
WEAK=dict(starter=4,academy=8,social=4,league=0,tournament=0,business=2)
MID=dict(starter=6,academy=12,social=6,league=4/7,tournament=0,business=3)
BASE=dict(starter=8,academy=16,social=8,league=4/7,tournament=1,business=4)
BEST=dict(BASE,business=6)
def calc(occupancy,price,mix):
 hours=1680*occupancy
 eventh=sum(OFFERS[k][1]*n for k,n in mix.items())
 assert eventh<=hours
 gross_e=sum(OFFERS[k][0]*n for k,n in mix.items())
 direct_e=sum((OFFERS[k][0]*FEE+OFFERS[k][1]*WEAR+OFFERS[k][2])*n for k,n in mix.items())
 regular=hours-eventh
 gross_r=regular*price
 net=(gross_r+gross_e)/VAT
 direct=direct_e+gross_r*FEE+regular*WEAR
 return net,direct,net-direct-FIX,eventh,regular
def validate():
 assert abs(ANN-3272.09209932)<0.01
 net,cost,sur,ev,reg=calc(.45,34,BASE)
 assert abs(net-25189.43577)<0.01
 assert abs(cost-3315.22286)<0.01
 assert abs(sur-1374.21292)<0.01
 assert abs(ev-116)<1e-6 and abs(reg-640)<1e-6
 assert abs(calc(.25,32,WEAK)[2]+9221.6568067)<0.01
 assert abs(calc(.55,36,BEST)[2]-7540.0135894)<0.01
 m=[.25,.28,.30,.32,.35,.37,.40,.42,.45,.46,.48,.50]
 results=[calc(oc,32 if i<3 else 33 if i<7 else 34,WEAK if i<3 else MID if i<7 else BASE)[2] for i,oc in enumerate(m)]
 assert abs(sum(results)+28931.6152413)<0.01
 bal=50000
 lowest=50000
 for x in results:
  bal+=x
  lowest=min(lowest,bal)
 assert abs(lowest-11429.949090)<0.01
 costs_e=sum((OFFERS[k][0]*FEE+OFFERS[k][1]*WEAR+OFFERS[k][2])*n for k,n in BASE.items())
 g_e=sum(OFFERS[k][0]*n for k,n in BASE.items())
 needed=(FIX+costs_e-g_e/VAT)/(34/VAT-34*FEE-WEAR)
 be=(needed+116)/1680
 assert abs(be-0.4201372319)<0.0000001
 print("OK: Darlehen, Szenarien, Courtstunden, Jahresanlauf und Break-even stimmen.")
 print("Basis: %.2f EUR vor weiteren Steuern und nicht erfassten Kosten"%sur)
 print("Break-even (konstante Eventbelegung): %.2f %%"%(be*100))
 print("Minimaler 50.000-Euro-Reservebestand: %.2f EUR"%lowest)
if __name__=="__main__":
 validate()
