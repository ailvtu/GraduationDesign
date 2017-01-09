import matplotlib.pyplot as plt
import os
import numpy as np 

def plotPie(data1,data2):
	plt.subplot(121)
	labels = ['mapshard1','mapshard2','mapshard3']
	colors = ['red','yellowgreen','lightskyblue']

	explode = (0.05,0.05,0.05)

	patches,l_text,p_text = plt.pie(data1,explode=explode,labels=labels,colors=colors,
	                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
	                                startangle = 90,pctdistance = 0.6)

	for t in l_text:
	    t.set_size=(30)
	for t in p_text:
	    t.set_size=(20)

	plt.axis('equal')
	plt.legend()
	plt.subplot(122)
	labels = ['mapshard1','mapshard2','mapshard3']
	colors = ['red','yellowgreen','lightskyblue']

	explode = (0.05,0.05,0.05)

	patches,l_text,p_text = plt.pie(data2,explode=explode,labels=labels,colors=colors,
	                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
	                                startangle = 90,pctdistance = 0.6)

	for t in l_text:
	    t.set_size=(30)
	for t in p_text:
	    t.set_size=(20)

	plt.axis('equal')
	plt.legend()
	plt.show()



sizes1 = [33.20,33.96,32.84]
sizes2 = [34.52,38.39,27.08]
plotPie(sizes1,sizes2)