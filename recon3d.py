import numpy as np

def reconstruct3D(transform_candidates, calibrated_1, calibrated_2):
  """This functions selects (T,R) among the 4 candidates transform_candidates
  such that all triangulated points are in front of both cameras.
  """

  best_num_front = -1
  best_candidate = None
  best_lambdas = None
  for candidate in transform_candidates:
    R = candidate['R']
    T = candidate['T']

    lambdas = np.zeros((2, calibrated_1.shape[0])).T
    """ YOUR CODE HERE
    """
    A = np.zeros((3,2))
    for i in range(calibrated_1.shape[0]):
      x1 = calibrated_1[i]
      x2 = calibrated_2[i]
      A = np.hstack([x2.reshape(3,1), -R@x1.reshape(3,1)])
      B = T.reshape((3,1))
      depth,_,_,_ =np.linalg.lstsq(A,B,rcond=-1)
  
      lambdas[i] = depth.reshape((2,))
    lambdas = lambdas.T
    """ END YOUR CODE
    """
    num_front = np.sum(np.logical_and(lambdas[0]>0, lambdas[1]>0))

    if num_front > best_num_front:
      best_num_front = num_front
      best_candidate = candidate
      best_lambdas = lambdas
      print("best", num_front, best_lambdas[0].shape)
    else:
      print("not best", num_front)


  P1 = best_lambdas[1].reshape(-1, 1) * calibrated_1
  P2 = best_lambdas[0].reshape(-1, 1) * calibrated_2
  T = best_candidate['T']
  R = best_candidate['R']
  return P1, P2, T, R