import matplotlib.pyplot as plt
import pickle as pk

with open('acc.pkl','rb') as f:
    data = pk.load(f)
#print(data)

x = []
y = []

for item in sorted(data.keys()):
    x.append(item)
    y.append(data[item])
#print(x,y)

plt.plot(x,y)
plt.show()

with open('rms.pkl','rb') as f:
    data = pk.load(f)

x = []
y = []

for item in sorted(data.keys()):
    x.append(item)
    y.append(data[item])

plt.plot(x,y)
plt.show()