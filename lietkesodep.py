def check(n):
    return str(n) == str(n)[::-1]
#check số viết ngược lại có bằng số ban đầu không
def list_(n):
    return [i for i in range(21, n) if check(i) 
            and all(digit in '24680' for digit in str(i)) 
            and len(str(i)) % 2 == 0] 

def main():
    n = int(input())
    for _ in range(n):
        num = int(input())
        print(' '.join(map(str, list_(num))))

if __name__ == "__main__":
    main()
