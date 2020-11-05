import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
datas = sp.find('table', id="Lotto649Control_history_dlQuery")
#sqlstr = "select * from currency where 期數 = '{}'".format(期數)
#cursor = conn.execute(sqlstr)
#row = cursor.fetchone

data1 = datas.find_all('table', class_='table_org td_hm')
data2 = datas.find_all('table', class_='table_gre td_hm')
# print(data1[0])

title0 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_0').text
print("期數(0)", title0, '\n大小順序')
aa = data1[0].find_all('td', {'class': 'td_w font_black14b_center'})
aaa = ""
for i in range(6, 12):
    aaa = aaa + " " + aa[i].text
num2_0 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_0').text
print('第二區', num2_0)
a = str(title0) + ", " + aaa + ", " + str(num2_0)
print(a)

title1 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_1').text
print("期數(1)", title1, '\n大小順序')
bb = data2[0].find_all('td', {'class': 'td_w font_black14b_center'})
for i in range(6, 12):
    print(bb[i].text)
num2_1 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_1').text
print('第二區', num2_1)

title2 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_2').text
print("期數(2)", title2, '\n大小順序')
cc = data1[1].find_all('td', {'class': 'td_w font_black14b_center'})
for i in range(6, 12):
    print(cc[i].text)
num2_2 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_2').text
print('第二區', num2_2)

title3 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_3').text
print("期數(3)", title3, '\n大小順序')
dd = data2[1].find_all('td', {'class': 'td_w font_black14b_center'})
for i in range(6, 12):
    print(dd[i].text)
num2_3 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_3').text
print('第二區', num2_3)

title4 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_4').text
print("期數(4)", title4, '\n大小順序')
ee = data1[2].find_all('td', {'class': 'td_w font_black14b_center'})
for i in range(6, 12):
    print(ee[i].text)
num2_4 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_4').text
print('第二區', num2_4)

title5 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_5').text
print("期數(5)", title5, '\n大小順序')
ff = data2[2].find_all('td', {'class': 'td_w font_black14b_center'})
for i in range(6, 12):
    print(ff[i].text)
num2_5 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_5').text
print('第二區', num2_5)

title6 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_6').text
print("期數(6)", title6, '\n大小順序')
gg = data1[3].find_all('td', {'class': 'td_w font_black14b_center'})
for i in range(6, 12):
    print(gg[i].text)
num2_6 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_6').text
print('第二區', num2_6)

title7 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_7').text
print("期數(7)", title7, '\n大小順序')
hh = data2[3].find_all('td', {'class': 'td_w font_black14b_center'})
for i in range(6, 12):
    print(hh[i].text)
num2_7 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_7').text
print('第二區', num2_7)

title8 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_8').text
print("期數(8)", title8, '\n大小順序')
jj = data1[4].find_all('td', {'class': 'td_w font_black14b_center'})
for i in range(6, 12):
    print(jj[i].text)
num2_8 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_8').text
print('第二區', num2_8)

title9 = datas.find(
    'span', id='Lotto649Control_history_dlQuery_L649_DrawTerm_9').text
print("期數(9)", title9, '\n大小順序')
kk = data2[4].find_all('td', {'class': 'td_w font_black14b_center'})
for i in range(6, 12):
    print(kk[i].text)
num2_9 = datas.find('span', id='Lotto649Control_history_dlQuery_SNo_9').text
print('第二區', num2_9)
