import pandas as pd

from pandas import DataFrame as f

c = pd.read_csv('emp.csv')

ef1 = f(c)

ef1

a = ef1['ephno']

ef2 = f(a)

ef1 = ef1[['ename','eno','edesig','esalary']]


ef1
