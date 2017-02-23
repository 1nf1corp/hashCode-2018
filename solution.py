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

    videos = sorted(videos, key=lambda r: r[1])

    cached = []
    for video in videos:
        v_id = video[0]

        if X >= S[v_id]:
            cached.append(v_id)
            X = X - S[v_id]

    return cached

if __name__ == '__main__':
    input = parse.parse('kittens.in')
    endpoints = input[0]
    requests = input[1]
    params = input[2]

    accumulated_requests = accumulate(requests)
    videosToCache = findOptimalVideos(params.X, params.S, accumulated_requests)

    print(videosToCache)

X = 10000
S = [1000, 5500, 6300, 2500]

test = {
    (0,4): 1500,
    (1,1): 100,
    (1,4): 1000,
    (1,3): 1000,
    (1,9): 1000,
    (3,4): 2000
}

requests = accumulate(test)
videos = findOptimalVideos(X, S, requests)

print(videos)