import json
import requests

url = 'https://outreach.vlabs.ac.in/nodal_centres';
r = requests.get(url);
r.status_code
data = r.json();
print len(data);

temp_dict = []
for n_center in range(0, len(data)):
    name = data[n_center]['created_by']['institute_name']
    temp_dict.append(name)

result ={}
for i in set(temp_dict):
    result[i] = temp_dict.count(i)

print result
