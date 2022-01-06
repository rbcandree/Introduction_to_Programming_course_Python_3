def main():
    num = int(input("Enter Your number, please: "))
    hailstone_list = hailstone(num)
    if (hailstone_list is None):
        print("Hailstone sequence is defined for positive integers only")
    else: 
        print("Hailstone sequence for n = {} is: {}".format(num, hailstone_list))
        print("Number of steps is : ",len(hailstone_list))

def hailstone(num):
    hailstone_list = []
    hailstone_list.append(int(num))
    while num != 1:
        if num <= 0:
            return None
        elif num % 2 == 0:
            num = num / 2
            hailstone_list.append(int(num))
        elif num % 2 == 1:
            num = 3 * num + 1
            hailstone_list.append(int(num))
    return hailstone_list
main()