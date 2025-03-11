import numpy as np

def gaussian_elimination(A, b):
    """
    Giải hệ phương trình Ax = b bằng phương pháp Gaussian Elimination.
    
    Tham số:
    - A: Ma trận hệ số (numpy array)
    - b: Vector hằng số (numpy array)
    
    Trả về:
    - x: Nghiệm của hệ phương trình
    """
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])  # Gộp A và b thành ma trận mở rộng

    # Forward elimination (Khử Gauss)
    for i in range(n):
        # Chọn hàng có phần tử lớn nhất tại cột i (pivoting)
        max_row = np.argmax(abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]  # Hoán đổi hàng

        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]

    # Back-substitution (Thế lùi)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]

    return x

# Test với hệ phương trình lớn
n = 1000 
A = np.random.rand(n, n) + np.eye(n) * 100  # Ma trận chéo trội
b = np.random.rand(n)

x = gaussian_elimination(A, b)
print("Nghiệm gần đúng:", x[:10])  # In 10 giá trị đầu tiên
