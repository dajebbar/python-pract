def least_occurence(str):
    least = {}
    res = []
    max = []
    for i in str:
        least[i] = str.count(i)
    
    for k, v in least.copy().items():
        if v == 1:
            res.append(k)
        else:
            max.append(k)

    return res, max



str = "Least Frequent Character in String"
print(least_occurence(str))