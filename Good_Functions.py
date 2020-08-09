# ------------------- Time ---------------------------
import time
start_time = time.time()
print(time.time())
# DO Something

print("%s" % (time.time()-start_time))

# ---------------------------------------------------
# ------------------ Enumarate ----------------------

my_list = ['January', 'February', 'March', 'April']
for index, value in enumerate(my_list):
    print(index, value)
# --- Or ---
print()
for index, value in enumerate(my_list, 1):
    print(index, value)

# ---------------------------------------------------
# ------------- İterate Dictionary ------------------
print()
dct={'bir': 1, 'iki': 2, 'dört': 4, 'beş': 5, 'üç': 3}
for key,value in dict.items(dct):
    print(key, value)