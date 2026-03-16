import numpy as np
from skimage import measure

# We can't easily instantiate ObjectWidget without a viewer,
# but we can test the logic it uses.


def test_segmentation_logic_float():
    # Simulate (C, Y, X) probability map
    data = np.zeros((3, 32, 32), dtype=float)
    # Background (class 0) is max everywhere except one patch
    data[0, ...] = 0.8
    # Class 1 patch
    data[1, 5:15, 5:15] = 0.9
    # Class 2 patch
    data[2, 20:25, 20:25] = 0.9

    # Logic from ObjectWidget.segment_objects
    argmax_axis = 1 if data.ndim == 4 else 0
    class_map = np.argmax(data, axis=argmax_axis)
    foreground = class_map > 0

    labels = measure.label(foreground)

    assert labels.max() == 2  # Two distinct patches
    assert np.any(labels[5:15, 5:15] > 0)
    assert np.any(labels[20:25, 20:25] > 0)


def test_segmentation_logic_int():
    # Simulate (Y, X) binary mask
    data = np.zeros((32, 32), dtype=int)
    data[5:15, 5:15] = 1
    data[20:25, 20:25] = 1

    # Logic from ObjectWidget.segment_objects
    foreground = data > 0
    labels = measure.label(foreground)

    assert labels.max() == 2
