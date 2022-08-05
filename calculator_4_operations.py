def option():
    operation = input("Which operation do you want to do?( Addition - 1, extraction(only 2 numbers)-2, multiplication- 3, division-4):")
    return operation

def exit_control():
    go_on = input('Text "E" to exit: ')
    return go_on

def data_input_control(data):
    if (data.isdigit()):
        return 1
    else:
        return 0

def data_input():
    number_list = []
    while True:
        number = input("Give us a number: ")

        control = data_input_control(number)
        if (control == 1):
            number = int(number)
            number_list.append(number)
        else:
            print("You wrote an invalid choice")
            continue

        result_of_data_control = exit_control()

        if (result_of_data_control == "E"):
            break
    print(number_list)
    return number_list
    
        

def addition(number_list):
    result = 0
    for i in number_list:
        result = result + i
    print(f"Result:{result}")

def extraction(number_list):
    if (len(number_list)==2):
        result= number_list[0]-number_list[1]
        print(result)
        print(f"Result:{result}")
    else:
         print("You can't give less or more than 2 numbers for extraction.")
        
def division(number_list):
    result = number_list[0]
    for i in range(1,len(number_list)):
        result = result / number_list[i]
    print(f"Result: {result}")

def multiplication(number_list):
    result=1
    for i in range(0,len(number_list)):
        result = result * number_list[i]
    print(f"Result:{result}")

def main():
    option_data = option()
    numbers = data_input()
    match option_data:
        case "1":
            addition(numbers)
        case "2":
            extraction(numbers)
        case "3":
            multiplication(numbers)
        case "4":
            division(numbers)
        case _:
            print("You made an invalid choice.")

main()
#by irembuseozkose 08/05/2022
