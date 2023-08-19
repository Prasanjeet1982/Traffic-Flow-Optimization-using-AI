from fastapi import FastAPI, Query
from data_processing import preprocess_traffic_data, generate_input_features
from simulation import simulate_traffic
from train_model import train_neural_network
from visualize import visualize_results

app = FastAPI()

@app.post("/simulate/")
def run_simulation(intersections: dict, time_steps: int):
    simulate_traffic(intersections, time_steps)
    return {"message": "Simulation completed successfully."}

@app.post("/train/")
def train_model():
    # Simulated input features and processed data
    input_features = generate_input_features(processed_data)
    model = train_neural_network(input_features, processed_data)
    return {"message": "Model training completed successfully."}

@app.get("/visualize/")
def show_visualization():
    visualize_results()  # Replace with your actual visualization function
    return {"message": "Visualization displayed."}
