import numpy as np
from scipy.interpolate import griddata

def generate_surface_model(df, resolution=0.5, method='linear'):
    """
    Interpolates sparse point cloud data into a continuous 3D grid.
    """
    points = df.select(["x", "y"]).to_numpy()
    values = df.select("z").to_numpy().flatten()

    # Define the grid extent
    grid_x, grid_y = np.mgrid[
        points[:,0].min():points[:,0].max():resolution,
        points[:,1].min():points[:,1].max():resolution
    ]

    # Perform the interpolation
    # Linear method maintains topographical integrity better than Nearest
    grid_z = griddata(points, values, (grid_x, grid_y), method=method)
    
    return grid_x, grid_y, grid_z
