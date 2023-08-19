import pandas as pd
import numpy as np

def preprocess_traffic_data(data_path):
    # Load traffic data from CSV or other sources
    traffic_data = pd.read_csv(data_path)
    
    # Perform data preprocessing
    
    # Convert datetime strings to datetime objects
    traffic_data['timestamp'] = pd.to_datetime(traffic_data['timestamp'])
    
    # Fill missing values (if any)
    traffic_data.fillna(method='ffill', inplace=True)
    
    # Calculate traffic density based on vehicle count and road length
    traffic_data['density'] = traffic_data['vehicle_count'] / traffic_data['road_length']
    
    # Normalize numerical features (e.g., density)
    traffic_data['density'] = (traffic_data['density'] - traffic_data['density'].min()) / (traffic_data['density'].max() - traffic_data['density'].min())
    
    # Map categorical variables to numerical values
    weather_mapping = {'sunny': 0, 'rainy': 1, 'cloudy': 2}
    traffic_data['weather_condition'] = traffic_data['weather_condition'].map(weather_mapping)
    
    day_of_week_mapping = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    traffic_data['day_of_week'] = traffic_data['day_of_week'].map(day_of_week_mapping)
    
    # Drop unnecessary columns
    traffic_data.drop(['timestamp', 'vehicle_count', 'road_length'], axis=1, inplace=True)
    
    return traffic_data

def generate_input_features(traffic_data):
    # Convert processed data into input features for AI models
    input_features = traffic_data[['density', 'weather_condition', 'day_of_week']]
    
    return input_features

if __name__ == "__main__":
    data_path = "traffic_data.csv"  # Path to your traffic data file
    processed_data = preprocess_traffic_data(data_path)
    input_features = generate_input_features(processed_data)
    
    # Save processed data and input features
    processed_data.to_csv("processed_data.csv", index=False)
    input_features.to_csv("input_features.csv", index=False)
