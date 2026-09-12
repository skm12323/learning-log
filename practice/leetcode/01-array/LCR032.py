# 有效的字母异位词
s = "anagram"
t = "nagaram"
fs = {}
ft = {}
for word in s:
    fs[word] = fs.get(word, 0) + 1
for word in t:
    ft[word] = ft.get(word, 0) + 1

if fs == ft and s != t:
    print("true")
else:
    print("false")