#!/usr/bin/python3
from models import storage
from models import city
from models.state import State
from models.city import City

print(storage.all(State))
x = storage.all(State)
statex = []
cityx = []
state_city = []
final = []
for x, y in x.items():
    statex.append([y.to_dict()["id"], y.to_dict()["name"]])

print(statex)

print("\n\n\n\n")
print("---------------------------------")
print(storage.all(City)['City.521a55f4-7d82-47d9-b54c-a76916479545'].to_dict())
# print(storage.all(City))
for x, y in storage.all(City).items():
    cityx.append([y.to_dict()['state_id'], y.to_dict()
                  ["name"], y.to_dict()["id"]])

print(cityx)

for x in statex:
    state_city = []

    for y in cityx:
        if x[0] == y[0]:
            state_city.append([y[1], y[2]])
    final.append([x[0], x[1], state_city])

print("------ final --------\n\n")
print(final)
