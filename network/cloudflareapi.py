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
    method = ''

    def __init__(self):
        self.headers["Content-Type"] = "application/json"

    def __del__(self):
        self.headers = None

    # Set auth methods
    def set_auth_token(self, token):
        self.headers["Authorization"] = f"Bearer {token}"

    def set_auth_key(self, key, email):
        self.headers["X-Auth-Key"] = key
        self.headers["X-Auth-Email"] = email

    # Actions
    def list_domains(self, account_id):
        self.url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/registrar/domains"

    # Send request
    def send_request(self):
        try:
            response = requests.request(self.method, self.url, headers=self.headers, data=self.body)
        except requests.exceptions.RequestException:
            error("Request failed")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str, help='set action')
    parser.add_argument('--auth-token', type=str, help="set auth token")
    parser.add_argument('--auth-key', type=str, help="set auth key")
    parser.add_argument('--auth-email', type=str, help="set auth email")
    parser.add_argument('--account-id', type=str, help="set account id")
    parser.add_argument('--zone-id', type=str, help="set zone id")
    args = parser.parse_args()

    cloudflare = Cloudflare()

    if args.auth_token:
        cloudflare.set_auth_token(args.auth_token)
    elif args.auth_key and args.auth_email:
        cloudflare.set_auth_key(args.auth_key, args.auth_email)
    else:
        error('Auth method not specified. Token or key and email must be set.')

    if args.action == 'list-domains':
        if not args.account_id:
            error('Account id not specified.')
        cloudflare.list_domains(args.account_id)
        cloudflare.send_request()