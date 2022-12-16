f = open('jj.txt','r')
content = f.read()

# print(content)

# def pp(x):
#     for i in x:
#         print(i)
#     return

'''now trying pandas instead'''
import pandas as pd
data = pd.read_csv('jj.txt', sep=" ", header=None)
