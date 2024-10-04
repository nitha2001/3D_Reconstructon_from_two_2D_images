import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """
  
  A = np.zeros((X1.shape[0],9))
  for i in range(X1.shape[0]):
    x1,y1,_ = X2[i]
    x2,y2,_ = X1[i]
    A[i] = [x1*x2,x1*y2,x1,y1*x2,y1*y2,y1,x2,y2,1]

  U,S,V = np.linalg.svd(A)
  E = V[-1,:].reshape(3,3)

  U, _, V = np.linalg.svd(E)
  E = U @ np.diag([1, 1, 0]) @ V

  """ END YOUR CODE
  """
  return E
