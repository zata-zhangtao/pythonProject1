import torch
learing = 0.001

x = torch.rand([500,1])
y = x*3+0.8

w= torch.rand([1,1],requires_grad=True)
b = torch.tensor(0,dtype=torch.float32,requires_grad=True)

for i in range(2000):
    predict_y = torch.matmul(x,w)+b
    loss = (predict_y - y).pow(2).mean()
    if w.grad is not None:
        w.gard.data.zero_()

    loss.backward()
