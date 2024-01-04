router_dict = {
    'interface': 'ge0/0',
    'description': 'connected to the MPLS Network',
    'ip-address': '192.168.3.1',
    'subnet-mask': '255.255.255.0',
}

print(router_dict)
print('*' * 100)
print('number of items in the dictionary: '+ str(len(router_dict)))

print('*' * 100)
interface_ip = router_dict['ip-address']
print('interface IP address is: '+ interface_ip)


