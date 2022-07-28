str = str(input())
str_low = str.lower()
arr = list(str_low)
for i in arr:
    if i!='a' and i!="o" and i!="y" and i!="u" and i!="e"  and i!="i":
        print("."+i, end="")

    