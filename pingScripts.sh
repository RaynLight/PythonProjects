#!/bin/bash

for i in {1..255}
do
    
    echo "
import os
import json


octTwo = 1
octThree = 1
octFour = 1

while octTwo < 255:
    
    ip = f'$i.{octTwo}.{octThree}.{octFour}'
    result = os.system(f'fping -a {ip} -i 1 -b 12')
    pingable = result == 0
    data = {ip:pingable}
    
    json.dumps(data)
    json_file_path = 'data$i.json'
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
    if octTwo == 255:
        break
" > ping$i.py
    
    
done