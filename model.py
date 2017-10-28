import pandas as pd
import numpy  as np
import pickle as pk
from sklearn import naive_bayes
import pickle as pk
from sklearn import tree
from math  import sqrt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def find_accuracy(a,b):
    den = len(a)
    count  =  0
    for i in range(len(a)):
        if a[i] == b[i]:
            count = count + 1
    return (count/den)
#with open('data_2005.pkl') as f:
data = pd.read_pickle('data_2005_final.pkl')
print('dataset loaded.')
train , test = train_test_split(data , test_size=0.20)
#print(train)
#print(test)
print('dataset loaded .')
print(len(train), len(test))

columns = list(data)
feature_columns = []
for line in columns:
    if line != 'manner_of_death' :
        feature_columns.append(line)

features = train[feature_columns]
features = np.array(features)
#print(features)
labels = train['manner_of_death']
#print(labels.values)

test_set = np.array(test[feature_columns])
test_labels = test['manner_of_death'].values

#print(test_set , test_labels)
print("Started training")
values = {}
rms = {}
for i in range(1,50):
    classifier = tree.DecisionTreeClassifier(min_samples_leaf=i)
    classifier.fit(features , labels.values)
    result  = classifier.predict(test_set)
    #print(test_labels , result , sep='\n')
    acc = find_accuracy(result, test_labels)
    values[i] = acc
    rms[i] = sqrt(mean_squared_error(test_labels,result))
    print(values[i] , rms[i])
print(values)
print(rms)
with open("acc.pkl", "wb") as F:
    pk.dump(values,F)
with open('rms.pkl','wb') as f:
    pk.dump(rms,f)