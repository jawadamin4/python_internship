import re

#  Searching for a pattern in a string
text = 'The quick brown fox jumps over the lazy dog.'
pattern = r'brown'

if re.search(pattern, text):
    print('Pattern found!')
else:
    print('Pattern not found.')

#  Extracting specific information using capturing groups
# ---------------------------------------------------------
text = 'Email: john@example.com'
pattern = r'Email: (\S+)'

match = re.search(pattern, text)
if match:
    email = match.group(1)
    print('Email:', email)

# Replacing patterns in a string
# ---------------------------------------------------------
text = 'Hello, World!'
pattern = r'Hello'

new_text = re.sub(pattern, 'Hi', text)
print(new_text)

#  Splitting a string based on a pattern
# ---------------------------------------------------------
text = 'apple,banana,orange'
pattern = r','
items = re.split(pattern, text)
print(items)
