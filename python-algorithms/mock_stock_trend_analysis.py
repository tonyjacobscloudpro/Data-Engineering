# Features and Functionality
# Mock Dataset Creation:
# Simulates realistic stock price behavior with an upward trend, sinusoidal fluctuations, and random noise.
# Peak and Valley Detection:
# Uses scipy.signal.find_peaks to identify key turning points.
# Visualization:
# Plots stock prices with annotations for peaks and valleys to make trends visible.
# Trend Analysis:
# Provides insights such as the number of peaks and valleys, average prices at peaks and valleys, and extrema.

# numpy, matplotlib, and scipy must also be installed.
# python
# pip install numpy pandas matplotlib

# stock_price_trends.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# 1. Generate Mock Stock Price Dataset
# - This section creates a synthetic dataset to simulate stock price trends.
# - The dataset includes an upward trend with added sinusoidal oscillations and random noise.
print("1. Generating Mock Stock Price Dataset")

def generate_mock_stock_data(days=100, base_price=100, noise_level=2):
    """
    Generates mock stock price data.
    :param days: Number of days for the stock prices.
    :param base_price: Initial stock price.
    :param noise_level: Amount of random noise to add.
    :return: Array of mock stock prices.
    """
    x = np.linspace(0, 4 * np.pi, days)  # Create x-axis values for oscillations.
    trend = np.linspace(base_price, base_price + 20, days)  # Upward trend over days.
    seasonal = 5 * np.sin(x)  # Oscillations to simulate market fluctuations.
    noise = np.random.normal(0, noise_level, days)  # Random noise.
    stock_prices = trend + seasonal + noise
    return stock_prices

days = 100
mock_stock_prices = generate_mock_stock_data(days)
print("Mock Stock Prices:", mock_stock_prices)

# 2. Identify Peaks and Valleys
# - Peaks are local maxima where stock prices rise and then fall.
# - Valleys are local minima where stock prices fall and then rise.
print("\n2. Identifying Peaks and Valleys")

def find_peaks_and_valleys(prices):
    """
    Identifies peaks and valleys in stock prices.
    :param prices: Array of stock prices.
    :return: Indices of peaks and valleys.
    """
    peaks, _ = find_peaks(prices)  # Find peaks using SciPy.
    valleys, _ = find_peaks(-prices)  # Find valleys by inverting the prices.
    return peaks, valleys

peaks, valleys = find_peaks_and_valleys(mock_stock_prices)
print("Peaks at indices:", peaks)
print("Valleys at indices:", valleys)

# 3. Visualize Stock Price Trends
# - Plot the stock prices and annotate the peaks and valleys.
print("\n3. Visualizing Stock Price Trends")

def plot_stock_trends(prices, peaks, valleys):
    """
    Plots stock prices with annotated peaks and valleys.
    :param prices: Array of stock prices.
    :param peaks: Indices of peaks.
    :param valleys: Indices of valleys.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(prices, label="Stock Prices", linewidth=2)
    plt.scatter(peaks, prices[peaks], color='red', label="Peaks", marker='o')
    plt.scatter(valleys, prices[valleys], color='green', label="Valleys", marker='x')
    plt.title("Stock Price Trends with Peaks and Valleys")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_stock_trends(mock_stock_prices, peaks, valleys)

# 4. Analyze Trends
# - This section calculates simple statistics about peaks and valleys to help identify trends.
print("\n4. Analyzing Stock Price Trends")

def analyze_trends(prices, peaks, valleys):
    """
    Analyzes stock price trends based on peaks and valleys.
    :param prices: Array of stock prices.
    :param peaks: Indices of peaks.
    :param valleys: Indices of valleys.
    :return: Analysis summary as a dictionary.
    """
    peak_prices = prices[peaks]
    valley_prices = prices[valleys]
    trend_analysis = {
        "Number of Peaks": len(peaks),
        "Number of Valleys": len(valleys),
        "Average Peak Price": np.mean(peak_prices) if len(peak_prices) > 0 else None,
        "Average Valley Price": np.mean(valley_prices) if len(valley_prices) > 0 else None,
        "Largest Peak": np.max(peak_prices) if len(peak_prices) > 0 else None,
        "Deepest Valley": np.min(valley_prices) if len(valley_prices) > 0 else None,
    }
    return trend_analysis

trend_analysis = analyze_trends(mock_stock_prices, peaks, valleys)
for key, value in trend_analysis.items():
    print(f"{key}: {value}")

# End of script
print("\nStock price trend analysis completed successfully!")
