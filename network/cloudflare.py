#!/usr/bin/env python3
import requests
import argparse
import sys


def error(msg):
    print(f"[ERROR] {msg}")
    sys.exit(1)


def info(msg):
    print(f"[INFO] {msg}")


class Cloudflare:
    url = ''
    headers = {}

    def __init__(self, token):
        if token is None:
            error("Api token is required")

        self.url = "https://api.cloudflare.com"
        self.headers["Content-Type"] = "application/json"
        self.headers["Authorization"] = f"Bearer {token}"

    def __del__(self):
        self.headers = None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--api', type=str, help="set api key")
    args = parser.parse_args()

    cloudflare = Cloudflare(args.api)
