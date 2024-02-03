import re
import ipaddress
from netmiko import ConnectHandler
import socket
from difflib import SequenceMatcher

# FQDN
pattern = r'^access-list\s+\S+\s+line\s+\d+\s+extended\s+permit\s+tcp\s+fqdn\s+(\S+)\s+(\S+)\s+host\s+(\S+)\s+eq\s+(\S+)\s+(\S+)'

# NORMAL
pattern2 = r'^access-list\s+(\S+)\s+line\s+\d+\s+extended\s+permit\s+(\S+)\s+host\s+(\S+)\s+host\s+(\S+)\s+eq\s+(\S+)\s+(\S+)\s+(\S+)'

# pattern for ACLs that have some sort of FQDN between hosts
pattern2_normal_with_FQDN = r'^access-list\s+(\S+)\s+line\s+\d+\s+extended\s+permit\s+(\S+)\s+host\s+(\S+)\s+(\S+)\s+host\s+(\S+)\s+eq\s+(\S+)\s+(\S+)\s+(\S+)'

# object-group FQDNesd
pattern4 = r'access-list\s+(\S+)\s+line\s+\d+\s+extended\s+permit\s+tcp\s+object-group\s+(\S+)\s+host\s+(\S+)\s+eq\s+(\S+)\s+(\S+)'

# permitIP
pattern_for_permit_ip = r'^access-list\s+(\S+)\s+line\s+\d+\s+extended\s+permit\s+ip\s+host\s+(\S+)\s+host\s+(\S+)\s+(\S+)\s+(\S+)'

# ACL with network source
patter_network = r'access-list\s+(\S+)\s+line\s+(\S+)\s+extended\s+permit\s+(\S+)\s+(\S+)\s+(\S+)\s+host\s+(\S+)\s+eq\s+(\S+)\s+(\S+)\s+(\S+)'

pattern_network_inverted = r'access-list\s+(\S+)\s+line\s+(\S+)\s+extended\s+permit\s+(\S+)\s+host\s+(\S+)\s+(\S+)\s+(\S+)\s+eq\s+(\S+)\s+(\S+)\s+(\S+)'

# ACL with network source and range of services
patter_network_range = r'access-list\s+(\S+)\s+line\s+(\S+)\s+extended\s+permit\s+(\S+)\s+(\S+)\s+(\S+)\s+host\s+(\S+)\s+range\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'

pattern_network_range_inverted = r'access-list\s+(\S+)\s+line\s+(\S+)\s+extended\s+permit\s+(\S+)\s+host\s+(\S+)\s+(\S+)\s+(\S+)\s+eq\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)'

# routing patterns
#ip_pattern = r'.*(\d+\.\d+\.\d+\.\d+)\/(\d+)\s+.*via\s\d+\.\d+\.\d+\.\d+,\s([^,]+),\s+.*'

ip_pattern = r'.* (.*)/(\d+)\s+.*via\s\d+\.\d+\.\d+\.\d+,\s([^,]+),\s+.*'
ip_pattern_2 = r'.*   (\S+[^\[^\]])\/(\S+) .*connected, (\S+[A-Z]*)\), .*'
ip_pattern_3 = r'.*   (\S+[^\[^\]])\/(\S+) .*connected, (\S+[A-Z]*)'
###################################################################################################
a = \
    """
    ################################################################################
                                        ATTENTION
        Dear user, thank you for trusting the script for migration to FortiGate.
        First you will be asked for your forti credentials in order to connect.
        Then the name of the path of the file where the CISCO ASA access-lists are.
        You will see aditional responses during the proces.
        If the desired newAddressObjects is not achieved, you have the ability to look at
        the "netmiko_session.log" for additional information.

    ################################################################################              
    """
print(a)


username = input("Provide firewall Username: ")
passw = input("Provide firewall password: ")

VDOM = input("Please enter the VDOM name: ")
""" 
###################################################################################
Connection Handler Fortigate 
###################################################################################
"""


net_connect = ConnectHandler(
    device_type="fortinet",
    host="192.168.112.26",
    username=username,
    password=passw,
    session_log='netmiko_session.log'
)


###################################################################################
#Query FortiGate for Route table, Service Objects and Address objects
###################################################################################

# Asking the Firewall for existing addresses

net_connect.send_command("config vdom \n", expect_string="#")
net_connect.send_command("edit " + VDOM + " \n", expect_string="#")
output_existing_addrs = net_connect.send_command("show firewall address", expect_string="#")
output_existing_servises = net_connect.send_command("show firewall service custom", expect_string="#")
routing_table = net_connect.send_command("get router info routing-table details", expect_string="#")

Existing_services_Forti = open("Existing_Servise.txt", "w+")  # creates file
Existing_services_Forti.write(output_existing_servises)
Existing_services_Forti.close()  # closes file



# saving the information to a file
Service_from_forti = open("Existing_Servise.txt", "r+")
existing_service = []
for i in Service_from_forti:
    existing_service.append(i)
Service_from_forti.close()


Existing_Addrs_Forti = open("forti_output_addrs.txt", "w+")
Existing_Addrs_Forti.write(output_existing_addrs)
Existing_Addrs_Forti.close()



# saving the information to a file
Addr_from_Forti = open("forti_output_addrs.txt", "r+")
existing_addr = []
for i in Addr_from_Forti:
    existing_addr.append(i)
Addr_from_Forti.close()



