import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy
from skfuzzy import control as ctrl

'''Data preparation'''
dataset = pd.read_csv('C:\\Users\\Okti\\Downloads\\ccc.csv', header=1)
#print(dataset.columns)
dataset['BILL TOTAL'] = dataset['BILL_AMT1'] + dataset['BILL_AMT2'] + dataset['BILL_AMT3'] + dataset['BILL_AMT4'] + dataset['BILL_AMT5'] + dataset['BILL_AMT6']
#print(dataset.columns)
#print(dataset['LIMIT_BAL'].mean())

'''Preprocesing data'''
x = dataset.iloc[:, [1, 25]].values
print(x.min() , x.max())

'''Normalizing data'''
scaler = MinMaxScaler()
x = scaler.fit_transform(x)

'''Clustering with fuzzy c-means'''
x.T.shape
clustering = skfuzzy.cmeans(data = x.T, c = 5, m = 2, error = 0.005, maxiter = 1000, init=None)
print(len(clustering))
predictions = clustering[1]
print(predictions.shape)
print(predictions)
'''Predictiong of customer membership, probability of belonging to a cluster and checking if sum is close to 1.0'''
print(predictions[0][0], predictions[1][0], predictions[2][0], predictions[3][0], predictions[4][0])
print(predictions[0][0] + predictions[1][0] + predictions[2][0] + predictions[3][0] + predictions[4][0])

'''Extracting index where higher value is located'''
predictions = predictions.argmax(axis = 0)
print(predictions)

'''Choosing best number of clusters'''
fpcs = []
for n_clusters in range(2,10):
    print(n_clusters)
    centers, predictions, _, _, _, _, fpc = skfuzzy.cmeans(data=x.T, c=n_clusters, m=2, error=0.005, maxiter=1000,init=None)
    fpcs.append(fpc)

fig, ax = plt.subplots()
ax.plot(range(2,10), fpcs)
ax.set_xlabel('Num of clusters')
ax.set_ylabel('FPC');
plt.show()

'''Visualising random number indexes of the clusters'''
np.unique(predictions, return_counts = True)
plt.scatter(x[predictions== 0, 0], x[predictions == 0, 1], c='red', label = 'Cluster 1')
plt.scatter(x[predictions== 1, 0], x[predictions == 1, 1], c='green', label = 'Cluster 2')
plt.scatter(x[predictions== 2, 0], x[predictions == 2, 1], c='yellow', label = 'Cluster 3')
plt.scatter(x[predictions== 3, 0], x[predictions == 3, 1], c='purple', label = 'Cluster 4')
plt.scatter(x[predictions== 4, 0], x[predictions == 4, 1], c='orange', label = 'Cluster 5')
plt.xlabel('Limit')
plt.ylabel('Bill amount')
plt.legend;
plt.show()


