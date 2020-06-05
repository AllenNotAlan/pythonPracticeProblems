import json
from collections import Counter

with open("dataBirthdays.json", "r") as f:
    data = json.load(f)

listOfMonths = []

for names in data:
    listOfMonths.append(data[names])

c = Counter(listOfMonths).items()
print(c)

result = [ value for key,value in c ]

print(result)