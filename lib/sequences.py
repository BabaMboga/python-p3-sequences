#!/usr/bin/env python3


def print_fibonacci(length):
    fibo_list = []

    # Handling 0 & 1 cases
    if length >= 1:
        fibo_list.append(0)
    if length >= 2:
        fibo_list.append(1)

    # Generating the sequence
    for i in range(2, length):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])

    # Printing the sequence
    return fibo_list

answer = print_fibonacci(10)
print(answer)