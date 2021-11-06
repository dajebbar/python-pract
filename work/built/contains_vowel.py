def check_vowels(str):
    is_vowel = False
    vowels = "AEUOIaeuoi"
    vowel_lst = {}
    lst = []
    for i in str:
        if i in vowels:
            vowel_lst[i] = str.count(i)

    for k in vowel_lst.keys():
        lst.append(k.lower())
    
    if len(set(lst)) >= 5:
        is_vowel = True
        return "All vowels are present"

    return f"Not Accepted! All vowels except '{set(lst)}' are not present"


# str = "ABeeIghiObhkUul"
str = 'geeksforgeeks'
print(check_vowels(str))
