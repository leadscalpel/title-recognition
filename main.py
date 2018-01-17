from title_rec import list_menu
from pdf2txt import pdf_to_txt
from text_sim import str_sim
import os

if __name__ == '__main__':
    # list_menu('/home/teddy/workspace/title_rec/material/txtTrans/信息传输、软件和信息技术服务业/', '/home/teddy/workspace/title_rec/material/txtTrans/信息传输、软件和信息技术服务业-done/')
    # list_menu('/home/teddy/workspace/title_rec/material/txtTrans/农、林、牧、渔业/', '/home/teddy/workspace/title_rec/material/txtTrans/农、林、牧、渔业-done/')
    # list_menu('/home/teddy/workspace/title_rec/material/txtTrans/卫生和社会工作/', '/home/teddy/workspace/title_rec/material/txtTrans/卫生和社会工作-done/')
    # list_menu('/home/teddy/workspace/title_rec/material/txtTrans/建筑业/', '/home/teddy/workspace/title_rec/material/txtTrans/建筑业-done/')
    # list_menu('/home/teddy/workspace/title_rec/material/txtTrans/房地产业/', '/home/teddy/workspace/title_rec/material/txtTrans/房地产业-done/')
    # list_menu('/home/teddy/workspace/title_rec/material/txtTrans/教育/', '/home/teddy/workspace/title_rec/material/txtTrans/教育-done/')
    # list_menu('/home/teddy/workspace/title_rec/material/txtTrans/电力、热力、燃气及水生产和供应业/', '/home/teddy/workspace/title_rec/material/txtTrans/电力、热力、燃气及水生产和供应业-done/')
    # list_menu('/home/teddy/workspace/title_rec/material/txtTrans/金融业/', '/home/teddy/workspace/title_rec/material/txtTrans/金融业-done/')
    # list_menu('/home/teddy/workspace/title_rec/material/test/', '/home/teddy/workspace/title_rec/material/test/')
    templates = open('./Exxresult.txt')
    temp = {}
    for template in templates:
        temp[template] = 0
    templates = open('./Exxresult.txt')
    dir = './done2/信息传输、软件和信息技术服务业-done'
    for template in templates:
        for file in os.listdir(dir):
            doc = open(os.path.join(dir, file))
            for line in doc:
                sim = str_sim(template.replace(' ', ''), line.replace(' ', ''))
                if sim > 0.8:
                    temp[template] += 1
                    # print('template: ' + template + 'text: ' + line + "similarity: " + str(sim))
    for i in temp:
        print(temp[i])