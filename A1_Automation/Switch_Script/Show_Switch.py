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

    output = net_connect.send_command("show ip access-list 55")
    print("The config of \n"
          + i
          + "\n"
          + output +
          "\n")
