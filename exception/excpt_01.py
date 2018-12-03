try:
    num = int(input("please input your number:"))
    ret = num / 0
    print("result : {0}".format(ret))

except ZeroDivisionError as zero:
    print("Error ...")
    print(zero)
    #exit()
print("Next tip ...")