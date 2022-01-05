def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]

lista = remove_repetidos(lista)
print (lista)

# Outro modo
# myList = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]
#
# resultantList = []
#
# for element in myList:
#     if element not in resultantList:
#         resultantList.append(element)
#
# print(resultantList)
# Resultado:
#
# [2, 1, 3, 0, 6, 7, 4, 8]

# Outro modo
# original_list = [80, 10, 50, 18, 3, 50, 8, 18, 9, 8]
#
# print("Original List is: ",original_list)
#
# convert_list_to_set = set(original_list)
# print("Set is: ",convert_list_to_set)
#
# new_list = list(convert_list_to_set)
# print("Resultant List is: ",new_list)
#
# original_list = list(convert_list_to_set)
# print("Removed duplicates from original list: ",original_list)
#
# from collections import OrderedDict
#
# myList = [2, 1, 2, 3, 0, 6, 7, 6, 8, 0, 4, 8]
#
# final_list = list(OrderedDict.fromkeys(myList))
#
# print(final_list)
# Resultado:
#
# [2, 1, 3, 0, 6, 7, 8, 4]
