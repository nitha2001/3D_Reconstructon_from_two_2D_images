import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  U,S,Vt = np.linalg.svd(E,full_matrices= True)
  T1 = U[:,-1]
  T2 = -U[:,-1]
  Rz = np.array([[0,-1,0],
                   [1,0,0],
                   [0,0,1]]) 
  R1 = U @ Rz.T @ Vt
  R2 = U @ Rz.T.T @ Vt

  c1 = {"R":R1,"T":T1}
  c2 = {"R":R2,"T":T1}
  c3 = {"R":R1,"T":T2}
  c4 = {"R":R2,"T":T2}
  transform_candidates = [c1,c2,c3,c4]
  """ END YOUR CODE
  """
  return transform_candidates