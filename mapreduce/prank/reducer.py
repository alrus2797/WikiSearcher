#!/usr/bin/python3

import sys
import os

current_url = None
current_outs = ""

for claveValor in sys.stdin:
    url, out_link = claveValor.rstrip().split("\t", 1)

    if current_url == url:
        current_outs += out_link + '|'
    else:
        if current_url:
            print(f"{current_url}\t{current_outs[:-1]}")
        current_outs = out_link
        current_url = url

if current_url == url:
    print(f"{current_url}\t{current_outs[:-1]}")
