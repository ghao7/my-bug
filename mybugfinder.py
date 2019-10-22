import javalang


def is_string(tokens, i, string_set):
    if type(tokens[i]) == javalang.tokenizer.String:
        return True
    if type(tokens[i]) == javalang.tokenizer.Identifier and tokens[i].value in string_set:
        return True
    return False


def is_operator(tokens, i):
    return type(tokens[i]) == javalang.tokenizer.Operator


def parse_file(fname):
    result = list()
    string_set = set()
    with open(fname, 'r') as file:
        data = file.read()
        tokens = list(javalang.tokenizer.tokenize(data))
        for i in range(len(tokens)):
            # print(tokens[i])
            if type(tokens[i]) == javalang.tokenizer.Identifier and tokens[i].value == "String":
                string_set.add(tokens[i+1].value)
            if i < len(tokens) - 2 and is_string(tokens, i, string_set) and is_operator(tokens, i+1)\
                    and is_string(tokens, i + 2, string_set):
                if tokens[i].position[0] != tokens[i+1].position[0] or \
                        tokens[i+1].position[0] != tokens[i + 2].position[0]:
                    continue
                if javalang.tokenizer.Operator.is_infix(tokens[i+1]):
                    result.append(tokens[i+1].position)

    print("There are {} bad string comparison in the program.".format(len(result)))
    print(result)


fname = 'test.java'
parse_file(fname)
