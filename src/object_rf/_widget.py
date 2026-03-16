from typing import TYPE_CHECKING

import numpy as np
from qtpy.QtWidgets import (
    QComboBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from skimage import measure

if TYPE_CHECKING:
    import napari


class ObjectWidget(QWidget):
    def __init__(self, viewer: 'napari.viewer.Viewer'):
        super().__init__()
        self.viewer = viewer

        # State
        self.clf = None  # Future RandomForestClassifier
        self.features_df = None
        self._clf_ready = False

        # --- UI Components ---
        self.setLayout(QVBoxLayout())

        # 1. Probability Layer Selection
        self.layout().addWidget(QLabel('Select Probability Layer:'))
        self.prob_layer_combo = QComboBox()
        self.prob_layer_combo.setToolTip(
            'Select the multi-channel probability layer (e.g., from napari-rf) or a single-channel mask.'
        )
        self.layout().addWidget(self.prob_layer_combo)

        self.btn_segment = QPushButton('Segment Objects')
        self.btn_segment.setToolTip(
            'Generate unique object labels from the selected probability or mask layer.'
        )
        self.btn_segment.clicked.connect(self.segment_objects)
        self.layout().addWidget(self.btn_segment)

        # 3. Feature Extraction
        self.btn_extract = QPushButton('Extract Features')
        self.btn_extract.setToolTip(
            'Calculate geometrical and intensity features for each segmented object.'
        )
        self.btn_extract.clicked.connect(self.extract_features)
        self.btn_extract.setDisabled(True)
        self.layout().addWidget(self.btn_extract)

        # 4. Training & Classification (Placeholders)
        self.btn_train = QPushButton('Train Object Classifier')
        self.btn_train.clicked.connect(self.train_classifier)
        self.btn_train.setDisabled(True)
        self.layout().addWidget(self.btn_train)

        self.btn_predict = QPushButton('Classify Objects')
        self.btn_predict.clicked.connect(self.predict_objects)
        self.btn_predict.setDisabled(True)
        self.layout().addWidget(self.btn_predict)

        # 5. IO
        self.btn_save_model = QPushButton('Save Object Model')
        self.btn_save_model.clicked.connect(self.save_model)
        self.btn_save_model.setDisabled(True)
        self.layout().addWidget(self.btn_save_model)

        self.btn_load_model = QPushButton('Load Object Model')
        self.btn_load_model.clicked.connect(self.load_model)
        self.layout().addWidget(self.btn_load_model)

        # Connect layer events to keep the dropdown updated
        self.viewer.layers.events.inserted.connect(self._update_combo)
        self.viewer.layers.events.removed.connect(self._update_combo)
        self._update_combo()

    def _update_combo(self, event=None):
        """Update the dropdown with available image/labels layers."""
        current_text = self.prob_layer_combo.currentText()
        self.prob_layer_combo.clear()

        # We accept Image layers (probabilities) or Labels layers
        layers = [layer.name for layer in self.viewer.layers]
        self.prob_layer_combo.addItems(layers)

        if current_text in layers:
            self.prob_layer_combo.setCurrentText(current_text)

    def get_selected_layer(self):
        name = self.prob_layer_combo.currentText()
        if name in self.viewer.layers:
            return self.viewer.layers[name]
        return None

    def segment_objects(self):
        """
        Segment objects from the selected layer.
        - If Probabilities (Float): Uses argmax to find the most likely class per pixel
          (axis 1 for 4D, axis 0 for 3D), treats classes > 0 as foreground.
        - If Labels/Mask (Integer): Treats all values > 0 as foreground.
        Finally, assigns unique object IDs to all identified foreground objects.
        """
        layer = self.get_selected_layer()
        if layer is None:
            return

        data = layer.data
        is_float = np.issubdtype(data.dtype, np.floating)

        if is_float:
            # Probability-to-Class logic from napari-rf
            # 2D multi-channel: (C, Y, X) -> axis 0
            # 3D multi-channel: (Z, C, Y, X) -> axis 1
            argmax_axis = 1 if data.ndim == 4 else 0
            class_map = np.argmax(data, axis=argmax_axis)
            foreground = class_map > 0
        else:
            # Already labels or binary mask
            foreground = data > 0

        # Assign unique IDs to discrete objects
        labels = measure.label(foreground)

        new_name = f'{layer.name}_objects'
        if new_name in self.viewer.layers:
            self.viewer.layers[new_name].data = labels
        else:
            self.viewer.add_labels(labels, name=new_name)

        self.btn_extract.setEnabled(True)

    def extract_features(self):
        """Placeholder for feature extraction."""
        print('Extracting features...')
        self.btn_train.setEnabled(True)

    def train_classifier(self):
        """Placeholder for training."""
        print('Training object classifier...')
        self._clf_ready = True
        self.btn_predict.setEnabled(True)
        self.btn_save_model.setEnabled(True)

    def predict_objects(self):
        """Placeholder for prediction."""
        print('Predicting object classes...')

    def save_model(self):
        print('Saving model...')

    def load_model(self):
        print('Loading model...')
