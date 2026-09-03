# for문

# for x in interable객체:
#   ...

for i in range(5):  # 0 ~ $
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)  # (시작 값, 끝 값, 간격)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

# 1 ~ 10, 2칸씩
for i in range(1, 11, 2):
    print(i, end=" ")
print()

# 5, 4, 3, 2, 1 거꾸로
for i in range( 5, 0, -1):
    print(1, end=" ")
print()

# 1 ~ 10까지 합
tot = 0
for i in range(1, 11):
    tot += i
else: 
    print(f"sum: {tot}")

print(sum(range(1, 11)))

s = "hi한글🥵🥵"

for c in s:
    print(c, end=" ")

print(len(s))

#구구단 출력
# 2 * 1 = 2
for i in range(2, 10):
    for j in range(2, 10):
        print(f"{i} * {j} = {i*j:<5d}", end=" ")
        j += 1
    print()
    i += 1
