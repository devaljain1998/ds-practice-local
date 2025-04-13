from collections import deque

def is_valid_parenthesis(s: str) -> bool:
	open_parenthesis_map = {
		"{": "}",
		"(": ")",
		"[": "]",
	}
	closed_parenthesis_map = {
		"}": "{",
		")": "(",
		"]": "[",	
	}

	stack: deque[str] = deque()

	if s[0] in open_parenthesis_map:
		stack.append(s[0])
	else:
		return False

	for i in range(1, len(s)):
		char = s[i]

		# If it is an open parenthesis then push it to stack
		if char in open_parenthesis_map:
			stack.append(char)

		# Check if it is reverse parenthesis then is it opposite
		# to the open parenthesis, then pop it from the stack
		elif stack[-1] == closed_parenthesis_map[char]:
			stack.pop()

		# If none of these then push it to the stack
		else:
			stack.append(char)

	return len(stack) == 0

print(is_valid_parenthesis("(){}[]"))
