from pytube import YouTube
import os
import json
from moviepy.editor import *
file = open("example-data.json")


videos = json.load(file)
    
def download(url):
    videoName = f"{YouTube(url).title}.mp4"
    for filename in os.listdir("./videos"):
        if filename == videoName:
            return videoName
    print(f"Downloading {videoName} . . . ")
    videoName = YouTube(url).streams.get_highest_resolution().download('./videos')
    return videoName.split("\\")[-1]

def cut(videoName, clipName, startTime, endTime):
    print(f"Cutting {videoName} . . .")
    clip = VideoFileClip(f"./videos/{videoName}").subclip(startTime, endTime).write_videofile(f"./clips/{clipName}.mp4")



if __name__ == "__main__":
    for video in videos:
        videoPath = download(video["url"])
        cut(videoPath, video["name"], video["startTime"], video["endTime"])
    