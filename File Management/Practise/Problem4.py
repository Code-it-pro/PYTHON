# Removing repeated texts
# importing re Module with a powerfull finding and replacing tools
import re 

word = "donkey"

with open("some_texts.txt") as file:
    texts = file.read()
    print(texts+"\n")

new_texts = re.sub(word , "#####", texts , flags=re.IGNORECASE)

with open("some_texts.txt" , "w") as file:
    file.write(new_texts)

print(new_texts)

#  New "re" Module is Python’s built-in library for regular expressions. 

# Useful re functions in Python

# o. re.compile(pattern, flags=0) — create a compiled regex object
# o. re.search(pattern, string, flags=0) — find first match anywhere
# o. re.match(pattern, string, flags=0) — match at the start only
# o. re.fullmatch(pattern, string, flags=0) — match the entire string
# o. re.findall(pattern, string, flags=0) — return a list of all matches
# o. re.finditer(pattern, string, flags=0) — return an iterator of match objects
# o. re.sub(pattern, repl, string, count=0, flags=0) — replace matches
# o. re.subn(pattern, repl, string, count=0, flags=0) — replace matches and return (new_string, num_subs)
# o. re.split(pattern, string, maxsplit=0, flags=0) — split string by pattern
# o. re.escape(pattern) — escape special regex characters in a literal string

#  Useful compiled-pattern methods
#  If you use re.compile(...), the returned object has the same methods:

# 0. pattern.search(text)
# 0. pattern.match(text)
# 0. pattern.fullmatch(text)
# 0. pattern.findall(text)
# 0. pattern.finditer(text)
# 0. pattern.sub(repl, text)
# 0. pattern.subn(repl, text)
# 0. pattern.split(text)

# Common flags

# o. re.IGNORECASE or re.I — case-insensitive matching
# o. re.MULTILINE or re.M — ^ and $ match line boundaries
# o. re.DOTALL or re.S — . matches newline too
# o. re.VERBOSE or re.X — allow whitespace/comments in pattern