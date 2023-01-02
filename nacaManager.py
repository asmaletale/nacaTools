# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd


class profileInfo:
    def __init__(self,importfile,fileHeader=0,fileSep="\t"):
        self.info=pd.read_csv(importfile,sep=fileSep,header=fileHeader)


class naca4dig:
    def __init__(self,first,second,third,fourth,dim=2,fileSkipRows=1,fileHeader=0,fileSep="\s+",fileComment="#"):
        self.maxCamber=first
        self.maxCamberPos=second
        self.thickness=int(str(third)+str(fourth))
        importfile="nacaDB/naca"+(str(first)+str(second)+str(third)+str(fourth))+".txt"

        # self.baseCoords=pd.read_csv(importfile,sep=fileSep,skiprows=fileSkipRows,names=["x","y"],comment=fileComment)
        self.baseCoords = pd.read_csv(importfile,comment=fileComment,names=["x","y"],sep=fileSep)
        self.newCoords = self.baseCoords
        self.name=int(str(first)+str(second)+str(third)+str(fourth))
        # if len(self.baseCoords)%2==0:
        #     separated=np.split(self.baseCoords,2)
        #     self.baseSS=separated[0]
        #     self.basePS=separated[1]
        # else:
        #     raise ValueError("IMPORTFILE MUST HAVE EVEN POINTS!")


    def scaleByChord(self, chord):

        self.newCoords=self.newCoords*chord

    def rotate(self,angle,rad=True):
        if rad:
            theta = angle
        else:
            theta = np.deg2rad(angle)
        rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        coords=self.newCoords.values
        for i in range(len(coords)):
            point=np.array(coords[i])
            coords[i]=np.dot(rot,point)
        pd.DataFrame(data=coords,columns=["x","y"])

    def translateMidChord(self,x,y):
        self.newCoords["x"] = self.newCoords["x"] + x
        self.newCoords["y"] = self.newCoords["x"] + y

    def printTransformedNaca(self,fileName):
        self.newCoords[["x","y","z"]].to_csv(fileName, sep=" ", header=False,index=False)

    def addZ(self,z):
        self.newCoords["z"]=z

    def shift(self,xShift=0,yShift=0,zShift=0):
        self.newCoords["x"] = self.newCoords["x"] + xShift
        self.newCoords["y"] = self.newCoords["y"] + yShift
        #self.newCoords["z"] = self.newCoords["z"] + zShift

    def symmetry(self,plane):
        self.newCoords[plane]=-self.newCoords[plane]

    def reduceChord(self,z,c_max,z_max,z_min,law="linear",startSpan=0.0,reducedTip=0.9):
        if law=="linear":
            c_min=c_max*reducedTip
            m=(c_max-c_min)/(startSpan*z_max+z_min-z_max)
            return z*m-z_max*m+c_min



