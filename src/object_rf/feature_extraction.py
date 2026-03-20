import pandas as pd
from skimage.measure import regionprops


class FeatureExtractor:
    def __init__(self):
        pass

    def generate_features(self, label_image, intensity_image=None):
        """
        Generator that yields progress (current, total, description)
        and finally yields a pandas DataFrame of features.

        Parameters
        ----------
        label_image : ndarray
            The segmented object labels (2D or 3D).
        intensity_image : ndarray, optional
            The raw intensity image for feature calculation.
        """
        props = regionprops(label_image, intensity_image=intensity_image)
        total_objects = len(props)

        if total_objects == 0:
            yield (0, 0, 'No objects found')
            return pd.DataFrame()

        all_features = []

        for i, prop in enumerate(props):
            # Report progress
            yield (
                i + 1,
                total_objects,
                f'Extracting features for object {prop.label}...',
            )

            # Feature dictionary for this object
            feat = {
                'label': prop.label,
                # Add more features here in the future
            }

            # Placeholder for exact feature creation logic
            # (To be implemented)

            all_features.append(feat)

        yield pd.DataFrame(all_features)
