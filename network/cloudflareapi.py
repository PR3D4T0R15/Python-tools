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
    body = {}

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
    parser.add_argument('--auth-token', type=str, help="set auth token")
    parser.add_argument('--auth-key', type=str, help="set auth key")
    parser.add_argument('--auth-email', type=str, help="set auth email")
    args = parser.parse_args()

    cloudflare = Cloudflare()

    if args.auth_token:
        cloudflare.set_authtoken(args.auth_token)
    elif args.auth_key and args.auth_email:
        cloudflare.set_authkey(args.auth_key, args.auth_email)
    else:
        error('Auth method not specified. Token or key and email must be set.')
