import sys
import json
from slpp import slpp as lua

filename = "C:\Program Files (x86)\World of Warcraft\_retail_\WTF\Account\FLESHMANJ\SavedVariables\Auctionator.lua"


with open(file=filename) as file:
    temp = file.read()

data = temp[temp.find("AUCTIONATOR_PRICE_DATABASE = ")+29:temp.find("AUCTIONATOR_POSTING_HISTORY = ")]

data = lua.decode(data)

for k, v in data.items():
    if isinstance(v, dict):
        for key, value in v.items():
            print(key, value)
