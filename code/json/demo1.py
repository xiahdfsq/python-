import json

json_str = '[{'name': 'kk'}]'
python_dict = json.loads(json_str)


python_dict2 = [{'name': 'kk'}]
json_str2 = json.dumps(python_dict2)