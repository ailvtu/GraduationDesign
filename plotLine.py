import matplotlib.pyplot as plt
import os
import numpy as np 
from dtw import dtw
from filters import LPF,HPF,meanF
from readFiles import readFile
#curPath=os.getcwd()
#magneticDataPath = '/home/dash/Pictures/sensorData/2016_11_23/magneticData'
magneticDataPath = '/home/dash/Pictures/sensorData/2016_11_25/magneticData'
magneticDataPath26 = '/home/dash/Pictures/sensorData/2016_11_26/magneticData'
magneticDataPathXiaoMi = '/home/dash/Pictures/sensorData/Xiaomi/magneticData'
magneticDataPathHuawei = '/home/dash/Pictures/sensorData/Huawei/magneticData'
#magneticDataPath = '/home/dash/Pictures/sensorData/2016_11_22/magneticData2'
acceleroDataPath = '/home/dash/Pictures/sensorData/2016_11_25/acceleroData'
#print os.listdir(magneticDataPath)
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

#plot 2 lines
def plotLine2(a,b,label):
	fig,ax = plt.subplots()
	if label=='LPF':
		ax.plot(a,'r-',label="$LPF-data$",linewidth=2)
		ax.plot(b,'k--',label="$raw-data$",linewidth=2)
	elif label == 'direction':
		ax.plot(a,'m-',label="$forward$",linewidth=2)
		ax.plot(b,'b--',label="$reverse$",linewidth=2)
	elif label=='HPF':
		ax.plot(a,'r-',label="$HPF-data$",linewidth=2)
		ax.plot(b,'k--',label="$raw-data$",linewidth=2)
	else:
		ax.plot(a,'r-',label="$rapid$",linewidth=2)
		ax.plot(b,'k--',label="$normal$",linewidth=2)
	plt.xlim(1, len(a))
	plt.ylim(33,42)	
	plt.ylabel('intensity/uT')
	plt.xlabel('distance')
	plt.legend()
	labels=['12','44','32','23']
	#ax.set_xticks(np.linspace(0,1,9))  
	#ax.set_xticklabels(('275','280','285','290','295', '300', '305', '310','315')) 
	plt.show()

#plot 3 line
def plotLine3(x,y,z):
	plt.figure(1)

#	plt.plot(x[1:65],'r-*',label="$left$",linewidth=2)
#	plt.plot(y[1:65],'g-o',label="$midle$",linewidth=2)
#	plt.plot(z[1:65],'b-^',label="$right$",linewidth=2)

	plt.plot(x,'k--',label="$Meizu$",linewidth=1.5)
	plt.plot(y,'m-',label="$Xiaomi$",linewidth=1.5)
	plt.plot(z,'b--.',label="$Huawei$",linewidth=1.5)
	#plt.xlabel('distance/dm')
	plt.ylabel('intensity/uT')
	plt.ylim(34,44)
	#plt.xlim(0, 65)		
	#plt.title('gallery magnetic field')
	plt.legend()
	plt.show()

def plotLine4(x,y,z,p):
	plt.figure(2)
	plt.subplot(221)
	plt.plot(x,'r-',linewidth=2)
	plt.title('magnetic of BH Path')
	plt.ylabel('intensity/uT')
	#plt.ylim(35, 42)

	plt.subplot(222)
	plt.plot(y,'g-',linewidth=2)
	plt.title('magnetic of BC Path')
	plt.ylabel('intensity/uT')
	#plt.ylim(35, 42)

	plt.subplot(223)
	plt.plot(z,'b-',linewidth=2)
	plt.title('magnetic of HG Path')
	plt.ylabel('intensity/uT')
	#plt.ylim(35, 42)

	plt.subplot(224)
	plt.plot(p,'k',linewidth=2)
	plt.title('magnetic of CF Path')
	plt.ylabel('intensity/uT')
	#plt.ylim(35, 42)	
	#lt.xlabel('xlable')
	#lt.ylabel('ylable')
	#plt.ylim(0, 15)	
	#Plt.title('gallery magnetic field')
	plt.show()
#plot 3 line
def plotLine4lines(x,y,z,d):
	plt.figure(1)
	plt.plot(x[1:len(x)],'r-*',label="$X$",linewidth=2)
	plt.plot(y[1:len(y)],'g-o',label="$Y$",linewidth=2)
	plt.plot(z[1:len(z)],'b-^',label="$Z$",linewidth=2)
	plt.plot(d[1:len(d)],'m-x',label="$D$",linewidth=2)
	#plt.xlabel('distance/dm')
	plt.ylabel('intensity/uT')
	#plt.ylim(0, 15)
	#plt.xlim(0, 60)		
	#plt.title('gallery magnetic field')
	plt.legend()
	plt.show()

def plotNlines(dataList1,dataList2):
	plt.subplot(211)
	for data in dataList1:
		plt.plot(data,linewidth=1.5)
	plt.subplot(212)
	for data2 in dataList2:
		plt.plot(data2,linewidth=1.5)
	plt.show()

def plotFilterLines(x,y,z):
	plt.subplot(311)
	plt.plot(x,linewidth=1.6)
	plt.subplot(312)
	plt.plot(y,'m-',linewidth=1.6)
	plt.subplot(313)
	plt.plot(z,'r-',linewidth=1.6)
	plt.show()
