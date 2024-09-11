#page332
figure = plt.figure(figsize=(12,12))
axes = figure.add_subplot(111)

vitamin = ['비타민A', '비타민B1', '비타민B2', '나이아신', '비타민B6', '비타민C', '비타민D', '비타민 E', '엽산']
data =[0.18,0.3,3.33, 3.75, 0.38,25,0.25, 2.75,0.1]

axes.pie(data,labels=vitamin,autopct='%0.1f%%')
plt.show()