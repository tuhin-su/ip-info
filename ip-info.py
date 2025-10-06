#!/bin/env python3

import requests
from rich import print
from sys import argv

API_URL="http://ip-api.com/json/"

def main():
    ip = ''
    if len(argv) > 1:
        ip = argv[1]
    try:
        rsp = requests.get(f'{API_URL}{ip}')
        print(rsp.json())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()