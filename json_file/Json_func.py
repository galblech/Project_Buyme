import json

json_file = open("C:\\Users\\galbr\\PycharmProjects\\Project2_pre\\json\\config.json", 'r')
data = json.load(json_file)

def browser_type():
    browser = data['browserType']
    return browser

def get_url():
    url_list = data.get("url", [])
    return url_list
