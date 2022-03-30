import pymongo
import pandas
myclient = pymongo.MongoClient( "mongodb+srv://bbbb:bbbb@cluster0.79s5x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = myclient["myfoodDB"]
mycol = mydb["foods"]

df_menu = pandas.read_csv('menu.txt')
df_label = pandas.read_csv('label.txt')
menu_label = pandas.concat([df_menu, df_label], axis=1, join='inner')

for index, row in menu_label.iterrows():
    mycol.insert_one({"menu":row['menu'], "type":row['type']})