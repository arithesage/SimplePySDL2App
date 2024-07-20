from os.path import isfile as file_exists
from os.path import join as make_path




def print_va (text: str, *variables) -> None:
    """
    Prints a message, replacing placeholders with the provided variables if any.
    This variant expects an array as the 'variables' object.
    Include place holders like '$[0]', '$[1]', etc. in text.
    Each one corresponds to an index of the 'variables' array.
    """    
    if (text != None):
        if (variables != None):
            if (len (variables) == 1) and type_of (variables[0], tuple):
                variables = variables[0]
            
            var_count = len (variables)
        
            for v in range (0, var_count):
                vPlaceHolder = ("$[" + str(v) + "]")

                if vPlaceHolder in text:
                    text = text.replace (vPlaceHolder, variables[v])

        print (text)


def str_empty (string: str) -> bool:
    """
    Returns True only if the given string isn't None OR EMPTY
    """
    return (string == None) or (string == "")


def type_of (variable: str, variable_type) -> bool:
    """
    Alias for 'isinstance'.
    Returns if a variable is of the given type.
    """
    return isinstance (variable, variable_type)

