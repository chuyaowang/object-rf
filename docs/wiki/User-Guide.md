# User Guide

This guide describes the workflow for using the `object-rf` plugin to perform object-level classification.

## Workflow Overview

### 1. Object Segmentation
The starting point is often a probability map (e.g., from `napari-rf`).
- **Select Probability Layer**: Choose the layer containing pixel-level probabilities.
- **Thresholding**: Apply a threshold to identify regions of interest.
- **Labeling**: Convert the binary mask into a labels layer where each object has a unique ID.

### 2. Feature Extraction
Once objects are identified, the plugin calculates features for each object:
- **Geometry**: Area, perimeter, eccentricity, major/minor axis lengths.
- **Intensity**: Mean, max, min, and median intensity within each label's boundary (calculated from the source image).
- **Texture**: Standard deviation, entropy (optional).

### 3. Annotation & Training
To teach the classifier, you must provide ground truth for some objects.
- **Select Labels**: Click on objects in the viewer and assign them a class label.
- **Train Classifier**: Click **"Train Object Classifier"** to fit a Random Forest model to the extracted features.

### 4. Application
- **Predict**: Apply the trained model to all objects in the current image stack or other datasets.
- **Results**: The labels layer will be colored according to the predicted classes.

## UI Features
- **Object Inspector**: Hover over or select an object to see its ID and associated features in a properties table.
- **Save/Load Classifier**: Export and import your trained object-level models (`.joblib`).
