import numpy as np

def calculate_mve(generated_dem, baseline_dem):
    """
    Calculates the Mean Vertical Error (MVE) between the generated model 
    and the OpenTopography baseline.
    """
    # Calculate the pixel-wise difference (DEM of Difference)
    dod = generated_dem - baseline_dem
    
    # Compute metrics
    mve = np.nanmean(np.abs(dod))
    rmse = np.sqrt(np.nanmean(dod**2))
    
    print(f"Validation Complete: MVE = {mve:.3f} meters")
    return mve, rmse
