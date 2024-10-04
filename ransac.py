from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """ YOUR CODE HERE
        """
        X1_S = X1[sample_indices]
        X2_S = X2[sample_indices]

        E = least_squares_estimation(X1_S,X2_S)
        e3_skew = np.array([[0,-1,0],
                            [1,0,0],
                            [0,0,0]])
        inliers = []
        for j in test_indices:
            x1 = X1[j]
            x2 = X2[j]
            d1 = np.linalg.norm(x2.T @ E @ x1)**2/np.linalg.norm(e3_skew@E@x1)**2
            d2 = np.linalg.norm(x1.T @ E.T @ x2) ** 2/np.linalg.norm(e3_skew@E.T@x2)**2
            d=(d1+d2)
            if d < eps:
                inliers.append(j)        
        """inliers = []
        for k, res in enumerate(resid):
            if res < eps:
                inliers.append(test_indices[k])"""
        inliers = np.array(inliers)
        inliers = np.append(sample_indices, inliers)    
        """ END YOUR CODE
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers


    return best_E, best_inliers