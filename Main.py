# The algorithm only works if the root
#
#


def polynomial_display(args):
    result = ""
    degree = int(len(args))-1
    print(len(args))
    if len(args) < 3:
        raise ValueError("You did not enter a polynomial.")
    #this is seriously hardcore spaghetti code
    for index, i in enumerate(args):
        if index == 0:
                result = result + "{}x^{} ".format(i, degree)
        elif i > 0:
            if degree == 1:
                result += "+ {}x ".format(i, degree)
            elif degree != 0:
                result = result + "+ {}x^{} ".format(i, degree)
            else:
                result = result + "+ {}".format(i)
                break
        else:
            if degree == 1:
                result += "{}x ".format(i, degree)
            elif degree != 0:
                result = result + "{}x^{} ".format(i, degree)
            else:
                result = result + "{}".format(i)
                break
        degree -= 1
    return result


def evaluate(x_value, *args):
    """
           Usage:

           Works for any number of x

           f(x_value) = arg[0]x^3 + arg[1]x^2 + arg[2]x + arg[3] ...
    """
    array = []
    degree = int(len(args))-1
    for i, arg in enumerate(args):
        array.append(int(arg*(x_value**(degree-i))))
    answer = sum(array)
    return answer


def roots(start_range, end_range, *coefficients):
    while True:
        print(start_range)
        print(end_range)
        left_response = evaluate(start_range, *coefficients)
        left_range = start_range

        right_response = evaluate(end_range, *coefficients)
        right_range = end_range
        print("left response: {}".format(left_response))
        print("right response: {}".format(right_response))
        if left_response > 0:
            left_positive = True
        else:
            left_positive = False

        if right_response > 0:
            right_positive = True
        else:
            right_positive = False

        if (right_positive and left_positive) or (not right_positive and not left_positive):
            if start_range > end_range:
                return print("No roots were found within the interval.")
            start_range += 1
            continue
        else:
            break

    midpoint = (left_range + right_range)/2.0
    midpoint_eval = evaluate(midpoint, *coefficients)

    print("midpoint: " + str(midpoint))
    if midpoint_eval <= 0:
        answer = midpoint
        left_range = midpoint
        if digits(answer) < 13:
            return roots(left_range, right_range, *coefficients)

    else:
        answer = midpoint
        right_range = midpoint
        if digits(answer) < 13:
            return roots(left_range, right_range, *coefficients)
    return answer


def digits(n):
    # returns the number of decimal points in a float.
    #TODO: this only works up to 14 decimals where str representation of long flots automatically turn into sci. notation
    #TODO: either dive deeper into spaghetti code and parse the string of the sci. notation and turn it into a str representation AGAIN
    #TODO: or find another way to display decimal points.
    strn = str(n)
    decimals = strn.split('.')[1]

    return len(decimals)


if __name__ == '__main__':
    while True:
        try:
            left_interval = int(input("[x1, x2]: Enter the x1 value for the interval you want to check."))
            break
        except ValueError:
            print("Input must be an integer.")

    while True:
        try:
            right_interval = int(input("[" + str(left_interval) + ", x2]: Enter the x2 value you want to check."))
            if right_interval < left_interval:
                print("Rightbound interval may not be smaller than leftbound.")
            else:
                break
        except ValueError:
            print("Input must be an integer.")
    print("[" + str(left_interval) + "," + str(right_interval) +"]")
    while True:
        try:
            coefficients = (input("Enter the coefficients of the polynomial ranging from leading to constant.(separate with spaces, if there's no constant, add 0)"))
            break
        except ValueError:
            print("Input must be an integer.")

    #split joins strings, we want int
    coefficientsx = list(map(int, coefficients.split()))

    print("Checking for roots in {} within [{},{}] up to 13 decimal points \nbecause after 13 it converts to scientific"
          " notation which fucks up my\nfunction for checking decimal points.\n".format(polynomial_display(coefficientsx), left_interval, right_interval))
    print("x = " + str(roots(left_interval, right_interval, *coefficientsx)))
