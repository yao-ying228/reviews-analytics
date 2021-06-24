data = []
count = 0
with open('reviews.txt','r') as f :
	for line in f :
		data.append(line)
		count +=1
		if count % 10000 == 0 :
		    print(len(data))
print('檔案讀取完畢總共有' , len(data) , '筆資料')

print(data[0])

sum_len = 0
for d in data:
	sum_len += len(d)
	
print('平均留言長度為:',sum_len/len(data),'個字數')	


new = []
for d in data:
	if len(d) < 100:
	   new.append(d)
print('總共有' , len(new) , '筆留言字數<100個字')

print(new[0])
print('---------')

good = []
for d in data :
	if 'good' in d:
		good.append(d)

print('總共有',len(good), '筆留言提到good')
print(good[0])


print('===========')
good = [d for d in data if 'good' in d]
print(good)	

# 文字搜尋與計數

wc = {} #work count 的意思
for d in data :
	words = d.split(' ')
	for word in words :
		if word in wc :
			wc[word] += 1

		else :
			wc[word] = 1 #增加新的Key到wc字典

for word in wc :
	if wc[word] > 10000 :
		print(word,wc[word])

print(len(wc))
print(wc['Marco'])

while True :
	word =input('請問你要搜尋那個字:')
	if word == 'q' :
		break
	if word in wc :
		print(word , '總共出現了' , wc[word] , '次')
	else :
		print('抱歉,這字沒有出現過喔!')
print('謝謝使用此搜尋功能')



	
