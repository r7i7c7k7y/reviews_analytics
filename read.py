data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f :
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有',len(data),'筆資料')

sum = 0
for x in data:
	i = len(x)
	sum = sum + i
print('留言平均長度為', sum/len(data))

new = []
for x in data:
	if len(x) < 100:
		new.append(x)
print('一共有', len(new), '筆小於長度100')
print(new[0])

good = []
for x in data:
	if 'good' in x:
		good.append(x)
print('一共有', len(good), '筆包含good')

