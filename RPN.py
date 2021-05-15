#from binarytree import Node
import re

class Stack:
  def __init__(self, maxN=None):
    self.maxN = maxN
    self.stack = []

  def isFull(self):
    if len(self.stack) == self.maxN: return True
    return False

  def isEmpty(self):
    if len(self.stack) == 0: return True
    return False

  def pop(self):
    if len(self.stack) == 0: return False
    return self.stack.pop()
  
  def push(self, data):
    if self.isFull(): return False
    self.stack.append(data)

  def peek(self):
    if len(self.stack) == 0: return None
    return self.stack[len(self.stack)-1]

class RPN:
  def __init__(self, expression, isRPN=False):
    self.operands = "+-/*^%"
    self.expression = expression
    self.isRPN = isRPN

  def convert(self):
    # Split the expression!
    operators = re.split("[-+/*%^]", self.expression)
    operands = re.findall("[-+/*%^]", self.expression)
    for i in range(0, len(operators)):
      if operators[i][0] == "(": operators[i] = operators[i][1:]
      elif operators[i][len(operators[i])-1] == ")":
        operators[i] = operators[i][:len(operators[i])-1]
    operands.reverse()
    expression = [*operators, *operands]
    self.expression = expression
    self.isRPN = True

  def findRPN(self):
    if not self.isRPN:
      self.convert()
    # RPN test
    count = 0
    stack = Stack()
    print(stack.isEmpty())
    while count != len(self.expression):
      # If its an operator
      if self.expression[count] not in self.operands:
        stack.push(int(self.expression[count]))
      else:
        # If its an operand, do the expression and push result
        a = stack.pop()
        b = stack.pop()
        operand = self.expression[count]

        if operand == "+":
          stack.push(a+b)

        elif operand == "-":
          stack.push(a-b)

        elif operand == "/":
          stack.push(a/b)

        elif operand == "^":
          stack.push(a**b)

        elif operand == "%":
          stack.push(a%b)
        
        elif operand == "*":
          stack.push(a*b)

      result = stack.peek()
      count += 1
      
    return result

rpn = RPN("2*(3*3)^2", False)
print(rpn.findRPN())
