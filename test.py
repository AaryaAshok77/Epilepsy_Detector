from glob import glob

# Specify the directory containing the files
directory = '/Users/aaryaashokk/Documents/Coding/Projects/DataSets/'

# Use glob to find all files ending with .edf and not .edf.seizure
edf_files = glob(directory + '*.edf')
edf_files = [file for file in edf_files if not file.endswith('.seizure.edf')]

print(edf_files)

import torch
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

print(f"PyTorch version: {torch.__version__}")

# Check PyTorch has access to MPS (Metal Performance Shader, Apple's GPU architecture)
print(f"Is MPS (Metal Performance Shader) built? {torch.backends.mps.is_built()}")
print(f"Is MPS available? {torch.backends.mps.is_available()}")

# Set the device      
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")