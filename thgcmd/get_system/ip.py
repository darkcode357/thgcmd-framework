from netifaces import *
import netifaces as ni
import json
class IpInformation:
    """
    >>> interface_info  = IpInformation()
    >>> interface_info.get_all_interfaces()
    lo: 127.0.0.1
    eth0: No IP addr
    wlan0: 192.168.0.116
    lxcbr0: 10.0.3.1
    docker0: 172.17.0.1
    teredo: No IP addr
    >>> print(interface_info.get_dict())
    {'lo': {'addr': '127.0.0.1', 'netmask': '255.0.0.0', 'peer': '127.0.0.1'}, 'eth0': {'addr': 'No IP addr'}, 'wlan0': {'addr': '192.168.0.116', 'netmask': '255.255.255.0', 'broadcast': '192.168.0.255'}, 'lxcbr0': {'addr': '10.0.3.1', 'netmask': '255.255.255.0', 'broadcast': '10.0.3.255'}, 'docker0': {'addr': '172.17.0.1', 'netmask': '255.255.0.0', 'broadcast': '172.17.255.255'}, 'teredo': {'addr': 'No IP addr'}}
    >>> print(interface_info.get_json())
    """
    def __init__(self):
        self.__list_of_interfaces = ni.interfaces()
    def get_ip_from_interface(self, interface):
        for list_interface in self.__list_of_interfaces:
            if interface in list_interface:
                return interface
    def get_all_interfaces(self):
        from netifaces import interfaces, ifaddresses, AF_INET
        for ifaceName in interfaces():
            addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
            print('{}: {}'.format(ifaceName, ', '.join(addresses)))
    def get_dict(self):
        addr_info_list  = []
        interfaces_list = []
        for i in interfaces():
            result = ifaddresses(i)
            addr_info_list.append(result)
        for interface in self.__list_of_interfaces:
            interfaces_list.append(interface)
        dictionary = dict(zip(interfaces_list, addr_info_list))
        dictionary_dic = dict(dictionary)
        return dictionary_dic
    def get_json(self):
        json_object = json.dumps(self.get_dict(), indent=4)
        return json_object



