#1강 강의 내용 
# import time

# n = int(input("Number of elements : "))
# haystack = [k for k in range(n)]

# print("Searching for the maximum value...")

# ts = time.time()
# maximum = max(haystack)
# elapsed = time.time() -ts

# print("Maximum element = %d, Elapsed time = %.2f" % (maximum, elapsed))

def solution(x):
    answer = x[0] +x[-1]
    return answer
print()
print('-' * 10)
print('답 : ', solution([5,3,8,2]))
print('-' * 10)