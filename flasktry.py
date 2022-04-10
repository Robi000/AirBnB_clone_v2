#!/usr/bin/python3
from models import storage
from models import city
from models.state import State
from models.city import City
from operator import itemgetter

print(storage.all(State))
x = storage.all(State)
statex = []
cityx = []
state_city = []
final = []
for x, y in x.items():
    statex.append([y.to_dict()["id"], y.to_dict()["name"]])
for x, y in storage.all(City).items():
    cityx.append([y.to_dict()['state_id'], y.to_dict()
                  ["name"], y.to_dict()["id"]])
meh = sorted(cityx, key=itemgetter(1))
print("\n*******statexx*******")
print(statex)
print("\n*******cityx*******")
print(cityx)
print("\n*******meh*******")
print(meh)


def state_city_finder(n):
    for x in statex:
        if x[0] == n:
            for y in cityx:
                if y[0] == n:
                    state_city.append([y[1], y[2]])
            final.append([x[0], x[1], state_city])
    return final


print("\n*********** final **********")
print(state_city_finder("421a55f4-7d82-47d9-b54c-a76916479545"))
