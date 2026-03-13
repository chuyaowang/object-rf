# Gemini Context: object-rf

## Project Overview
`object-rf` is a napari plugin for object-level classification using Random Forest. It bridges pixel-level segmentation and high-level object analysis by extracting morphological and intensity features from segmented objects and training classifiers to categorize them.

### Main Technologies
- **Python**: Core language.
- **napari**: Multi-dimensional image viewer and plugin framework.
- **scikit-image**: Used for segmentation (thresholding), labeling (`measure.label`), and feature extraction (`measure.regionprops`).
- **scikit-learn**: Provides the `RandomForestClassifier` for object-level classification.
- **Qt/qtpy**: GUI framework.
- **joblib**: Model serialization.

### Key Architecture
- **`ObjectWidget` (`src/object_rf/_widget.py`)**: (Planned) The main GUI for controlling thresholding, feature extraction, and training.
- **Feature Extraction**: Leverages `regionprops_table` to generate a tabular representation of objects for machine learning.
- **Workflow**:
    1.  Convert Probability maps (from `napari-rf`) into Labels.
    2.  Compute geometrical (area, perimeter) and intensity (mean, max) features.
    3.  User-guided training (annotating specific labels with classes).
    4.  Full-stack object classification.

---

## Development Workflow & Preferences

### Git and Source Control
- **Branching**: Use descriptive feature branches (e.g., `feature/object-extraction`).
- **Commit Logic**: Commit logically grouped changes.
- **Commit Message Style**: **Comprehensive and detailed**. Include a summary and a bulleted list of technical improvements.

### Documentation and Wiki
- **"Code Wiki" Preference**: Maintain a technical "code wiki" in `docs/wiki/`.
- **Comprehensiveness**: Integrate new features into the existing context without deleting existing documentation.
- **Technical Detail**: Specify data shapes, feature lists, and architectural flows.

---

## Building and Running

### Development Setup
```bash
pip install -e .
pip install -e ".[testing]"
```

### Running and Testing
- Launch: `napari`
- Tests: `pytest`
- Tox: `tox`

---

## Technical Conventions

### Data Integration
- **Upstream Compatibility**: Designed to ingest probability layers produced by `napari-rf`.
- **Feature Robustness**: Handle multi-dimensional images (2D/3D stacks) during feature extraction.
- **State Management**: Persist feature tables associated with label layers to avoid redundant computations.
