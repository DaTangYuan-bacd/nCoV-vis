import requests
import json
from codecs import open


def format_json(data):
    with open('nCoV.json', 'w') as f:
        f.write(json.dumps([{'confirmedCount': i['confirmedCount'],
                             'suspectedCount': i['suspectedCount'],
                             'curedCount': i['curedCount'],
                             'deadCount': i['deadCount']}
                            for i in data[::-1]]))


# requestFILE = 'https://lab.isaaclin.cn/nCoV/api/overall?latest=0'
# The API do not response time-series data anymore

data = json.loads(open('nCoV.json', encoding='utf-8').read())
format_json(data)

data = [(i['confirmedCount'],
             i['suspectedCount'],
             i['curedCount'],
             i['deadCount'])\
            for i in data[::-1]]

confirmed, suspected, cured, dead \
    = [list(i) for i in zip(*data)]

length = len(data)

if __name__ == '__main__':
    print(data)
