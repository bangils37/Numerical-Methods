def bisection(f, a, b, tol=1e-6, max_iter=100):
    """Tìm nghiệm của phương trình f(x) = 0 bằng phương pháp chia đôi"""
    if f(a) * f(b) > 0:
        raise ValueError("f(a) và f(b) phải trái dấu")

    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Ví dụ: Tìm nghiệm của x^3 - x - 2 = 0
f = lambda x: x**3 - x - 2
root = bisection(f, 1, 2)
print("Nghiệm gần đúng (Bisection):", root)
