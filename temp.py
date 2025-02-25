import sounddevice as sd
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Constants
SAMPLERATE = 44100  # Standard audio sample rate
DURATION = 3  # Record 3 seconds of system audio
CHANNELS = 2  # Stereo input

def callback(indata, frames, time, status):
    """Process real-time audio data."""
    if status:
        print(status)
    # Convert stereo to mono
    mono_audio = np.mean(indata, axis=1)

    # Compute short-time Fourier transform (STFT)
    onset_env = librosa.onset.onset_strength(y=mono_audio, sr=SAMPLERATE)

    # Detect peaks (beats)
    peaks, _ = find_peaks(onset_env, height=np.mean(onset_env) * 1.5)  

    # Plot detected beats
    plt.figure(figsize=(10, 4))
    plt.plot(onset_env, label="Onset Strength")
    plt.scatter(peaks, onset_env[peaks], color='r', label="Beats")
    plt.legend()
    plt.title("Beat Detection from System Audio")
    plt.xlabel("Time")
    plt.ylabel("Strength")
    plt.show()

# Start capturing system audio
with sd.InputStream(callback=callback, channels=CHANNELS, samplerate=SAMPLERATE):
    print("Listening... Press Ctrl+C to stop.")
    sd.sleep(DURATION * 1000)  # Capture for a few seconds
