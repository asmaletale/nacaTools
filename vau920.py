# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd
from nacaManager import naca4dig as n4
from nacaManager import profileInfo as profiles


blade=profiles("profileInfoVAU920.txt",fileSep="\t")
nProfiles=len(blade.info)
deltaChordFactorLE=0.1
cutExtraChord=True
deltaAOA=0.05
reducedChord=True
reducedTip=0.9
startSpan=0.0
#MODIFICARE: METTI DENTRO IL LOOP, LEGGI IL PROFILO DA PROFILE INFO, USA UN SOLO COSTRUTTORE
# sec10=n4(8,4,0,5)
# sec9=n4(8,4,0,5)
# sec8=n4(8,4,0,6)
# sec7=n4(8,4,0,6)
# sec6=n4(8,4,0,7)
# sec5=n4(8,4,0,8)
# sec4=n4(8,4,0,8)
# sec3=n4(8,4,0,8)
# sec2=n4(8,4,0,8)
# sec1=n4(8,4,0,8)


sec10=n4(8,4,0,8)
sec9=n4(8,4,0,8)
sec8=n4(8,4,0,8)
sec7=n4(8,4,0,8)
sec6=n4(8,4,0,8)
sec5=n4(8,4,0,8)
sec4=n4(8,4,0,8)
sec3=n4(8,4,0,8)
sec2=n4(8,4,0,8)
sec1=n4(8,4,0,8)


# sec10=n4(8,5,0,5)
# sec9=n4(8,5,0,5)
# sec8=n4(8,5,0,6)
# sec7=n4(8,5,0,6)
# sec6=n4(8,5,0,7)
# sec5=n4(8,5,0,8)
# sec4=n4(8,5,0,8)
# sec3=n4(8,5,0,8)
# sec2=n4(8,5,0,8)
# sec1=n4(8,5,0,8)

# sec10=n4(7,5,0,5)
# sec9=n4(7,5,0,5)
# sec8=n4(7,5,0,6)
# sec7=n4(7,5,0,6)
# sec6=n4(7,5,0,7)
# sec5=n4(7,5,0,8)
# sec4=n4(7,5,0,8)
# sec3=n4(7,5,0,8)
# sec2=n4(7,5,0,8)
# sec1=n4(7,5,0,8)

# sec10=n4(7,4,0,5)
# sec9=n4(7,4,0,5)
# sec8=n4(7,4,0,6)
# sec7=n4(7,4,0,6)
# sec6=n4(7,4,0,7)
# sec5=n4(7,4,0,8)
# sec4=n4(7,4,0,8)
# sec3=n4(7,4,0,8)
# sec2=n4(7,4,0,8)
# sec1=n4(7,4,0,8)

# sec10=n4(4,4,0,5)
# sec9=n4(4,4,0,5)
# sec8=n4(4,4,0,6)
# sec7=n4(4,4,0,6)
# sec6=n4(4,4,0,7)
# sec5=n4(4,4,0,8)
# sec4=n4(4,4,0,8)
# sec3=n4(4,4,0,8)
# sec2=n4(4,4,0,8)
# sec1=n4(4,4,0,8)

#profile List tip to root
profileList=[sec10,sec9,sec8,sec7,sec6,sec5,sec4,sec3,sec2,sec1]
blade.info["profiles"]=profileList
profileConcat=[]
c_max=np.max(blade.info["chord"])
z_max=np.max(blade.info["z"])
z_min=np.min(blade.info["z"])
for i in range(nProfiles):
    infoi=blade.info.iloc[i]
    nacai=infoi["profiles"]
    chord=infoi["chord"]
    angle=infoi["a1"]
    x=infoi["x"]
    y=infoi["y"]
    z=infoi["z"]

    if reducedChord:
        chord=nacai.reduceChord(z,c_max,z_max,z_min,startSpan=startSpan, reducedTip=reducedTip)

    extraChord=chord*deltaChordFactorLE
    nacai.scaleByChord(chord+extraChord)
    print("")
    if cutExtraChord:
        nacai.newCoords=nacai.newCoords[nacai.baseCoords["x"].lt(1-deltaChordFactorLE)]
        print("")
    extraAngle=np.pi/2*0.015
    nacai.rotate(-extraAngle)
    nacai.shift(xShift=-chord / 2)
    nacai.symmetry("y")
    nacai.rotate(-(np.pi/2 - angle))
    #nacai.rotate(-(90 - angle))
    nacai.shift(xShift=x, yShift=y)
    nacai.addZ(z)
    profileConcat.append(nacai.newCoords)
    nacai.printTransformedNaca("nacaTransf/"+str("VAU920")+"_T"+str(nProfiles-i)+".txt")

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

