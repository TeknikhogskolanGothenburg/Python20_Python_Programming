# 0 1 1 2 3 5 8 13 21 34
# 0 1 2 3 4 5 6 7  8
import time

@time_it
def recur_fibo(n, mem={}):
    if n <= 1:
        return n
    else:
        if n-1 in mem:
            n1 = mem[n-1]
        else:
            n1 = recur_fibo(n-1)
            mem[n-1] = n1
        if n-2 in mem:
            n2 = mem[n-2]
        else:
            n2 = recur_fibo(n-2)
            mem[n-2] = n2
        return n1 + n2

@time_it
def recur_fibo2(n):
    if n <= 1:
        return n
    else:
        return recur_fibo2(n-1) + recur_fibo2(n-2)

def main():
    start = time.time()
    print(recur_fibo2(40))
    end = time.time()
    print(f"It took {end-start} seconds")

    start = time.time()
    print(recur_fibo(40))
    end = time.time()
    print(f"It took {end-start} seconds")


if __name__ == '__main__':
    main()
