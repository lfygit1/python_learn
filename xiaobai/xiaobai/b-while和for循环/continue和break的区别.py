k=[5,2,9,10,6]
for i in k:
    if i >6:
        print(i)
        # break  # 执行到符合条件的语句时跳出整个循环，后面的不在执行
    else:
        if i<=6:
            continue # 跳过本次循环，继续下次循环
        print('666')
