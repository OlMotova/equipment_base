# -*- coding: utf-8 -*-
from functions import *
from service_functions import *
import pandas as pd
import ipaddress
from datetime import datetime
import sys
import numpy as np
from contextlib import redirect_stdout

df = df_loading('Main_file.xlsx')
equipment_df = df_loading('equipment_database.xlsx')

print(unique_equipment(equipment_df, 'equipment_name'))
equipment_name = input("Введите (скопируйте) имя устройства: ")

df_2 = df_filter(df, 'equipment_name', equipment_name)
equipment_df_2 = df_filter(equipment_df, 'equipment_name', equipment_name)

print(unique_equipment(equipment_df_2, 'equipment_type'))
equipment_type = input("Введите (скопируйте) тип устройства: ")

#df_3 = df_filter(df_2, 'equipment_type', equipment_type)
#equipment_df_3 = df_filter(equipment_df_2, 'equipment_type', equipment_type)

stickers_count = int(input("Введите колличество этикеток: "))

#______________________________________

#program part
text, flag = calculating_button (df, equipment_df, equipment_name, equipment_type, stickers_count)

text_out = save_button (df, equipment_df, equipment_name, equipment_type, stickers_count)
