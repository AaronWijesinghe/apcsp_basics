import os

url = input("Enter YouTube URL: ")
name = input("Enter SFX Name (no .mp3): ")
os.system(f"yt-dlp -x \"{url}\" -ooutput")
os.system("ffmpeg -i output.opus output.mp3")
os.rename("output.mp3", f"{name}.mp3")
if os.path.exists("output.opus"):
    os.remove("output.opus")