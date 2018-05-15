import numpy as np
import nibabel as nib


class NiftiStream:
    def __init__(self):
        self.__images = np.ndarray([0], dtype=np.uint8)

    def load_file(self, filename):
        current_file_data = nib.load(filename)
        # print(current_file_data.shape)
        self.__images = current_file_data

    def get_images(self):
        return self.__images
