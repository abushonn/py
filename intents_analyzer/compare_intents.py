import pandas as pd

def file2list(file_name):
    expected_file = open(file_name, "r")
    content = expected_file.read()
    expected_content_list = content.split("\n")
    expected_file.close()
    # print(expected_content_list)

    return expected_content_list

def cmp2lists(list1, list2):
    for (l1, l2) in zip (list1, list2):
        if (l1 == l2):
            #print("OK: " + l1)
            print("OK")
        else:
            #print("NOT_EQUAL: " +  l1 + " : " + l2)
            print("NOT_EQUAL")


expected_list = file2list("expected.txt")
actual_list = file2list("actual.txt")

# cmp2lists(expected_list, actual_list)

# Example
# [Utterance]	[Confidence]	[Actual Intent]	[Expected Intent] [IsEqual]
# [hi i thought that i had already met my deductible so why did i get a bill]	[0.950656176]	[deductible_oop_inquiry]	[deductible_oop_inquiry]	[OK]

df = pd.read_csv('results-94755.csv', delimiter=',')
list_of_lists = [list(row) for row in df.values]
# print(list_of_lists)

def printNotEqual(list):
    for l in list:
        (utter,actual,expected,is_ok) = l[0], l[2], l[3], l[4]
        if is_ok == 'NOT_EQUAL':
            print (utter + ' : ' + actual + ' : ' + expected + ' : ' + is_ok)


printNotEqual(list_of_lists)


