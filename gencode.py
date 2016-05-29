from types import MethodType, FunctionType

def gencode(namespace, classname, *args):

    # Create a blank class of name `classname`
    class_definition = "global " + classname + "\nclass " + classname + "(object):\n  pass"
    compiled_class_definition = compile(class_definition, '<string>', 'exec')
    exec(compiled_class_definition)
    defined_class = eval(classname)

    # Add each of the required methods
    for method in args:
        if type(method) is FunctionType:
            add_method = classname + "." + method.__name__ + " = method"
            compiled_method_addition = compile(add_method, '<string>', 'exec')
            exec(compiled_method_addition)

    namespace[classname] = defined_class
