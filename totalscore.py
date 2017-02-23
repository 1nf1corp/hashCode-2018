# Takes: dict of requests
# Returns: list of tuples (video_id, total_requests), sorted by video_id
def accumulate(all_reqs):
    ret = {}
    for (vid,ep), val in all_reqs.items():
        if vid in ret:
            ret[vid] = ret[vid] + val
        else:
            ret[vid] = val
    return ret

test = {
        (0,4): 1500,
        (1,1): 100,
        (1,4): 1000,
        (1,3): 1000,
        (1,9): 1000,
        (3,4): 2000
        }

# print(accumulate(test))

# Input: Dict with
# key: tuple (video_id, endpoint_id)
# value: number_requests
# returns: sorted by video id
# UNUSED FOR NOW
# def sorted_reqs(unsorted):
#     return sorted(unsorted, key=lambda tup : tup[0])
