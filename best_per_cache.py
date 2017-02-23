import tools

def solve_per_cache(cache, max_cap, S, req_dict):
    eps = endpoints_connected_to_cache(cache)
    # brøds function for getting best videos for a cache
    pq = top_videos_endpoint(eps, req_dict)
    idx = 0
    # As long as we can pick more, do so
    while (idx < len(pq) and S[pq[idx][1]] <= max_cap):
        max_cap = max_cap - S[pq[idx]]
        idx = idx + 1
    solution = pq[:idx]
    new_req_dict = remove_vid_from_eps(solution, eps, req_dict)
    return (solution, new_req_dict)

def remove_vid_from_eps(vids, eps, req_dict):
    for (v, ep) in req_dict.items():
        if v in vids and ep in eps:
            del req_dict[(v,ep)]
    return req_dict
