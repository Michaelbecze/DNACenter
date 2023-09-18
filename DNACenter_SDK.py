from dnacentersdk import api 
import json

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com', username='devnetuser', password='Cisco123!', verify=False)


devices = dna.devices.get_device_list()
print(json.dumps(devices, indent=2, sort_keys=True))

#print('{0:25}{1:1}{2:45}{3:1}{4:15}'.format("Device Name", "|", "Device Type", "|", "Up Time"))
#print("-" * 95)
#for device in devices.response:
#    print('{0:25}{1:1}{2:45}{3:1}{4:15}'.format(device.hostname, "|", device.type, "|", device.upTime))

#health = dna.clients.get_overall_client_health()
#print(health)