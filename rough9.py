def mean(numlist):
    no_of_eles = len(numlist)
    summ = sum(numlist)
    avg = summ / no_of_eles
    print("Mean for given set of numbers is : ", avg)
    return


def median(numlist):
    numlist.sort()
    if (len(numlist) % 2 != 0):
        i = len(numlist) // 2
        print("Median for given set of numbers is : ", numlist[i])
    else:
        i = len(numlist) // 2
        print("Median for given set of numbers is : ",
              (numlist[i - 1] + numlist[i]) / 2)
    return


def mode(numlist):
    modedict = {}
    mincount = 1
    for ele in numlist:
        maxcount = numlist.count(ele)
    if (maxcount >= mincount):
        mincount = maxcount
        modedict[ele] = mincount
    if (mincount == 1):
        print("Mode for given set of numbers is : None")
    else:
        print("Mode for given set of numbers is : ", end='')
        for ele in modedict:
            if (modedict[ele] == mincount):
                print(ele, end=' ')
        return


numlist = []
n = int(input("Enter number of elements to be insert:"))
for i in range(n):
    ele = int(input("Enter element:"))
    numlist.append(ele)
mean(numlist)
median(numlist)
mode(numlist)