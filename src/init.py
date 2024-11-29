# Import necessary libraries
import pandas as pd
import numpy as np
import sys
import os
import pandas as pd

# Use a relative path
file_path = os.path.join(os.path.dirname(__file__), "../data/agriculture_dataset.csv")
data = pd.read_csv(file_path)


# Load the data
#data = pd.read_csv(r"C:\Users\kumar\rosh_corpararate\Machine learning\crop prediction\data\agriculture_dataset.csv")
