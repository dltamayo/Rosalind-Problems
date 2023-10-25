#!/usr/bin/python
import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

def fibonacci(n, k):
    """Returns fibonacci calculation after n months with k offspring."""
    fibo_cache = {}
    
    def fibonacci_recursive(n, k):
        if n == 1 or n == 2:
            return 1
        if (n,k) not in fibo_cache:
            fibo_cache[(n,k)] = fibonacci_recursive(n-1,k) + k * fibonacci_recursive(n-2, k)
        return fibo_cache[(n,k)]
    
    fibonacci_recursive(n, k)
    return fibo_cache[(n,k)]

if __name__ == '__main__':
    with open(inFile, 'r') as input_file, open(outFile, 'w') as output_file:
        input = input_file.read()
        input_list = [int(x) for x in input.split()]
        n,k = input_list[0],input_list[1]
        output = fibonacci(n, k)
        output_file.writelines(str(output))