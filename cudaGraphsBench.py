import torch
from tqdm import tqdm
from torchvision import datasets, transforms

torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction = True
torch.backends.cudnn.allow_tf32 = True
torch.backends.cudnn.benchmark = True
torch.backends.cudnn.enabled = True
torch.backends.cudnn.deterministic = True

model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet101', pretrained=False)
