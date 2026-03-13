# API Reference

This page provides technical details for the primary classes and functions of the `object-rf` plugin.

## `object_rf.ObjectClassifier`
(Planned) Machine learning logic for object-level data.

### `ObjectClassifier(model=None)`
- **`train(features, ground_truth)`**: Fits the classifier to object-level features.
- **`predict(features)`**: Categorizes objects into classes.

---

## `object_rf.features`
(Planned) Feature calculation logic.

### `extract_object_features(label_image, intensity_image=None)`
- Computes morphological and intensity-based features for each label.
- **Input**:
    - `label_image`: (Y, X) or (Z, Y, X) labels layer.
    - `intensity_image` (Optional): Source image for intensity calculations.
- **Output**: Pandas DataFrame.

---

## `object_rf.ObjectWidget`
(Planned) The Qt GUI interface.

### Primary Methods
- `threshold_probabilities()`: Generates a labels layer from a probability map.
- `on_train_clicked()`: Orchestrates feature calculation and model fitting.
- `on_predict_clicked()`: Applies the trained classifier to all objects.
- `save_classifier()` / `load_classifier()`: IO operations for the ML model.
