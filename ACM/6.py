columnNumber = int(input())
string = ""
while columnNumber>127:
    k = columnNumber%127
    if k==0:
        columnNumber = columnNumber//127-1
        string += chr(127)
    else:
        columnNumber = columnNumber//127
        string += chr(k)
string += chr(columnNumber)
print( string[::-1])   