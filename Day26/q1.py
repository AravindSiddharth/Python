import MySQLdb as db
import pandas as pd
import numpy as np
from sqlalchemy import create_engine as ce
import math


con = db.connect("127.0.0.1",'ai','ai','ai')
result = []



def dataFrame1():
    data1 = pd.read_sql("select * from ai_01__emp",con)
    data2 = pd.read_sql("select * from ai_01__dpt",con)
    result = pd.merge(data1, data2, left_on = 'dptcode',right_on = 'dept_no',how = 'left')[['empno','name','dpt_nam','salary']].sort_values(by='salary', ascending=True)
    print(result)    

        
def storeDataToDB():
    if(len(self.result) > 0):
        cel = ce('mysql://ai:ai@127.0.0.1/ai')
        result.to_sql("ai_20_result",cel)
        print("Table Created")
        
          

def readCsv():
    item = pd.read_csv('items.csv')
    sales = pd.read_csv('sales.csv')
    item = item.fillna(item['stock'].mean())
    result = pd.merge(item, sales, left_on = 'id',right_on = 'tid')[['name','region','sale_qty']]
    print(result)    
        

def createPivot(self):
    if(len(self.result) > 0):
        result = self.result.pivot(columns = 'name', index = 'region')
        print("========Pivot====================")
        print(result)
    else:
        print("Record not found")
        
        
            
            
        
