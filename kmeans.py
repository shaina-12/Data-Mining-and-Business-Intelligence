import math
import numpy as np
class datapoints:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

def distance(dp1,dp2):
    return math.pow((dp1.x-dp2.x),2)+math.pow((dp1.y-dp2.y),2)

def updation(dps,assign,k):
    cent = []
    counter = []
    for i in range(k):
        cent.append(datapoints(0,0))
        counter.append(0)
    for i in range(len(dps)):
        cent[assign[i]].x += dps[i].x
        cent[assign[i]].y += dps[i].y
        counter[assign[i]] += 1
    for i in range(k):
        cent[i].x = cent[i].x/counter[i]
        cent[i].y = cent[i].y/counter[i]
    return cent

def clustering(dps,k,cent,n):
    assign = []
    iterations = 5
    for l in range(iterations):
        matrix = []
        print('iteration: '+str(l))
        #print(k)
        #print(n)
        for i in range(n):
            cluster = []
            ass = -2147483648
            ed = 99999999999999.99999999999999999
            for j in range(k):
                #print(i,j)
                dist = distance(dps[i],cent[j])
                cluster.append(dist)
                if(dist < ed):
                    ass = j
                    ed = distance(dps[i],cent[j])
                #print(ass)
                #print(cluster)
            assign.append(ass)
            matrix.append(cluster)
        #print(assign)
        #print(matrix)
        arr = np.array(matrix)
        arr = np.transpose(arr)
        for i in range(k):
            print(f'({cent[i].x},{cent[i].y}) ->',end=" ")
            for j in range(n):
                print(f'{arr[i][j]} |',end=" ")
            print()
        print('Assignment: ')
        for i in range(n):
            print(f'{assign[i]} |',end=" ")
        cent = updation(dps,assign,k)
        assign.clear()
        print('Updated Centroids Are:')
        for i in range(k):
            print(f'Cluster {i+1}: ({cent[i].x},{cent[i].y})')
        print()

# main program
n = 8
dps = [datapoints(2,10),
    datapoints(2,5),
    datapoints(8,4),
    datapoints(5,8),
    datapoints(7,5),
    datapoints(6,4),
    datapoints(1,2),
    datapoints(4,9)]
k = 3
cent = [datapoints(2,10),
    datapoints(5,8),
    datapoints(1,2)]
# training of data points
clustering(dps,k,cent,n)


