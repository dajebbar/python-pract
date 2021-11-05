from cats_name import names
from functions import *

# Avoid double names and check if length is adequate to 100
cat_names = list(set(names))
# print(len(cat_names))


# Adding 0 hat to all my cats
my_cats = {k: 0 for k in cat_names}
# print(my_cats)


# Adding hats to all cats
add_hat(my_cats)


# Adding hats only to pair cats
check_odd_cat(my_cats)


# Adding hats only to odd cats
check_3_cat(my_cats)

cnt = 0
res_hat = []
for k, v in my_cats.items():
    if v == 1:
        cnt += 1
        res_hat.append(k)
print(f"{cnt} cats with hats")
print(res_hat)

# print(my_cats)
