def bubble(list):
  for i in range(len(list) - 1, 0, -1):
    no_swap = True
    for k in range(0, i):
      if list[k + 1] < list[k]:
        list[k], list[k + 1] = list[k + 1], list[k]
        no_swap = False
    if no_swap:
      return

list = input('Enter the list of numbers: ').split()
list = [int(x) for x in list]
bubble(list)
print('Sorted list: ', end='')
print(list)
