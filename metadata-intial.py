import requests
import json

url = 'http://169.254.169.254/latest/meta-data/'


def get_metadata_json(url):
    output = {}
    r = requests.get(url)
    text = r.text
    value_list = r.text.splitlines() #convert the above text string into list at line breaks
    print(value_list)
    for i in value_list:
        newurl = url + i
        r = requests.get(newurl)
        if i[-1] == "/":
            nested_list = r.text.splitlines()
            print(nested_list)
            for n in nested_list:
                nestednewurl = newurl + n
                print(nestednewurl)
                r = requests.get(nestednewurl)
                text = r.text
                print(text)
                print(json.dumps(text))



get_metadata_json(url)