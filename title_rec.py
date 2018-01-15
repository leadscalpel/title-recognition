# coding=utf-8

import os
import re

class Catalog:
    def __init__(self, name, num, priority, page):
        self.name = name    # 目录的名字
        self.child = 0    # 子节点个数
        self.children = []    # 字节点列表
        self.father = self    # 父节点
        self.num = num    # 标题序数
        self.priority = priority    # 标题优先级
        self.page = page    # 标题所在页数

    # 向该目录下添加一个目录或叶节点
    def add(self, leaf):
        self.children.append(leaf)
        leaf.father = self
        self.child += 1

    # 查找以name为名字的节点是否在子节点列表中，若在返回下表，不在返回-1
    def name_in(self, name):
        for i in range(len(self.children)):
            if name == self.children[i].name:
                return i
        return -1

    # 删除该目录下的以leaf_name为名字的子节点，若无抛出异常
    def delete(self, leaf_name):
        index = self.name_in(leaf_name)
        if index >= 0:
            del self.children[index]
        else:
            raise Exception("Catalog without the deleted items")

    # 删除该目录下的所有子节点，若无抛出异常
    def delete_all(self):
        for j in range(len(self.children)):
            del self.children[0]

    # 展示树形结构
    def display(self, depth, filename):
        filename.write('-'*depth + self.name + str(int(depth / 2)) + '.........' + str(self.page) + '\n')
        for child in self.children:
            child.display(depth+2, filename)


# 目录标号表
dic = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二',
       '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十', '二十一', '二十二',
       '二十三', '二十四', '二十五', '二十六', '二十七', '二十八', '二十九', '三十', '三十一',
       '三十二', '三十三', '三十四', '三十五', '三十六', '三十七', '三十八', '三十九', '四十']


# 获取标题信息
def title_check(string):

    for i in range(36, 0, -1):
        if ('第' + dic[i] + '节') in string:
            return 1, i, '第' + dic[i] + '节'
        if ('第' + dic[i] + '章') in string:
            return 1, i, '第' + dic[i] + '章'


        if (dic[i] + '、') in string:
            return 2, i, dic[i] + '、'

    test = string
    # 排除首字符汉字
    string = string.replace(' ', '')
    if is_chinese(string[0:1]):
        return 0, 0, 0

    for i in range(36, 0, -1):

        if ('（' + dic[i] + '）') in string:
            if (is_chinese(string[len('（' + dic[i] + '）') : len('（' + dic[i] + '）') + 1])):
                return 3, i, '（' + dic[i] + '）'
        if ('(' + dic[i] + ')') in string:
            if (is_chinese(string[len('(' + dic[i] + ')') : len('(' + dic[i] + ')') + 1])):
                return 3, i, '（' + dic[i] + '）'
        if ('(' + dic[i] + '）') in string:
            if (is_chinese(string[len('(' + dic[i] + '）') : len('(' + dic[i] + '）') + 1])):
                return 3, i, '（' + dic[i] + '）'
        if ('（' + dic[i] + ')') in string:
            if (is_chinese(string[len('（' + dic[i] + ')') : len('（' + dic[i] + ')') + 1])):
                return 3, i, '（' + dic[i] + '）'

        if (str(i) + ' ') in test:
            if (is_chinese(string[len(str(i)): len(str(i)) + 1])):
                return 4, i, str(i) + ' '

        if (str(i) + '、') in string:
            if (is_chinese(string[len(str(i) + '、'): len(str(i) + '、') + 1])):
                return 5, i, str(i) + '、'
        if (str(i) + '.') in string:
            if (is_chinese(string[len(str(i) + '.'): len(str(i) + '.') + 1])):
                return 5, i, str(i) + '.'

        if ('(' + str(i) + ')') in string:
            if (is_chinese(string[len('(' + str(i) + ')'): len('(' + str(i) + ')') + 1])):
                return 6, i, '(' + str(i) + ')'
        if ('（' + str(i) + '）') in string:
            if (is_chinese(string[len('（' + str(i) + '）'): len('（' + str(i) + '）') + 1])):
                return 6, i, '(' + str(i) + ')'
        if ('(' + str(i) + '）') in string:
            if (is_chinese(string[len('(' + str(i) + '）'): len('(' + str(i) + '）') + 1])):
                return 6, i, '(' + str(i) + ')'
        if ('（' + str(i) + ')') in string:
            if (is_chinese(string[len('（' + str(i) + ')'): len('（' + str(i) + ')') + 1])):
                return 6, i, '(' + str(i) + ')'

    return 0, 0, 0


# 是否至少存在n个数字
def ndigit_exist(string, n):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    if count < n:
        return 1
    else:
        return 0


# 判断是否符号
def is_symbol(char):
    symbols = ':;。】』'
    if char in symbols:
        return 1
    return 0


# 判断是否包含符号
def contain_symbol(string):
    symbols = '！@#￥%&*《》。．/；.\\“”"？'
    for i in string:
        if i in symbols:
            return 1
    return 0


# 判断是否汉字
def is_chinese(char):
    if char >= u'\u4e00' and char <= u'\u9fa5':
        return True
    else:
        return False


# 新建父标题
def new_title(title, now, num, priority, page):
    title.append(Catalog(now.replace('\n', ''), num, priority, page))    # 实例化节点
    title[-2].add(title[-1])    # 认父


# 添加子标题
def add_title(title, now, num, priority, page):
    title.pop()
    title.append(Catalog(now.replace('\n', ''), num, priority, page))
    title[-2].add(title[-1])


# 删除栈顶目录的所有子标题
def del_top(title):
    for i in range(len(title[-1].children)):
        del title[-1].children[0]


# 主要过程
def list_menu(path2r, path2w):
    dir2r = os.listdir(path2r)
    for file in dir2r:
        if '.txt' in file and not 'done' in file:
            f2w = open(os.path.join(path2w, file.replace('.txt', '-done.txt')), 'w+')
            f2r = open(os.path.join(path2r, file))
            total = 0    # 储存总行数
            now = 0    # 正在扫描的行数
            content = []    # 储存文本内容
            for line in f2r:
                content.append(line)
                total += 1

            while now < total-1:
                page = re.match('^(\d+)/(\d+)$', content[now].replace(' ', ''))
                while now < total - 1:
                    now_priority, now_num, now_title = title_check(content[now][0:5])
                    if now_priority\
                        and not contain_symbol(content[now][len(now_title):])\
                        and ndigit_exist(content[now], 4)\
                            and is_chinese(content[now].replace(' ', '')[len(now_title):len(now_title)+1]):
                            f2w.write(content[now])
                            print(content[now])
                    now += 1

            f2r.close()
            f2w.close()