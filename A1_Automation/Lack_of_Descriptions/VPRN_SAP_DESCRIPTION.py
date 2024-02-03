import os
import re
import time
import netmiko
from netmiko import redispatch

VPRN = r'/configure\s+service\s+vprn\s+(.*)\s+name\s+(.*)\s+customer\s+(.*)\s+interface\s+(.*)\s+sap\s+(.*)\s+create'

server_user = str(input("What is your user_name for the jump server"))
server_passw = str(input("What is your password for the jump server"))

net_connect = netmiko.ConnectHandler(
    device_type="linux_ssh",
    host="10.251.192.162",
    username=server_user,
    password=server_passw,
    session_log='netmiko_session.log',
)

user = input("please provide a username to log on the device. ")
passw = input("plese provide a password for log on the device. ")

path = "/Configs_2023_22_08/"
os.chdir(path)
path_for_new_config = "/new_configs_2023_22_08/"

# iterate through all file
for file in os.listdir():

    list_device_config = []
    vprn_INT_names = []
    vprn_srvID = []
    vprn_customer = []
    vprn_name = []
    vprn_sap_int = []
    sap_int_to_be_removed = []
    # Check whether file is in text format or not
    if file.endswith(".setconf"):
        file_path = f"{path}/{file}"
        new_name = file.split(".")
        with open(file_path, 'r') as device_config:
            result = open(path_for_new_config + new_name[0] + "-newconfig.txt", "w+")
            for x in device_config:
                list_device_config.append(x)

            for i in list_device_config:
                match = re.match(VPRN, i)
                if match and match.group(4) not in vprn_INT_names:
                    # print(match.group(1) + " " + match.group(2) + " " + match.group(3) + " " + match.group(4) + " " + match.group(5))
                    vprn_customer.append(match.group(3))
                    vprn_name.append(match.group(2))
                    vprn_srvID.append(match.group(1))
                    vprn_INT_names.append(match.group(4))
                    vprn_sap_int.append(match.group(5))

            # /configure service vprn 10001 name "Abis" customer 10 interface "Abis-Kopernik" sap 1/1/1:2434 create
            for x in range(len(vprn_INT_names)):
                description_patter = r'/configure service vprn {0} name {1} customer {2} interface {3} sap {4} description (.*)'.format(
                    re.escape(vprn_srvID[x]),
                    re.escape(vprn_name[x]),
                    re.escape(vprn_customer[x]),
                    re.escape(vprn_INT_names[x]),
                    re.escape(vprn_sap_int[x]))

                for i in list_device_config:
                    match_des = re.match(description_patter, i)
                    if match_des:
                        print(match_des.group(1))
                        sap_int_to_be_removed.append(vprn_sap_int[x])

            for n in range(len(vprn_INT_names)):
                if vprn_sap_int[n] not in sap_int_to_be_removed:
                    result.write('/configure service vprn {0} name {1} customer {2} interface {3} sap {4} description {5}'.format(vprn_srvID[n],
                                                                                                                                  vprn_name[n],
                                                                                                                                  vprn_customer[n],
                                                                                                                                  vprn_INT_names[n],
                                                                                                                                  vprn_sap_int[n],
                                                                                                                                  vprn_INT_names[n]))
                    result.write("\n")
                    print('/configure service vprn {0} name {1} customer {2} interface {3} sap {4} description {5}'.format(vprn_srvID[n],
                                                                                                                           vprn_name[n],
                                                                                                                           vprn_customer[n],
                                                                                                                           vprn_INT_names[n],
                                                                                                                           vprn_sap_int[n],
                                                                                                                           vprn_INT_names[n]))
            result.write("\n")
            result.close()

        net_connect.write_channel(f" ssh {user}@{new_name[0]}\n")
        time.sleep(2)
        response = net_connect.read_channel()
        if response.endswith("? "):
            net_connect.write_channel("yes\n")
            time.sleep(10)
            net_connect.write_channel(f"{passw}\n")
            time.sleep(10)
            print(net_connect.find_prompt())
            redispatch(net_connect, device_type="nokia_sros")
            net_connect.send_config_from_file(path_for_new_config + new_name[0] + "-newconfig.txt", cmd_verify=False, read_timeout=120.0)
            net_connect.send_command("logout", expect_string="$", cmd_verify=False, read_timeout=120.0)
        if "password" in response:
            net_connect.write_channel(f"{passw}\n")
            time.sleep(10)
            print(net_connect.find_prompt())
            redispatch(net_connect, device_type="nokia_sros")
            net_connect.send_config_from_file(path_for_new_config + new_name[0] + "-newconfig.txt", cmd_verify=False, read_timeout=120.0)
            net_connect.send_command("logout", expect_string="$", read_timeout=120.0)

net_connect.disconnect()
