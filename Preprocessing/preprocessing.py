import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def preprocessing(csv_file_path):
    data = pd.read_csv(csv_file_path)
    data.columns = ["EC_number", "Species", "Compound", "Compound_name", "Amino_encoding", "Kcat", "unit"]
    data = pd.DataFrame(data)
    return data
