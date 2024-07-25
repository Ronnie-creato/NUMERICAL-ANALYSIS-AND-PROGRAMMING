import numpy as np
def qr_algorithm(A, num_simulations: int):
    A_k = np.copy(A)
    Q_total = np.eye(A.shape[0])
    
    for _ in range(num_simulations):
        Q, R = np.linalg.qr(A_k)
        A_k = np.dot(R, Q)
        Q_total = np.dot(Q_total, Q)
    
    eigenvalues = np.diag(A_k)
    eigenvectors = Q_total
    
    return eigenvalues, eigenvectors

# Example usage
eigenvalues_qr, eigenvectors_qr = qr_algorithm(A, 100)
print(f"QR Algorithm:\nEigenvalues: {eigenvalues_qr}\nEigenvectors:\n{eigenvectors_qr}")
