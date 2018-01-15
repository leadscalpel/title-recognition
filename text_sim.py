import jieba
from collections import Counter

def str_sim(self, str1, str2):
	# 字符串预处理， 去掉分隔符
	str1 = str1.replace('，','')	
	str2 = str2.replace('，','')
	# 结巴分词
	str1 = jieba.cut(str1, 0)
	str2 = jieba.cut(str2, 0)
	# 两个字符串分别一个Counter容器，和一个总容器
	counter1 = Counter()
	counter1.update(str1)
	counter2 = Counter()
	counter2.update(str2)
	counter = counter1 + counter2
	# 初始化余弦角的分子分母
	numerator = 0
	dinominator1 = 0
	dinominator2 = 0
	# 遍历Counter容器
	for word in counter.elements():
		numerator += counter1[word] * counter2[word]
		dinominator1 += counter1[word] ** 2
		dinominator2 += counter2[word] ** 2
	dinominator = (dinominator1 * dinominator2) ** 0.5
	return(numerator / dinominator)