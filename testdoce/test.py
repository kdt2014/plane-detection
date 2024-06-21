import numpy as np
import scipy.ndimage
from utils import geometry

# mesh_siz = np.array([255, 221])
# mesh_r = (mesh_siz - 1) / 2  # 计算了从中心到边缘的距离
# x_lin = np.linspace(-mesh_r[0], mesh_r[0], mesh_siz[0])
# y_lin = np.linspace(-mesh_r[1], mesh_r[1], mesh_siz[1])  # 均匀分布的 x 和 y 坐标，最大最小值是半径
# xy_coords = np.meshgrid(y_lin, x_lin)  # meshgrid 函数创建了 2D 网格坐标。
#
# # print(xy_coords[1].reshape(-1))
#
# # print(x_lin)
# # print(np.shape(x_lin))
# # print(y_lin)
# print(xy_coords)
# print(np.shape(xy_coords))

image = np.random.randint(0, 256, (161, 255, 221), dtype=np.uint8)  # 0 到 255 的随机整数

num_mesh_points = 56355
# 创建网格数组
mesh = np.zeros((4, num_mesh_points))
# 用随机数填充 x, y, z 坐标
# 假设坐标范围在 -100 到 100 之间
mesh[:3, :] = np.random.uniform(-100, 100, (3, num_mesh_points))
# 设置齐次坐标为 1
mesh[3, :] = 1

mesh_size = np.array([255, 221])
print(mesh_size)


img_siz = np.array(image.shape)
print(img_siz)
img_c = (img_siz - 1) / 2.0
mesh_new = mesh[:3, :] + np.expand_dims(img_c, axis=1)

a = img_c[np.newaxis, :, np.newaxis]

# print(a)

# print(img_c)
#
# print(mesh_new.shape)
# print(np.expand_dims(img_c, axis=1))
