import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import pathlib

data_dir = tf.keras.utils.get_file(origin=dataset_url,
                                   fname='flower_photos',
                                   untar=True)
data_dir = pathlib.Path(data_dir)
