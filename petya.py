
def compare(first_string,second_string):
    for index in range(len(first_string)):
        if first_string[index]>second_string[index]:
            return 1
        if first_string[index]<second_string[index]:
            return -1
    return 0
# take input 
first_string=input().upper()
second_string=input().upper()
print(compare(first_string,second_string))

