import os
from pathlib import Path

import hdf5storage
import numpy as np
import scipy.io as sio

def load_mat(mat_path):
    if 'Chikusei' in mat_path:
        hdfile = hdf5storage.loadmat(mat_path)
        mat = hdfile
        if 'GT' in mat:
            mat['GT'] = mat['GT'][0][0][0]
    else:
         mat = sio.loadmat(mat_path)
    
    return mat

def load_dataset(dataset_name,root_path,path_hsi = "",name_hsi = "",path_gt = "",name_gt = ""):
    if dataset_name !="":
        folder_path = Path(root_path,dataset_name)
        if not folder_path.exists():
            raise FileNotFoundError(folder_path)

        file_list = []
        for mat_file in folder_path.glob('*.mat'):
            file_list.append([str(mat_file),os.path.getsize(mat_file)])
            
        file_list.sort(key = lambda x: x[1])
        hsi = load_mat(file_list[-1][0])
        
        for vals in hsi.values():
            if isinstance(vals,np.ndarray):
                hsi = vals
                break
        
        gt = load_mat(file_list[0][0])
        for vals in gt.values():
            if isinstance(vals,np.ndarray):
                gt = vals
                break
    else:
        hsi = load_mat(path_hsi).get(name_hsi)
        gt = load_mat(path_gt).get(name_gt)
    return hsi,gt