def print_peak(pyramid_size, line_index):
    print(" " * ((pyramid_size - line_index) - 1), end="")
    print("*" * (line_index + (line_index + 1)))

def print_base(pyramid_size, line_index):
    string_of_stars = (line_index + 1) * "*"
    half_stars = len(string_of_stars)
    print(" " * ((pyramid_size - line_index) - 1), end="")  # blank spaces
    print("*" * (half_stars - 2), end="")
    print_door()
    print("*" * (half_stars - 2))

def print_door():
    print("   ", end="")

def print_pyramid():
    valid_number = False

    while (not valid_number):
        pyramid_size = input(
            "Please enter the requested pyramid size (max of 15): ")

        if (pyramid_size.isnumeric()):
            pyramid_size = int(pyramid_size)

            if ((pyramid_size) < 15) and ((pyramid_size) > 1):
                valid_number = True

                for line_index in range(pyramid_size):

                    if line_index < 2:
                        print_peak(pyramid_size, line_index)

                    elif line_index >= (pyramid_size - 3) and line_index <= pyramid_size:
                        print_base(pyramid_size, line_index)

                    else:
                        print_peak(pyramid_size, line_index)

            else:
                print("Please enter a number between 1 and 15")
                valid_number = False

        else:
            print("Please enter a valid number")
            valid_number = False

print_pyramid()