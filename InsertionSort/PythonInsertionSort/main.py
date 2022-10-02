array = [11, 4, 7, 6, 12, 9]
print(array)

for i in range(1, len(array)):
    key = array[i]
    j = i-1
    while key < array[j] and j >= 0:
        array[j+1] = array[j]
        j -= 1
    array[j+1] = key
print(array)

# swap insert Sort/не дублируем ключ в тоже место, но больше тратим на swap
# buf = 0
# for i in range(len(array)):
#     # key = array[i+1]
#     for j in reversed(range(0, i)):
#         if array[j] > array[j + 1]:
#             buf = array[j + 1]
#             array[j + 1] = array[j]
#             array[j] = buf
#         else:
#             break







