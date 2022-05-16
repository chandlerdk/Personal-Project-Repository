#This program will use Clock-in/Clock-out data to calculate hours worked for employeess
#This is a comment
#Program will be called CICObot
print('Hello')
print()
print("I am CICObot. I will be calculating employee's hours")
print()

def main ():
    outfile = open('employee_data.txt', 'w')
    month = input('Please enter the name of the month we will be working with: ')
    week_start = int(input('Enter start day of shift week: '))
    week_end = int(input('Enter end date of the shift week: '))
    number_of_employees = int(input("How many employee's used time cards this week?: "))
    for employees in range (0,number_of_employees):
        get_name = str(input("Employee name: "))
        punch_count = int(input('How many punches did the employee have this week?: '))
        total = 0
        for CICO in range (0,punch_count,2):
            CO_request = float(input('Enter Clock out punch: '))
            CI_request = float(input('Enter Clock in punch: '))
            time_worked = (CO_request - CI_request)
            total = total + time_worked
            round_total= "{:.2f}".format(total)
        print('--------------------------------')
        print(get_name,' worked a total of ',round_total,' hours this week.')
        outfile.write(get_name)
        outfile.write('\t')
        outfile.write(round_total)
        outfile.write('\n')
        print('--------------------------------')
    outfile.close()
    print('---------------------')
    outfile = open('employee_data.txt', 'r')
    for  line in outfile:
        print(line)
        print()

main()
                              
