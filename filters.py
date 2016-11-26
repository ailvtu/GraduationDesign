#low-pass filtering
def LPF(dataArray):
	aft=[]
	aft.append(dataArray[0])
	for x in xrange(1,len(dataArray)):
		d = 0.4*float(dataArray[x])+0.6*float(aft[x-1])
		aft.append(d)
	return aft

def HPF(dataArray):
	hpf = []
	hpf.append(0)
	for x in xrange(1,len(dataArray)):
		h = 0.95*(float(hpf[x-1]))+0.95*(float(dataArray[x])-float(dataArray[x-1]))
		hpf.append(h)
	return hpf
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

#def standard(dataArray):
