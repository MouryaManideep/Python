def towofhanoi(n):
    if n==0 :
        return 0

    return 2 * towofhanoi(n-1) + 1

print(towofhanoi(64))