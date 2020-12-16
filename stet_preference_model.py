from valve_keyvalues_python.keyvalues import KeyValues
import glob
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import copy

import torch
import torchvision

from zplib import zp4

font_name = fm.FontProperties(fname="C:\\Windows\\Fonts\\malgun.ttf").get_name()
matplotlib.rc('font', family=font_name)

pdDataList = []
stetList = ["power", "speed", "armor"]

x_data = []
y_data = []

w = torch.tensor([0.0, 0.0, 0.0], requires_grad = True)
def forward(x):
    return x * w[0], x * w[1], x * w[2]

def loss(x,y):
    y_pred = forward(x)
    return torch.abs(y_pred[0] - y[0]) + torch.abs(y_pred[1] - y[1]) + torch.abs(y_pred[2] - y[2])

for kv in zp4.get_players_keyvalues():
    dataList = []
    if not ("stet" in kv):
        continue

    x_data.append(int(kv["level"]))
    stetData = []
    for keyName in stetList:
        try:
            stetData.append(int(kv["stet"][keyName]))
        except:
            stetData.append(0)
    y_data.append(stetData)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# Training loop
print("predict (before training)" , 4, forward(80))
for epoch in range(100):
    for x_val, y_val in zip(x_data, y_data): #1
        l = loss(x_val, y_val) #2
        l.backward() #3
        w.data = w.data - 0.01 * w.grad.data #4
        # Manually zero the gradients after updating weights
        w.grad.data.zero_() #5

    #print("progress:", epoch, l.data[0])
print("predict (after training)" , 4, forward(80))