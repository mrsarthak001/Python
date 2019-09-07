l1=[1, 3, 5, 7]
l2=[2, 4, 6, 8]

def avg_finder(l1,l2):
    avg=[]
    for pair in zip(l1,l2):
        avg.append(sum(pair)/len(pair))
    return avg
print(avg_finder(l1,l2))


# multiple list
#
# def avg_finder(*args):
#     avg=[]
#     for pair in zip(*args):
#         avg.append(sum(pair)/len(pair))
#     return avg
# print(avg_finder([1, 3, 5, 7],[2, 4, 6, 8],[3,4,5,6],[5,6,7,8] ))
#
# # with the lambda
#
# avg_fin = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
# print(avg_fin([1, 3, 5, 7],[2, 4, 6, 8],[3,4,5,6],[5,6,7,8] ))