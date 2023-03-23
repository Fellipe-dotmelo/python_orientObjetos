def empty(s):
    if len(s) == 0:
        return True;

    else:
        return False;


def pop(s):
    temp=s[0]
    s.remove(s[0])
    return temp


stack = ['calça, meias, paletó, gravata, camisa']

if not empty(stack):
    print(pop(stack))

else:
    print('Pilha vazia')

