#bai16
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Để dễ dàng xử lý phần tử cuối cùng

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

def maxRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    max_area = 0
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    
    for row in matrix:
        for i in range(cols):
            if row[i] == 0:
                heights[i] = 0
            else:
                heights[i] += 1
        max_area = max(max_area, largestRectangleArea(heights))
    
    return max_area

# Ví dụ
matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
print("Diện tích hình chữ nhật lớn nhất là:", maxRectangle(matrix))
