import numpy as np

def cubic_spline(x_points, y_points, x):
    """Nội suy Spline bậc 3 tại điểm x"""
    n = len(x_points) - 1  # Số đoạn
    h = [x_points[i + 1] - x_points[i] for i in range(n)]
    
    # Tạo hệ phương trình để tìm moment (đạo hàm bậc hai)
    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)
    
    # Điều kiện biên tự nhiên: M0 = Mn = 0
    A[0, 0] = 1
    A[n, n] = 1
    
    for i in range(1, n):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 6 * ((y_points[i + 1] - y_points[i]) / h[i] - (y_points[i] - y_points[i - 1]) / h[i - 1])
    
    # Giải hệ để tìm moment
    M = np.linalg.solve(A, b)
    
    # Tìm đoạn chứa x
    for i in range(n):
        if x_points[i] <= x <= x_points[i + 1]:
            t = (x - x_points[i]) / h[i]
            a = y_points[i]
            b = y_points[i + 1]
            c = M[i] * h[i]**2 / 6
            d = M[i + 1] * h[i]**2 / 6
            return (1 - t) * a + t * b + t * (1 - t) * ((1 - t) * c - t * d)
    raise ValueError("x nằm ngoài khoảng nội suy")

# Ví dụ sử dụng
x_data = [0, 1, 2, 3]
y_data = [1, 2, 0, 5]
x_test = 1.5
result = cubic_spline(x_data, y_data, x_test)
print("Nội suy Spline tại x =", x_test, ":", result)