def qwkappa(y, y_pred):
    import numpy as np
    from sklearn.metrics import confusion_matrix
    n = len(y)
    w = np.zeros((n,n))

    # The matrix O is the confusion matrix
    O = confusion_matrix(y, y_pred)

    # Create histogram vectors of outcomes
    # Actual:
    N = 6
    hist_actual = np.zeros([N])
    for val in y:
        hist_actual[val] += 1
    # Predicted:
    hist_pred = np.zeros([N])
    for val in y_pred:
        hist_pred[val] += 1

    # The matrix E is the outer product between the actual
    # histogram vector of outcomes and the predicted
    E = np.outer(hist_actual, hist_pred)

    # Normalize E and O - just divide them by their sum so that
    # the sum of both of them are 1
    O = O / O.sum()
    E = E / E.sum()

    # Calculate weights
    w = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            w[i][j] = (i-j)**2/(N-1)**2
    
    # Calculate Kappa
    num = 0
    den = 0
    for i in range(N):
        for j in range(N):
            num += w[i][j] * O[i][j]
            den += w[i][j] * E[i][j]
    
    return 1-num/den