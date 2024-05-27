import re

def filter_digits(test_cases):
    results = []
    for test in test_cases: 
        numbers = re.split('\D+', test)     
        numbers = [int(num) for num in numbers if num]
        results.append(numbers)
    return results

T = int(input().strip()) 
test_cases = [input().strip() for _ in range(T)]  
filtered_results = filter_digits(test_cases)  


for result in filtered_results:
    print(min(result))
