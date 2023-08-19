from data_processing import preprocess_traffic_data, generate_input_features
from simulation import simulate_traffic, visualize_traffic
from train_model import train_neural_network
from visualize import visualize_results

if __name__ == "__main__":
    # Data Processing
    data_path = "traffic_data.csv"  # Replace with your data path
    processed_data = preprocess_traffic_data(data_path)
    input_features = generate_input_features(processed_data)
    
    # Simulation
    intersections = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    time_steps = 10
    simulate_traffic(intersections, time_steps)
    
    # Train Model
    model = train_neural_network(input_features, processed_data)
    
    # Visualization
    visualize_traffic(processed_data)  # Visualization from data processing
    visualize_results()  # Visualization of simulation or model results
