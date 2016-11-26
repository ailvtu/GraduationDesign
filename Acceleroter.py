import matplotlib.pyplot as plt
import os
import numpy as np 
from dtw import dtw
from filters import LPF,HPF,meanF
from readFiles import readFile

acceleroDataPath = '/home/dash/Pictures/sensorData/2016_11_25/acceleroData'
win=5
#plot 1 lines
def plotLine(g):
	plt.subplot()
	plt.plot(g,'b-',linewidth=2)
	plt.xlim(1, len(g))
	#plt.ylim(34,45)	
	plt.ylabel('intensity/uT')
	#plt.xlabel('distance/dm')
	plt.legend()
	plt.show()

#plot 3 line
def plotLine3(x,y,z):
	plt.figure(1)

#	plt.plot(x[1:65],'r-*',label="$left$",linewidth=2)
#	plt.plot(y[1:65],'g-o',label="$midle$",linewidth=2)
#	plt.plot(z[1:65],'b-^',label="$right$",linewidth=2)

	plt.plot(x,'k-',label="$X$",linewidth=1.5)
	plt.plot(y,'m-',label="$Y$",linewidth=1.5)
	plt.plot(z,'b-',label="$Z$",linewidth=1.5)
	#plt.xlabel('distance/dm')
	plt.ylabel('m/s2')
	plt.ylim(-5,18)
	#plt.xlim(0, 65)		
	#plt.title('gallery magnetic field')
	plt.legend()
	plt.show()


def plotNlines(dataList1,dataList2):
	plt.subplot(211)
	i = 0
	for data in dataList1:
		plt.plot(data,linewidth=1.5)
		i=i+1
	plt.ylabel('m/s2')
	plt.subplot(212)
	i = 0
	for data2 in dataList2:
		plt.plot(data2,linewidth=1.5)
		i=i+1
	#plt.ylim(-5,20)
	plt.ylabel('m/s2')
	plt.legend()
	plt.show()

def main():

	BH2x,BH2y,BH2z,BH2xyz=readFile(acceleroDataPath,'BH2.txt')
	label=['x','Y','Z','D']
	AlistRaw = [BH2x,BH2y,BH2z,BH2xyz]
	#JZx,JZy,JZz,JZxyz=readFile('jiaozheng.txt')#path 1123
	#plotNlines(AlistRaw,label)
#############
	AlistMean = []
	AlistLPF = []
	for data in AlistRaw:
		AlistMean.append(meanF(data,win))
	for data2 in AlistMean:
		AlistLPF.append(LPF(data2))
	plotNlines(AlistRaw,AlistLPF)	
	#plotLine3(BH2x,BH2y,BH2z)




if __name__ == '__main__':
	main()
