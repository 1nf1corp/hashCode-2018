import sys
import parse

def accumulate(all_reqs):
    ret = {}
    for (vid,ep), val in all_reqs.items():
        if vid in ret:
            ret[vid] = ret[vid] + val
        else:
            ret[vid] = val
    return ret

def findOptimalVideos(X, S, requests):
    videos = []
    for v_id, R_n in requests.items():
        videos.append((S[v_id], R_n, v_id))

    return pack5(videos, X)

# Borrowed from 0-1 knapsack problem dynamic program
# David Eppstein, ICS, UCI, 2/22/2002
# https://www.ics.uci.edu/~eppstein/161/python/knapsack.py
def itemSize(item): return item[0]
def itemValue(item): return item[1]
def itemName(item): return item[2]
def pack5(items,sizeLimit):
    P = {}
    for nItems in range(len(items)+1):
        print(nItems)
        for lim in range(sizeLimit+1):
            if nItems == 0:
                P[nItems,lim] = 0
            elif itemSize(items[nItems-1]) > lim:
                P[nItems,lim] = P[nItems-1,lim]
            else:
                P[nItems,lim] = max(P[nItems-1,lim],
                    P[nItems-1,lim-itemSize(items[nItems-1])] +
                    itemValue(items[nItems-1]))

    L = []
    nItems = len(items)
    lim = sizeLimit
    while nItems > 0:
        if P[nItems,lim] == P[nItems-1,lim]:
            nItems -= 1
        else:
            nItems -= 1
            L.append(itemName(items[nItems]))
            lim -= itemSize(items[nItems])

    L.reverse()
    return L

if __name__ == '__main__':
    filename = sys.argv[1]
    input = parse.parse(filename)
    endpoints = input[0]
    requests = input[1]
    params = input[2]

    accumulated_requests = accumulate(requests)
    videosToCache = findOptimalVideos(params['X'], params['S'], accumulated_requests)

    print(params['C'])
    string = " ".join(map(str, videosToCache))
    for c in range(params['C']):
        print(str(c), string)
