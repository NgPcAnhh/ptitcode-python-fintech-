def main():
    # Nhập input từ người dùng
    input_string = input()

    # Tách chuỗi thành các chữ
    characters = list(input_string)

    # Tạo một tập hợp từ các chữ
    char_set = set(characters)

    # Thực hiện hoán vị 
    permutations = get_permutations(char_set)

    # Sắp xếp theo thứ tự từ điển
    sorted_permutations = sorted(permutations)

    # In kết quả
    print()
    for perm in sorted_permutations:
        print("".join(perm))

def get_permutations(char_set):
    if len(char_set) == 0:
        return [[]]
    
    first_char = char_set.pop()
    smaller_permutations = get_permutations(char_set)
    result = []
    for perm in smaller_permutations:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + [first_char] + perm[i:]
            result.append(new_perm)
    return result

if __name__ == "__main__":
    main()
