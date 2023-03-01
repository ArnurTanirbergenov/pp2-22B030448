import json
with open("sample-data.json","r", encoding='utf-8') as json_file:
   a = json.load(json_file)
   print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU
-------------------------------------------------- --------------------  ------  ------""")
   for item in a["imdata"]:
       attributes = item["l1PhysIf"]["attributes"]
       print(f"{attributes['dn'] + ' '* (50 - len(attributes['dn']))} {' '* (20)} {attributes['speed'] + ' '* (8 - len(attributes['speed']))}  {attributes['mtu'] + ' '* (6 - len(attributes['mtu']))}")
print(list(map(len, "-------------------------------------------------- --------------------  ------  ------".split())))
#topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
