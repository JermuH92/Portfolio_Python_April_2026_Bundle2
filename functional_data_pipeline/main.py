
########### Decorator ###########
# receives a second function, it's task is to wrap the function and add new features to it.
# In this case prints without changing the original code.

def debug_logger(func):

    def wrapper(data):
        print(f"Executing function: {func.__name__}") # Before execution

        result = func(data) # Execute second function
        print(f"Result: {result}") # Result after execution

        return result
    
    return wrapper

@debug_logger # drives "trim_whitespace through the logger at the top"
def trim_whitespace(data):
    return data.strip()

@debug_logger
def to_lowercase(data):
    return data.lower()

########### CURRYING and CLOSURE ###########

def remove_character(char_to_remove):
    # Higher order function. Doesn't handle data directly.
    # It receives a character, "remembers" it and returns
    # new function (inner_func), that does the work.
    # This makes it possible to create dynamic functions in to a list.
    def inner_func(data):
        return data.replace(char_to_remove, "")

    return inner_func

@debug_logger
def replace_with_dashes(data):
    split = data.split(" ")
    return "-".join(split)

########### RECURSIVE PIPELINE ###########

def recursive_pipeline(data, funcs):
    # Base case
    if len(funcs) == 0:
        return data
    
    # Grab first function in a list and run data through it.
    active_func = funcs[0](data)

    # Recursion: calls itself again, new data is the result of the
    # previous function and give the remainder list of the functions list.
    return recursive_pipeline(active_func, funcs[1:])

def main():

    # Listed First-Class Functions

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

    # Run data through the recursive pipe
    print(recursive_pipeline(test_data, function_list))



if __name__ == "__main__":
    main()