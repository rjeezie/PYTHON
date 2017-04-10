
import json
import yaml

my_list = range(8)
my_list.append('Whatever')
my_list.append('test')
my_list.append('{}')
my_list.append({})
my_list[-1]['ip_addr'] = '10.10.10.239'
my_list[-1]['attribs'] = range(5)

with open("WEEK1YAML.yml", "w") as f:
	f.write(yaml.dump(my_list, default_flow_style=False))

with open("WEEK1JSON.json", "w") as f:
	json.dump(my_list, f)
