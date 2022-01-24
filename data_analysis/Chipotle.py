import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path = "../../../data/chipotle.tsv"
chipo = pd.read_csv(file_path, sep='\t')

# chipo 라는 Dataframe에서 순서대로 10개의 row 데이터를 보여줍니다.
chipo.head(10)

print(chipo.shape)
print("---------------------------")
print(chipo.info())

chipo.describe()

print(chipo.columns)
print("---------------------------")
print(chipo.index)

# order_id는 숫자의 의미를 가지지 않기 때문에 str으로 변환합니다.
chipo['order_id'] = chipo['order_id'].astype(str)
print(chipo.describe())  # chipo dataframe에서 수치형 피처들의 요약 통계량을 확인합니다.

print(len(chipo['order_id'].unique()))  # order_id의 개수를 출력합니다.
print(len(chipo['item_name'].unique()))  # item_name의 개수를 출력합니다.

chipo['item_name'].value_counts()  # 각 항목의 개수 출력

# 가장 많이 주문한 item : top 10을 출력합니다.
item_count = chipo['item_name'].value_counts()[:10]
for idx, (val, cnt) in enumerate(item_count.iteritems(), 1):
    print("top", idx, ":", val, cnt)

chipo['item_name'].value_counts().index.tolist()[0]

# item당 주문 개수를 출력합니다.
order_count = chipo.groupby('item_name')['order_id'].count()
order_count[:10]  # item당 주문 개수를 출력합니다.

# item당 주문 총량을 출력합니다.
item_quantity = chipo.groupby('item_name')['quantity'].sum()
item_quantity[:10]  # item당 주문 총량을 출력합니다.

item_name_list = item_quantity.index.tolist()
x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()

plt.bar(x_pos, order_cnt, align="center")
plt.ylabel('ordered_item_count')
plt.title('Distribution if all orderd item')

plt.show()
