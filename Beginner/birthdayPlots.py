from bokeh.plotting import figure, show, output_file
import json
from collections import Counter

#specify output file
months = ["January", "March", "April", "July", "August"]

with open("dataBirthdays.json", "r") as f:
    data = json.load(f)

listOfMonths = []
for names in data:
    listOfMonths.append(data[names])

c = Counter(listOfMonths).items()
result = [ value for key,value in c ] #just value of each key in c

output_file("plot.html")
x_categories = months
title = "Birthday Histogram"

#load x and y data
x = months
y = result

#create/initialise figure
p = figure(x_range = x_categories, title=title)


#create a histogram
p.vbar(x=x, top=y, width=0.5)

show(p)