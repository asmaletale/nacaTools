import pandas
import pandas as pd
import numpy as np
import os
import shutil
#THIS SCRIPT REQUIRES  THE IBLE FILES WITHOUT THE HEADER
fileList=["naca4510_a167_l67","naca4510_a167_l67_bsk_55","naca4510_a167_l67_fsk_55","naca4510_straight_le","naca4510_straight_le_bsk_55","naca4510_straight_le_fsk_55"]
for folder in fileList:
    full_path = os.path.join("iblSource",folder)
    if not os.path.exists(full_path):
        os.mkdir(full_path)

fileNames=[r"iblSource/"+i +r".ibl" for i in fileList]
#bladeFileNames=[r"iblSource/"+i +r"-fullBlade.txt" for i in fileList]
print(fileList)
print(fileNames)
for f,file in enumerate(fileNames):
    print(file)
    bigfile= open(file,"r")
    reader = bigfile.read()
    profList=[]
    #bladeFile=open(bladeFileNames[f],"r")
    for i, part in enumerate(reader.split("begin curve !")):
        newProfile=[]
        if i>0:
            newfile=open(r"iblSource\\"+fileList[f]+'\profile_' + str(i)+'.txt',"w+")
            part=part[part.find('\n')+1:]
            points=part.split("\n")
            for p,point in enumerate(points):
                coords=point.split("\t")
                newProfile.append(coords)
            half_length = len(points) // 2
            first_half, second_half = newProfile[:half_length], newProfile[half_length:]
            first_half.append(second_half[0])#!!! aggiungo al LE il primo punto della seconda metà così fa dei loft sovrapposti. Attenzione, funziona solo se parto da TE a TE
            pdpart=pd.DataFrame(newProfile)
            ss=pd.DataFrame(data=first_half)
            ps=pd.DataFrame(data=second_half)
            ss.to_csv(r"iblSource\\" + fileList[f] +'\profile_SS_' + str(i)+'.txt', sep="\t", header=False, index=False)
            ps.to_csv(r"iblSource\\" + fileList[f] + '\profile_PS_' + str(i)+'.txt', sep="\t", header=False, index=False)
            newfile.write(part)
            profList.append(pdpart)
    blade=pd.concat(profList,axis=0)
    blade.to_csv(r"iblSource\\"+fileList[f]+'-fullBlade.txt',sep="\t",header=False,index=False)
    print("")

