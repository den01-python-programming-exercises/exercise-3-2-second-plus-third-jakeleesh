def main():
    #write your code below this line
    number_list = []
    while True:
        num = int(input())
        if (num == 0):
            break
        else:
            number_list.append(num)
    print(number_list[1] + number_list[2])

if __name__ == '__main__':
    main()
