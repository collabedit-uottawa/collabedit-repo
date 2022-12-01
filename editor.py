from moviepy.editor import *

def trim(clip, start, end):
    return clip.subclip(start, end)

def extractAudio(clip):
    clip.audio.write_audiofile(trimFName + ".mp3")

def resize(clip, size):
    return clip.resize(height=size)

def save(clip):
    clip.write_videofile(trimFName + "_new.mp4")

def changeAudio(clip, audio):
    clip.audio = audio
    return clip

fname = "files/video.mp4"
audioName = "files/audio.mp3"
trimFName = fname[0:-4]
clip = VideoFileClip(fname)
a = AudioFileClip(audioName)

addedAudio = changeAudio(clip, a)

trimmed = trim(addedAudio, 0, 5)

size = resize(trimmed, 360)
save(size)

extractAudio(size)
