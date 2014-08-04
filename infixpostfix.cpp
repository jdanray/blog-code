#include <string>
#include <stack>

//Returns true if the string is a digit
bool isOperand(string token)
{
       return token == "0" ||
              token == "1" ||
              token == "2" ||
              token == "3" ||
              token == "4" ||
              token == "5" ||
              token == "6" ||
              token == "7" ||
              token == "8" ||
              token == "9";
}

//Returns true if the string is "*", "/", "+", or "-"
bool isOperator(string token)
{
	return token == "*" ||
               token == "/" ||
               token == "+" ||
               token == "-";
}

//Returns true if the second operator has the same or greater precedence than the first
bool hasPrecedence(string operator1, string operator2)
{
	if (operator2 == "(" || operator2 == ")")
		return false;
	else if ((operator1 == "*" || operator1 == "/") && (operator2 == "+" || operator2 == "-"))
		return false;
	else
        	return true;
}

//Applies an operation to two operands
int executeOperation(string operation, int operand1, int operand2)
{
	if (operation == "*")
		return operand1 * operand2;
	else if (operation == "/")
		return operand1 / operand2;
	else if (operation == "+")
		return operand1 + operand2;
	else if (operation == "-")
        	return operand1 - operand2;
}

/* Scans the expression from left to right
 * If a token is:
 * An operand:	Push it onto the stack
 * An operator:	1. Pop the stack twice
 *		2. Apply the operation to the two operands
 *		3. Push the result onto the stack
 * The stack should be empty except for the result of all the operations
 * Returns the top of the stack
 */
int evaluatePostfix(string expression)
{
   string	  token;
   stack<int> stack;
   int		  operand1;
   int		  operand2;

	for (unsigned int i = 0; i < expression.length(); i++) {
		token = expression.substr(i, 1);
        	if (isOperand(token))
			stack.push(atoi(token.c_str()));
     		else if (isOperator(token)) {
           		operand2 = stack.top(); stack.pop();
           		operand1 = stack.top(); stack.pop();
           		stack.push(executeOperation(token, operand1, operand2));
	 	}
   	}
	return stack.top();
}

/* Scans the expression from left to right
 * If a token is:
 * An operand:			Append it to the postfix expression
 * An operator:			1. While the stack is not empty and the top of the stack
 *				has the same or greater precedence than the token, 
 *				append the top of the stack to the postfix expression
 *				2. Push the token onto the stack
 * A left parenthesis:		Push it onto the stack
 * A right parenthesis:		While the top of the stack is not a left parenthesis, 
 *				append the top of the stack to the postfix expression
 * While the stack is unempty, append the top of the stack to the postfix expression.
 * Returns the postfix expression.
 */
string infixToPostfix(string infix)
{
	string        postfix;
    	string	      token;
	stack<string> stack;

	for (unsigned int i = 0; i < infix.length(); i++) {
		token = infix.substr(i, 1);
		if (token == "(")
            		stack.push(token);
        	else if (token == ")") {
			while (stack.top() != "(") {
				postfix.append(stack.top());
                		postfix.append(" ");
        			 stack.pop();
            		}
            		stack.pop(); //Throw the left parenthesis away
		} else if (isOperand(token)) {
			postfix.append(token);
            		postfix.append(" ");
		} else if (isOperator(token)) {
			while (!stack.empty() && hasPrecedence(token, stack.top())) {
				postfix.append(stack.top());
                		postfix.append(" ");
				stack.pop();
			}
			stack.push(token);
		}
	}

	//Append the rest of the operators to the postfix expression
	while (!stack.empty()) {
		postfix.append(stack.top());
        	postfix.append(" ");
		stack.pop();
	}
	
	return postfix;
}
