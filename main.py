import sys
        
#Input = <User Input>
#Output = '3 Apples, 4 Pears'
#Desc: Accepts user input from the console and creates a combined string
def get_input_helper():
    this_input = input()
    if this_input != 'q' and this_input != 'Q':
        if ' ' not in this_input: #Will not accept input if there are not 2 arguments per item
            print('Please enter both a quantity and item name separated by \' \'.')
            return get_input_helper()
        elif this_input.split(' ')[0].isnumeric() == False: #Will not accept input if first argument is not numeric
            print('Please enter a valid number for quantity.')
            return get_input_helper()
        else:
            return this_input + ',' + get_input_helper()
    return ''

#Input = None
#Output = ['3 Apples, 4 Pears']
#Desc: Driver function for manual input function
def get_input_manual():
    print("Enter inventory item (<Quantity> <Name>) or (\"Q\" to quit):")
    return get_input_helper().split(',')[:-1]

#Input = ['3', 'Apples', '4', 'Pears']
#Output = ['3 Apples', '4 Pears']
#Desc: Converts input from command-line args to combined list
def get_input_arg(args):
    end_flag = 0
    i = 0
    final_list = []
    while end_flag != 1:
        j = 1
        if i >= len(args):
            end_flag = 1
        else:
            str = ''
            amt = args[i]
            if args[i].isnumeric() == True: #Each entry must start with the quantity
                while i + j < len(args) and args[i + j].isnumeric() == False:
                    str += args[i + j] + ' '
                    j += 1
                if str.strip() == '': #If there isn't an argument for the item name
                    end_flag = 1
                    print('Name of item cannot be blank.')
                    return []
                final_list.append(amt + ' ' + str.strip())
            else:
                end_flag = 1
                print('Please enter a number for quantity.')
                return []
            i = i + j
    return final_list

#Input = ['3 Apples', '4 Pears']
#Output = {'Apples': 3, 'Pears': 4}
#Desc: Sorts incoming item list, cleans up item names, and converts to dictionary
def inv_management(input_list):
    item_dict = {}
    for item_combo in input_list:
        #Make item names pretty
        name = ' '.join(word[0].upper() + word[1:].lower() for word in item_combo.split(' ', 1)[1].split(' '))
        amt = int(item_combo.split(' ')[0])
        if name not in item_dict: #If the name hasn't appeared in the dictionary yet, create a new entry
            item_dict[name] = amt
        else: #Otherwise, update the existing entry's count
            item_dict[name] += amt
    #Alphabetically sort the dictionary by key value
    sorted_item_dict = dict(sorted(item_dict.items(), key=lambda x: x[0]))
    return sorted_item_dict

#Input = {'Apples': 3, 'Pears': 4}
#Output = <Ascii data table>
#Desc: Creates an inventory table based on item names and quantities
def print_inv(input_dict):
    max_name_len = len(max(input_dict.keys(), key=len)) + 2
    max_quantity_len = 5
    #Print header row
    print('Item'.ljust(max_name_len) + '|'.ljust(max_quantity_len) + 'Quantity')
    #Print dividing line
    for i in range(0, max_name_len + max_quantity_len + 12):
        print('-', end = '')
    print()
    #Print item name followed by quantity
    for key in input_dict.keys():
        print(key.ljust(max_name_len) + '|'.ljust(max_quantity_len) + str(input_dict[key]))
    for i in range(0, max_name_len + max_quantity_len + 12):
        print('-', end = '')
    print()
    #print total quantity for all items
    print('Total'.ljust(max_name_len) + '|'.ljust(max_quantity_len) + str(sum(input_dict.values())))
    
def main():
    if len(sys.argv) > 1: #If there are any command-line arguments, get input from there
        print_inv(inv_management(get_input_arg(sys.argv[1:])))
    else: #Otherwise, read input directly from user
        print_inv(inv_management(get_input_manual()))

if __name__ == "__main__":
    main()
