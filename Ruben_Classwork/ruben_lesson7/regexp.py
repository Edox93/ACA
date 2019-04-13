import re


texts = [" \t5 6 +", "a 6 +", "     56 6 -", "56 6123 %"]

expr = r"^\s*([0-9]+) ([0-9]+) ([+-/*])"

for text in texts:
    res = re.findall(expr, text)
    if res:
        print(text, res)
