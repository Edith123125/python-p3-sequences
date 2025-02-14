#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    # Initialize Fibonacci sequence  [0, 1]
    fibonacci_sequence = [0, 1]

    for i in range(2, length):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2] 
        fibonacci_sequence.append(next_fib)

    print(fibonacci_sequence[:length])
    
    