# Existing table from FortiGate
Forti_routing_Table = open("forti_Routing_Table.txt", "w+")
Forti_routing_Table.write(routing_table)
Forti_routing_Table.close()




# saving the routing table to a file
Forti_routing_Table = open("forti_Routing_Table.txt", "r+")
list_routing_table = []
for i in Forti_routing_Table:
    list_routing_table.append(i)
Forti_routing_Table.close()

pattern_existing_obj = r'^    edit\s+\"(\S+)\"'
existing_obj = []
for i in existing_addr:
    match_existing_addr = re.match(pattern_existing_obj, i)
    if match_existing_addr and match_existing_addr.group(1) not in existing_obj:
        existing_obj.append(match_existing_addr.group(1))

""" 
###################################################################################
Opens file with Migration Access-lists from ASA
###################################################################################
"""

Cisco_output = open("test.txt")
cisco_list_output = []
for i in Cisco_output:
    cisco_list_output.append(i.lstrip())
Cisco_output.close()

newAddressObjects = open("newAddressObjects.txt", "w+")
customService = open("new_Custom_service.txt", "w+")
srcIp = []
destIP = []
FQDN = []
service = []
# network arrays

# routing addrs
binary_addr = []
interface_names = []
binary_masks = []
# parsing the addrs and interface_names to arrays as binaries
for i in list_routing_table:
    match_ip = re.match(ip_pattern, i)
    match_ip_2 = re.match(ip_pattern_2, i)
    match_ip_3 = re.match(ip_pattern_3, i)
    if match_ip_2:
        # print(str(a) + " " + match_ip_2.group(1) + "/" + match_ip_2.group(2) + "---->" + match_ip_2.group(3))
        if not match_ip_2.group(1).startswith("[") and not match_ip_2.group(2).endswith("]"):
            ip = match_ip_2.group(1)
            routing_netw = ipaddress.IPv4Network(ip + "/" + match_ip_2.group(2))
            routing_mask = str(routing_netw.netmask)
            binary_addr.append('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
            interface_names.append(match_ip_2.group(3))
            binary_masks.append('.'.join([bin(int(x) + 256)[3:] for x in routing_mask.split('.')]))
    elif match_ip:
        if not match_ip.group(1).startswith("[") and not match_ip.group(2).endswith("]"):
            # print(str(a) + " " + match_ip.group(1) + "/" + match_ip.group(2) + "---->" + match_ip.group(3))
            ip = match_ip.group(1)
            routing_netw = ipaddress.IPv4Network(ip + "/" + match_ip.group(2))
            routing_mask = str(routing_netw.netmask)
            binary_masks.append('.'.join([bin(int(x) + 256)[3:] for x in routing_mask.split('.')]))
            binary_addr.append('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
            interface_names.append(match_ip.group(3))
    elif match_ip_3:
        if not match_ip_3.group(1).startswith("[") and not match_ip_3.group(2).endswith("]"):
            # print(str(a) + " " + match_ip.group(1) + "/" + match_ip.group(2) + "---->" + match_ip.group(3))
            ip = match_ip_3.group(1)
            routing_netw = ipaddress.IPv4Network(ip + "/" + match_ip_3.group(2))
            routing_mask = str(routing_netw.netmask)
            binary_masks.append('.'.join([bin(int(x) + 256)[3:] for x in routing_mask.split('.')]))
            binary_addr.append('.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')]))
            interface_names.append(match_ip_3.group(3))

"""
################################################################################################################
Takes IP addrs from ACL -> convert -> FortiGate Address Object
################################################################################################################
"""
# network hosts
networks = []
network_hosts = []  # The IP addrs that are under this network

# Arrays for "permit IP" case
src_permit_IP = []
dest_permit_IP = []
###################################################################################
patern_Service_Alphabetic = r'^    edit\s+\"(\S+)\"'
service_From_Forti = []

for i in existing_service:
    match_existing_service = re.match(patern_Service_Alphabetic, i)
    if match_existing_service:
        service_From_Forti.append(match_existing_service.group(1))

####################################################################################


newAddressObjects.write("config firewall address" + "\n")
customService.write("config firewall service custom \n")

