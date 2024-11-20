introto tensor

- scalar = torch.tensor(7)
- ```

```
scaler = torch.tensor(7)

# Number of dimensions
scalar = no dimensions
scalar.item()

# vectory
vector = torch.tensor([7,7,])
# magnitude and direction
vector.ndim 
vector.shape

# matrix
MATRIX = torch.tensor([[7,8], [9,10]])
MATRIX.ndim # 2
MATRIX.shape # [2,2]

# tensor
TENSOR = torch.tensor ([[
						[1,2,3],
						[4,5,6],
						[7,8,9]
						]])
TENSOR
TENSOR.ndim
--------------------------------
# random tensors

# start with random numbers and then update from data
random_tensor = torch.rand(3,4)

random_image_size_tensor = torch.rand(size(224,224,3))


```

## creating tensors with zeros one in pytorch

```
### zeros and ones

zero = torch.zeros(size=(3,4))
zeros
ones = torch.ones(size=(3,4))


ones.dtype
```

## Creating a tensor range and tensors like other tensors

```
### range of tensors

one_to_ten = torch.arange(start=0,end=10, step=77)
one_to_ten

### Creating tensors like
ten_zeros = torch.zeros_like(input=one_to_ten)
ten_zeros


```

## dealing with tensor data types

```
### float 32 tensor

float_32_tensor = torch.tensor([3.0,6.0,9.0],
								dtype=torch.float32,
								device=none,
								requires_grad=False])
### more or less precision
```

## Getting tensor attributes

tensor.shape
tensor.device
tensor.dtype

## MAnipulating Tensors

- addition 
- subtraction
- multiplication
- division
- matrix multiplication

```
tensor + 10

```

## matrix multiplication

two ways

Element-wise multiplication
matrix-wise (dot product)

torch.matmul



------
# reshaping
view shares the same memory