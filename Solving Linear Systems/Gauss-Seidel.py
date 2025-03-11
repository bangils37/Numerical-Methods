import numpy as np

def gauss_seidel(A, b, tol=1e-10, max_iter=10000):
    """
    Giải hệ phương trình Ax = b bằng phương pháp Gauss-Seidel.
    
    Tham số:
    - A: Ma trận hệ số (numpy array)
    - b: Vector hằng số (numpy array)
    - tol: Ngưỡng hội tụ
    - max_iter: Số lần lặp tối đa
    
    Trả về:
    - x: Nghiệm gần đúng của hệ phương trình
    """
    n = len(b)
    x = np.zeros(n)  # Khởi tạo nghiệm ban đầu là vector 0

    for _ in range(max_iter):
        x_new = np.copy(x)
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])   # Phần đã cập nhật
            sum2 = np.dot(A[i, i+1:], x[i+1:])   # Phần chưa cập nhật
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]

        # Kiểm tra điều kiện hội tụ
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        
        x = x_new  # Cập nhật nghiệm

    raise Exception("Không hội tụ sau {} lần lặp".format(max_iter))

# Test với hệ phương trình lớn
n = 1000  
A = np.random.rand(n, n) + np.eye(n) * 100  # Ma trận chéo trội để đảm bảo hội tụ
b = np.random.rand(n)

x = gauss_seidel(A, b)
print("Nghiệm gần đúng:", x[:10])  # In 10 giá trị đầu tiên