# Going through the network cases
for x in cisco_list_output:
    match_network = re.match(patter_network, x)
    match_network_range = re.match(patter_network_range, x)
    match_network_inverted = re.match(pattern_network_inverted, x)
    match_network_range_inverted = re.match(pattern_network_range_inverted, x)

    if match_network and match_network.group(4) != "host":
        network_obj = ipaddress.IPv4Network(match_network.group(4) + "/" + match_network.group(5), strict=False)
        a = network_obj.prefixlen
        b = match_network.group(3).upper() + "-" + match_network.group(7)
        if match_network.group(6) not in destIP:
            destIP.append(match_network.group(6))
        if network_obj not in networks:
            networks.append(network_obj)
        if match_network.group(7).isdigit() == False and match_network.group(7).upper() not in service:
            service.append(match_network.group(7).upper())
            if match_network.group(7).upper() not in service_From_Forti:
                customService.write(
                    "edit " + match_network.group(7).upper() + "\n"
                    + "set " + match_network.group(3) + "-portrange " + str(
                        socket.getservbyname(match_network.group(7))) + "\n"
                    + "next" + "\n")
        if match_network.group(7).isdigit() and b not in service:
            service.append(b)

            if b not in service_From_Forti:
                customService.write("edit " + b + "\n"
                                    + "set " + match_network.group(3) + "-portrange " + match_network.group(7) + "\n"
                                    + "next" + "\n")

    elif match_network_range_inverted and match_network_range_inverted.group(5) != "host":
        service1 = match_network_range_inverted.group(7)
        service2 = match_network_range_inverted.group(8)
        mask = match_network_range_inverted.group(6)
        dest_addr = match_network_range_inverted.group(5)
        src_addr = match_network_range_inverted.group(4)
        b = match_network_range_inverted.group(3).upper() + "-" + service1 + "-" + service2  # TCP-1232-32434
        network_obj = ipaddress.IPv4Network(dest_addr + "/" + mask, strict=False)
        if dest_addr not in destIP:
            destIP.append(dest_addr)
        if network_obj not in networks:
            networks.append(network_obj)
        if src_addr not in srcIp:
            srcIp.append(src_addr)
        if service1.isdigit() and service2.isdigit() == False and (
                (match_network_range_inverted.group(3).upper() + "-" + service1 + "-" + str(
                    socket.getservbyname(service2))) not in service):
            if (match_network_range_inverted.group(3).upper() + "-" + service1 + "-" + str(
                    socket.getservbyname(service2))) not in service_From_Forti:
                customService.write("edit " + b + "\n"
                                    + "set " + match_network_range_inverted.group(
                    3) + "-portrange " + service1 + "-" + str(
                    socket.getservbyname(service2)) + "\n"
                                    + "next" + "\n")
                service.append(match_network_range_inverted.group(3) + "-portrange " + service1 + "-" + str(
                    socket.getservbyname(service2)))

        if service1.isdigit() == False and service2.isdigit() and (
                (match_network_range_inverted.group(3).upper() + "-" + str(
                    socket.getservbyname(service1)) + "-" + service2) not in service):
            if (match_network_range_inverted.group(3).upper() + "-" + str(
                    socket.getservbyname(service1)) + "-" + service2) not in service_From_Forti:
                customService.write(
                    "edit " + match_network_range_inverted.group(3).upper() + "-" + str(
                        socket.getservbyname(service1)) + "-" + service2 + "\n"
                    + "set " + match_network_range_inverted.group(3) + "-portrange " + str(
                        socket.getservbyname(service1)) + "-" + service2 + "\n"
                    + "next" + "\n"
                )

            service.append(match_network_range_inverted.group(3).upper() + "-" + str(
                socket.getservbyname(service1)) + "-" + service2)

        if service1.isdigit() == False and service2.isdigit() == False and (
                (match_network_range_inverted.group(3).upper() + "-" + str(socket.getservbyname(service1)) + "-" + str(
                    socket.getservbyname(service2))) not in service):
            if (match_network_range_inverted.group(3).upper() + "-" + str(socket.getservbyname(service1)) + "-" + str(
                    socket.getservbyname(service2))) not in service_From_Forti:
                customService.write(
                    "edit " + match_network_range_inverted.group(3).upper() + "-" + str(
                        socket.getservbyname(service1)) + "-" + str(
                        socket.getservbyname(service2)) + "\n"
                    + "set " + match_network_range_inverted.group(3) + "-portrange " + str(
                        socket.getservbyname(service1)) + "-" + str(
                        socket.getservbyname(service2)) + "\n"
                    + "next" + "\n")

            service.append(
                match_network_range_inverted.group(3).upper() + "-" + str(socket.getservbyname(service1)) + "-" + str(
                    socket.getservbyname(service2)))

        if service1.isdigit() and service2.isdigit() and b not in service:
            if b not in service_From_Forti:
                customService.write("edit " + b + "\n"
                                    + "set " + match_network_range_inverted.group(
                    3) + "-portrange " + service1 + "-" + service2 + "\n"
                                    + "next" + "\n")
            service.append(b)

    elif match_network_inverted and match_network_inverted.group(5) != "host" and match_network_inverted.group(
            8).startswith("(hitcnt="):
        network_obj = ipaddress.IPv4Network(match_network_inverted.group(5) + "/" + match_network_inverted.group(6),
                                            strict=False)
        if match_network_inverted.group(5) not in destIP:
            destIP.append(match_network_inverted.group(5))
        if network_obj not in networks:
            networks.append(network_obj)
        if match_network_inverted.group(4) not in srcIp:
            srcIp.append(match_network_inverted.group(4))
        if match_network_inverted.group(7).isdigit() == False and match_network_inverted.group(
                7).upper() not in service:
            service.append(match_network_inverted.group(7).upper())
            if match_network_inverted.group(7).upper() not in service_From_Forti:
                customService.write(
                    "edit " + match_network_inverted.group(7).upper() + "\n"
                    + "set " + match_network_inverted.group(3) + "-portrange " + str(
                        socket.getservbyname(match_network_inverted.group(7))) + "\n"
                    + "next" + "\n")

        if match_network_inverted.group(7).isdigit() and match_network_inverted.group(
                3).upper() + "-" + match_network_inverted.group(
                7) not in service:
            service.append(match_network_inverted.group(3).upper() + "-" + match_network_inverted.group(7))
            if match_network_inverted.group(3).upper() + "-" + match_network_inverted.group(
                    7) not in service_From_Forti:
                customService.write(
                    "edit " + match_network_inverted.group(3).upper() + "-" + match_network_inverted.group(7) + "\n"
                    + "set " + match_network_inverted.group(3) + "-portrange " + match_network_inverted.group(7) + "\n"
                    + "next" + "\n"
                )

    elif match_network_range:
        service1 = match_network_range.group(7)
        service2 = match_network_range.group(8)
        mask = match_network_range.group(5)
        src_network = match_network_range.group(4)
        network_obj = ipaddress.IPv4Network(src_network + "/" + mask, strict=False)
        b = match_network_range.group(3).upper() + "-" + service1 + "-" + service2  # TCP-1232-32434
        if match_network_range.group(6) not in destIP:
            destIP.append(match_network_range.group(6))
        if network_obj not in networks:
            networks.append(network_obj)
        if service1.isdigit() and service2.isdigit() == False and (
                (match_network_range.group(3).upper() + "-" + service1 + "-" + str(
                    socket.getservbyname(service2))) not in service):
            if (match_network_range.group(3).upper() + "-" + service1 + "-" + str(
                    socket.getservbyname(service2))) not in service_From_Forti:
                customService.write("edit " + b + "\n"
                                    + "set " + match_network_range.group(3) + "-portrange " + service1 + "-" + str(
                    socket.getservbyname(service2)) + "\n"
                                    + "next" + "\n")
                service.append(
                    match_network_range.group(3) + "-portrange " + service1 + "-" + str(socket.getservbyname(service2)))

        if service1.isdigit() == False and service2.isdigit() and (
                (match_network_range.group(3).upper() + "-" + str(
                    socket.getservbyname(service1)) + "-" + service2) not in service):
            if (match_network_range.group(3).upper() + "-" + str(
                    socket.getservbyname(service1)) + "-" + service2) not in service_From_Forti:
                customService.write(
                    "edit " + match_network_range.group(3).upper() + "-" + str(
                        socket.getservbyname(service1)) + "-" + service2 + "\n"
                    + "set " + match_network_range.group(3) + "-portrange " + str(
                        socket.getservbyname(service1)) + "-" + service2 + "\n"
                    + "next" + "\n"
                )

            service.append(
                match_network_range.group(3).upper() + "-" + str(socket.getservbyname(service1)) + "-" + service2)

        if service1.isdigit() == False and service2.isdigit() == False and (
                (match_network_range.group(3).upper() + "-" + str(socket.getservbyname(service1)) + "-" + str(
                    socket.getservbyname(service2))) not in service):
            if (match_network_range.group(3).upper() + "-" + str(socket.getservbyname(service1)) + "-" + str(
                    socket.getservbyname(service2))) not in service_From_Forti:
                customService.write(
                    "edit " + match_network_range.group(3).upper() + "-" + str(
                        socket.getservbyname(service1)) + "-" + str(
                        socket.getservbyname(service2)) + "\n"
                    + "set " + match_network_range.group(3) + "-portrange " + str(
                        socket.getservbyname(service1)) + "-" + str(
                        socket.getservbyname(service2)) + "\n"
                    + "next" + "\n")

            service.append(
                match_network_range.group(3).upper() + "-" + str(socket.getservbyname(service1)) + "-" + str(
                    socket.getservbyname(service2)))

        if service1.isdigit() and service2.isdigit() and b not in service:
            if b not in service_From_Forti:
                customService.write("edit " + b + "\n"
                                    + "set " + match_network_range.group(
                    3) + "-portrange " + service1 + "-" + service2 + "\n"
                                    + "next" + "\n")
            service.append(b)

