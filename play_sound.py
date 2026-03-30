import os
import subprocess

def main():
    print("Hello from claude0code hook course")
    wav_path = os.path.join(os.path.dirname(__file__), "hi.wav")
    subprocess.run(["afplay", wav_path])

if __name__ == "__main__":
    main()

