import requests
import json

url = "https://arbor.a1.bg/api/sp/alerts/?filter=/data/attributes/alert_class=dos"

api_token = "iknkDnxplBCmOUH6tJC_sflCP9Ky1fXkQRitrzJ_"
headers = {
    'X-Arbux-APIToken': api_token
}
response = requests.request("GET", url, headers=headers)
id_numb = []
for data in response.json()['data']:
    res = data["relationships"]

    try:

        if res["managed_object"]["data"]["id"] not in id_numb:
            id_numb.append(res["managed_object"]["data"]["id"])
            # print(res["managed_object"]["data"]["id"])
    except:
        print("no")

url2 = "https://arbor.a1.bg/api/sp/managed_objects/619"
response_mn_obj = requests.request("GET", url2, headers=headers)
for data in response_mn_obj.json()["data"]:

    try:
        print("for object with id " + data["id"] + " and name " + data["attributes"]["name"])
        print(data["attributes"]["match"])
    except:
        print("no mane")