#1
num: float = float(input('enter a number: '))
if num > 10:
    print(num - 10)
else:
    print(num * 10)

#2
num1: float = float(input('enter a number: '))
num2: float = float(input('enter a number: '))
num3: float = float(input('enter a number: '))

num4: float = num1 + num2 + num3
if num4 > 100:
    print(num4)
else:
    print('num is smaller than 100')

#3
shever_1: float = num1 % 1
shever_2: float = num2 % 1
if shever_1 > shever_2:
    print(shever_1)
elif shever_2 > shever_1:
    print(shever_2)
else:
    print('equal')

#4
age: float = float(input('enter your age: '))
if 0 < age < 120:
    print(age)
else:
    print('age is incorrect')

#5
num3d: int = int(input('enter 3 digits number: '))
if num3d > 0:
    num3d = num3d // 10
    print(num3d % 10)

#6
n: int = int(input('enter a number: '))
for i in range(n, 0, -1):
    print(i)

#7
n1: int = int(input('enter a number: '))
n2: int = int(input('enter a number: '))
for x in range(n1, n2 +1, 2):
    print(x)

#8
l1: list[int] = []
num: int = int(input('enter a number: '))
for i in range(num+1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

#9
num: int = int(input('enter a number: '))
for i in range(0, num+1, 7):
    print(i)

#11
nums: list[int]= []
while True:
    num: int = int(input('enter a number: '))
    if num < 0:
        nums.append(num)
    if num == 0:
        break
print(sum(nums))

#12
nums: list[int]= []

for i in range(10):
    num: int = int(input('enter a number: '))
    nums.append(num)
print(sorted(nums))

#13
SENTINEL: int = 0
counter: int = 0
while True:
    try:
        num: int = int(input('enter number [0 to exit]: '))
        if num == SENTINEL:
            break
        if num < 2:
            continue
        is_prime: bool = True

        for divider in range(2, num ** 0.5 + 1):
            if num % divider == 0:
                is_prime = False
                break
        if is_prime:
            counter += 1
    except:
        print('bad number')

print(f'{counter} prime numbers...')

#14
nums: list[int] = []
counter: int = 0
for _ in range (5):
    num: int = int(input('enter a number: '))
    nums.append(num)
av: float = sum(nums) / len(nums)
print(av)

for num in nums:
    if num > av:
        counter += 1
print(counter)

#15
num1: int = int(input('enter a num: '))
num2: int = int(input('enter a num: '))
counter: int = 0

while num1 > 0:
    num1 = num1 - num2
    counter += 1
print(counter)

#16
num: int = int(input('enter a num: '))
sum: int = 0
while num > 0:
    rightd = num % 10
    sum += rightd
    num = num // 10
if sum % 3 == 0:
    print('divides by 3')
else:
    print('does not divide by 3')

#17
word1: str = input('enter a word- ')
word2: str = word1[::-1]
if word1 == word2:
    print('swapped')
else:
    print('not swapped')

