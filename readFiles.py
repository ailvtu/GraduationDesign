#read the data from file
def readFile(dataPath,fileName):
	x=[]
	y=[]
	z=[]
	xyz=[]
	data=[]
	f = open(dataPath+'/'+fileName)
	lines = f.readlines()
	len(lines)
	for line in lines:
		data.append(line.replace('\n',''))
	f.close()
	i=0
	while i < len(data):
		x.append(data[i])
		y.append(data[i+1])
		z.append(data[i+2]) 
		xyz.append(data[i+3])
		i=i+4
	return x,y,z,xyz