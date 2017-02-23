
# Inputs
# V, E, R, C, X
# S_1, S_2, ..., S_no_videos
# E endpoints:
#   L_D, K
#   K lines (one per cache)
#       C (cache id)
#       L_C (latency from E to K)
# R lines (request descriptions):
#   R_v (video), R_e (endpoint), R_n (#request)

def parse(filename):
    with open(filename, 'r') as f:
        V, E, R, C, X = parse_line(f)
        S = list(map(int, f.readline().split()))
        endpoints = parse_endpoints(f, E)
        requests = parse_requests(f, R)
        params = {"V": V, "E": E, "R": R, "C": C, "X": X, "S": S}
        return endpoints, requests, params

def parse_requests(f_open, R):
    requests = {}
    for r in range(R):
        # for each request description
        vid_id, endp_id, no_reqs = parse_line(f_open)
        requests[(vid_id, endp_id)] = no_reqs
    return requests

def parse_endpoints(f_open, no_endp):
    endpoints = []
    for i in range(no_endp):
        # for each endpoint
        latency, no_caches = parse_line(f_open)
        endpoints.append((latency, {}))
        for j in range(no_caches):
            # for each cache connected to this endpoint
            cache, cache_latency = parse_line(f_open)
            endpoints[-1][1][cache] = cache_latency
    return endpoints

def parse_line(f_open):
    return list(map(int, f_open.readline().split()))

if __name__ == "__main__":
    endpoints, requests, params = parse("kittens.in")
    print("ENDPOINTS: --------")
    print(endpoints[0])
    print("REQUEST: ---------")
    print(requests.popitem())
    print("PARAMS: ----------")
    print(params)
