from torch.utils.data import DataLoader

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

train_features, train_label = next(iter(train_dataloader))
print(f"Feature batch shape: {train_features.size()}")
print(f"Labels bath shape: {train_labels.size()}")
img = train_features[0].squeeze()
label = train_labels[0]
plt.imgshow(img, cmap="gray")
plt.show()
print(f"Label: {label}")

# Feature batch shape: torch.Size([64, 1, 28, 28])
# Labels batch shape: torch.Size([64])
# Label: 5