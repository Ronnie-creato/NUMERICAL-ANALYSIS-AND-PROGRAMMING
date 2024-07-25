import numpy as np
import matplotlib.pyplot as plt

def compute_fft(f1, f2, sampling_rate, duration):
    # Time array
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Signal
    s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    
    # Compute FFT
    fft_values = np.fft.fft(s)
    
    # Frequency array
    freqs = np.fft.fftfreq(len(t), 1 / sampling_rate)
    
    # Plot the signal
    plt.figure(figsize=(14, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(t, s)
    plt.title('Time Domain Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    
    # Plot the FFT magnitude
    plt.subplot(2, 1, 2)
    plt.stem(freqs[:len(freqs) // 2], np.abs(fft_values)[:len(freqs) // 2], use_line_collection=True)
    plt.title('Frequency Domain Signal')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    
    plt.tight_layout()
    plt.show()

# Parameters
f1 = 50  # Hz
f2 = 120  # Hz
sampling_rate = 1000  # Hz
duration = 1  # second

# Compute and plot FFT
compute_fft(f1, f2, sampling_rate, duration)
