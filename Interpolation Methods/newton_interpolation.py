def newton_difference_table(x_points, y_points):
    """Tạo bảng sai phân Newton"""
    n = len(x_points)
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y_points[i]
    
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_points[i + j] - x_points[i])
    return table

def newton_interpolation(x_points, y_points, x):
    """Nội suy Newton tại điểm x"""
    n = len(x_points)
    table = newton_difference_table(x_points, y_points)
    result = table[0][0]  # Giá trị đầu tiên
    product = 1
    for i in range(1, n):
        product *= (x - x_points[i - 1])
        result += table[0][i] * product
    return result

# Ví dụ sử dụng
x_data = [0, 1, 2, 3]
y_data = [1, 2, 0, 5]
x_test = 1.5
result = newton_interpolation(x_data, y_data, x_test)
print("Nội suy Newton tại x =", x_test, ":", result)