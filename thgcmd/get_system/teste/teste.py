from thgcmd.get_system.ip import IpInformation
import json
ipinfo = IpInformation()
print(ipinfo)
print("get_all_interfaces")
ipinfo.get_all_interfaces()
print('get_dict')
print(ipinfo.get_dict())
print(ipinfo.get_json())
