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
####

def findPeakTHreshold(dataArray):
	px = []
	peaks = []
	tx = []
	troughs = []
	ThresholdUP = 3.2
	ThresholdLOW = 1.5

	peak = 3
	trough = 0

 	Threshold = []
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
		Threshold.append((peak+trough)/2)
	return px,peaks,tx,troughs, Threshold
####

def avrAbs(dataArray):
	sumD =0
	for data in dataArray:
		sumD = sumD+abs(data)
	return (sumD/len(dataArray))

def StepSize(dataArray):
	stepFlag = 0
	stepizeList1 = [];stepizeList2 = [];stepizeList3 = [];stepizeList4 = [];
	stepList=[]
	for idx in range(1, len(dataArray)-1):
		stepList.append(dataArray[idx])
		if dataArray[idx-1] < dataArray[idx] > dataArray[idx+1]:
			stepFlag = stepFlag+1
			if stepFlag >= 2:
				maxA = max(stepList)
				minA = min(stepList)
				aver = avrAbs(stepList)

				stepize1 = 0.5*(maxA-minA)** (1./4)
				stepize2 = 2*((aver-minA)/(maxA-minA))
				stepize3 = 0.56*aver** (1./3)
				#stepize4  = 0.25*((maxA-minA)*0.35+(maxA-minA)** (1./4))
				#print stepize1,stepize2,stepize3,stepize4

				stepizeList1.append(stepize1);stepizeList2.append(stepize2)
				stepizeList3.append(stepize3);

				stepFlag = 0
	return stepizeList1,stepizeList2,stepizeList3;
		#if dataArray[idx-1] > dataArray[idx] < dataArray[idx+1]:


#plot 1 lines
def plotLine1(b):
	plt.subplot()

	plt.plot(b,'b-*',linewidth=2)
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
	
	px, peaks,tx,troughs,Threshold = findPeakTHreshold(a)

	plt.scatter(px,peaks, marker = '*',color = 'r', s = 50)
	#plt.scatter(tx,troughs, marker = 'o',color = 'm', s = 50)
	plt.plot(Threshold,'m-',label="$Threshold$",linewidth=2)
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

def plotNline(dataList1,dataList2,dataList3):
	plt.subplot(311)
	i = 0
	colorShape = ['k-*','m-^','b-o','r--','g-o']
	for data in dataList1:
		plt.plot(data,colorShape[i],linewidth=1.5)
		i=i+1
	plt.ylim(0.5,0.8)
	plt.xlim(0,25)
	plt.ylabel('m/step')
	plt.title('Weinberg,Scarlet,Kim')
	plt.subplot(312)
	i = 0
	colorShape = ['k-*','m-^','b-o','r--','g-o']
	for data2 in dataList2:
		plt.plot(data2,colorShape[i],linewidth=1.5)
		i=i+1
	#plt.ylim(0.2,0.8)
	plt.ylabel('m/step')
	plt.xlim(0,25)
	plt.subplot(313)
	i = 0
	colorShape = ['k-*','m-^','b-o','r--','g-o']
	for data3 in dataList3:
		plt.plot(data3,colorShape[i],linewidth=1.5)
		i=i+1
	#plt.ylim(0.2,0.8)
	plt.ylabel('m/step')
	plt.xlabel('steps')
	plt.xlim(0,25)
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

	BC2x,BC2y,BC2z,BC2xyz=readFile(acceleroDataPath,'BC.txt')
	BH2x,BH2y,BH2z,BH2xyz=readFile(acceleroDataPath,'BH.txt')
	DB2x,DB2y,DB2z,DB2xyz=readFile(acceleroDataPath,'AF.txt')
	AF2x,AF2y,AF2z,AF2xyz=readFile(acceleroDataPath,'DB.txt')

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
	BC2xyzm=meanF(BC2xyz,win)
	BH2xyzm=meanF(BH2xyz,win)
	DB2xyzm=meanF(DB2xyz,win)
	AF2xyzm=meanF(AF2xyz,win)
	#lxyz = LPF(BH2xyzm)
	#plotLine2(BH2xyz,BH2xyzm)
	Wei = []
	Scar = []
	Kim = []
	reaL=[14.8,12,30,17.78]
	j=0
	dataList = [BC2xyzm,BH2xyzm,DB2xyzm,AF2xyzm]
	for data in dataList:
		stepizeList1,stepizeList2,stepizeList3 = StepSize(data)
		#print sum(stepizeList1),sum(stepizeList2),sum(stepizeList3),reaL[j],\
		#sum(stepizeList1)/reaL[j],sum(stepizeList2)/reaL[j],sum(stepizeList3)/reaL[j];
		print avrAbs(stepizeList1),avrAbs(stepizeList2),avrAbs(stepizeList3)
		Wei.append(stepizeList1)
		Scar.append(stepizeList2)
		Kim.append(stepizeList3)

	plotNline(Wei,Scar,Kim)
	#plotLine1(stepizeList)
	#plotLine(BH2xyzm)


if __name__ == '__main__':
	main()
