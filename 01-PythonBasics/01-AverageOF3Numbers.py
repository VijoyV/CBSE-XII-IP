# Enter 3 Numbers and find it's average

num1 = int(input('Enter num 1 : '))
num2 = int(input('Enter num 2 : '))
num3 = int(input('Enter num 3 : '))

avg=(num1+num2+num3)/3

print('Average of 3 numberes entered = ', avg)

roundedAvg = round(avg, 2)

print('Average of 3 numberes entered rounded to 2 decimal places = ', roundedAvg)

print('Lowest number = ', min(num1, num2, num3))

print('highest number = ', max(num1, num2, num3))
