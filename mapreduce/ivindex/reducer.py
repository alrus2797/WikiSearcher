#!/usr/bin/python3

import sys
import os

current_word = None
current_url = None
current_value = None

url_count = {}

for claveValor in sys.stdin:
    word, url = claveValor.rstrip().split("\t", 1)
    print("-", claveValor[:-1])

    if current_word == word:
        print('\tMore ', current_url, url, url_count)
        if current_url == url:
            url_count += 1
        else:
            print('\tOther URL')
            current_value += f"{url}|{url_count}" + '|'
            current_url = url
            url_count = 1
    else:
        if current_word:
            print(f"{current_word}\t{current_value[:-1]}")
        current_url = url
        current_word = word
        url_count = 1
        current_value = f"{current_url}|1\n"

if current_word == word:
    print(f"{current_word}\t{current_value[:-1]}")
