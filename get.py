import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import sys

toolbar_width = 20

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))

temp=[]
x = input("Go to Yocket and search for universities, then categorize them according to Name, Status (admit, interested, rejected) and Field (CompSci, Mechanical ... whatever")
name = input("Name of the University")
print("______________")
print(x)
print("Fetching URL...")
print("______________")
print("There is a wait time for 10s between each request here, we don't want to overload Yocket servers, be nice and don't remove that. After you continously run the program 3-4 times, give it a break of 4 hours. Happy apps!")

for i in range(toolbar_width):
    page = requests.get(x.format(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    time.sleep(10)
    name_containers = soup.find_all('div', class_ = 'col-sm-6')
    sys.stdout.write("#")
    sys.stdout.flush()
    for i in name_containers:
        k =(i.div.text)
        t=[i for i in k.strip().split("\n") if len(i) is not 0]
        temp.append(t)
sys.stdout.write("]\n") 

r= pd.DataFrame(temp)

r.rename(columns={0: 'Name', 'newName2': 'University', 1: 'University', 2: 'Year', 3: 'Status',4: 'GRE',5: 'GRE_SCORE',6: 'Eng_test',7:'Test_score',8: 'Undergrad',9: 'Undergrad_score',11: 'work_ex'}, inplace=True)

r = r.iloc[2:]
r = r.drop(['University'], axis = 1) 
r = r.drop(['Status'], axis = 1) 
r = r.drop(['GRE'], axis = 1) 
r = r.drop(['Undergrad'], axis = 1)
r.to_csv(name + '.csv')
print("______________")
print(r)
print("______________")
print("Go ahead and run visualize.py for summary and visualizations")
