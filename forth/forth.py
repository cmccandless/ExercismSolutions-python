StackUnderflowError = IndexError


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def evaluate(input_data):
    stack = []
    user_defined = {}
    for line in input_data:
        if line.startswith(':'):
            tokens = line.lower().split(' ')[1:-1]
            key = tokens.pop(0)
            if is_integer(key):
                raise ValueError('cannot redefine numbers')
            values = []
            for t in tokens:
                if t in user_defined:
                    values.extend(user_defined[t])
                else:
                    values.append(t)
            user_defined[key] = values
        else:
            tokens = line.split(' ')
            while tokens:
                token = tokens.pop(0).lower()
                if is_integer(token):
                    stack.append(int(token))
                    continue
                if token in user_defined:
                    tokens = user_defined[token] + tokens
                elif token in {'+', '-', '*', '/'}:
                    stack.append(int(eval('{}{}{}'.format(
                        stack.pop(-2), token, stack.pop()
                    ))))
                elif token == 'dup':
                    stack.append(stack[-1])
                elif token == 'drop':
                    stack.pop()
                elif token == 'swap':
                    stack.append(stack.pop(-2))
                elif token == 'over':
                    stack.append(stack[-2])
                else:
                    raise ValueError('unknown word ' + token)
    return stack
