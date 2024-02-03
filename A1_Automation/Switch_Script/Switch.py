from netmiko import ConnectHandler

user = input("Please enter ssh user of devie ")
password = input("Please enter ssh password of devie ")

f = open("device.txt")

for i in f:
    net_connect = ConnectHandler(
        device_type="cisco_ios",
        host=i,
        username=user,
        password=password,
    )



    output = net_connect.send_config_set("conf t",
                                         "ip access-list standard 55",
                                         "permit host 10.155.19.27",
                                         "permit host 10.155.19.28"
                                         )

    print(output)