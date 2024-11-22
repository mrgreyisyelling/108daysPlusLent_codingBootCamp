import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

ds = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)

# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz
# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz to data/FashionMNIST/raw/train-images-idx3-ubyte.gz

#   0%|          | 0.00/26.4M [00:00<?, ?B/s]
#   0%|          | 65.5k/26.4M [00:00<01:12, 364kB/s]
#   1%|          | 197k/26.4M [00:00<00:33, 783kB/s]
#   2%|1         | 492k/26.4M [00:00<00:20, 1.27MB/s]
#   6%|6         | 1.67M/26.4M [00:00<00:05, 4.46MB/s]
#  15%|#4        | 3.83M/26.4M [00:00<00:02, 7.95MB/s]
#  34%|###4      | 9.01M/26.4M [00:00<00:00, 19.4MB/s]
#  49%|####8     | 12.8M/26.4M [00:00<00:00, 21.8MB/s]
#  61%|######    | 16.1M/26.4M [00:01<00:00, 23.5MB/s]
#  81%|########1 | 21.5M/26.4M [00:01<00:00, 31.6MB/s]
#  94%|#########4| 24.9M/26.4M [00:01<00:00, 28.7MB/s]
# 100%|##########| 26.4M/26.4M [00:01<00:00, 19.5MB/s]
# Extracting data/FashionMNIST/raw/train-images-idx3-ubyte.gz to data/FashionMNIST/raw

# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz
# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz to data/FashionMNIST/raw/train-labels-idx1-ubyte.gz

#   0%|          | 0.00/29.5k [00:00<?, ?B/s]
# 100%|##########| 29.5k/29.5k [00:00<00:00, 326kB/s]
# Extracting data/FashionMNIST/raw/train-labels-idx1-ubyte.gz to data/FashionMNIST/raw

# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz
# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz to data/FashionMNIST/raw/t10k-images-idx3-ubyte.gz

#   0%|          | 0.00/4.42M [00:00<?, ?B/s]
#   1%|1         | 65.5k/4.42M [00:00<00:12, 361kB/s]
#   5%|5         | 229k/4.42M [00:00<00:06, 678kB/s]
#  20%|##        | 885k/4.42M [00:00<00:01, 2.52MB/s]
#  44%|####3     | 1.93M/4.42M [00:00<00:00, 4.08MB/s]
# 100%|##########| 4.42M/4.42M [00:00<00:00, 6.06MB/s]
# Extracting data/FashionMNIST/raw/t10k-images-idx3-ubyte.gz to data/FashionMNIST/raw

# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz
# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz to data/FashionMNIST/raw/t10k-labels-idx1-ubyte.gz

#   0%|          | 0.00/5.15k [00:00<?, ?B/s]
# 100%|##########| 5.15k/5.15k [00:00<00:00, 30.9MB/s]
# Extracting data/FashionMNIST/raw/t10k-labels-idx1-ubyte.gz to data/FashionMNIST/raw

