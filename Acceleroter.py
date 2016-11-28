import matplotlib.pyplot as plt
import os
import numpy as np 
from dtw import dtw
from filters import LPF,HPF,meanF
from readFiles import readFile

#acceleroDataPath = '/home/dash/Pictures/sensorData/2016_11_25/acceleroData'
acceleroDataPath = '/home/dash/Pictures/sensorData/acce'
win=5

def lines(lineType,value,num):
	X = []
	Y = []
	if lineType == 'row':
		for i in xrange(0,num):
			X.append(i)
			Y.append(value)
	elif lineType == 'col':
		for i in xrange(0,num):
			Y.append(i)
			X.append(value)
	return X,Y
def findMaxMin(dataArray):
	px = []
	peaks = []
	tx = []
	troughs = []
	ThresholdUP = 3.2
	ThresholdLOW = 1.5

	peak = 3
	trough = 0

 	pt = []
	for idx in range(1, len(dataArray)-1):
		if dataArray[idx-1] < dataArray[idx] > dataArray[idx+1]:
			if dataArray[idx] > ThresholdUP:
				px.append(idx)
				peaks.append(dataArray[idx])
				peak = dataArray[idx]
		if dataArray[idx-1] > dataArray[idx] < dataArray[idx+1]:
			if dataArray[idx] < ThresholdLOW:
				tx.append(idx)
				troughs.append(dataArray[idx])
				trough = dataArray[idx]
		pt.append((peak+trough)/2)
	return px,peaks,tx,troughs,pt

#plot 1 lines
def plotLine1(b):
	plt.subplot()

	plt.plot(b,'b-',linewidth=2)
	plt.xlim(1, len(b))

	plt.ylabel('m/s^2')
	plt.xlabel('samples')
	plt.legend()
	plt.show()

#plot 1 lines
def plotLine(a):
	plt.subplot()

	plt.plot(a,'b-^',label="$Acceleration$",linewidth=2)
	#plt.plot(b,'r-',linewidth=2)
	plt.xlim(1, len(a))
	
	#plt.ylim(34,45)
	X,Y = lines('col',3,7)
	plt.plot(X,Y,'r',linewidth=1.5)
	X1,Y1 = lines('col',10,7)
	plt.plot(X1,Y1,'r',linewidth=1.5)
	
	px, peaks,tx,troughs,pt = findMaxMin(a)

	plt.scatter(px,peaks, marker = '*',color = 'r', s = 50)
	#plt.scatter(tx,troughs, marker = 'o',color = 'm', s = 50)
	plt.plot(pt,'m-',label="$Threshold$",linewidth=2)
	plt.ylabel('m/s^2')
	plt.xlabel('samples')
	plt.legend()
	plt.show()
#####
def plotLine2(a,b):
	plt.subplot(211)
	plt.plot(a,'b-',linewidth=2.0)
	plt.ylabel('m/s^2')
	plt.title('Raw data')
	plt.xlim(1, len(a))	
	plt.subplot(212)
	plt.plot(b,'k-',linewidth=1.5)
	plt.xlim(1, len(b))
	plt.title('After filtered')	
	plt.ylabel('m/s^2')
	plt.xlabel('samples')
	plt.legend()
	plt.show()
#plot 3 line
def plotLine3(x,y,z):
	plt.figure(1)


	plt.plot(x,'k-',label="$X$",linewidth=1.5)
	plt.plot(y,'m-',label="$Y$",linewidth=1.5)
	plt.plot(z,'b-',label="$Z$",linewidth=1.5)
	plt.xlabel('samples')
	plt.ylabel('m/s^2')
	#plt.ylim(-5,18)
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

	BH2x,BH2y,BH2z,BH2xyz=readFile(acceleroDataPath,'BC.txt')
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
	#plotNlines(AlistRaw,AlistLPF)	
	#plotLine3(BH2x,BH2y,BH2z)
	#plotLine1(BH2xyz)
	BH2xyzm=meanF(BH2xyz,win)
	#lxyz = LPF(BH2xyzm)
	#plotLine2(BH2xyz,BH2xyzm)
	
	plotLine(BH2xyzm)


if __name__ == '__main__':
	main()
