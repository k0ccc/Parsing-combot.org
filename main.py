import requests
import pandas as pd

add = 50
offset = 0
limit = add
channelsTemp = []
channels = []
someMath = 0 

while True:
    offset += add;
    limit += add;
    res = requests.get(
        "https://combot.org/api/chart/all?limit=" +
        str(limit) + "&offset=" + str(offset))
        
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


# columns = ['t', 'u', 'pc', 'l', 'a', 'i', 'p', 'baa', 'baa', 'baa']


# with file:
#     writer.writeheader()
#     # print(channels)
#     for i in channels:
#         # a = i.split( "},{")
#         print(i)
#         # for z in a:
#         #     print(z)
#             # writer.writerow([a,u])


print("Writing complete")
# while true:
#     offset =+ add;
#     limit =+ add;
#     res = requests.get("https://combot.org/api/chart/all?limit=" + str(10) + "&offset=" + str(offset))
#     if (res.text == '[]'):
#         break
#     else:
#         channels.append(res.text)
