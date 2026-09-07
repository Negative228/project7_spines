import os
from pathlib import Path
import itertools
import shutil

import numpy as np
import tifffile as tf
import cv2 as cv

IMAGE_EXTENSIONS = {'*.jpg', '*.jpeg', '*.png', '*.tiff', '*.tif'}

def get_all_nested_folders(root_directory):
    image_dir = []
    root_path = Path(root_directory)
    
    for file_path in root_path.rglob('*'):
        if file_path.is_dir() and not any(child.is_dir() for child in file_path.iterdir()):
            image_dir.append(str(file_path))
    
    return image_dir

def get_zstack(img_directory):
    img_path = Path(img_directory)
    images = itertools.chain.from_iterable(img_path.glob(ext) for ext in IMAGE_EXTENSIONS)
    
    return np.array([cv.imread(img, cv.IMREAD_GRAYSCALE) for img in images])
    
def copy_file(settings_file, target_folder):
    destination = os.path.join(
        target_folder,
        os.path.basename(settings_file)
    )

    shutil.copy2(settings_file, destination)
    return {'status':'ok'}


def respan_prepare(data_dir: str, target_dir: str, yaml_path: str, suffix='', separate=False):
    folders = get_all_nested_folders(data_dir)
    for folder in folders:
        image = get_zstack(folder)
        if separate:
            dataset_name = suffix + folder.split('\\')[-2]
            image_name = folder.split('\\')[-1] + '.tif'
        else:
            dataset_name = suffix + folder.split('\\')[-3]
            image_name = folder.split('\\')[-2] + '.tif'
        dir_path = os.path.join(target_dir, dataset_name)

        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        tf.imwrite(os.path.join(dir_path, image_name), image.astype(np.uint8))
        copy_file(yaml_path, os.path.join(target_dir, dataset_name))
    return {'status':'ok'}
