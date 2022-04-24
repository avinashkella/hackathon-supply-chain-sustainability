import open3d as o3d

def image2ply(color_raw, depth_raw, fileName):

    # we can get two images(depth and colour)
    color_raw = o3d.io.read_image(color_raw)
    depth_raw = o3d.io.read_image(depth_raw)


    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_raw, depth_raw)

    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])

    # to visualize cloud points
    o3d.visualization.draw_geometries([pcd])

    o3d.io.write_point_cloud(fileName, pcd)

    return fileName