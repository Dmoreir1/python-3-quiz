from ValidationException import ValidationException

def validate_file(file_path):
    file = open(file_path, 'r')
    list = []
    for user in users:
        numbers = [0,1,2,3,4,5,6,7,8,9]
    with open("users.txt", 'r') as file:
    for line in file:
        user_data = line.strip().split(',')
        print(line)
        if numbers in user_data:
            raise ValidationException(f"Invalid User Name: {user} ")
        # else:
        #     print("true")

    #     if char in numbers:
    #     print("false")

    # for user, line in enumerate(file):
    #     if user.isnumeric():
    #         # line_values = line.split(',')
    #         try:
    #             int(line_values[1])
    #         except:
    #             raise ValidationException (f"Invalid User Name: {line_values[1]}")

    # try:
    #
    # except:
    #     raise ValidationException(f"Invalid first name: {user} ")



    file.close()

def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)

test()
