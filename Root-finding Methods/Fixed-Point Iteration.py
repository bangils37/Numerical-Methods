def fixed_point(g, x0, tol=1e-6, max_iter=100):
    """Giải phương trình bằng phương pháp điểm bất động"""
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Ví dụ: Tìm nghiệm của x = sqrt(x + 2)
g = lambda x: (x + 2)**(1/2)  # Chuyển đổi f(x) = 0 thành x = g(x)

root = fixed_point(g, x0=1.5)
print("Nghiệm gần đúng (Fixed-Point):", root)
