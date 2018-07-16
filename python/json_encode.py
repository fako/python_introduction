import os
import json
from datetime import datetime


print("Start test")
data_file = os.path.join("data", "data.json")
t0 = datetime.now()


with open(data_file, "r") as fp:
    data = json.load(fp)

t1 = datetime.now()

with open(data_file, "w") as fp:
    json.dump(data, fp)

t2 = datetime.now()

print("Loading took {}".format(t1 - t0))
print("Dumping took {}".format(t2 - t1))
print("End test")
