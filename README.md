# hackathon-supply-chain-sustainability


----------------------------------------------------------------------------------------------------------------------------------

## Steps:
1. First we have to take images(stereo and colour) using **Luxonis OAK-D-Lite Spatial AI camera**.

2. After that run **stereo2DepthMap.py** to get **depthMap image**.

3. Then to get point cloud **images2Ply.py** and generate **.ply** file

4. Once you get **.ply** file then use [pyRANSAC-3D](https://github.com/leomariga/pyRANSAC-3D) to **get_oriented_bounding_box** for object

Once you get bouding box then just intersect box and object bounding box.

![object bounding box](https://github.com/avinashkella/hackathon-supply-chain-sustainability/blob/main/pensRGB.png?raw=true)

![object bounding box](https://github.com/avinashkella/hackathon-supply-chain-sustainability/blob/main/pens.png?raw=true)

![object bounding box](https://github.com/avinashkella/hackathon-supply-chain-sustainability/blob/main/Capture1.PNG?raw=true)

![object bounding box](https://github.com/avinashkella/hackathon-supply-chain-sustainability/blob/main/Capture.PNG?raw=true)

![object bounding box](https://github.com/avinashkella/hackathon-supply-chain-sustainability/blob/main/Capture2.PNG?raw=true)


