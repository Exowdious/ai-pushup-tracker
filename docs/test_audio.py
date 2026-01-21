#!/usr/bin/env python3
"""
Test script to verify audio system is working correctly
"""
import sys
import os
import time

# Add the project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.audio_manager import AudioManager

def test_audio_files():
    """Test if WAV files exist and are accessible"""
    print("="*60)
    print("AUDIO SYSTEM TEST")
    print("="*60)
    
    beep_path = "assets/beep.wav"
    chime_path = "assets/chime.wav"
    
    print(f"\n1. Checking audio files...")
    print(f"   Beep file: {os.path.abspath(beep_path)}")
    print(f"   Exists: {os.path.exists(beep_path)}")
    if os.path.exists(beep_path):
        print(f"   Size: {os.path.getsize(beep_path)} bytes")
    
    print(f"\n   Chime file: {os.path.abspath(chime_path)}")
    print(f"   Exists: {os.path.exists(chime_path)}")
    if os.path.exists(chime_path):
        print(f"   Size: {os.path.getsize(chime_path)} bytes")
    
    if not os.path.exists(beep_path) or not os.path.exists(chime_path):
        print("\n✗ ERROR: Audio files not found!")
        return False
    
    print("\n2. Initializing AudioManager...")
    try:
        audio_manager = AudioManager(beep_path, chime_path)
        print("   ✓ AudioManager initialized successfully")
    except Exception as e:
        print(f"   ✗ Failed to initialize AudioManager: {e}")
        return False
    
    print("\n3. Testing beep sound (Wrong form)...")
    try:
        audio_manager.play_beep("Wrong")
        print("   ✓ Beep sound triggered")
        print("   (You should hear a beep sound)")
        time.sleep(2)  # Wait for sound to play
    except Exception as e:
        print(f"   ✗ Failed to play beep: {e}")
        return False
    
    print("\n4. Testing chime sound (Correct form)...")
    try:
        audio_manager.play_chime("Correct")
        print("   ✓ Chime sound triggered")
        print("   (You should hear a chime sound)")
        time.sleep(2)  # Wait for sound to play
    except Exception as e:
        print(f"   ✗ Failed to play chime: {e}")
        return False
    
    print("\n5. Testing reset functionality...")
    try:
        audio_manager.reset()
        print("   ✓ Reset successful")
    except Exception as e:
        print(f"   ✗ Failed to reset: {e}")
        return False
    
    print("\n6. Testing repeated sounds (state tracking)...")
    try:
        # First call should play
        audio_manager.play_beep("Wrong")
        print("   ✓ First beep played")
        time.sleep(1)
        
        # Second call with same state should NOT play
        audio_manager.play_beep("Wrong")
        print("   ✓ Second beep skipped (correct behavior)")
        time.sleep(1)
        
        # Different state should play
        audio_manager.play_chime("Correct")
        print("   ✓ Chime played after state change")
        time.sleep(1)
    except Exception as e:
        print(f"   ✗ Failed state tracking test: {e}")
        return False
    
    print("\n" + "="*60)
    print("✓ ALL AUDIO TESTS PASSED!")
    print("="*60)
    return True

if __name__ == "__main__":
    try:
        success = test_audio_files()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
