import re
import time
import netmiko
import os
from netmiko import redispatch
from datetime import datetime, timedelta
from getpass import getpass
import sys

# /configure service vprn 50001 name "AXS-MGMT" customer 50 interface "sfl-xploretv-sw_AXS-MGMT_2" vrrp 48 init-delay 900

server_user = str(input("What is your user_name for the jump server: "))
server_passw = getpass("What is your passw for the jump server: ")

net_connect = netmiko.ConnectHandler(
    device_type="linux_ssh",
    host="10.251.192.162",
    username=server_user,
    password=server_passw,
    session_log='netmiko_session.log',
)

user = input("please provide a username to log on the device. ")
passw = getpass("plese provide a password for log on the device. ")

path = "C:/Users/User/PycharmProjects/Automation/Initial_deley/configs/"
path_for_new_config = "C:/Users/User/PycharmProjects/Automation/Initial_deley/new_configs/"
device_names = []

os.chdir(path)
for file in os.listdir():
    # Check whether file is in text format or not
    list_config_device = []
    if file.endswith(".setconf"):
        file_path = f"{path}/{file}"
        new_name = file.split(".")
        with open(file_path, 'r') as device_config:
            print("############### " + new_name[0] + " ###############")
            device_names.append(new_name[0])
            vrrp_number = []
            vrrp_name = []
            vrrp_customer = []
            vrrp_int = []
            vrrp_id = []
            checker_vprn_vrrp = []
            for i in device_config:
                list_config_device.append(i)

            patter_vrrp = r'/configure service vprn (.*) name (.*) customer (.*) interface (.*) vrrp (\S+) '

            for x in list_config_device:
                match_vrrp = re.match(patter_vrrp, x)
                if match_vrrp:
                    checker = str(match_vrrp.group(1) + "-" + match_vrrp.group(4) + "-" + match_vrrp.group(5))
                    if checker not in checker_vprn_vrrp:
                        vrrp_number.append(match_vrrp.group(1))
                        vrrp_name.append(match_vrrp.group(2))
                        vrrp_customer.append(match_vrrp.group(3))
                        vrrp_int.append(match_vrrp.group(4))
                        vrrp_id.append(match_vrrp.group(5))
                        checker_vprn_vrrp.append(checker)
                        print(match_vrrp.group(1) + match_vrrp.group(2) + match_vrrp.group(3) + match_vrrp.group(4) + match_vrrp.group(5))

            if vrrp_number:
                result = open(path_for_new_config + new_name[0] + "-newconfig.txt", "w+")
                for i in range(len(vrrp_number)):
                    result.write("/configure service vprn {0} name {1} customer {2} interface {3} vrrp {4} init-delay 900 \n".format(vrrp_number[i],
                                                                                                                                     vrrp_name[i],
                                                                                                                                     vrrp_customer[i],
                                                                                                                                     vrrp_int[i],
                                                                                                                                     vrrp_id[i]))
                result.close()
            else:
                print("No vrrp")

os.chdir(path_for_new_config)

for i in os.listdir():
    if i.endswith(".txt"):
        new_name = i.split("-new")
        commands = []
        f = open(i)
        for n in f:
            commands.append(n)

        net_connect.write_channel(f" ssh {user}@{new_name[0]}\n")
        now = datetime.now()
        while datetime.today() < now + timedelta(seconds=100):
            response = net_connect.read_channel()
            if response != "":
                break
            time.sleep(1)
        if response.endswith("? "):
            net_connect.write_channel("yes\n")
            now = datetime.now()  # 10:00
            while datetime.today() < now + timedelta(seconds=100):
                response = net_connect.read_channel()
                if response != "":
                    break
                time.sleep(1)
            # net_connect.send_config_from_file(path_for_new_config + new_name[0] + "-newconfig.txt", read_timeout=120.0)
        if response.endswith("? "):
            net_connect.write_channel("yes\n")
            now = datetime.now()  # 10:00
            while datetime.today() < now + timedelta(seconds=100):
                response = net_connect.read_channel()
                if response != "":
                    break
                time.sleep(1)
        if "password" in response:
            net_connect.write_channel(f"{passw}\n")
            now = datetime.now()
            while datetime.today() < now + timedelta(seconds=100):
                response = net_connect.read_channel()
                if response != "":
                    break
                time.sleep(1)
            print(net_connect.find_prompt())
            redispatch(net_connect, device_type="nokia_sros")
            for q in commands:
                output = net_connect.send_command(q, read_timeout=120.0)
                if "MINOR: VRRP #1111 Operation not allowed - not allowed in passive vrrp" in output:
                    print(output)
                elif "MINOR:" in output or "MAJOR:" in output or "CRITICAL:" in output or "ERROR:" in output:
                    print(output)
                    exit()
                    # net_connect.send_config_from_file(path_for_new_config + new_name[0] + "-newconfig.txt", read_timeout=120.0)
            net_connect.send_command("exit all\n", read_timeout=120.0)
            net_connect.send_command("admin save\n", expect_string="#", read_timeout=120.0)
            net_connect.send_command("logout", expect_string="$", read_timeout=120.0)
            redispatch(net_connect, device_type="linux_ssh")

net_connect.disconnect()