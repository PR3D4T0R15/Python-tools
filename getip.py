#!/usr/bin/env python3

import requests


def getIp():
    url = "https://api.ipify.org"
    data = {}
    response = None

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        data['status'] = "ERROR"
    else:
        data['status'] = "OK"
        data['address'] = response.text

    return data


if __name__ == '__main__':
    output = getIp()
    print(output)
