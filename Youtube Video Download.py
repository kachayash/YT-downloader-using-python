
from pytube import YouTube
from pytube import Playlist
def video(link ,path):
    yt_1 = YouTube(link)
    print('wait....')
    vid = yt_1.streams.filter(only_video=True)
    v = list(enumerate(vid))
    for i in v:
        print(i)
    print()
    str = int(input("Enter Your Index:- "))
    vid[str].download(path)
    print("Successfully Download.....")

def Music(link , path):
    yt_1 = YouTube(link)
    print('wait....')
    vid = yt_1.streams.filter(only_audio=True)
    v = list(enumerate(vid))
    for i in v:
        print(i)
    print()
    str = int(input("Enter Your Index:- "))
    vid[str].download(path)
    print("Successfully Download.....")

def playlist(link , path):
    py = Playlist(link)
    print(f'Playlist name: {py.title}')

    for video in py.videos:
        print('wait....')
        video.streams.get_highest_resolution().download(path)
        print("Successfully: ",video.title)

    print("All video download:- ")



def menu():
    print('-------------------------')
    print('-----YT Downloader-------')
    print('-------------------------')
    print()
    print('You can download👇')
    print('1. Video')
    print('2. Audio')
    print('3. Playlist')
    print('4. Exit')
    print()

menu()
print('Select a step....')
select = int(input('Enter your step:- '))
while True:
    if select == 1:
        path = input("Enter location for download video:- ")
        link = input("Enter your video link:- ")
        video(link ,path)
        break
    elif select == 2:
        path = input("Enter location for download video:- ")
        link = input("Enter your video link:- ")
        Music(link , path)
        break
    elif select == 3:
        path = input("Enter location for download video:- ")
        link = input("Enter your playlist link:- ")
        playlist(link, path)
        break
    elif select == 4:
        print("Thank u for using YT Downloader")
        break
    else:
        break