# python3
#Leons Jūlijs Strupītis 13. gr. Apl. nr. 221RDB402

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            
            #Pārbauda pirmo iekavu
            opening_brackets_stack.append(Bracket(next, i))         

        if next in ")]}":
            #Pārbauda otro iekavu
            if not opening_brackets_stack:
                return i + 1 
            
            #Ja nesakrīt
            if not are_matching(opening_brackets_stack[-1].char,next):
                opening_brackets_stack.pop()
                return i + 1
            
   
            
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    # Atbildes kods
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
   


if __name__ == "__main__":
    main()