######################################################################################################################################################

# Going through the normal cases

for x in cisco_list_output:
    match = re.match(pattern, x)
    match2 = re.match(pattern2, x)
    match4 = re.match(pattern4, x)
    match_normal_with_FQDN = re.match(pattern2_normal_with_FQDN, x)
    match_permit_ip = re.match(pattern_for_permit_ip, x)

    if match:  # FQDN
        if match.group(1) not in FQDN:
            FQDN.append(match.group(1))
        del x
        print("yes")
    elif match2:  # Fortigate Command for Normal access list
        a = match2.group(2).upper() + "-" + match2.group(5)
        if match2.group(3) not in srcIp:
            srcIp.append(match2.group(3))
        if match2.group(4) not in destIP:
            destIP.append(match2.group(4))
        if match2.group(5).upper() not in service and match2.group(5).isdigit() == False:
            service.append(match2.group(5).upper())
            if match2.group(5).upper() not in service_From_Forti:
                # Writing to the file which will add the new service
                customService.write(
                    "edit " + match2.group(5).upper() + "\n"
                    + "set " + match2.group(2) + "-portrange " + str(socket.getservbyname(match2.group(5))) + "\n"
                    + "next" + "\n")
        if match2.group(5).isdigit() and a not in service:
            service.append(a)
            if a not in service_From_Forti:
                customService.write("edit " + a + "\n"
                                    + "set " + match2.group(2) + "-portrange " + match2.group(5) + "\n"
                                    + "next" + "\n")

        print("yes")

        # Normal ACL that have FQDn in between
    elif match_normal_with_FQDN:
        a = match_normal_with_FQDN.group(2).upper() + "-" + match_normal_with_FQDN.group(6)
        if match_normal_with_FQDN.group(3) not in srcIp:
            srcIp.append(match_normal_with_FQDN.group(3))
        if match_normal_with_FQDN.group(5) not in destIP:
            destIP.append(match_normal_with_FQDN.group(5))
        if match_normal_with_FQDN.group(6).upper() not in service and match_normal_with_FQDN.group(
                6).isdigit() == False:
            service.append(match_normal_with_FQDN.group(6).upper())
            if match_normal_with_FQDN.group(6).upper() not in service_From_Forti:
                # Writing to the file which will add the new service
                customService.write(
                    "edit " + match_normal_with_FQDN.group(6).upper() + "\n"
                    + "set " + match_normal_with_FQDN.group(2) + "-portrange " + str(
                        socket.getservbyname(match_normal_with_FQDN.group(6))) + "\n"
                    + "next" + "\n")
        if match_normal_with_FQDN.group(6).isdigit() and a not in service:
            service.append(a)
            if a not in service_From_Forti:
                customService.write("edit " + a + "\n"
                                    + "set " + match_normal_with_FQDN.group(
                    2) + "-portrange " + match_normal_with_FQDN.group(6) + "\n"
                                    + "next" + "\n")

        print("Yes")
    # Permit IP
    elif match_permit_ip:
        src_permit_IP.append(match_permit_ip.group(2))
        dest_permit_IP.append(match_permit_ip.group(3))
        print("yes")
    elif match4:
        del x
        print("Yes")
    else:
        print("invalid \n")
        print(x + "\n")

