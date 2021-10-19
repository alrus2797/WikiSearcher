#!/usr/bin/python3

import sys
import os
import glob
from bs4 import BeautifulSoup as bs
import re
# sys.stdin.reconfigure(encoding='utf-8')

# a[0].encode('latin-1').decode('utf-8')

seen_urls = {}

token_sep = "( |,|\\.|-|_|;)"


def replace(text):
    chars = " []()$#?!¿¡%+.=,;<>-_{}"
    for c in chars:
        if c in text:
            text = text.replace(c, '')
    return text


for line in sys.stdin:
    try:
        # print("Lineasds: ", line, len(line),
        #       line[300:312] if len(line) >= 312 else '')
        filename, line = line.split(':', 1)
        line.encode('latin-1').decode('utf-8')

        # filename = os.environ['mapreduce_map_input_file']
        doc = bs(line, 'html.parser')
        currentUrl = filename.split("/", 2)[-1]
        text = doc.getText().strip()
        # print("efore: ", text)
        text = re.split(token_sep, text, flags=re.UNICODE)
        # print("efore: ", text)
        for word in text:
            # word = re.sub(
            #     r'(\"|\'|\\[|\\]|\\(|\\)|\\$|#|\\?|!|\\*|¿|¡|%|\\+)', '', word)
            word = replace(word)
            if word is not None and len(word):
                print(f"{word}\t{currentUrl}")

        # print("Line: ", filename.split, line)
        # print("Links", list([el.get('href') for el in outlinks]))
        # print('---------------------------------------')
    except UnicodeEncodeError as e:
        # print(e)
        # print('***************************************')
        pass
    # anyo, mes, temp = line.split("\t", 2)
    # print("%s\t%s" % (anyo, temp))
