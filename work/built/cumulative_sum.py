# from functools import reduce

lst = [10, 20, 30, 40, 50]
cumul = []
for i in range(len(lst)+1):
    cumul.append(lst[i] + lst[i+1])
    if lst[i+1] == lst[-1]:
        break
print(cumul)
    # print(lst[i] + lst[i+1])
    # if lst[i+1] == lst[-1]:
    #     break


