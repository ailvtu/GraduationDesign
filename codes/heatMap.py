from matplotlib import mpl  
import matplotlib.pyplot as plt  
import numpy as np  
import os

from readFiles import readFile
from filters import LPF,HPF,meanF,standard

magneticDataPath = '/home/dash/Pictures/sensorData/4lines'


def reverse(FileName):
	listRe = []
	for dirs in os.listdir(magneticDataPath +FileName):
		print dirs
		CF01x,CF01y,CF01z,CF01xyz = readFile(magneticDataPath +FileName,dirs);
		listRe.append(CF01xyz.reverse())
	return listRe,

def readData(FileName):
	Datalist=[]
	MinLen = []

	for dirs in os.listdir(magneticDataPath +FileName):
		print dirs
		CF01x,CF01y,CF01z,CF01xyz = readFile(magneticDataPath +FileName,dirs);
		Datalist.append(CF01xyz);MinLen.append(len(CF01xyz))
		Datalist.append(CF01xyz);MinLen.append(len(CF01xyz))
	
	minL = min(MinLen)
	return 	minL,Datalist


minLL,CFlist = readData('/FI')
print minLL

hpTest =[]
mCFlist=[]
hpfCFlist=[]
standList = []
for Mdata in CFlist:
	mCFlist.append(meanF(Mdata,5))
for mCF0 in mCFlist:
	hpfCFlist.append(HPF(mCF0[:minLL/5]))
#standList = standard(mCFlist)	
for data in mCFlist:
	standList.append(standard(data))



hpTest = np.array(hpfCFlist)
data=np.clip(hpTest,-3,3) 


fig = plt.figure()  
ax = fig.add_subplot(111)  
im = ax.imshow(data)  
plt.colorbar(im,ticks=[-2,0,2])   
  

 
   
  
plt.show()  