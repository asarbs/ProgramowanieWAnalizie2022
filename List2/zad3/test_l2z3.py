from l2z3 import *

num_list = [88, 19, 13, 44, 53, 59, 87, 41, 8, 29, 95, 42, 50, 85, 43, 78, 17, 24, 52, 28, 31, 56, 68, 80, 46]


def test_getMinMax():
    assert getMin(num_list) == 8
    assert getMax(num_list) == 95

def test_getSum():
    assert getSum(num_list) == 1236

def test_sort():
    res_ascending = [8, 13, 17, 19, 24, 28, 29, 31, 41, 42, 43, 44, 46, 50, 52, 53, 56, 59, 68, 78, 80, 85, 87, 88, 95]
    res_descending = [95, 88, 87, 85, 80, 78, 68, 59, 56, 53, 52, 50, 46, 44, 43, 42, 41, 31, 29, 28, 24, 19, 17, 13, 8]
    assert sortAscending(num_list) == res_ascending
    assert setDescending(num_list) == res_descending


def test_get3min3Max():
    res = get3min3Max(num_list)
    assert res == [8, 13, 17, 87, 88, 95]

def test_remove_dupicates():
    res = remove_dupicates(num_list)
    assert res == [8, 13, 17, 19, 24, 28, 29, 31, 41, 42, 43, 44, 46, 50, 52, 53, 56, 59, 68, 78, 80, 85, 87, 88, 95]