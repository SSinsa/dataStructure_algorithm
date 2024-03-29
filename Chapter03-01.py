# 강의내용
# L1= sorted(L)
# L.sort()
# L2 = sorted(L, reverse=True)
# L.sort(reverse=True)

# sorted(L, key=lambda x: len(x)) 길이로 정렬
# L.sort(key=lambda x:x['키명'], reverse=True)

# 지금까지 비교는 선형탐색 -> O(n)  
# 이진탐색은 이미 정렬되어있다는 가정하에 lower, middle, upper -> O(log n)
# lower =0
# upper = len(L) -1
# idx = -1
# while lower <= upper :
#     middle = (lower + upper) / 2
#     if L[middle] == target :
#         ...
#     elif L[middle] < target :
#         lower = ...
#     else : 
#         upper = ...

# 실습문제
# 리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어질 때, x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

# 예를 들어,
# L = [2, 3, 5, 6, 9, 11, 15]
# x = 6
# 의 인자들이 주어지면, L[3] == 6 이므로 3 을 리턴해야 합니다.

# 또 다른 예로,
# L = [2, 5, 7, 9, 11]
# x = 4
# 로 주어지면, 리스트 L 내에 4 의 원소가 존재하지 않으므로 -1 을 리턴해야 합니다.

# 이 연습문제에서는 알고리즘의 효율성도 평가합니다. 만약 순차 (선형) 탐색 알고리즘을 구현하는 경우에는 제한 시간 요구사항을 만족하지 못하여 효율성 테스트 케이스들을 통과하지 못할 수도 있습니다.

def solution(L, x):
    answer = 0
    lower = 0
    upper = len(L) -1
    while lower < upper :
         middle = int((lower + upper)/2)
         if L[middle] == x :
             answer = middle
             break
         elif L[middle] < x :    
             upper = middle
         elif L[middle] < x :
             lower = middle    
    else : answer = -1
    return answer

print()
print('-' * 10)
print('답 : ', solution([2, 3, 5, 6, 9, 11, 15], 6))
print('-' * 10)