L = input("\033[34mВведите\033[35m\033[1m целые числа через пробел: \033[0;0m")
try:
    L_mod = list(map(int, L.split()))
except ValueError:
    print("\033[31m\033[1mВы ввели не целое число,начните сначала.\033[0;0m")
    quit()
L_mod = list(map(int, L.split()))
print(("\033[32mВсе нормально.Ваш список чисел:\033[0;0m"), (L_mod))
try:
    n = input("\033[34mВведите\033[35m\033[1m целое число:\033[0;0m ")
    num = int(n)
    print("\033[32mВсе нормально. Вы ввели число:\033[0;0m", num)
except ValueError:
    print("\033[31m\033[1mВы ввели не целое число,начните сначала.\033[0;0m")
    quit()
L_mod.append(num)
L_mod.sort()
print(("\033[33mВаш отсортированный список:\033[0;0m"),(L_mod))
def binary_search(L_mod,num,left,right):
    if left>right:
        return False
    middle = (right+left)//2
    if L_mod[middle] == num:
        return middle
    elif num < L_mod[middle]:
        return binary_search(L_mod, num, left, middle-1)
    else:
        return binary_search(L_mod, num, middle+1, right)
print(("\033[33mИндексы вашего числа из списка,\033[35m\033[1mсогласно условиям задачи практики:\033[0;0m "),
      (binary_search(L_mod, num, 0, len(L_mod))-1),
      (binary_search(L_mod, num, 0, len(L_mod))))
