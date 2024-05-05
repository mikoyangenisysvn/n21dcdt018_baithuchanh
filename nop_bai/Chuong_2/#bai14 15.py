#bai14 15
def first_common_subsequence(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i+k < len(a) and j+k < len(b) and a[i+k] == b[j+k]:
                k += 1
            if k > 0:
                return a[i:i+k]
    return []

def longest_common_subsequence(a, b):
    # Sử dụng kỹ thuật tương tự như trên nhưng lưu lại kết quả dài nhất
    longest = []
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i+k < len(a) and j+k < len(b) and a[i+k] == b[j+k]:
                k += 1
            if k > len(longest):
                longest = a[i:i+k]
    return longest

# Ví dụ sử dụng
a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [9, 6, 2, 5, 3, 7, 8, 1, 5]

print(first_common_subsequence(a, b))  # [6, 2]
print(longest_common_subsequence(a, b))  # [6, 2, 5, 3, 7]
