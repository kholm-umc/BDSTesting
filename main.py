import pprint
import pandas as pd

file = r"C:\temp\info.csv"

# print(f"Reading {file}")

df = pd.read_csv(file)

badZip = df[df.zip.str.len() == 4]

listOfBadCities = []
listOfBadStates = []

bad = {}

for row in badZip.iterrows():
    # print(row[1][3])
    # print(f"Adding {row[1][1]}")
    listOfBadCities.append(row[1][1])
    listOfBadCities.append(row[1][2])
    # print(row)

# print(listOfBadStates)

# pprint.pprint(badZip)

goodData = {"city1": {"city": "Dallas", "state": "TX", "zip": 12345}}

alternateGoodData = {"DallasTX": 12345}

badData = {"city2": {"city": "Dallas", "state": "TX"},
           "city3": {"city": "Jackson", "state": "MS"}}

for row in badData:
    badKey = badData[row]["city"] + badData[row]["state"]
    try:
        newZip = alternateGoodData[badKey]
        newZip = str(newZip)[0] + "0000"
        print(f"I found a zip for {badKey} {newZip}")
    except:
        print("No match")
