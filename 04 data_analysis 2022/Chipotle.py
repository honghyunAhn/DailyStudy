import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path = "./data/chipotle.tsv"
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


# 주문당 평균 계산금액을 출력합니다.
chipo.groupby('order_id')['item_price'].sum().mean()

# 한 주문에 10달러 이상 사용한 id를 출력합니다.
chipo_orderid_group = chipo.groupby('order_id').sum()
results = chipo_orderid_group[chipo_orderid_group.item_price >= 10]

print(results[:10])
print(results.index.values)

# 각 아이템의 가격을 계산합니다.
chipo_one_item = chipo[chipo.quantity == 1]
price_per_item = chipo_one_item.groupby('item_name').min()
price_per_item.sort_values(by='item_price', ascending=False)[:10]
# 아이템 가격 분포 그래프를 출력합니다.
itme_name_list = price_per_item.index.tolist()
x_pos = np.arange(len(item_name_list))
item_price = price_per_item['item_price'].tolist()

plt.bar(x_pos, item_price, align='center')
plt.ylabel('item price($)')
plt.title('Distribution of item price')

plt.show()

# 아이템 가격 히스토그램을 출력합니다.
plt.hist(item_price)
plt.ylabel('counts')
plt.title('Hisogram of item price')

plt.show()

# 가장 비싼 주문에서 item이 총 맻개 팔렸는지를 계산합니다.
chipo.groupby('order_id').sum().sort_values(
    by='item_price', ascending=False)[:5]

# "Veggie Salad Bowl" 이 몇 번 주문되었는지를 계산합니다.
chipo_salad = chipo[chipo['item_name'] == "Veggie Salad Bowl"]
# 한 주문 내에서 중복 집계된 item_name을 제거합니다.
chipo_salad = chipo_salad.drop_duplicates(['item_name', 'order_id'])

print(len(chipo_salad))
chipo_salad.head(5)
