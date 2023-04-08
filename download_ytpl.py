import os
from pytube import Playlist, YouTube

url = input("Enter your YouTube playlist link: ")
folder_name = input("Enter the folder name to store your videos: ")
current_path = os.path.abspath(os.getcwd())
videos_stored_in = current_path + '\\' + folder_name
count = 1

print("Generating playlist...")
p = Playlist(url)
count_video = len(p.videos)
print(f"Playlist \'{p.title}\' has {count_video} videos. Downloading to \'{videos_stored_in}\'.")
for video in p.videos:  
    print(f"\t{count}) Downloading video {count}/{count_video}...")
    video.streams.filter(file_extension='mp4').get_highest_resolution().download(videos_stored_in)
    print("\t\tDownload finished. ")
    count += 1
    
print(f"Finished downloading {len(p.video_urls)} videos.")