import requests
import json
from settings import config


def send_request(holder = config.holder, token = config.token):
    #define requests
    returned_value = requests.get("https://scan.tomochain.com/api/token-txs/trc21?holder={}&token={}".format(holder,token)) #raw value
    jsonified_value = returned_value.json() #jsonified
    items = jsonified_value['items']
    return items

#relatives is a list which contains holders
def request_relative(relatives, holder = config.holder):
    print(f'Tracking user: {holder}')
    items = send_request(holder)
    for item in items:
        transaction = [item['to']]
        for partner in transaction:
            if partner not in relatives:
                relatives.append(partner)
                request_relative(relatives, holder=partner)
    return

def get_all_relatives():
    relatives = []
    request_relative(relatives)
    count = len(relatives)
    json_data = {
        'count': count,
        'relatives': relatives
    }
    with open('relatives.json', 'w') as f:
        json.dump(json_data, f)
    return json_data

if __name__ == "__main__":
    get_all_relatives()