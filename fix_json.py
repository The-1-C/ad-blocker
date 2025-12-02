
file_path = 'c:/Users/Kaden/Desktop/Projects/ad-blocker/rules.json'

with open(file_path, 'r') as f:
    content = f.read().strip()

# Fix the trailing comma issue
if content.endswith(",\n]"):
    content = content[:-3] + "\n]"
elif content.endswith(",]"):
    content = content[:-2] + "]"
# Also check for just trailing comma if I appended ']' with echo and there was a newline
elif content.endswith("}, \n]"): # Handle potentially weird spacing
     content = content.replace("}, \n]", "}\n]")
elif "},\n]" in content: # Standard case if I just appended ]
    # Find the last occurrence
    last_comma_idx = content.rfind(",")
    last_bracket_idx = content.rfind("]")
    if last_comma_idx < last_bracket_idx:
        # Replace the last comma with empty string
        content = content[:last_comma_idx] + content[last_comma_idx+1:]

with open(file_path, 'w') as f:
    f.write(content)

print("Fixed")
