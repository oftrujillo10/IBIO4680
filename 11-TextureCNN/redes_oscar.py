import math
import torch.nn as nn
import pdb
class TextureNet(nn.Module):
    def __init__(self):
        super(KtaNet,self).__init__()
        self.op_1 = nn.Conv2d(3, 32, kernel_size=(5,5), padding=(2,2), 
             stride=(2,2),bias=False)
	self.op_2 = nn.ReLU(inplace = True)
	self.op_3 = nn.MaxPool2d(kernel_size=(3,3), padding=(1,1),
             stride=(2,2), dilation=(1,1), ceil_mode = True)
        self.op_4 = nn.Conv2d(32,64, kernel_size=(3,3), padding=(1,1),
             stride=(2,2),bias = False)
        self.op_5 = nn.Conv2d(64,64, kernel_size=(3,3), padding=(1,1),
             stride=(1,1),bias = False)
        self.op_6 = nn.Conv2d(64, 128, kernel_size=(3,3), padding=(1,1),
             stride=(2,2),bias = False)
        self.op_7 = nn.Conv2d(128, 256, kernel_size=(3,3), padding=(1,1),
             stride=(2,2),bias = False)
        self.op_8 = nn.MaxPool2d(kernel_size=(3,3), padding=(1,1),
             stride=(2,2), dilation=(1,1), ceil_mode = True)
        self.op_9 = nn.Linear(256*9,25)
        self.op = nn.Sequential(self.op_1, self.op_2, self.op_3, 
             self.op_4, self.op_5, self.op_6, self.op_7, self.op_8, self.op_9)

    def forward(self,x):
        x = self.op_1(x)
        x = self.op_2(x)
        x = self.op_3(x)
	x = self.op_2(x)
        x = self.op_4(x)
        x = self.op_2(x)
	x = self.op_5(x)
        x = self.op_2(x)
	x = self.op_6(x)
        x = self.op_2(x)
	x = self.op_7(x)
	x = self.op_8(x)
        x = x.view(x.size(0),-1)
        x = self.op_9(x)
        
        return x
