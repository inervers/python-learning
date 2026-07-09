import time
import numpy as np

# 1. 纯Python：生成100万个数的平方
data_py = list(range(1_000_000))

start = time.time()
result_py = [x ** 2 for x in data_py]
end = time.time()
print(f"纯Python耗时：{end - start:.4f}秒")

# 2. NumPy：生成100万个数的平方
data_np = np.arange(1, 1_000_001)

start = time.time()
result_np = data_np ** 2
end = time.time()
print(f"NumPy耗时：{end - start:.4f}秒")

# 3. 矩阵乘法（NumPy核心优势）
a = np.random.rand(500, 500)
b = np.random.rand(500, 500)

start = time.time()
c = a @ b  # 矩阵乘法
end = time.time()
print(f"NumPy 500x500矩阵乘法耗时：{end - start:.4f}秒")

# 4. 统计运算
data = np.random.randn(10_000)  # 10000个正态分布随机数
print(f"\n均值：{data.mean():.4f}")
print(f"标准差：{data.std():.4f}")
print(f"最小值：{data.min():.4f}")
print(f"最大值：{data.max():.4f}")
print(f"中位数：{np.median(data):.4f}")
