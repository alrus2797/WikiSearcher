import random
from typing import no_type_check

alphabet = [chr(i) for i in range(65, 91)]


def genWord(length=5):
    return ''.join(random.choice(alphabet) for i in range(length))


def generateUids(n=1000, uid_length=5):
    uids = []
    while len(uids) < n:
        word = genWord(uid_length)
        if word not in uids:
            uids.append(word)
        else:
            print("Duplicate: ", word)
    return uids


def generateRelationFiles(uids, wfile, maxOuts=20, ocurrences=1):
    n_uids = int(len(uids) * ocurrences)
    for uid in uids[n_uids:]:
        n_out = random.randint(1, maxOuts)
        print(uid, end=",", file=wfile)
        curr_out = random.sample(uids, n_out)
        print(','.join(curr_out), file=wfile)


def checkUnique(uids):
    buc = set()
    for uid in uids:
        if uid not in buc:
            buc.add(uid)
        else:
            return False
    return True


wfile = open('prtest.txt', 'w')

uids = generateUids(n=2000, uid_length=4)
print(checkUnique(uids))
generateRelationFiles(uids, wfile, ocurrences=0.5)
