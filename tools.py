def videos_endpoint(endpoint, requests):
    videos = []
    for (video, endp), reqs in requests.items():
        if endpoint == endp:
            videos.append((reqs, video))
    return videos

#def top_videos_endpoints(endpoints, requests):
#    reqs_per_video = {}
#    for e in endpoints:
#        videos = videos_endpoint(e, requests)
#        for reqs, video in videos:
#            if video in reqs_per_video:
#                reqs_per_video[video] += reqs
#            else:
#                reqs_per_video[video] = reqs
#    
#    top_videos = []
#    for video, reqs in reqs_per_video.items():
#        top_videos.append((reqs, video))
#    return sorted(top_videos, reverse=True)

def top_videos_endpoints(endpoints, requests):
    reqs_per_video = {}
    for (video, _), reqs in requests.items():
        if video in reqs_per_video:
            reqs_per_video[video] += reqs
        else:
            reqs_per_video[video] = reqs
    
    top_videos = []
    for video, reqs in reqs_per_video.items():
        top_videos.append((reqs, video))
    return sorted(top_videos, reverse=True)
