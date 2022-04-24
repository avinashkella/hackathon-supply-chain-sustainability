from binascii import a2b_base64
import cv2
import open3d as o3d
import numpy as np
import pyransac3d as pyrsc
from images2Ply import image2ply
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# we can get two images(depth and colour)

file = image2ply("pensRGB.png","pens.png","image.ply")


# Load saved point cloud and visualize it
box_pcd_load = o3d.io.read_point_cloud("caixa.ply")
# o3d.visualization.draw_geometries([pcd_load])

box_points = np.asarray(box_pcd_load.points)
box_plano1 = pyrsc.Cuboid()
box_best_eq, box_best_inliers = box_plano1.fit(box_points, 0.01)

print("box plane equation is")
print(box_best_eq)

plane = box_pcd_load.select_by_index(box_best_inliers).paint_uniform_color([1, 0, 0])
obb = plane.get_oriented_bounding_box()
obb2 = plane.get_axis_aligned_bounding_box()
obb.color = [0, 0, 1]
obb2.color = [0, 1, 0]
not_plane = box_pcd_load.select_by_index(box_best_inliers, invert=True)

o3d.visualization.draw_geometries([not_plane, plane, obb, obb2])

print("box dimensions are:")
print(obb)
print(obb2)

# Load saved point cloud and visualize it
object_pcd_load = o3d.io.read_point_cloud(file)
# o3d.visualization.draw_geometries([pcd_load])

object_points = np.asarray(object_pcd_load.points)
object_plano1 = pyrsc.Cuboid()
object_best_eq, object_best_inliers = object_plano1.fit(object_points, 0.01)

print("object plane equation is")
print(object_best_eq)

plane = object_pcd_load.select_by_index(object_best_inliers).paint_uniform_color([1, 0, 0])
obb = plane.get_oriented_bounding_box()
obb2 = plane.get_axis_aligned_bounding_box()
obb.color = [0, 0, 1]
obb2.color = [0, 1, 0]
not_plane = object_pcd_load.select_by_index(object_best_inliers, invert=True)

o3d.visualization.draw_geometries([not_plane, plane, obb, obb2])

print("object dimensions are:")
print(obb)
print(obb2)
