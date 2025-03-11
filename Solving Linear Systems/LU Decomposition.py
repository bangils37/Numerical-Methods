import numpy as np

def lu_decomposition(A):
    """
    Phân rã LU của ma trận A (A = L * U)
    
    Tham số:
    - A: Ma trận vuông (numpy array)
    
    Trả về:
    - L: Ma trận tam giác dưới
    - U: Ma trận tam giác trên
    """
    n = len(A)
    L = np.eye(n)  # Ma trận L (tam giác dưới), khởi tạo là ma trận đơn vị
    U = np.zeros((n, n))  # Ma trận U (tam giác trên)

    for i in range(n):
        for j in range(i, n):  # Tính U
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        
        for j in range(i+1, n):  # Tính L
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    return L, U

def forward_substitution(L, b):
    """Giải Ly = b bằng phương pháp thế tiến"""
    n = len(b)
    y = np.zeros(n)
    
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    
    return y

def backward_substitution(U, y):
    """Giải Ux = y bằng phương pháp thế lùi"""
    n = len(y)
    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    
    return x

def solve_lu(A, b):
    """Giải hệ Ax = b bằng LU Decomposition"""
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

# Test với hệ phương trình lớn
n = 1000 
A = np.random.rand(n, n) + np.eye(n) * 100  # Ma trận chéo trội
b = np.random.rand(n)

x = solve_lu(A, b)
print("Nghiệm gần đúng:", x[:10])  # In 10 giá trị đầu tiên
