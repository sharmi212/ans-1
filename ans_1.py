# -*- coding: utf-8 -*-
"""ans 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1noag2V-fK0EhwjrxWBwqtO_6XMhSbPKJ
"""

from google.colab import files
uploaded = files.upload()

import numpy as np
import matplotlib.pyplot as plt

# Load the data from the uploaded file
data = np.loadtxt('Data_1.txt')

# Initialize lists to store indices of maxima and minima
maxima = []
minima = []

# Iterate through the dataset
for i in range(1, len(data) - 1):
    if data[i - 1] < data[i] > data[i + 1]:
        maxima.append(i)
    if data[i - 1] > data[i] < data[i + 1]:
        minima.append(i)

# Plot the signal
plt.plot(data, label='Signal')

# Plot maxima points
plt.scatter(maxima, data[maxima], color='red', label='Maxima')

# Plot minima points
plt.scatter(minima, data[minima], color='blue', label='Minima')

plt.title('Signal with Maxima and Minima')
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Print the indices of maxima and minima
print("Maxima indices:", maxima)
print("Minima indices:", minima)

from google.colab import files
uploaded = files.upload()

import numpy as np
import matplotlib.pyplot as plt

# Load the data from the uploaded file
data = np.loadtxt('Data_2.txt')

# Initialize lists to store indices of maxima and minima
maxima = []
minima = []

# Iterate through the dataset
for i in range(1, len(data) - 1):
    if data[i - 1] < data[i] > data[i + 1]:
        maxima.append(i)
    if data[i - 1] > data[i] < data[i + 1]:
        minima.append(i)

# Plot the signal
plt.plot(data, label='Signal')

# Plot maxima points
plt.scatter(maxima, data[maxima], color='red', label='Maxima')

# Plot minima points
plt.scatter(minima, data[minima], color='blue', label='Minima')

plt.title('Signal with Maxima and Minima')
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Print the indices of maxima and minima
print("Maxima indices:", maxima)
print("Minima indices:", minima)