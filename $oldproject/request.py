import requests
import json


def request():
    requestFILE = 'https://lab.isaaclin.cn/nCoV/api/overall?latest=0'

    jsontext = requests.get(requestFILE).text
    with open('data.json', 'w') as f:
        f.write(jsontext)

    data = [(i['confirmedCount'],
             i['suspectedCount'],
             i['curedCount'],
             i['deadCount'])\
            for i in json.loads(jsontext)['results']][::-1]
    data = [list(i) for i in zip(*data)]
    
    return {'confirmed': data[0],
            'suspected': data[1],
            'cured': data[2],
            'dead': data[3]}

if __name__ == '__main__':
    print(request())
