import pandas as pd
import cv2
import numpy as np

train = pd.read_parquet("C:\\Users\\2925724\\Image Processing and Computer Vision\\Project\\task1_test1.parquet", engine='pyarrow')

#image = train[0]

var = int.from_bytes(train.iloc[0]["image"]["bytes"],"big")

import PIL.Image as Image
import io
import numpy
var = Image.open(io.BytesIO(train.iloc[0]["image"]["bytes"]))
pix = numpy.array(var)

from matplotlib import pyplot as plt
#img1 = val['image'][4].reshape(500,500,3)
# showing image
plt.imshow(pix)
plt.axis('off')
plt.show()

# from competition_toolkit.dataloader import download_dataset
# data_type = "train" # or "validation"
# task = 1 # or 2, but does not matter for train and validation data types
# # paths is a list of dicts, where each dict is a data sample, 
# # and each dict have "image", "lidar", and "mask" keys
# # with the path to the corresponding file
# paths = download_dataset(data_type, task)

# data_sample = paths