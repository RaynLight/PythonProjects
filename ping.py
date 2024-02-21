"""
This python file pings all IP addresses and records it in a json file
Pings from 1.1.1.1 to 255.255.255.255
Records true if IP pinged back and false if IP didn't respond
Only pings once to improve efficiency, may improve this python file in the future
"""


import os
import json

octOne = 1
octTwo = 1
octThree = 1
octFour = 1

json_file_path = input("What would you like your JSON file to be named?")

while octOne < 255:
    
    ip = f"{octOne}.{octTwo}.{octThree}.{octFour}"
    result = os.system(f"ping -4 -n 1 {ip}")
    pingable = result == 0
    data = {ip:pingable}
    
    json.dumps(data)

    with open(json_file_path, 'a') as json_file:
        json.dump(data, json_file)
        json_file.write('\n')

    octFour += 1
    if octFour >= 255:
        octThree += 1
        octFour = 1
    if octThree >= 255:
        octTwo += 1
        octThree = 1
    if octTwo >= 255:
        octOne += 1
        octTwo = 1
    if octOne == 255:
        break
