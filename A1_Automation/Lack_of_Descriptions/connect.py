import os
import time
import netmiko
from netmiko import redispatch

VPRN = r'/configure\s+service\s+vprn\s+(.*)\s+name\s+(.*)\s+customer\s+(.*)\s+interface\s+(.*)\s+sap\s+(.*)\s+create'

server_user = str(input("What is your user_name for the jump server"))
server_passw = str(input("What is your password for the jump server"))
user = input("please provide a username to log on the device. ")
passw = input("plese provide a password for log on the device. ")
net_connect = netmiko.ConnectHandler(
    device_type="linux_ssh",
    host="10.251.192.164",
    username=server_user,
    password=server_passw,
    session_log='netmiko_session.log'
)

path = "/Configs_2023_22_08/"
os.chdir(path)
path_for_new_config = "/new_configs_2023_22_08/"
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
        print(net_connect.find_prompt())
        net_connect.write_channel(f" ssh {user}@{new_name[0]}\n")
        time.sleep(2)
        response = net_connect.read_channel()
        if response.endswith("?"):
            net_connect.write_channel("yes")
        if "password" in response:
            net_connect.write_channel(f"{passw}\n")
            time.sleep(2)
            print(net_connect.find_prompt())
            redispatch(net_connect, device_type="nokia_sros")
            net_connect.send_config_from_file(path_for_new_config + new_name[0] + "-newconfig.txt", cmd_verify=False)
            net_connect.send_command("logout", expect_string="$", cmd_verify=False, read_timeout=15.0)
net_connect.disconnect()
