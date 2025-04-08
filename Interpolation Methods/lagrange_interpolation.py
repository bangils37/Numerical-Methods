def lagrange_interpolation(x_points, y_points, x):
    """Nội suy Lagrange tại điểm x với danh sách điểm (x_points, y_points)"""
    n = len(x_points)
    result = 0
    for i in range(n):
        # Tính đa thức cơ sở Lagrange L_i(x)
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Ví dụ sử dụng
x_data = [0, 1, 2, 3]
y_data = [1, 2, 0, 5]
x_test = 1.5
result = lagrange_interpolation(x_data, y_data, x_test)
print("Nội suy Lagrange tại x =", x_test, ":", result)