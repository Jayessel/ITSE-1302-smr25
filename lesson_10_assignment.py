import ITSE_1302 as itse

def get_string(message):
    input_string = input(message)
    return input_string.lower()

def find_string(string,message):
    if string in message:
        index = message.find(string)
        return index
    else:
        print('String not found...')
        print()
        index = -1
        return index

def replace_string(string,message):
    replace = get_string(f'Do you want to replace {string} with somthing else (y/n)? ')
    if replace == 'n':
        return
    else:
        replacement = get_string('Enter the replacement string: ')
        new_string = message.replace(string,replacement)
        print(f'New String: {new_string}')
        return new_string

def main():
    index = -1
    print('string replacement tool'.title())
    print('-'*25)
    message = get_string('Enter the string to search through: ')

    while index < 0:
        string = get_string('Enter the string to search for: ')
        print()
        print('Searching for substring...')
        print('-'*25)
        index = find_string(string,message)
  
    print(f'{string} was found in the main string at index {index}')
    print()

    print('string replacement processing'.title())
    print('-'*25)

    new_string = replace_string(string,message)
    print()

    print('Thank you for using my program!')
    itse.jl_sign()
    

if __name__ == "__main__":
    main()