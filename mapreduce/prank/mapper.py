#!/usr/bin/python3

import sys
import os
import glob
from bs4 import BeautifulSoup as bs
# sys.stdin.reconfigure(encoding='utf-8')

# a[0].encode('latin-1').decode('utf-8')

seen_urls = {}

for line in sys.stdin:
    try:
        # print("Lineasds: ", line, len(line),
        #       line[300:312] if len(line) >= 312 else '')
        filename, line = line.split(':', 1)
        line.encode('latin-1').decode('utf-8')

        # filename = os.environ['mapreduce_map_input_file']
        doc = bs(line, 'html.parser')
        outlinks = doc.find_all('a')
        currentUrl = filename.split("/", 2)[-1]

        currentUrlRank = f"{currentUrl}|1"
        if currentUrlRank not in seen_urls:
            seen_urls[currentUrlRank] = set()
        for link in outlinks:
            url = link.get('href')
            if url is not None and url[0] == 'h' and url not in seen_urls[currentUrlRank]:
                print(f"{currentUrlRank}\t{url}")
                seen_urls[currentUrlRank].add(url)

        # print("Line: ", filename.split, line)
        # print("Links", list([el.get('href') for el in outlinks]))
        # print('---------------------------------------')
    except UnicodeEncodeError as e:
        # print(e)
        # print('***************************************')
        pass
    # anyo, mes, temp = line.split("\t", 2)
    # print("%s\t%s" % (anyo, temp))
