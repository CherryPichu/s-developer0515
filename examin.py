import sys
import os
import re
import pandas as pd
# awk '{print $1, $7}' /var/log/apache2/access.log > ~/extracted_attacks.log

def extract_sqlInjection(log : str) :
    pattern = r"(?:%27|['\"#])\S+" # by chatgpt
    return re.findall(pattern, log)

def extract_sqlInjection(log : str) :
    pattern = r"(?:%27|['\"#])\S+" # by chatgpt
    return re.findall(pattern, log)

logs = []

with open("./access.log", "rt+") as f : 
    for log in f.read().split("\n") :
        logs.append(log)
        
data = []

for log in logs :
    injecion = extract_sqlInjection(log)
    if len(injecion) < 1 :
        continue
    data.append(
        {
            "ip" : log.split(" ")[0],
            "url" : log.split(" ")[2],
            "date" : log.split(" ")[1][1:],
            "sqlInjection" : injecion[0]
        }
    )
    
# print(data)
    
df = pd.DataFrame(data)
df.to_csv("./sqlInjection.csv", index=False)

