import json
import requests

organization = "virtual-labs"
no_of_pages = 6
vlabs_repos = []

for page in range(1, (no_of_pages+1)):
    print page;
    url = 'https://api.github.com/orgs/%s/repos?page=%d' %(organization, page);
    r = requests.get(url);
    r.status_code
    data = r.json();
    print len(data);

    for repo in range(0, len(data)):
        temp_dict = {}
        name = data[repo]['name']
        url = data[repo]['clone_url'];
        temp_dict['repo_name'] =  name
        temp_dict['repo_url'] =  url
        vlabs_repos.append(temp_dict)
f= open("virtual-labs-repos.json","w+")
f.write(json.dumps(vlabs_repos))
print json.dumps(vlabs_repos);
