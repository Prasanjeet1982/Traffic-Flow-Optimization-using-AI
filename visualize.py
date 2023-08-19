import numpy as np
import matplotlib.pyplot as plt

# Simulated or actual data for visualization
time_steps = np.arange(10)  # Replace with your actual time steps
congestion_levels = np.random.rand(10)  # Replace with your actual congestion level data

def visualize_results(time_steps, congestion_levels):
    plt.figure(figsize=(10, 6))
    plt.plot(time_steps, congestion_levels, marker='o')
    plt.xlabel("Time Steps")
    plt.ylabel("Congestion Level")
    plt.title("Traffic Flow Optimization Results")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    visualize_results(time_steps, congestion_levels)
