import numpy as np

def jacobi_method(A, b, tol=1e-10, max_iterations=1000):
    """
    Giải hệ phương trình tuyến tính Ax = b bằng phương pháp Jacobi.
    
    - A: Ma trận hệ số (n x n)
    - b: Vector kết quả (n x 1)
    - tol: Ngưỡng sai số hội tụ
    - max_iterations: Số lần lặp tối đa
    
    Trả về:
    - x: Nghiệm gần đúng của hệ phương trình
    - iterations: Số lần lặp thực hiện
    """
    n = len(A)
    x = np.zeros(n)  # Khởi tạo nghiệm x_0 = [0, 0, ..., 0]

    # Tách ma trận A thành D, L, U
    D = np.diag(A)  # Đường chéo chính
    R = A - np.diagflat(D)  # Phần còn lại

    for iteration in range(max_iterations):
        x_new = (b - np.dot(R, x)) / D  # Công thức Jacobi

        # Kiểm tra điều kiện hội tụ
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, iteration + 1  # Trả về nghiệm và số lần lặp
        
        x = x_new

    raise Exception("Jacobi method did not converge within the maximum iterations")

# Kiểm tra với hệ phương trình lớn
if __name__ == "__main__":
    n = 1000  
    A = np.random.rand(n, n) + np.eye(n) * 10  # Ma trận chéo trội để đảm bảo hội tụ
    b = np.random.rand(n)

    solution, iterations = jacobi_method(A, b)
    print(f"Nghiệm đầu tiên: {solution[:5]} ...")
    print(f"Jacobi hội tụ sau {iterations} lần lặp.")
