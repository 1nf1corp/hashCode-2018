import tools

def endpoints_connected_to_cache(endpoints):
    return {0: [1,3], 1: [0,1]}

def solve_per_cache(max_cap, endpoints, S, req_dict):
    cache_eps = endpoints_connected_to_cache(endpoints)
    all_solutions = {}
    for cache, eps in cache_eps.items():
        # brøds function for getting best videos for a cache
        pq = tools.top_videos_endpoints(eps, req_dict)
        idx = 0
        # As long as we can pick more, do so
        while (idx < len(pq) and S[pq[idx][1]] <= max_cap):
            max_cap = max_cap - S[pq[idx][1]]
            idx = idx + 1
        solution = pq[:idx]
        req_dict = remove_vid_from_eps(solution, eps, req_dict)
        all_solutions[cache] = solution
    return all_solutions

def remove_vid_from_eps(vids, eps, req_dict):
    for (v, ep) in req_dict.items():
        if v in vids and ep in eps:
            del req_dict[(v,ep)]
    return req_dict

# Endpoints connected to cache
def endpointsConnectedToCache(endPoints):
  connectedCaches = {}
  for e in range(len(endPoints)):
  # for idx,endPoint in enumerate(endPoints):
    for cache, cache_lat in endPoints[e][1].items():
      if cache in connectedCaches:
        connectedCaches[cache].append(e)
      else:
        connectedCaches[cache] = [e]

  for key, value in connectedCaches.items() :
    print (key, value)

  return connectedCaches

# req_dict = {(0,2): 1000, (2,3): 1500}
# endpoints = [(4, {0: 1, 1:3}), (10, {}), (3, {0: 2, 1:2}) ]
# print(solve_per_cache(100, endpoints, [30,100,40,50,80], req_dict))
