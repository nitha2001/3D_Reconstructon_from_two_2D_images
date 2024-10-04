# 3D_Reconstructon_from_two_2D_images
This project focuses on reconstructing the 3D geometry of a scene using two 2D images captured by different camera poses. Leveraging epipolar geometry, we estimate the relative pose between the two cameras and reconstruct the 3D coordinates of points in the scene. This is achieved using key concepts such as the essential matrix, triangulation, and epipolar constraint enforcement.

The pipeline starts with matching points between the two images using feature detection, proceeds to estimate the essential matrix robustly, and finally triangulates the 3D points to visualize the scene’s structure.

## Key Objectives
-Estimate the Essential Matrix: Compute the essential matrix using least-squares and RANSAC methods to robustly estimate the relative geometry between two images.
-Draw Epipolar Lines: Visualize epipolar constraints by drawing epipolar lines on both images.
-Recover Camera Pose: Decompose the essential matrix to recover the relative rotation and translation between the two camera positions.
-3D Reconstruction via Triangulation: Reconstruct the 3D structure of the scene by triangulating the matched points from both images.
-Reprojection Error Analysis: Compare the reprojected points from 3D to 2D with the original image points to measure accuracy.

## Contents

- `lse.py (Essential Matrix Estimation (8-Point Algorithm))`: Implements the 8-point algorithm to compute the essential matrix from point correspondences. Singular Value Decomposition (SVD) is used to enforce the rank-2 constraint on the matrix.
- `ransac.py (Robust Estimation with RANSAC)`: Uses RANSAC to eliminate outlier point matches and estimate the essential matrix robustly, significantly improving the accuracy of camera pose estimation.
- `plot_epi.py (Epipolar Line Visualization)`: Uses the estimated essential matrix to compute and draw epipolar lines on both images. These lines show the geometric relationship between corresponding points in the two views.
- `pose.py (Camera Pose Recovery)`: Decomposes the essential matrix into possible rotations and translations between the two camera poses. The correct pose is selected by verifying that reconstructed points lie in front of both cameras.
- `recon3d.py (3D Reconstruction via Triangulation)`: Triangulates the 3D points from the corresponding 2D points using the recovered camera poses. The result is a set of 3D points representing the scene structure.
- `show_reproj.py (Reprojection Comparison): Reprojects the 3D points back onto the image planes to compare the original 2D points with the reconstructed ones, evaluating the quality of the reconstruction by measuring reprojection error.

## Results
- Essential Matrix: Estimated using both the least-squares method and RANSAC.
- Epipolar Lines: Drawn on the image pair, showing the geometric relationship between corresponding points.
- Camera Pose: Recovered relative rotation and translation between the two camera views.
- 3D Reconstruction: Visualization of the 3D points triangulated from the two 2D image correspondences.
- Reprojection Comparison: Visual comparison of the original 2D points with the reprojected 3D points to validate reconstruction accuracy.

## Sample Output
Below is a Visualization of the Epipole and the 3D Reconstruction
All matches:
![image](https://github.com/user-attachments/assets/030b1e51-9f6c-47ef-80f8-a40660fe8270)
Epipolar Lines:
![image](https://github.com/user-attachments/assets/2f2e7d6a-eb38-4fde-8ac6-8a894de1505b)
RANSAC Inlier Matches:
![image](https://github.com/user-attachments/assets/1b093451-a4e7-4acf-b6cd-a40dc40a840a)
Recon 3D:
![image](https://github.com/user-attachments/assets/8017d497-1a0c-4f24-86f0-a9afdc391613)
Reprojection:
![image](https://github.com/user-attachments/assets/a99f49b4-caf5-43a9-a24f-28e8cabe6b8a)
SIFT:
![image](https://github.com/user-attachments/assets/5fa08ef5-b9ba-4a08-b4cf-1d560fe10558)
SIFT:
![image](https://github.com/user-attachments/assets/55a9daaf-0d84-4da9-94e2-b30f24b304a6)






  
