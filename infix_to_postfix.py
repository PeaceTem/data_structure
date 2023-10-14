# This code contains a class to convert Infix expressions to postfix expression

# Associativity
class LR:
    name = "Left-to-Right"

class RL:
    name = "Right-to-Left"

class NN:
    name = "Null"



# The Stack Data Structure
class Stack:
    def __init__(self):
        self.content = ""
        self.size = 30

    def __str__(self):
        return f"{self.content}"
    

    def push(self, data: str) -> None:
        self.content += data

    def pop(self) -> str:
        last_element = self.content[-1]
        self.content = self.content[:len(self.content) - 1]
        return last_element

    def peek(self) -> str:
        return self.content[-1]
    
    def isEmpty(self) -> bool:
        if len(self.content) > 0:
            return False
        
        return True
    
    def isFull(self) -> bool:
        if len(self.content) >= self.size:
            return True
        
        return False




class Infix:
    operators = {
        # operator : (Associativity, Precedence)
        "(": (NN, None),
        ")": (NN, None),
        "^": (RL, 3),
        "/": (LR, 2),
        "*": (LR, 2),
        "+": (LR, 1),
        "-": (LR, 1),
        ";": (NN, None), # end of expression
    }

    @classmethod
    def convert_to_postfix(cls, infix_exp: str) -> str:
        postfix_exp = ""
        stack = Stack(); #try to use a normal stack

        for char in infix_exp:
            if char not in cls.operators.keys():
                postfix_exp += char

            else:
                if char == "(":
                    stack.push(char)

                elif char == ")":
                    # pop the data of the stack until it reaches ( and pop ( too
                    while stack.peek() != "(" and not stack.isEmpty():
                        postfix_exp += stack.pop()
                    if stack.peek() == "(":
                        stack.pop()

                # when it reaches the end of the string
                elif char == ";":
                    while not stack.isEmpty():
                        postfix_exp += stack.pop()

                else:
                    # push operator to the stack if empty or the top is (
                    if stack.isEmpty() or stack.peek() == "(":
                        stack.push(char)
                    
                    # for left to right associativity
                    elif cls.operators[stack.peek()][0] == LR:
                        
                        if cls.operators[stack.peek()][1] < cls.operators[char][1]:
                            stack.push(char)

                        elif cls.operators[stack.peek()][1] >= cls.operators[char][1]:
                            while not stack.isEmpty() and cls.operators[stack.peek()][1] >= cls.operators[char][1]:
                                postfix_exp += stack.pop()
                            stack.push(char)

                    # for left to right associativity
                    elif cls.operators[stack.peek()][0] == RL:
                        if cls.operators[stack.peek()][1] >= cls.operators[char][1]:
                            stack.push(char)

                        elif cls.operators[stack.peek()][1] < cls.operators[char][1]:
                            while not stack.isEmpty() and cls.operators[stack.peek()][1] < cls.operators[char][1]:
                                postfix_exp += stack.pop()
                            stack.push(char)

                    
                    else:
                        print("An error has occurred!")
                        break


            print(char, "|", stack, "|", postfix_exp)
        

        return postfix_exp



# print(Infix.convert_to_postfix("A+B;"))
# print(Infix.convert_to_postfix("A*B-C;"))
print(Infix.convert_to_postfix("K+L-M*N+(O^P)*W/U/V*T+Q;"))
                    
                        


