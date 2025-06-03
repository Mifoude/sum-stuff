import time
import string
letters = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.whitespace)

text ="May is coming to an end, so... may you leave?"

cur_str=""

while cur_str != text:
    for i in letters:
        print(cur_str + i)
        time.sleep(0.08)

        if cur_str + i == text[:len(cur_str + i)]:
            cur_str += i
            break