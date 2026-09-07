def safe_print_list(my_list=[], x=0):
    result = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            result = i + 1
        except IndexError:
            break

    print("")
    return result
