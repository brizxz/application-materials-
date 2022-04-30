import urllib.request as re
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with re.urlopen(src) as response:
 #   data=response.read().decode("utf-8")
    data=json.load(response)
#print(data)
#取得公司名稱，並列表
clist=data["result"]["results"]
print(clist)
with open("aaa.txt","w", encoding="utf-8") as file:
    for company in clist:       
        file.write(company["公司名稱"]+"\n")