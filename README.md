# UAV LiDAR Spatial Pipeline
An automated Python-driven engine for processing massive 3D point clouds into survey-grade surface models.

## **Project Overview**
This project demonstrates a scalable, programmatic approach to standardizing UAV LiDAR data. By bypassing the constraints of commercial GUI software, this pipeline ingests over 19 million points to generate high-resolution Digital Elevation Models (DEM), Digital Surface Models (DSM), and Canopy Height Models (CHM). 

The pipeline includes a custom validation module that co-registers generated surfaces against baseline standards, achieving a Mean Vertical Error (MVE) of 0.129m.

## **Technical Pedigree**
The architecture of this system is informed by a unique dual-background:
* **Engineering Foundation:** Years of research in Water Resources Engineering (IIT Bombay) and Remote Sensing/GIS (University of British Columbia) specializing in geodetic mass balance and high-altitude mountain hydrology.
* **Algorithmic Rigor:** Experience in quantitative system architecture and algorithmic modeling, focusing on memory-efficient processing of high-throughput time-series and spatial datasets.

## **Core Features**
* **High-Performance Ingestion:** Utilizes `laspy` and `polars` for memory-efficient loading and filtering of heavy `.laz` point clouds.
* **Surface Generation:** Implementation of `scipy.interpolate` (Linear and Nearest-Neighbor) for robust 3D grid generation.
* **Automated Validation:** Scripted co-registration against OpenTopography standards to calculate precise vertical accuracy and generate a "DEM of Difference" (DoD).
* **Modular Design:** Decoupled modules for ingestion, classification, modeling, and QA/QC.

## **Tech Stack**
* **Language:** Python
* **Computational Libraries:** NumPy, SciPy, Polars, Pandas
* **Spatial Libraries:** Laspy, Rasterio, Geopandas, Open3D
* **Visualization:** Matplotlib

## **Repository Structure**
* `/src`: Modular Python scripts for the processing engine.
* `/notebooks`: Interactive Jupyter Notebooks for visualization and accuracy reporting.
* `/docs`: Technical background on the geodetic methods and spatial math used.

## **How to Use**
1. Install dependencies: `pip install -r requirements.txt`
2. Configure data paths in `src/ingestion.py`.
3. Run the pipeline: `python src/main.py`
