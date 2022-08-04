# cAPS lOCK
str = str(input())
str_copy = str
if str == str_copy.upper():
    print(str.lower())
else:
    arr = list(str)
    if arr[0].lower() == arr[0]:
        asd = ""
        for i in range(1,len(arr)):
            asd+=arr[i]
        if asd == asd.upper():
            print(arr[0].upper()+asd.lower())
        else:
            print(str)
    else:
        print(str)

            


