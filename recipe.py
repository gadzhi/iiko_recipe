import csv
import pandas


import pandas as pd

goods = pd.read_csv("goods_export.csv", error_bad_lines=False, sep=";", usecols=["NAME","NUM"])
recipe = pd.read_csv("recipes export.csv", error_bad_lines=False, sep=";")
recipe2 = recipe

#print(goods)
goods_dict = {}
for index, row in goods.iterrows():
    sku = row['NUM']
    name = row['NAME']

    goods_dict[sku] = name
ds = []
for index2, row2 in recipe.iterrows():

    if row2['ITEM_CODE'] in goods_dict:

        ds.append(goods_dict[row2['ITEM_CODE']])
        #
    else:
        pass
recipe2['NEw'] = ds
recipe2.to_csv("New.csv", sep=";", encoding='utf-8')

#saved_column = goods.NUM

#print(saved_column)