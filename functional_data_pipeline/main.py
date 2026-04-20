def debug_logger(func):

    def wrapper(data):
        print(f"Executing function: {func.__name__}")

        result = func(data)
        print(f"Result: {result}")

        return result
    
    return wrapper

@debug_logger
def trim_whitespace(data):
    return data.strip()

@debug_logger
def to_lowercase(data):
    return data.lower()

def remove_character(char_to_remove):

    def inner_func(data):
        return data.replace(char_to_remove, "")

    return inner_func

@debug_logger
def replace_with_dashes(data):
    split = data.split(" ")
    return "-".join(split)

def recursive_pipeline(data, funcs):
    if len(funcs) == 0:
        return data
    
    active_func = funcs[0](data)
    
    return recursive_pipeline(active_func, funcs[1:])

def main():

    function_list = [
        trim_whitespace,
        to_lowercase,
        remove_character("a"),
        remove_character("e"),
        replace_with_dashes
    ]


    test_data = "   This sentence has useless whitespace to be removed     "
    test_data2 = "THis SenTEnce neeDs TO BE All loweRCAse"
    test_data3 = "This sentence needs to change whitespace between to dashes"

    print(recursive_pipeline(test_data, function_list))



if __name__ == "__main__":
    main()