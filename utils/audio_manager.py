import simpleaudio as sa
import threading
import os

class AudioManager:
    def __init__(self, beep_path: str, chime_path: str):
        """
        Initialize AudioManager with paths to beep and chime audio files.
        Supports .wav audio files.
        """
        self.beep_path = os.path.abspath(beep_path)
        self.chime_path = os.path.abspath(chime_path)
        self._lock = threading.Lock()
        self._current_play = None
        self._last_form_state = None
        
        # Verify audio files exist
        if not os.path.exists(self.beep_path):
            print(f"[AudioManager] Warning: Beep file not found at {self.beep_path}")
        if not os.path.exists(self.chime_path):
            print(f"[AudioManager] Warning: Chime file not found at {self.chime_path}")

    def _play_sound(self, path):
        """Play a WAV audio file"""
        try:
            if not os.path.exists(path):
                print(f"[AudioManager] Error: Audio file not found at {path}")
                return
                
            with self._lock:
                # Stop any currently playing sound
                if self._current_play and self._current_play.is_playing():
                    self._current_play.stop()

                # Load and play WAV audio file asynchronously
                wave_obj = sa.WaveObject.from_wave_file(path)
                self._current_play = wave_obj.play()
        except Exception as e:
            print(f"[AudioManager] Error playing sound from {path}: {e}")

    def play_beep(self, form_state):
        """Play beep once when incorrect form is detected."""
        if form_state == "Wrong" and self._last_form_state != "Wrong":
            self._play_sound(self.beep_path)
            self._last_form_state = "Wrong"

    def play_chime(self, form_state):
        """Play chime once when form becomes correct again."""
        if form_state == "Correct" and self._last_form_state != "Correct":
            self._play_sound(self.chime_path)
            self._last_form_state = "Correct"

    def reset(self):
        """Reset internal state when resetting repetitions."""
        with self._lock:
            if self._current_play and self._current_play.is_playing():
                self._current_play.stop()
            self._last_form_state = None