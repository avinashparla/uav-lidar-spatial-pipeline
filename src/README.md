# Source Code
This directory contains the core Python scripts for the LiDAR processing engine.

* **ingestion.py**: Handles high-performance loading of `.laz` files using `laspy` and `polars`.
* **processing.py**: Contains algorithms for noise removal and ground/non-ground point classification.
* **modeling.py**: Implements `scipy.interpolate` for the generation of high-resolution DEM, DSM, and CHM grids.
* **validation.py**: Script for spatial co-registration and calculating the Mean Vertical Error (MVE) against baseline datasets.
