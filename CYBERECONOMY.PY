import pandas
import numpy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
eco1 = pandas.read_csv('gdp_Tamilnadu.csv')
print(eco1)
plt.figure(figsize=(5.8, 4.2))
speed = [198,197,200,386,297,285,475]
x = range(len(eco1['Year']))
plt.plot(x, eco1['Chennai'])
plt.xticks(x, eco1['Year'])
plt.xlabel('Year')
plt.ylabel('Tamilnadu(GDP)')
plt.show()

car = [198,197,200,376,297,285,475]
plt.figure(figsize=(5.8, 4.2))
x = range(len(eco1['Year']))
plt.plot(x, eco1['Salem'])
plt.xticks(x, eco1['Year'])
plt.xlabel('Year')
plt.ylabel('Tamilnadu(GDP)')
plt.show()

plt.figure(figsize=(5.8, 4.2))
vrd = [198,197,200,376,297,285,435]
x = range(len(eco1['Year']))
plt.plot(x, eco1['Erode'])
plt.xticks(x, eco1['Year'])
plt.xlabel('Year')
plt.ylabel('Tamilnadu(GDP)')
plt.show()

kee = [198,167,200,376,297,285,435]
plt.figure(figsize=(5.8, 4.2))
x = range(len(eco1['Year']))
plt.plot(x, eco1['Coimbatore'])
plt.xticks(x, eco1['Year'])
plt.xlabel('Year')
plt.ylabel('Tamilnadu(GDP)')
plt.show()

rsa = [198,167,200,376,297,185,235]
plt.figure(figsize=(5.8, 4.2))
x = range(len(eco1['Year']))
plt.plot(x, eco1['Dharmapuri'])
plt.xticks(x, eco1['Year'])
plt.xlabel('Year')
plt.ylabel('Tamilnadu(GDP)')
plt.show()

cars = ['Salem', 'Erode', 'Coimbatore',
        'Dharmapuri', 'Chennai']
 
data = [23, 17, 35, 29, 41]
 

explode = (0.1, 0.0, 0.2, 0.3, 0.0)

colors = ( "red", "yellow", "brown",
          "grey", "green", "white")

wp = { 'linewidth' : 1, 'edgecolor' : "blue" }
 
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  explode = explode,
                                  labels = cars,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, cars,
          title ="District",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("DATA ANALYTICS ECONOMY")
 
# show plot
plt.show()

x = numpy.std(speed)
print("Chennai Crime GDP Accuracy",x)

x = numpy.std(car)
print("Salem Crime GDP Accuracy",x)

x = numpy.std(vrd)
print("Erode CrimeGDP Accuracy",x)

x = numpy.std(kee)
print("Coimbatore CrimeGDP Accuracy",x)
x = numpy.std(rsa)
print("Dharmapuri CrimeGDP Accuracy",x)
