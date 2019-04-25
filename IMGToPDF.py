'''
Auther : Haozl
Created : 2019/4/25
Desc : 图片转PDF

'''
import os

from reportlab.platypus import SimpleDocTemplate, Image, PageBreak
from reportlab.lib.pagesizes import A4, landscape

from PIL import Image as pilImage


def convert_imagesToPDF(file_dir, save_name):
    '''
    转换一个目录文件夹下的图片至PDF
    参数：
        file_dir: 图片所在的文件夹的路径
        save_name: 目标PDF的文件名（需以.pdf结尾）
    '''
    book_pages = []
    
    for parent, dirnames, filenames in os.walk(file_dir):        #-- os.walk()方法：返回的是一个三元组(root,dirs,files)
        # 选中目录下的所有图片                                     #-- root 所指的是当前正在遍历的这个文件夹的本身的地址
        for file_name in filenames:                              #-- dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
            file_path = os.path.join(parent, file_name)          #-- files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
            book_pages.append(file_path)

        save_path = os.path.join(file_dir, save_name)

        if len(book_pages) > 0 :
            #开始转换
            print("-----开始转换-----")
            __converted(save_path, book_pages)
            print("-----转换完成-----")
def __converted(save_book_name, book_pages = []):
    '''
    开始转换
    参数：
        save_book_name : 保存的pdf文件路径
        book_pages: 图片数组
    '''
    # A4 纸的宽高
    __a4_w, __a4_h = landscape(A4)

    # 对数据进行排序
    book_pages.sort()

    bookPagesData = []
    
    #创建一个简单模板
    bookDoc = SimpleDocTemplate(save_book_name)

    for page in book_pages:
        #获取图片的宽和高
        img_w, img_h = ImageTools().getImageSize(page)
        #取合适的比例
        if __a4_w / img_w < __a4_h / img_h:
            ratio = __a4_w / img_w
        else:
            ratio = __a4_h / img_h

        data = Image(page, img_w * ratio, img_h * ratio)
        bookPagesData.append(data)
        bookPagesData.append(PageBreak())

    bookDoc.build(bookPagesData)

class ImageTools:
    def getImageSize(self, imagePath):
        '''
        由图片路径获取宽和高
        
        '''
        img = pilImage.open(imagePath)
        return img.size

convert_imagesToPDF("images", "1.pdf")
        
    
