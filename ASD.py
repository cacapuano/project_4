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

    def load_data(self):
        """Loads data from the given file."""
        try:
            self.data = pd.read_csv(
                self.file_path, sep="\t", comment=";", header=None,
                names=["Time(s)", "polarized_x_a", "polarized_y_a", "polarized_x_b", "polarized_y_b"]
            )
            print("Data successfully loaded.")
        except Exception as e:
            print(f"Error loading the file: {e}")
            exit()

    def perform_fft(self, signal_column):
        """Performs FFT on the specified signal column."""
        time = self.data["Time(s)"].values
        signal = self.data[signal_column].values
        dt = time[1] - time[0]  # Time step
        N = len(signal)

        self.freq = fftfreq(N, dt)  # Frequency array
        fft_signal = fft(signal)  # Perform FFT

        psd = np.abs(fft_signal)**2 / N  # Power Spectral Density
        self.asd = np.sqrt(psd)  # Amplitude Spectral Density

        # Keep only positive frequencies
        self.positive_freq = self.freq[:N//2]
        self.positive_asd = self.asd[:N//2]

    def detect_peaks(self, min_amplitude=0.01, prominence=0.005, width=None):
        """
        Detects peaks in the ASD with a focus on tall amplitudes.
        
        Parameters:
        - min_amplitude: Minimum amplitude for peaks.
        - prominence: Minimum prominence to distinguish peaks from noise.
        - width: Minimum width of peaks.
        """
        while True:
            # Find peaks with constraints on amplitude, prominence, and width
            peaks, properties = find_peaks(
                self.positive_asd, height=min_amplitude, prominence=prominence, width=width
            )
            peak_frequencies = self.positive_freq[peaks]
            peak_amplitudes = self.positive_asd[peaks]

            # Print detected peaks with tall amplitudes
            print("\nDetected Peaks with Tall Amplitudes:")
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

            # Prompt the user to adjust thresholds or accept the results
            user_input = input(
                "\nAdjust thresholds? (y/n) or type 'reset' to enter new values: "
            ).strip().lower()
            if user_input == 'y':
                continue
            elif user_input == 'reset':
                try:
                    min_amplitude = float(input("Enter new minimum amplitude (e.g., 0.01): "))
                    prominence = float(input("Enter new prominence threshold (e.g., 0.005): "))
                    width = float(input("Enter new minimum width (e.g., 1) or leave blank: ") or "None")
                    width = None if width == "None" else float(width)
                except ValueError:
                    print("Invalid input. Retaining current thresholds.")
            elif user_input == 'n':
                break
            else:
                print("Invalid input. Exiting threshold adjustment.")
                break

        return peak_frequencies, peak_amplitudes

    def plot_asd(self, save_path=None, peaks=None):
        """Plots the ASD and optionally marks the peaks."""
        plt.figure(figsize=(10, 6))
        plt.loglog(self.positive_freq, self.positive_asd, label='ASD')

        # Mark peaks if provided
        if peaks:
            peak_frequencies, peak_amplitudes = peaks
            plt.scatter(peak_frequencies, peak_amplitudes, color='red', label='Peaks')

        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude Spectral Density (m/√Hz)')
        plt.title(f'FFT Plot of {self.file_name}')
        plt.legend()
        plt.grid(True)

        if save_path:
            plt.savefig(save_path)
        plt.show()


# Main function
def main():
    # Step 1: Ask the user for the file path
    file_path = input("Enter the path to your data file (e.g., /path/to/data.lvm): ")

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
