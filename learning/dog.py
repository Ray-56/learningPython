#!/usr/bin/python3

age = int(input('请输入你家狗狗的年龄: '))
print('')
if age < 0:
   print('这个时候应该还是个细胞!')
elif age == 1:
   print('相当于14岁的人类')
elif age == 2:
    print('相当于22岁的人类')
elif age > 2:
    human = 22 + (age - 2) * 5
    print('对应人类年龄: ', human)

# 退出提示
input('点击 enter 键退出')