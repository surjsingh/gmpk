import requests
import json

url = 'http://169.254.169.254/latest/'
endpoint = ["meta-data/"]


def metadatatree(url,endpoint):
    output = {}
    for entry in endpoint:
        new_url = url + entry
        r = requests.get(new_url)
        text = r.text
        if entry[-1] == "/":
            splitvalues = r.text.splitlines()
            output[entry[:-1]] = metadatatree(new_url, splitvalues)
        else:
           output[entry] = text
    return output


def get_metadata_json():
    metadata = metadatatree(url,endpoint)
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json


print(get_metadata_json())