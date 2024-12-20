import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks


class FFTAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.data = None
        self.freq = None
        self.asd = None
        self.positive_freq = None
        self.positive_asd = None

    def load_data(self):  # Load the data from the specified file path
        try:
            self.data = pd.read_csv(
                self.file_path, sep="\t", comment=";", header=None,
                names=["Time(s)", "polarized_x_a", "polarized_y_a", "polarized_x_b", "polarized_y_b"]
            )
            print("Data successfully loaded.")
        except Exception as e:
            print(f"Error loading the file: {e}")
            exit()

    def perform_fft(self, signal_column):  # Perform FFT on the specified signal column
        time = self.data["Time(s)"].values  # Extract time data
        signal = self.data[signal_column].values  # Extract signal data
        dt = time[1] - time[0]  # Calculate time step
        N = len(signal)  # Number of samples

        self.freq = fftfreq(N, dt)  # Generate frequency array
        fft_signal = fft(signal)  # Perform FFT
        psd = np.abs(fft_signal)**2 / N  # Power Spectral Density
        self.asd = np.sqrt(psd)  # Amplitude Spectral Density

        # Keep only positive frequencies
        self.positive_freq = self.freq[:N//2]
        self.positive_asd = self.asd[:N//2]

    def detect_peaks(self, min_amplitude=0.01, prominence=0.005, width=None):  # Detect peaks in ASD
        peaks, properties = find_peaks(
            self.positive_asd, height=min_amplitude, prominence=prominence, width=width
        )
        peak_frequencies = self.positive_freq[peaks]
        peak_amplitudes = self.positive_asd[peaks]

        # Print detected peaks
        print("\nDetected Peaks:")
        if len(peaks) > 0:
            for i, (freq, amp) in enumerate(zip(peak_frequencies, peak_amplitudes)):
                print(f"Peak {i+1}: Frequency = {freq:.2f} Hz, Amplitude = {amp:.4f}")
        else:
            print("No peaks detected with the current parameters.")

        # Show the plot with current thresholds
        plt.figure(figsize=(10, 6))
        plt.loglog(self.positive_freq, self.positive_asd, label='ASD')
        if len(peaks) > 0:
            plt.scatter(peak_frequencies, peak_amplitudes, color='red', label='Peaks')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude Spectral Density (m/√Hz)')
        plt.title(f'FFT Plot with Peaks of {self.file_name}')
        plt.legend()
        plt.grid(True)
        plt.show()

        # Ask the user to adjust thresholds or accept results once
        user_input = input(
            "\nAdjust thresholds? Type 'reset' to adjust or 'no' to accept: "
        ).strip().lower()
        if user_input == 'reset':
            try:
                min_amplitude = float(input("Enter new minimum amplitude (e.g., 0.01): "))
                prominence = float(input("Enter new prominence threshold (e.g., 0.005): "))
                width = input("Enter new minimum width (e.g., 1) or leave blank: ")
                width = None if width.strip() == "" else float(width)
                # Re-run peak detection with new thresholds
                return self.detect_peaks(min_amplitude, prominence, width)
            except ValueError:
                print("Invalid input. Retaining current thresholds.")
        elif user_input == 'no':
            print("Thresholds accepted.")
        else:
            print("Invalid input. Thresholds retained.")

        return peak_frequencies, peak_amplitudes

    def plot_asd(self, save_path=None, peaks=None):  # Plot the ASD and optionally mark peaks
        plt.figure(figsize=(10, 6))
        plt.loglog(self.positive_freq, self.positive_asd, label='ASD')

        if peaks:  # Mark peaks if provided
            peak_frequencies, peak_amplitudes = peaks
            plt.scatter(peak_frequencies, peak_amplitudes, color='red', label='Peaks')

        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude Spectral Density (m/√Hz)')
        plt.title(f'FFT Plot of {self.file_name}')
        plt.legend()
        plt.grid(True)

        if save_path:  # Save the plot if a path is provided
            plt.savefig(save_path)
        plt.show()


def main():
    # Step 1: Ask the user for the file path
    file_path = input("Enter the path to your data file: ")

    # Initialize FFTAnalyzer
    analyzer = FFTAnalyzer(file_path)

    # Step 2: Load the data
    analyzer.load_data()

    # Step 3: Perform FFT on 'polarized_x_a'
    analyzer.perform_fft(signal_column="polarized_x_a")

    # Step 4: Detect peaks focusing on tall amplitudes
    peaks = analyzer.detect_peaks(min_amplitude=0.05, prominence=0.01)

    # Step 5: Plot ASD with peaks
    analyzer.plot_asd(save_path=f"FFT_Plot_with_Peaks_{analyzer.file_name}.png", peaks=peaks)


if __name__ == "__main__":
    main()
