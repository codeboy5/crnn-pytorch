import torch
from torch.utils.data import DataLoader
from torch.nn import CTCLoss
from tqdm import tqdm

from config import evaluate_config as config

torch.backends.cudnn.enabled = False

from dataset import UPTIDataset, upti_collate_fn

eval_batch_size = config['eval_batch_size']
cpu_workers = config['cpu_workers']
reload_checkpoint = config['reload_checkpoint']

img_height = config['img_height']
img_width = config['img_width']

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'device: {device}')

test_dataset = UPTIDataset(root_dir='data/UPTI', mode='test', img_height=img_height, img_width=img_width)

test_loader = DataLoader(
    dataset=test_dataset,
    batch_size=eval_batch_size,
    shuffle=False,
    num_workers=cpu_workers,
    collate_fn=upti_collate_fn)

num_classes = len(UPTIDataset.LABEL2CHAR) + 1

print(len(test_dataset))

print(num_classes)

    # test_loader = DataLoader(
    #     dataset=test_dataset,
    #     batch_size=eval_batch_size,
    #     shuffle=False,
    #     num_workers=cpu_workers,
    #     collate_fn=synth90k_collate_fn)
    # num_class = len(Synth90kDataset.LABEL2CHAR) + 1