def getMin(num_list):
    return min(num_list)


def getMax(num_list):
    return max(num_list)


def getSum(num_list):
    return sum(num_list)

def sortAscending(num_list):
    num_list.sort()
    return num_list

def setDescending(num_list):
    num_list.sort(reverse=True)
    return num_list


def get3min3Max(num_list):
    num_list.sort()
    x = num_list[0:3]
    y = num_list[-3:]
    return  x + y


def remove_dupicates(num_list):
    return list(set(num_list))