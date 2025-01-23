#!/usr/bin/env python3
import requests
import argparse
import sys


def error(msg):
    print({'status': 'error', 'message': msg})
    sys.exit(1)


class Cloudflare:
    url = ''
    headers = {}

    def __init__(self):
        self.url = "https://api.cloudflare.com"
        self.headers["Content-Type"] = "application/json"

    def __del__(self):
        self.headers = None

    def set_authtoken(self, token):
        self.headers["Authorization"] = f"Bearer {token}"

    def set_authkey(self, key, email):
        self.headers["X-Auth-Key"] = key
        self.headers["X-Auth-Email"] = email


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--authtoken', type=str, help="set auth token")
    parser.add_argument('--authkey', type=str, help="set auth key")
    parser.add_argument('--authemail', type=str, help="set auth email")
    args = parser.parse_args()

    cloudflare = Cloudflare()
