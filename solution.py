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
        videos.append((v_id, R_n))

    videos = sorted(videos, key=lambda r: r[1], reverse=True)

    cached = []
    for video in videos:
        v_id = video[0]

        if X >= S[v_id]:
            cached.append(v_id)
            X = X - S[v_id]

    return cached

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