######################################################################################################################################################


ID = int(input("Please enter the ID of the new policy want to migrate to "))
Policy_Name = input("Please enter the name of the new policy want to migrate to ")
FinalPolicy = open("Final_Policy.txt","w+")

# Creating the policy
name_number = 0
for x in destIP:
    dest_lpm = 0
    dest_int = ""
    dest_addr = x
    # Using the algorithm for LPM in order to find the destination interface in the routing table
    dest_bin_addr = '.'.join([bin(int(x) + 256)[3:] for x in dest_addr.split('.')])
    for y in range(len(binary_addr)):
        routing_table_mask = str(binary_masks[y])
        routing_addr = ""
        for i in range(len(dest_bin_addr)):
            if dest_bin_addr[i] == "1" and routing_table_mask[i] == "1":
                routing_addr += "1"
            elif dest_bin_addr[i] == "." and routing_table_mask[i] == ".":
                routing_addr += "."
            else:
                routing_addr += "0"
            if routing_addr == binary_addr[y]:
                dest_int = interface_names[y]

    for n in range(len(service)):

        src = []
        serv = []
        netw_host = []
        src_networks = []
        net_mask = ""
        src_net_mask = []
        for i in cisco_list_output:
            match2 = re.match(pattern2, i)
            match_normal_with_FQDN = re.match(pattern2_normal_with_FQDN, i)
            match_network = re.match(patter_network, i)
            match_network_inverted = re.match(pattern_network_inverted, i)
            match_network_range = re.match(patter_network_range, i)
            match_network_range_inverted = re.match(pattern_network_range_inverted, i)

            if match2 and match2.group(4) == x and (
                    match2.group(5).upper() == service[n] or match2.group(2).upper() + "-" + match2.group(5) == service[
                n]):
                b = match2.group(2).upper() + "-" + match2.group(5)
                if match2.group(3) not in src:
                    src.append(match2.group(3))
                    src_net_mask.append(" ")
                if match2.group(5).isdigit() and b not in serv:
                    serv.append(b)
                if match2.group(5).isdigit() == False and match2.group(5).upper() not in serv:
                    serv.append(match2.group(5).upper())

            elif match_normal_with_FQDN and match_normal_with_FQDN.group(5) == x and (
                    match_normal_with_FQDN.group(6).upper() == service[n] or match_normal_with_FQDN.group(
                2).upper() + "-" + match_normal_with_FQDN.group(6) == service[n]):

                b = match_normal_with_FQDN.group(2).upper() + "-" + match_normal_with_FQDN.group(6)
                if match_normal_with_FQDN.group(3) not in src:
                    src.append(match_normal_with_FQDN.group(3))
                    src_net_mask.append(" ")
                if match_normal_with_FQDN.group(6).isdigit() and b not in serv:
                    serv.append(b)
                if match_normal_with_FQDN.group(6).isdigit() == False and match_normal_with_FQDN.group(
                        6).upper() not in serv:
                    serv.append(match_normal_with_FQDN.group(6).upper())

            elif match_network and match_network.group(6) == x and match_network.group(6) != "host" and (
                    match_network.group(7).upper() == service[n] or (
                    match_network.group(3).upper() + "-" + match_network.group(7)) == service[n]):
                b = match_network.group(3).upper() + "-" + match_network.group(7)
                a = ipaddress.IPv4Network(match_network.group(4) + "/" + match_network.group(5), strict=False)
                if match_network.group(4) not in src:
                    src.append(match_network.group(4))
                    netw_host += a.hosts()
                    src_net_mask.append(match_network.group(5))
                if match_network.group(7).isdigit() == False and match_network.group(7).upper() not in serv:
                    serv.append(match_network.group(7).upper())
                if match_network.group(7).isdigit() and b not in serv:
                    serv.append(b)

            elif match_network_inverted and match_network_inverted.group(5) == x and match_network_inverted.group(
                    5) != "host" \
                    and match_network_inverted.group(8).startswith("(hitcnt=") and (
                    match_network_inverted.group(7).upper() == service[n] or
                    (match_network_inverted.group(3).upper() + "-" + match_network_inverted.group(7) == service[n])):
                b = match_network_inverted.group(3).upper() + "-" + match_network_inverted.group(7)
                a = ipaddress.IPv4Network(match_network_inverted.group(5) + "/" + match_network_inverted.group(6),
                                          strict=False)
                net_mask = match_network_inverted.group(6)
                if match_network_inverted.group(4) not in src:
                    src.append(match_network_inverted.group(4))
                    netw_host += a.hosts()
                    src_net_mask.append(match_network_inverted.group(6))
                if match_network_inverted.group(7).isdigit() == False and match_network_inverted.group(
                        7).upper() not in serv:
                    serv.append(match_network_inverted.group(7).upper())
                if match_network_inverted.group(7).isdigit() and b not in serv:
                    serv.append(b)

            #########################################################################################################################
            elif match_network_range and match_network_range.group(6) == x:
                a = ipaddress.IPv4Network(match_network_range.group(4) + "/" + match_network_range.group(5),
                                          strict=False)
                service1 = match_network_range.group(7)
                service2 = match_network_range.group(8)
                b = match_network_range.group(3).upper() + "-" + service1 + "-" + service2  # TCP-1232-32434

                if service1.isdigit() and service2.isdigit() == False and (
                        (match_network_range.group(3).upper() + "-" + service1
                         + "-" + str(socket.getservbyname(service2))) == service[n]):
                    net_mask = match_network_range.group(5)
                    if match_network_range.group(4) not in src:
                        src.append(match_network_range.group(4))
                        netw_host += a.hosts()
                        src_net_mask.append(match_network_range.group(5))
                    if (match_network_range.group(3).upper() + "-" + service1 + "-" + str(
                            socket.getservbyname(service2))) not in serv:
                        serv.append(
                            match_network_range.group(3).upper() + "-" + match_network_range.group(7) + "-" + str(
                                socket.getservbyname(service2))
                        )

                if service1.isdigit() == False and service2.isdigit() and (
                        (match_network_range.group(3).upper() + "-" + str(
                            socket.getservbyname(service1)) + "-" + service2) == service[n]
                ):
                    net_mask = match_network_range.group(5)
                    if match_network_range.group(4) not in src:
                        src.append(match_network_range.group(4))
                        netw_host += a.hosts()
                        src_net_mask.append(match_network_range.group(5))
                    if (match_network_range.group(3).upper() + "-" + str(
                            socket.getservbyname(service1)) + "-" + service2) not in serv:
                        serv.append(
                            match_network_range.group(3).upper() + "-" + str(
                                socket.getservbyname(service1)) + "-" + service2
                        )

                if service1.isdigit() == False and service2.isdigit() == False \
                        and ((match_network_range.group(3).upper() + "-" + str(socket.getservbyname(service1)) + "-"
                              + str(socket.getservbyname(service2))) == service[n]):
                    net_mask = match_network_range.group(5)
                    if match_network_range.group(4) not in src:
                        src.append(match_network_range.group(4))
                        netw_host += a.hosts()
                        src_net_mask.append(match_network_range.group(5))
                    if match_network_range.group(3).upper() + "-" + str(socket.getservbyname(service1)) + "-" + str(
                            socket.getservbyname(service2)) not in serv:
                        serv.append(match_network_range.group(3).upper() + "-" + str(
                            socket.getservbyname(service1)) + "-" + str(
                            socket.getservbyname(service2)))

                if match_network_range.group(7).isdigit() and match_network_range.group(8).isdigit() and b == service[
                    n]:
                    net_mask = match_network_range.group(5)
                    if match_network_range.group(4) not in src:
                        src.append(match_network_range.group(4))
                        netw_host += a.hosts()
                        src_net_mask.append(match_network_range.group(5))
                    if b not in serv:
                        serv.append(b)
            #########################################################################################################################
            elif match_network_range_inverted and match_network_range_inverted.group(5) == x:
                service1 = match_network_range_inverted.group(7)
                service2 = match_network_range_inverted.group(8)
                b = match_network_range_inverted.group(3).upper() + "-" + service1 + "-" + service2  # TCP-1232-32434
                a = ipaddress.IPv4Network(
                    match_network_range_inverted.group(5) + "/" + match_network_range_inverted.group(6))

                if service1.isdigit() and service2.isdigit() == False and (
                        (match_network_range_inverted.group(3).upper() + "-" + service1
                         + "-" + str(socket.getservbyname(service2))) == service[n]):

                    net_mask = match_network_range_inverted.group(6)
                    if match_network_range_inverted.group(4) not in src:
                        src.append(match_network_range_inverted.group(4))
                        netw_host += a.hosts()
                        src_net_mask.append(match_network_range_inverted.group(6))

                    if (match_network_range_inverted.group(3).upper() + "-" + service1 + "-" + str(
                            socket.getservbyname(service2))) not in serv:
                        serv.append(
                            match_network_range_inverted.group(3).upper() + "-" + match_network_range_inverted.group(
                                7) + "-" + str(
                                socket.getservbyname(service2))
                        )

                if service1.isdigit() == False and service2.isdigit() and (
                        (match_network_range_inverted.group(3).upper() + "-" + str(
                            socket.getservbyname(service1)) + "-" + service2) == service[n]
                ):

                    net_mask = match_network_range_inverted.group(6)
                    if match_network_range_inverted.group(4) not in src:
                        src.append(match_network_range_inverted.group(4))
                        netw_host += a.hosts()
                        src_net_mask.append(match_network_range_inverted.group(6))
                    if (match_network_range_inverted.group(3).upper() + "-" + str(
                            socket.getservbyname(service1)) + "-" + service2) not in serv:
                        serv.append(
                            match_network_range_inverted.group(3).upper() + "-" + str(
                                socket.getservbyname(service1)) + "-" + service2
                        )

                if service1.isdigit() == False and service2.isdigit() == False and (
                        (match_network_range_inverted.group(3).upper() + "-" + str(socket.getservbyname(service1))
                         + "-" + str(socket.getservbyname(service1))) == service[n]):

                    net_mask = match_network_range_inverted.group(6)
                    if match_network_range_inverted.group(4) not in src:
                        src.append(match_network_range_inverted.group(4))
                        netw_host += a.hosts()
                        src_net_mask.append(match_network_range_inverted.group(6))
                    if match_network_range_inverted.group(3).upper() + "-" + str(
                            socket.getservbyname(service1)) + "-" + str(
                            socket.getservbyname(service1)) not in serv:
                        serv.append(match_network_range_inverted.group(3).upper() + "-" + str(
                            socket.getservbyname(service1)) + "-" + str(
                            socket.getservbyname(service1)))

                if match_network_range_inverted.group(7).isdigit() and match_network_range_inverted.group(
                        8).isdigit() and b == service[n]:
                    net_mask = match_network_range_inverted.group(6)
                    if match_network_range_inverted.group(4) not in src:
                        src.append(match_network_range_inverted.group(4))
                        netw_host += a.hosts()
                        src_net_mask.append(match_network_range_inverted.group(6))
                    if b not in serv:
                        serv.append(b)
            #########################################################################################################################
        if src and serv:
            FinalPolicy.write("config firewall policy \n"
                              + "edit " + str(ID) + "\n"
                              + "set name " + Policy_Name + "_" + str(name_number) + "\n"
                              + "set dstintf " + dest_int + "\n"
                              )
            if x.endswith(".0"):
                netw = ipaddress.IPv4Network(x + "/" + net_mask, strict=False)
                FinalPolicy.write("set dstaddr " + str(netw) + "\n")
            else:
                FinalPolicy.write("set dstaddr " + x + "/32\n")

            ID += 1
            name_number += 1

            for q in range(len(src)):
                if ipaddress.ip_address(src[q]) not in netw_host:

                    if len(src) == 1:
                        if src[q].endswith(".0"):
                            FinalPolicy.write("set srcaddr " + str(
                                ipaddress.IPv4Network(src[q] + "/" + src_net_mask[q], strict=False)) + "\n")
                        else:
                            FinalPolicy.write("set srcaddr " + src[q] + "/32" + "\n")
                    elif q == 0:
                        if src[q].endswith(".0"):
                            FinalPolicy.write("set srcaddr " + str(
                                ipaddress.IPv4Network(src[q] + "/" + src_net_mask[q], strict=False)))
                        else:
                            FinalPolicy.write("set srcaddr " + src[q] + "/32")
                    elif q == (len(src) - 1):
                        if src[q].endswith(".0"):
                            FinalPolicy.write(
                                " " + str(ipaddress.IPv4Network(src[q] + "/" + src_net_mask[q], strict=False)) + "\n")
                        else:
                            FinalPolicy.write(" " + src[q] + "/32" + "\n")
                    elif 0 < q < len(src):
                        if src[q].endswith(".0"):
                            FinalPolicy.write(
                                " " + str(ipaddress.IPv4Network(src[q] + "/" + src_net_mask[q], strict=False)))
                        else:
                            FinalPolicy.write(" " + src[q] + "/32")

            src_int = []
            for q in range(len(src)):
                addr = src[q]
                bin_addr = '.'.join([bin(int(x) + 256)[3:] for x in addr.split('.')])
                source_int = ""
                for y in range(len(binary_addr)):
                    routing_table_mask = str(binary_masks[y])
                    routing_addr = ""
                    for i in range(len(bin_addr)):
                        if bin_addr[i] == "1" and routing_table_mask[i] == "1":
                            routing_addr += "1"
                        elif bin_addr[i] == "." and routing_table_mask[i] == ".":
                            routing_addr += "."
                        else:
                            routing_addr += "0"
                        if routing_addr == binary_addr[y]:
                            source_int = interface_names[y]
                if source_int not in src_int:
                    src_int.append(source_int)

            for q in range(len(src_int)):
                if len(src_int) == 1:
                    FinalPolicy.write("set srcintf " + src_int[q] + "\n")
                elif q == 0:
                    FinalPolicy.write("set srcintf " + src_int[q])
                elif q == (len(src_int) - 1):
                    FinalPolicy.write(" " + src_int[q] + "\n")
                elif 0 < q < len(src_int):
                    FinalPolicy.write(" " + src_int[q])

            for i in range(len(serv)):
                if len(serv) == 1:
                    FinalPolicy.write("set service " + serv[i] + "\n")
                elif i == 0:
                    FinalPolicy.write("set service " + serv[i])
                elif i == (len(serv) - 1):
                    FinalPolicy.write(" " + serv[i] + "\n")
                elif 0 < i < len(serv):
                    FinalPolicy.write(" " + serv[i])

            FinalPolicy.write("set action accept \n" + "set schedule always \n" + "end \n")

