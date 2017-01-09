import numpy as np
import matplotlib.pyplot as plt


n_groups = 4

items = [10000, 100000, 500000, 1000000]

shardT = [4.087162018,40.60927796,240.167542,465.29400897] 
noshardT = [6.830083132,66.12888598,332.1937711,778.932121038]




shard = map(lambda (a,b):a/b, zip(items,shardT))
noshard = map(lambda (a,b):a/b, zip(items,noshardT))



plt.subplot()
index = np.arange(n_groups)
bar_width = 0.35

rects1 = plt.bar(index, shard, bar_width, color='b',label='Sharding')
rects2 = plt.bar(index + bar_width, noshard, bar_width,color='r',label='SingleInstace')
plt.xlabel('Test-Item')
plt.ylabel('items/s')
#plt.title('')
plt.xticks(index + bar_width, ('10000', '100000', '500000', '1000000'))
#plt.ylim(0,40)
plt.legend()




plt.show()
'''
plt.subplot(122)
index = np.arange(n_groups)
bar_width = 0.35
rects1 = plt.bar(index, shard, bar_width, color='b',label='1Process')
rects2 = plt.bar(index + bar_width, hunShard, bar_width,color='r',label='100Processes')
plt.xlabel('TestItem')
plt.ylabel('items/s')
#plt.title('')
plt.xticks(index + bar_width, ('10000', '100000', '500000', '1000000'))
#plt.ylim(0,40)
plt.legend()
plt.show()'''
