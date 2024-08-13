def all_variants(text):
    res = ''
    for i in range(len(text)):
        for k in range(i, len(text)):
            res = text[i:k+1]
            yield res


a = all_variants("abc")
print(a)
for i in a:
    print(i)
