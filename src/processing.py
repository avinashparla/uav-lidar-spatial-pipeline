import polars as pl

def filter_ground_points(df):
    """
    Filters the point cloud to isolate ground returns. 
    In a production environment, this would involve Cloth Simulation Filters (CSF) 
    or Simple Morphological Filter (SMRF).
    """
    # High-performance filtering using Polars
    # Specifically targeting Class 2 (Ground) based on standard LAS classification
    ground_df = df.filter(pl.col("classification") == 2)
    
    # Statistical outlier removal to handle 'low noise' points
    z_mean = ground_df["z"].mean()
    z_std = ground_df["z"].std()
    
    return ground_df.filter((pl.col("z") > z_mean - 3 * z_std) & 
                            (pl.col("z") < z_mean + 3 * z_std))