#############################################################################################################################################################


# creating PERMIT IP policy
seen_addrs = []
for i in range(len(dest_permit_IP)):
    src_int = []
    src_permit_addr = []
    dest_int = ""
    dest_permit_ip_addr = dest_permit_IP[i]
    binary_dest_permit_ip = '.'.join([bin(int(x) + 256)[3:] for x in dest_permit_ip_addr.split('.')])
    if dest_permit_ip_addr not in seen_addrs:
        for y in range(len(binary_addr)):
            routing_table_mask = str(binary_masks[y])
            routing_addr = ""
            for q in range(len(binary_dest_permit_ip)):
                if binary_dest_permit_ip[q] == "1" and routing_table_mask[q] == "1":
                    routing_addr += "1"
                elif binary_dest_permit_ip[q] == "." and routing_table_mask[q] == ".":
                    routing_addr += "."
                else:
                    routing_addr += "0"
                if routing_addr == binary_addr[y]:
                    dest_int = interface_names[y]

        FinalPolicy.write("config firewall policy \n"
                          + "edit " + str(ID) + "\n"
                          + "set name " + Policy_Name + "_" + str(name_number) + "\n"
                          + "set dstintf " + dest_int + "\n"
                          )
        ID += 1
        name_number += 1
        FinalPolicy.write("set dstaddr " + dest_permit_IP[i] + "/32\n")
        for a in range(len(dest_permit_IP)):
            if dest_permit_ip_addr == dest_permit_IP[a]:
                src_permit_addr.append(src_permit_IP[a])
                seen_addrs.append(dest_permit_IP[i])
        for n in range(len(src_permit_addr)):
            src_addr_temp = src_permit_addr[n]
            binary_src_permit_addr_temp = '.'.join([bin(int(x) + 256)[3:] for x in src_addr_temp.split('.')])
            source_int = ""
            if len(src_permit_addr) == 1:
                FinalPolicy.write("set srcaddr " + src_permit_addr[n] + "/32" + "\n")
            elif n == 0:
                FinalPolicy.write("set srcaddr " + src_permit_addr[n] + "/32")
            elif n == (len(src_permit_addr) - 1):
                FinalPolicy.write(" " + src_permit_addr[n] + "/32" + "\n")
            elif 0 < n < len(src_permit_addr):
                FinalPolicy.write(" " + src_permit_addr[n] + "/32")
            for p in range(len(binary_addr)):
                routing_table_mask = str(binary_masks[p])
                routing_addr = ""
                for b in range(len(binary_src_permit_addr_temp)):
                    if binary_src_permit_addr_temp[b] == "1" and routing_table_mask[b] == "1":
                        routing_addr += "1"
                    elif binary_src_permit_addr_temp[b] == "." and routing_table_mask[b] == ".":
                        routing_addr += "."
                    else:
                        routing_addr += "0"
                    if routing_addr == binary_addr[p]:
                        source_int = interface_names[p]
            if source_int not in src_int:
                src_int.append(source_int)
        for s in range(len(src_int)):
            if len(src_int) == 1:
                FinalPolicy.write("set srcintf " + src_int[s] + "\n")
            elif s == 0:
                FinalPolicy.write("set srcintf " + src_int[s])
            elif s == (len(src_int) - 1):
                FinalPolicy.write(" " + src_int[s] + "\n")
            elif 0 < s < len(src_int):
                FinalPolicy.write(" " + src_int[s])
        FinalPolicy.write("set action accept \n" + "set schedule always \n" + "set service all \n" + "end \n")
