import numexpr as ne

def calc(arg_str):
    return str(ne.evaluate(arg_str))
