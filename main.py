from gtts import gTTS
from moviepy.editor import *

# Step 1: Hindi horror story
story = "Ek andheri raat thi. Ravi ne suna ki koi uske peeche chal raha hai..."

# Step 2: Voiceover
tts = gTTS(text=story, lang='hi')
tts.save("voice.mp3")

# Step 3: (Optional) Combine audio with image
# clip = ImageClip("image.jpg").set_duration(30)
# clip = clip.set_audio(AudioFileClip("voice.mp3"))
# clip.write_videofile("final_video.mp4", fps=24)