######################################################################################################################################################
# Config the FQDN object
for i in FQDN:
    if i not in existing_obj:
        newAddressObjects.write("edit " + i + "\n")
        newAddressObjects.write("set type fqdn" + "\n")
        newAddressObjects.write("set fqdn " + i + "\n")
        newAddressObjects.write("next" + "\n")

for i in range(len(srcIp)):  # For loop for making the objects
    if srcIp[i] not in existing_obj and srcIp[i].endswith(".0") == False:
        newAddressObjects.write("edit " + srcIp[i] + "/" + "32" + "\n")
        newAddressObjects.write("set subnet " + srcIp[i] + "/" + "32" + '\n')
        newAddressObjects.write("next" + "\n")

for i in range(len(destIP)):
    if destIP[i] not in existing_obj and destIP[i].endswith(".0") == False:
        newAddressObjects.write("edit " + destIP[i] + "/" + "32" + "\n")
        newAddressObjects.write("set subnet " + destIP[i] + "/" + "32" + "\n")
        newAddressObjects.write("next" + "\n")

for i in range(len(src_permit_IP)):
    if src_permit_IP[i] not in existing_obj:
        newAddressObjects.write("edit " + src_permit_IP[i] + "\n")
        newAddressObjects.write("set subnet " + src_permit_IP[i] + "/32" + '\n')
        newAddressObjects.write("next" + "\n")

# setting the dest addrs
for i in range(len(dest_permit_IP)):
    if dest_permit_IP[i] not in existing_obj:
        newAddressObjects.write("edit " + dest_permit_IP[i] + "\n")
        newAddressObjects.write("set subnet " + dest_permit_IP[i] + "/32" + '\n')
        newAddressObjects.write("next" + "\n")

for i in range(len(networks)):
    a = str(networks[i])
    if a not in existing_obj:
        newAddressObjects.write("edit " + a + "\n"
                                + "set subnet " + str(networks[i]) + "\n"
                                + "next" + "\n")

customService.write("end \n")
newAddressObjects.write("end \n")
newAddressObjects.close()
customService.close()
FinalPolicy.close()

######################################################################################################################################################

conformation = input("Do you want to proceed? yes/no")

if conformation == "yes":
    net_connect.send_config_from_file("newAddressObjects.txt")
    net_connect.send_config_from_file("new_Custom_service.txt")
    net_connect.send_config_from_file("Final_Policy.txt", cmd_verify=False)
    print("The script finished successfully")
else:
    print("The script is stopped")
