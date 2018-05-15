import numpy as np
import nibabel as nib


class NiftiStream:
    def __init__(self):
        self.__images = None

    def load_file(self, filename):
        current_file_data = nib.load(filename).get_data()
        # print(current_file_data.shape)
        if self.__images is None:
            self.__images = current_file_data
        else:
            self.__images.append([current_file_data])

    def get_images(self):
        return self.__images
