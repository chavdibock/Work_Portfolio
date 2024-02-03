import requests

# URL за достъпване на ARBOR API за иаминалите аларми
url = "https://arbor.a1.bg/api/sp/alerts/?filter=/data/attributes/alert_class=dos"

api_token = "iknkDnxplBCmOUH6tJC_sflCP9Ky1fXkQRitrzJ_"
headers = {
    'X-Arbux-APIToken': api_token
}
response = requests.request("GET", url, headers=headers)

# Отговора се парсва в масив от dictionaries
for data in response.json()['data']:
    res = data['relationships']
    ongoing = data["attributes"]["ongoing"]  # boolean variable
    try:
        if ongoing:  # IF it is true
            object_id = str(res["managed_object"]["data"]["id"])
            id_alert = str(data["id"])
            start = data["attributes"]["start_time"]
            # Достъпване на обектите, за които е имало аларма
            url2 = "https://arbor.a1.bg/api/sp/managed_objects/" + object_id
            res_mnh_obj = requests.request("GET", url2, headers=headers)
            inf = res_mnh_obj.json()['data']
            family = inf["attributes"]["family"]
            if family == "customer":
                object_name = inf['attributes']['name']
                print("########## Ongoing attack ##########" + '\n'
                      + "alert id " + id_alert + " to " + object_name + " id " + object_id + "\n"
                      + "start time " + start)

        else:  # If it is false
            object_id = str(res["managed_object"]["data"]["id"])
            id_alert = str(data["id"])
            start = data["attributes"]["start_time"]
            end = data["attributes"]["stop_time"]
            url2 = "https://arbor.a1.bg/api/sp/managed_objects/" + object_id
            res_mnh_obj = requests.request("GET", url2, headers=headers)
            inf = res_mnh_obj.json()['data']
            object_name = inf['attributes']['name']
            family = inf["attributes"]["family"]
            if family == "customer":
                print("########## Past attack ##########" + '\n'
                      + "alert id " + id_alert + " to " + object_name + " id " + object_id + "\n"
                      + "start time " + start + " stop time " + end + '\n')
    except:
        print("no")
