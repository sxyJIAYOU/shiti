import csv

import requests

url = 'https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN'
data = {
"pageNo": "1",
"pageSize": "15",
"bondType": "100001",
"issueYear": "2023",
}
response = requests.post(url,data=data)
#html_data = response.text
json_data = response.json()
data = json_data['data']['resultList']


#定义需要提取的列明
columns = ['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating']

data1 = []
for i in data:
    isin = i['isin']
    bond_code = i['bondCode']
    issuer = i['entyFullName']
    bond_type1 = i['bondType']
    issue_data = i['issueStartDate']
    latest_rating = i['debtRtng']
    data1.append([isin,bond_code,issuer,bond_type1,issue_data,latest_rating])

with open('data1.csv','w') as f:
    write = csv.writer(f)
    write.writerow(columns)
    write.writerow(data1)