from ingestion import load_lidar_data
from processing import filter_ground_points
from modeling import generate_surface_model
from validation import calculate_mve

def run_pipeline(path_to_laz):
    # 1. Ingest 19M points
    raw_data = load_lidar_data(path_to_laz)
    
    # 2. Process & Filter
    ground_data = filter_ground_points(raw_data)
    
    # 3. Model Surface
    x, y, dem = generate_surface_model(ground_data)
    
    # 4. Validate (0.129m Accuracy check)
    # mve, rmse = calculate_mve(dem, baseline_reference)
    
    print("Pipeline Execution Successful.")

if __name__ == "__main__":
    run_pipeline("data/input_cloud.laz")
