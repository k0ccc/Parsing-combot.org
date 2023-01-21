import requests
import pandas as pd

add = 50
offset = 0
limit = add
channels = []
someMath = 0 

while True:
    res = requests.get(
        "https://combot.org/api/chart/all?limit=" +
        str(limit) + "&offset=" + str(offset))
    offset += add;
    limit += add;
    json = res.json()
    if not json:
        print('Done')
        break
    else:
        someMath += 50
        print('get ' + str(someMath) + ' channels')
        channels += res.json()
        
print("Create CSV 'data'")
data = pd.DataFrame(channels)
data.to_csv("./data.csv")

print("Writing complete")

