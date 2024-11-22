import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matpotlib.pyplot as pyplot

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data"
    train=False,
    download=True,
    transform=ToTensor()
)

# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz
# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz to data/FashionMNIST/raw/train-images-idx3-ubyte.gz

#   0%|          | 0.00/26.4M [00:00<?, ?B/s]
#   0%|          | 65.5k/26.4M [00:00<01:12, 363kB/s]
#   1%|          | 229k/26.4M [00:00<00:38, 682kB/s]
#   4%|3         | 950k/26.4M [00:00<00:11, 2.19MB/s]
#  14%|#4        | 3.77M/26.4M [00:00<00:03, 7.47MB/s]
#  37%|###7      | 9.90M/26.4M [00:00<00:00, 17.0MB/s]
#  61%|######    | 16.0M/26.4M [00:01<00:00, 22.7MB/s]
#  83%|########2 | 21.9M/26.4M [00:01<00:00, 26.0MB/s]
# 100%|##########| 26.4M/26.4M [00:01<00:00, 19.4MB/s]
# Extracting data/FashionMNIST/raw/train-images-idx3-ubyte.gz to data/FashionMNIST/raw

# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz
# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz to data/FashionMNIST/raw/train-labels-idx1-ubyte.gz

#   0%|          | 0.00/29.5k [00:00<?, ?B/s]
# 100%|##########| 29.5k/29.5k [00:00<00:00, 328kB/s]
# Extracting data/FashionMNIST/raw/train-labels-idx1-ubyte.gz to data/FashionMNIST/raw

# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz
# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz to data/FashionMNIST/raw/t10k-images-idx3-ubyte.gz

#   0%|          | 0.00/4.42M [00:00<?, ?B/s]
#   1%|1         | 65.5k/4.42M [00:00<00:12, 361kB/s]
#   5%|5         | 229k/4.42M [00:00<00:06, 679kB/s]
#  21%|##        | 918k/4.42M [00:00<00:01, 2.10MB/s]
#  83%|########2 | 3.67M/4.42M [00:00<00:00, 7.24MB/s]
# 100%|##########| 4.42M/4.42M [00:00<00:00, 6.06MB/s]
# Extracting data/FashionMNIST/raw/t10k-images-idx3-ubyte.gz to data/FashionMNIST/raw

# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz
# Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz to data/FashionMNIST/raw/t10k-labels-idx1-ubyte.gz

#   0%|          | 0.00/5.15k [00:00<?, ?B/s]
# 100%|##########| 5.15k/5.15k [00:00<00:00, 33.8MB/s]
# Extracting data/FashionMNIST/raw/t10k-labels-idx1-ubyte.gz to data/FashionMNIST/raw

# batch_size = 64

# train_dataloader = DataLoader(training_data, bath_size=batch_size)
# test_dataloader = DataLoader(test_data, batch_size=batch_size)

# for X, y in test_dataloader:
#     print(f"Shape of X [N, C, H, W]: {X.shape}")
#     print(f"Shape of y: {y.shape} {y.dtype}")
#     break

# # Shape of X [N, C, H, W]: torch.Size([64, 1, 28, 28])
# # Shape of y: torch.Size([64]) torch.int64




labels_map= {
    0: "T-shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Book",
}
figure = plt.figure(figsize=(8,8))
cols, rows = 3,3
for i in range(1, cols * rows +1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()

