from collections import Counter
import re

# Read the text file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Clean and Tokenize the text
cleaned_text: str = re.sub(r"[^\w\s]", "", text.lower().split())

# Use Counter() to count the words
word_counts: Counter = Counter(cleaned_text)

# Printing second highest most common word
most_commmon = counter.most_common(
    2
)  # passed in Number will denotes how many common numbers we want (counting starts from 1-n)
print(
    "Second Most Common Word is: ", most_commmon[0]
)  # print in zeroth index element from 2 most common ones

"""
# Output:
Second Most Common Number is: ('data', 82)
"""
