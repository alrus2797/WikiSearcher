all:
	grep -r '' ../pages/es.wikipedia.org/wiki/ | python mapper.py | sort -k1,1 | python reducer.py > initranks.txt

map: 
	grep -r '' ../pages/es.wikipedia.org/wiki/ | python mapper.py