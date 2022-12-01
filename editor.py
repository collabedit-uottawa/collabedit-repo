from moviepy.editor import *

def trim(clip, start, end):
    return clip.subclip(start, end)

def extractAudio(clip):
    clip.audio.write_audiofile(trimFName + ".mp3")

def resize(clip, size):
    return clip.resize(height=size)

def save(clip):
    newName = trimFName + "_new.mp4"
    clip.write_videofile(newName)

def changeAudio(clip, audio):
    clip.audio = audio
    return clip

fname = "files/video.mp4"
audioName = "files/audio.mp3"
trimFName = fname[0:-4]
clip = VideoFileClip(fname)
audio = AudioFileClip(audioName)

# clip = changeAudio(clip, audio)
# clip = trim(clip, 0, 5)
clip = resize(clip, 144)
save(clip)

# extractAudio(size)
