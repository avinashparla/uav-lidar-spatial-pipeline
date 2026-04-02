import laspy
import polars as pl
import numpy as np

def load_lidar_data(file_path):
    """
    Load .laz or .las files using laspy and convert to a Polars DataFrame 
    for high-speed memory-efficient processing.
    """
    with laspy.open(file_path) as fh:
        las = fh.read()
        
    # Extract coordinates as a dictionary for Polars ingestion
    data = {
        "x": np.array(las.x),
        "y": np.array(las.y),
        "z": np.array(las.z),
        "intensity": np.array(las.intensity),
        "classification": np.array(las.classification)
    }
    
    return pl.DataFrame(data)

if __name__ == "__main__":
    # Example usage for 19M point cloud
    print("Initializing LiDAR ingestion engine...")
