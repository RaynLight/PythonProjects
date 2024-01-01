import os
import shutil

audio = ( ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
          ".voc", ".wav", )

video = (".webm", ".mov",".mp4")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif")

code = (".c", ".py")

school = (".docx", ".doc" ".txt", ".pptx", ".zip")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_code(file):
    return os.path.splitext(file)[1] in code

def is_school(file):
    return os.path.splitext(file)[1] in school

os.chdir('/Users/DSU Student/Downloads')

for file in os.listdir():
    if is_audio(file):
        shutil.move(file, "/Users/DSU Student/Desktop/audio")
    elif is_video(file):
        shutil.move(file, "/Users/DSU Student/Desktop/video")
    elif is_image(file):
        shutil.move(file, "/Users/DSU Student/Desktop/images")
    elif is_code(file):
        shutil.move(file, "/Users/DSU Student/Desktop/code")
    elif is_school(file):
        shutil.move(file, "/Users/DSU Student/Desktop/school")
    else:
        shutil.move(file, "/Users/DSU Student/Desktop/document")