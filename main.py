from gtts import gTTS
from moviepy.editor import *

def generate_story_video(story_text, output="output.mp4"):
    # TTS
    tts = gTTS(text=story_text, lang='hi')
    tts.save("voice.mp3")
    # Video clip
    clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=10)
    audio = AudioFileClip("voice.mp3")
    clip = clip.set_audio(audio)
    clip.write_videofile(output, fps=24)
    print("Video generated:", output)

if __name__ == "__main__":
    story = "Ek andheri raat thi. Ravi ne suna ki koi uske peeche chal raha hai..."
    generate_story_video(story)