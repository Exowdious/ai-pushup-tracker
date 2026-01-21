#!/usr/bin/env python3
"""
Script to convert MP3 audio files to WAV format
"""
from pydub import AudioSegment
import os

def convert_mp3_to_wav(mp3_path, wav_path):
    """Convert MP3 file to WAV format"""
    try:
        print(f"Converting {mp3_path} to {wav_path}...")
        audio = AudioSegment.from_mp3(mp3_path)
        audio.export(wav_path, format="wav")
        print(f"✓ Successfully converted {mp3_path}")
        return True
    except Exception as e:
        print(f"✗ Error converting {mp3_path}: {e}")
        return False

def main():
    assets_dir = "assets"
    
    # Files to convert
    files = [
        ("beep.mp3", "beep.wav"),
        ("chime.mp3", "chime.wav")
    ]
    
    success_count = 0
    for mp3_file, wav_file in files:
        mp3_path = os.path.join(assets_dir, mp3_file)
        wav_path = os.path.join(assets_dir, wav_file)
        
        if os.path.exists(mp3_path):
            if convert_mp3_to_wav(mp3_path, wav_path):
                success_count += 1
        else:
            print(f"✗ File not found: {mp3_path}")
    
    print(f"\n{'='*50}")
    print(f"Conversion complete: {success_count}/{len(files)} files converted")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
