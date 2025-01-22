#!/usr/bin/env python3
import requests


def get_ip():
    url = "https://api.ipify.org"
    data = {}

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        data['status'] = "ERROR"
    else:
        data['status'] = "OK"
        data['address'] = response.text

    return data


if __name__ == '__main__':
    output = get_ip()
    print(output)
