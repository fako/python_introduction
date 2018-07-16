import os
import json
from copy import copy


PYTHON_DEVELOPERS = (
    "Fako Berkers",
    "Wouter de Winter",
    "Jeroen de Hoek",
)

BASE_OBJECT = {
    "company": "VANAD Create",
    "knowsPython": True,
    "manipulatesData": True,
    "top10Buildins": [
        "super()", "max()", "print()", "len()", "iter()", "list()", "enumerate()", "sorted()", "zip()", "min()"
    ],
    "win32": False,
    "level": 5,
    "answerToEverything": ord("*"),
    "ipythonFan": True,
    "headInClouds": False,
    "motto": "programming for humans"
}


def set_name(obj, name):
    names = name.split(" ")
    obj["firstName"] = names[0]
    obj["lastName"] = " ".join(names[1:])
    obj["top10Buildins"] *= 5
    return obj


data = [
    set_name(copy(BASE_OBJECT), full_name) for full_name in PYTHON_DEVELOPERS
]
data *= 1000
print("Length of data:", len(data))

data_file = os.path.join("data", "data.json")
with open(data_file, "w") as fp:
    json.dump(data, fp)
