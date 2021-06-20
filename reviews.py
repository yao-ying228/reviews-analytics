data = []
count = 0
with open('reviews.txt','r') as f :
	for line in f :
		data.append(line)
		count +=1
		if count % 50000 == 0 :
		    print(len(data))
print('檔案讀取完畢總共有' , len(data) , '筆資料')

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
print(new[239])
