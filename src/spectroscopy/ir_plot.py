import matplotlib.pyplot as plt
import numpy as np

INTENSITY_MAP = {"weak": 0.3,
                 "medium": 0.6, 
                 "strong": 1.0}

SHAPE_MAP = {"sharp": 10,
             "broad": 50,
             "very broad": 100}

def get_band_center(range_string):
    """
    Convert example:
    '1705-1725 cm-1
    -> 1715
    """

    low, high = map(int, range_string.replace(" cm-1", "").split("-"))

    return(low + high) / 2

def generate_ir_spectrum(bands):

    x = np.linspace(400, 4000, 5000)

    spectrum = np.zeros_like(x)

    labels = []

    for band in bands:

        center = get_band_center(band["range"])

        amplitude = INTENSITY_MAP[band["intensity"]]

        width = SHAPE_MAP[band["shape"]]

        peak = amplitude * np.exp(-(x - center) **2 / (2 * width **2))

        spectrum += peak

        labels.append({"band": band["band"], "center": center})

    return x, spectrum, labels

def plot_ir_spectrum(x, spectrum, labels, title):
    # normalize

    spectrum = spectrum / spectrum.max()

    # convert to transmittance

    transmittance = 100 - (spectrum * 60)
    
    plt.figure(figsize=(12, 6))

    plt.plot(x, transmittance, color="black", linewidth=1.5)

    plt.gca().invert_xaxis()

    plt.ylim(0, 100)

    for i, label in enumerate(labels):

        idx = np.argmin(np.abs(x - label["center"]))

        peak_y = transmittance[idx]

        y_pos = 10 + (i % 4) * 8

        plt.annotate(label["band"],
                     xy=(label["center"], peak_y),
                     xytext=(label["center"], y_pos),
                     fontsize=8, 
                     ha="center",
                     arrowprops={"arrowstyle":"-", "lw":0.5})

    plt.xlabel("Wavenumber (cm⁻¹)")
    plt.ylabel("% Transmittance")

    plt.title(title)

    plt.grid(True)

    plt.tight_layout()

    plt.show()