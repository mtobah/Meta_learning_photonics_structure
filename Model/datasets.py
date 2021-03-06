import pandas as pd
import numpy as np
import pickle as pkl
from sklearn.preprocessing import StandardScaler

import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader

class SiliconColor(Dataset):
    
    def __init__(self, filepath, split='train', inverse=False):
        super(SiliconColor).__init__()
        self.data = pkl.load(open(filepath, 'rb')).to_numpy()

        x = self.data[:,:4]
        y = self.data[:,4:]
        if inverse:
            x, y = y, x
        self.data = np.hstack((x, y))
        
        self.scaler = StandardScaler()
        self.scaler.fit(self.data[:7000])
        
        if split is 'train':
            self.data = self.data[:7000]
        elif split is 'val':
            self.data = self.data[7000:8000]
        else:
            self.data = self.data[8000:]
            
        self.data = self.scaler.transform(self.data)
        self.data = torch.tensor(self.data).float()
        if inverse:
            self.x, self.y = self.data[:, :3], self.data[:, 3:]
        else:
            self.x, self.y = self.data[:, :4], self.data[:, 4:]
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]


def get_dataloaders(model):
    datapath = 'data\data_rcwa.pkl'
    if model in ['forward_model', 'vae', 'inn']:
        train_dt = SiliconColor(datapath, 'train')
        val_dt = SiliconColor(datapath, 'val')
        test_dt = SiliconColor(datapath, 'test')

    else:
        train_dt = SiliconColor(datapath, 'train', inverse = True)
        val_dt = SiliconColor(datapath, 'val', inverse = True)
        test_dt = SiliconColor(datapath, 'test', inverse = True)
        
    train_loader = DataLoader(train_dt, batch_size=128, shuffle=True)
    val_loader = DataLoader(val_dt, batch_size=128, shuffle=False)
    test_loader = DataLoader(test_dt, batch_size=128, shuffle=False)

    return train_loader, val_loader, test_loader

    

