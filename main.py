# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd
from nacaManager import naca4dig as n4
from nacaManager import profileInfo as profiles


blade=profiles("profileInfo.txt")
nProfiles=len(blade.info)
#MODIFICARE: METTI DENTRO IL LOOP, LEGGI IL PROFILO DA PROFILE INFO, USA UN SOLO COSTRUTTORE
sec10=n4(4,4,0,6)
sec9=n4(4,4,0,6)
sec8=n4(4,4,0,7)
sec7=n4(4,4,0,8)
sec6=n4(4,4,1,0)
sec5=n4(4,4,1,1)
sec4=n4(4,4,1,2)
sec3=n4(4,4,1,3)
sec2=n4(4,4,1,4)
sec1=n4(4,4,1,5)

#profile List tip to root
profileList=[sec10,sec9,sec8,sec7,sec6,sec5,sec4,sec3,sec2,sec1]
blade.info["profiles"]=profileList
profileConcat=[]
for i in range(nProfiles):
    infoi=blade.info.iloc[i]
    nacai=infoi["profiles"]
    chord=infoi["chord"]
    angle=infoi["a1"]
    x=infoi["x"]
    y=infoi["y"]
    z=infoi["z"]
    nacai.scaleByChord(chord)
    nacai.shift(xShift=-chord / 2)
    nacai.symmetry("x")
    nacai.rotate(-(90 - angle))
    nacai.shift(xShift=-x, yShift=-y)
    nacai.addZ(z)
    profileConcat.append(nacai.newCoords)
    nacai.printTransformedNaca("nacaTransf/"+str(nacai.name)+"_T"+str(nProfiles-i)+".txt")

pdprofile=pd.concat(profileConcat,axis=0)
pdprofile[["x","y","z"]].to_csv("nacaTransf/fullBladePoints.txt", sep=" ", header=False,index=False)

# naca4412.scaleByChord(chord)
# naca4412.shift(xShift=-chord/2)
# naca4412.symmetry("x")
# naca4412.rotate(-(90-angle))
# naca4412.shift(xShift=-x,yShift=-y)
#
#
#
# naca4412.printTransformedNaca("nacaTransf/naca4412_T.txt")


print("done")

