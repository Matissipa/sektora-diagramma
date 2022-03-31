from cProfile import label
from matplotlib import colors
import matplotlib.pyplot as plt #importē grafiku bibliotēku
dalas=[15,29,58,99]
labels=["Xiaomi", "Huaweii", "Samsung", "Apple"]
krasas=["blue", "red", "green", "yellow"]
sizes = [15, 20, 25, 40]

plt.pie(dalas, colors=krasas, labels=labels)
plt.pie#beigas. testē
plt.show()