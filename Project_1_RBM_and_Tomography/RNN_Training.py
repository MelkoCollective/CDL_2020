import sys
import torch
from torch import nn
from torch.autograd import Variable
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
%matplotlib inline

# Added code to run on google colab
IN_COLAB = 'google.colab' in sys.modules
if IN_COLAB:
    ! git clone https: // github.com/olgOk/CohortProject_2020.git
    from google.colab import drive
    drive.mount('/content/gdrive')
    %cd CohortProject_2020/
    %cd Project_1_RBM_and_Tomography/
    ! git pull

torch.manual_seed(1)

# Hyper Parameters
EPOCH = 1               # train the training data n times, to save time, we just train 1 epoch
BATCH_SIZE = 1
TIME_STEP = 1          # rnn time step / image height
INPUT_SIZE = 100         # rnn input size / image width
LR = 0.01               # learning rate

# Load data
training_data = torch.from_numpy(np.loadtxt("Rydberg_data.txt")).float()
train_loader = torch.utils.data.DataLoader(dataset=training_data,
                                           batch_size=BATCH_SIZE, shuffle=True)
# RNN Model using LSTM


class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()

        self.rnn = nn.LSTM(         # if use nn.RNN(), it hardly learns
            input_size=INPUT_SIZE,
            hidden_size=64,         # rnn hidden unit
            num_layers=1,           # number of rnn layer
            # input & output will has batch size as 1s dimension. e.g. (batch, time_step, input_size)
            batch_first=True,
        )

        self.out = nn.Linear(64, 10)

    def forward(self, x):
        # x shape (batch, time_step, input_size)
        # r_out shape (batch, time_step, output_size)
        # h_n shape (n_layers, batch, hidden_size)
        # h_c shape (n_layers, batch, hidden_size)
        # None represents zero initial hidden state
        r_out, (h_n, h_c) = self.rnn(x, None)

        # choose r_out at the last time step
        out = self.out(r_out[:, -1, :])
        return out


rnn = RNN()
print(rnn)


def SimpleLoss(rnn_output, label):
    return rnn_output + label


# optimize all cnn parameters
optimizer = torch.optim.Adam(rnn.parameters(), lr=LR)
# Change to CrossEntropy for improved results
loss_func = SimpleLoss
exact_energy = -4.1203519096

# training and testing
for epoch in range(EPOCH):
    it = iter(train_loader)
    iter_count = 0
    while iter_count < 1000:
        first = next(it)
        X = first.view(-1, *first.size())
        # reshape x to (batch, time_step, input_size)
        b_first = Variable(first.view(1, 1, 100))
        # rnn sampling output
        RNN_samples = rnn(b_first)
        iter_count = iter_count + 1
        outp = float(RNN_samples[0][0])
        sampled_energy = SimpleLoss(outp, exact_energy)
        if iter_count % 100 == 0:
            print("\nIteration: ", iter_count)
            print("Sampling...")                # cross entropy loss
            print('Energy from RNN sample: ' + str(sampled_energy))
        # clear gradients for this training step
        optimizer.zero_grad()
        # Gradient descent to be improved with cross entropy loss function and backpropagation
