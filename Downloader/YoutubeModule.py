from pytube import YouTube as yt


def get_video(url):
    video = yt(url).streams
    resolutions = []

    for i in range(len(video)):
        if video[i].resolution is None:
            pass
        elif video[i].resolution in resolutions:
            pass
        else:
            resolutions.append(video[i].resolution)

    return print(resolutions)
