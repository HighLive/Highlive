import json, os

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error : Can not initialize path :" + path)

def return_json(input_data, path):
    if type(input_data) != type({}):
        data = input_data.to_dict()
    else: 
        data = input_data

    json_data = [[k, v] for k, v in data.items()]
    with open(path, 'w') as outfile:
        json.dump(json_data, outfile)

def make_path(data_dir, data_type, id):
    path = {}
    for type in data_type:
        dir_path = data_dir + type + '/'
        create_dir(dir_path)
        path[type] = dir_path + id + '.json'
    return path