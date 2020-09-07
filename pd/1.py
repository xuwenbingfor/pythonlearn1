import pandas  as pd

############################# 准备工作 start ##########################
# pip install pandas
# pip install xlrd ：https://jingyan.baidu.com/article/908080228f1e6ebd90c80f41.html
# pip install openpyxl
############################# 准备工作 end ############################

############################# 变量定义 start ##########################
source_excel = 'C:/Users/xwb/Desktop/1.xlsx'
target_excel = 'C:/Users/xwb/Desktop/2.xlsx'
row_start_index = 2
row_end_index = 12
col_name = '内容'
append_content = 'bcdef'
############################# 变量定义 end ############################

data = pd.read_excel(source_excel)
data_updated = data.loc[row_start_index: row_end_index, [col_name]] + append_content
data.loc[row_start_index: row_end_index, [col_name]] = data_updated
# print(data)
# print(type(data))
data.to_excel(target_excel, sheet_name='Sheet1', index=False, header=True)