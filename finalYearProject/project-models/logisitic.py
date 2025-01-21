# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:16:57 2025

@author: bigir
"""

import pandas as pd
import numpy as np
import sklearn as sk


heart_data = pd.read_csv('./heart_cleveland_upload.csv')
print(heart_data.head(4))