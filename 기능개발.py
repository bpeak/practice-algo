def solution(jobs, speeds):
    done = []
    while len(jobs) != 0:
        # work
        for i in range(len(jobs)):
            jobs[i] += speeds[i]

        # done check
        doneJobCount = 0
        for i in range(len(jobs)):
            if jobs[i] < 100:
                break
            
            doneJobCount += 1
        
        # remove done job
        if doneJobCount > 0:
            for i in range(doneJobCount):
                jobs.pop(0)
                speeds.pop(0)
            done.append(doneJobCount)
    return done

print(solution([93,30,55], [1,30,5])) # [2,1]
print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7])) # [1,2,3]
print(solution( [93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7])) # [2,4]

"""
***1 이터레이터 돌리는데 중간에 값 제거하는 경우 ( 조심해야함 )

< 괜찮음 >
a = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)):
  print(i)
  if i == 3:
    a.remove(2)

< 안괜찮음 > ( 앞에 2를 뺐는데 다음 4가 출력이 안됨 ( 배열재배치로 인해서 밀렸음 ))
a = [1,2,3,4,5,6,7,8,9,10]
for v in a:
  print(v)
  if v == 3:
    a.remove(2)

***2 두가지 배열을 동시에 컨트롤 하는 경우
jobs, speeds 는
인덱스가 동기화 되어야함 ( jobs에서는 뺐는데 speeds 에선 안빼주면 안되지 )

jobs.pop()
speeds.pop()
알아서 해줄수 도 있겠지만

하나의 리스트로 합쳐주고 dict 형태로 관리하는게 실수 확률은 굉장히 낮을듯

"""