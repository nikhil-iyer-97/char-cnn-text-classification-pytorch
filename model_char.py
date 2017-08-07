import torch
import torch.nn as nn
import torch.nn.functional as F

class  CharCNN(nn.Module):
    
    def __init__(self, args):
        super(CharCNN, self).__init__()
        self.args = args
        self.conv1 = nn.Sequential(
            nn.Conv1d(70, 256, kernel_size=7, stride=1),
            nn.Threshold(),
            nn.MaxPool1d(kernel_size=3, stride=3)
        )

        self.conv2 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=7, stride=1),
            nn.Threshold(),
            nn.MaxPool1d(kernel_size=3, stride=3)
        )

        self.conv3 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=3, stride=1),
            nn.Threshold()
        )

        self.conv4 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=3, stride=1),
            nn.Threshold()
        )

        self.conv5 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=3, stride=1),
            nn.Threshold()
        )

        self.conv6 = nn.Sequential(
            nn.Conv1d(256, 256, kernel_size=3, stride=1),
            nn.Threshold(),
            nn.MaxPool1d(kernel_size=3, stride=3)
        )

        
        self.fc1 = nn.Sequential(
            nn.Linear(8704, 1024)
            nn.Threshold(),
            NN.Dropout(P=0.5)
        )
        self.fc2 = nn.Sequential(
            nn.Linear(1024, 1024)
            nn.Threshold(),
            NN.Dropout(P=0.5)
        )
        self.fc3 = nn.Sequential(
            nn.Linear(1024, 4)
            nn.LogSoftmax()
        )

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.conv6(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.fc2(x)
        output = self.fc3(x)

        return output