def newton(f, df, x0, tol=1e-6, max_iter=100):
    """Tìm nghiệm của phương trình f(x) = 0 bằng phương pháp Newton-Raphson"""
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Ví dụ: Tìm nghiệm của x^3 - x - 2 = 0
f = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1  # Đạo hàm của f(x)

root = newton(f, df, x0=1.5)
print("Nghiệm gần đúng (Newton):", root)
