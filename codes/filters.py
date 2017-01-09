import numpy
#low-pass filtering
def LPF(dataArray):
	aft=[]
	aft.append(dataArray[0])
	for x in xrange(1,len(dataArray)):
		d = 0.4*float(dataArray[x])+0.6*float(aft[x-1])
		aft.append(d)
	return aft
#high-pass filtering
def HPF(dataArray):
	hpf = []
	hpf.append(0)
	for x in xrange(1,len(dataArray)):
		h = 0.98*(float(hpf[x-1]))+0.4*(float(dataArray[x])-float(dataArray[x-1]))
		hpf.append(h)
	return hpf
#mean filtering
def meanF(dataArray,window):
	temdata = 0 
	x = 0
	dataArray2 = []
	for arrayData in dataArray:
		#print arrayData
		temdata = temdata+float(arrayData)
		x = x +1
		if x >= window:
			dataArray2.append(temdata/window)
			temdata=0
			x=0
	return dataArray2
#standardization
def standard(dataArray):
	newList = []
	narray=numpy.array(dataArray)
	sum1=narray.sum()
	narray2=narray*narray
	sum2=narray2.sum()
	mean=sum1/len(dataArray)
	var=sum2/len(dataArray)-mean**2
	#print mean,var
	for data in dataArray:
		newdata = (data-mean)/var
		newList.append(newdata)
	return newList
#	sumData = 0.0
#	for data in dataArray:
#		sumData = sumData + float(data)
#	print sumData/len(dataArray)