def main():

	BH1x,BH1y,BH1z,BH1xyz=readFile(magneticDataPath,'BH1.txt')
	BH2x,BH2y,BH2z,BH2xyz=readFile(magneticDataPath,'BH2.txt')
	BH3x,BH3y,BH3z,BH3xyz=readFile(magneticDataPath,'BH3.txt')

	BCx,BCy,BCz,BCxyz=readFile(magneticDataPath,'BC.txt')
	CFx,CFy,CFz,CFxyz=readFile(magneticDataPath,'CF.txt')
	HGx,HGy,HGz,HGxyz=readFile(magneticDataPath,'HG.txt')

	CBx,CBy,CBz,CBxyz=readFile(magneticDataPath,'CB.txt')
	FCx,FCy,FCz,FCxyz=readFile(magneticDataPath,'FC.txt')
	GHx,GHy,GHz,GHxyz=readFile(magneticDataPath,'GH.txt')

	BC2x,BC2y,BC2z,BC2xyz=readFile(magneticDataPath,'BC2.txt')

	CF2x,CF2y,CF2z,CF2xyz=readFile(magneticDataPath,'CF2.txt')

    

	CFlist=[]
	CF01x,CF01y,CF01z,CF01xyz=readFile(magneticDataPath26,'CF01.txt');CFlist.append(CF01xyz);
	CF02x,CF02y,CF02z,CF02xyz=readFile(magneticDataPath26,'CF02.txt');CFlist.append(CF02xyz);
	CF03x,CF03y,CF03z,CF03xyz=readFile(magneticDataPath26,'CF03.txt');CFlist.append(CF03xyz);
	CF04x,CF04y,CF04z,CF04xyz=readFile(magneticDataPath26,'CF04.txt');CFlist.append(CF04xyz);
	CF05x,CF05y,CF05z,CF05xyz=readFile(magneticDataPath26,'CF05.txt');CFlist.append(CF05xyz);
	CF06x,CF06y,CF06z,CF06xyz=readFile(magneticDataPath26,'CF06.txt');CFlist.append(CF06xyz);
	CF07x,CF07y,CF07z,CF07xyz=readFile(magneticDataPath26,'CF07.txt');CFlist.append(CF07xyz);
	CF08x,CF08y,CF08z,CF08xyz=readFile(magneticDataPath26,'CF08.txt');CFlist.append(CF08xyz);
	CF09x,CF09y,CF09z,CF09xyz=readFile(magneticDataPath26,'CF09.txt');CFlist.append(CF09xyz);
	CF10x,CF10y,CF10z,CF10xyz=readFile(magneticDataPath26,'CF10.txt');CFlist.append(CF10xyz);



	BCx,BCy,BCz,BCxyz=readFile(magneticDataPath,'BC.txt')
	BCxMI,BCyMI,BCzMI,BCxyzMI=readFile(magneticDataPathXiaoMi,'BC.txt')
	BCxHW,BCyHW,BCzHW,BCxyzHW=readFile(magneticDataPathHuawei,'BC.txt')
	#JZx,JZy,JZz,JZxyz=readFile('jiaozheng.txt')#path 1123

#############
	mGH=meanF(GHxyz,win)
	GHmhf1=LPF(mGH)
	#plotLine2(GHmhf1,mGH,'LPF')#plot the LPF raw data

#############

	mBH1=meanF(BH1xyz,win)
	mBH2=meanF(BH2xyz,win)
	mBH3=meanF(BH3xyz,win)
	BHf1=LPF(mBH1)
	BHf2=LPF(mBH2)
	BHf3=LPF(mBH3)

	#plotLine3(BHf1,BHf2,BHf3)#plot the 3 in one 

##################

	mBC=meanF(BCxyz,win)
	mCF=meanF(CFxyz,win)
	mHG=meanF(HGxyz,win)
	BCf=LPF(mBC)
	CFf=LPF(mCF)
	HGf=LPF(mHG)
	#plotLine4(BHf2,BCf,HGf,CFf)#4lines4gallary

###################
	mGH=meanF(GHxyz,win)
	GHf=LPF(mGH)
	GHf.reverse()
    #plotLine2(GHf,HGf,'direction')#plot the TWO direction
    #plotLine2(GHf,HGf,'HPF')#plot the HPFd raw data
###################
	mBC2=meanF(BC2xyz,win)
	BC2f=LPF(mBC2)
	#plotLine2(BCf,BC2f,'')
	#and the slow
###################
	mCFlist=[]
	lpfCFlist=[]
	hpfCFlist=[]
	hlpfCFlist=[]
	for Mdata in CFlist:
		mCFlist.append(meanF(Mdata,win))
	for mCF0 in mCFlist:
		lpfCFlist.append(LPF(mCF0))
	for mCF0 in mCFlist:
		hpfCFlist.append(HPF(mCF0))
	for mhCF0 in hpfCFlist:
		hlpfCFlist.append(LPF(mhCF0))	
	#plotNlines(lpfCFlist,hlpfCFlist)

###################
#plot 3 line for 3 devices 
	mBC=meanF(BCxyz,win)
	BCL=LPF(mBC)
	mBCMI=meanF(BCxyzMI,win)
	BCLMI=LPF(mBCMI)
	mBCHW=meanF(BCxyzHW,win)
	BCLHW=LPF(mBCHW)
	print dtw(mBC,mBCHW)
	print dtw(mBCMI,mBC)
	print dtw(mBCMI,mBCHW)
	#plotLine3(BCL,BCLMI,BCLHW)#plot the 3 DEVICES
#####################
	#plotFilterLines(BCxyz,mBC,BCL)
#####################


if __name__ == '__main__':
	main()