redballs = []
blueballs = []
i = 1
j = 1
while i <= 6:
    redball = int(input('select red ball num：'))
    if redball >=1 and redball<=32:
        if redball not in redballs:
            redballs.append(redball)
            # print(redballs)
            i += 1
        else:
            print('the num %s is in list' %redball)
    else:
        print('only can select between 1-32')
        continue
# print(redballs)
while j <= 2:
    blueball = int(input('select blue ball num：'))
    if blueball >=1 and blueball<=16:
        if blueball not in blueballs:
            blueballs.append(blueball)
            # print(blueballs)
            j += 1
        else:
            print('the num %s is in list' %blueball)
    else:
        print('only can select between 1-16')
        continue
print(redballs)
print(blueballs)


