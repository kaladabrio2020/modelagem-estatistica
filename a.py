print("hello world")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
data

print(data)

# Define your model architecture (e.g., simple linear regression)
class SimpleLinearRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(SimpleLinearRegression, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)

# Instantiate the model and optimizer
model = SimpleLinearRegression(input_dim=10, output_dim=1)  # Example input dimension 10, output dimension 1
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent with learning rate 0.01

# Define your loss function and training loop (example using mean squared error)
criterion = nn.MSELoss()  
for epoch in range(100):  # Train for 100 epochs
    # ... Your training logic here, including forward pass, backward pass, and optimization step ...

    # Calculate loss and update weights
    loss = criterion(model(x_train), y_train)
    optimizer.zero_grad()  # Clear gradients before calculating the next loss
    loss.backward()  # Backpropagation to calculate gradients
    optimizer.step()  # Update model parameters based on calculated gradients

# Evaluate your model (example using mean squared error)
with torch.no_grad():  # Disable gradient calculation for evaluation
    y_pred = model(x_test) 
    loss = criterion(y_pred, y_test)
    print('Loss:', loss.item())