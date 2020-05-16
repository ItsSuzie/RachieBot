def to_weird_case(weirdStr):
    upper = True
    weridCase = ""
    for i in weirdStr:
        if i == " ":
            weridCase += " "
            upper = True
            continue
        elif upper:
            weridCase += i.upper()
            upper = False
        else:
            weridCase += i.lower()
            upper = True
        
    return weridCase

# myStr = input("Enter a string to make weird case: ")
# print("\n\n" + to_weird_case(myStr))

