# finds avg of values typed into cli

numbers = []

while True:

    curNum = input("Type a number: ")

    if not curNum.isdigit():
        # print average then quit when 'q' is typed
        if curNum == 'q' and len(numbers) > 0:
            print(f"Average: {sum(numbers) / len(numbers)}")
            quit()
        print("Please type a number, or 'q' to quit")

    # if user types number: add(number) to list of nums
    else:
        numbers.append(float(curNum))
