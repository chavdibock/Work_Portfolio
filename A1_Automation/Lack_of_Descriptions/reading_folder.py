import os
import time
import netmiko
from netmiko import redispatch

path = "/Configs_2023_22_08/"
os.chdir(path)
path_for_new_config = "/new_configs_2023_22_08/"

VPRN = r'/configure\s+service\s+vprn\s+(.*)\s+name\s+(.*)\s+customer\s+(.*)\s+interface\s+(.*)\s+sap\s+(.*)\s+create'

server_user = str(input("What is your user_name for the jump server"))
server_passw = str(input("What is your password for the jump server"))
user = input("please provide a username to log on the device. ")
passw = input("plese provide a password for log on the device. ")
net_connect = netmiko.ConnectHandler(
    device_type="linux_ssh",
    host="10.251.192.162",
    username=server_user,
    password=server_passw,
    session_log='netmiko_session.log',
)
router_name = "lab-ngu-gw1"

print(net_connect.find_prompt())
net_connect.write_channel(f" ssh {user}@{router_name}\n")
time.sleep(2)
response = net_connect.read_channel(read_timeout=120)
if response.endswith("?"):
    net_connect.write_channel("yes")
if "password" in response:
    net_connect.write_channel(f"{passw}\n")
    time.sleep(2)
    print(net_connect.find_prompt())
    redispatch(net_connect, device_type="nokia_sros")
    net_connect.send_config_from_file(path_for_new_config + router_name + "-newconfig.txt")
