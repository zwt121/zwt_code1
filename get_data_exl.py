import xlrd
from xlrd import xldate_as_tuple
from wechat import*
from tkinter import messagebox
class Select_Student_info():
    def __init__(self,work_sheet) -> None:
        self.work_sheet=work_sheet
    def select_student_time(self,student_name):
        account=['数学','英语','物理','生物','化学','语文']
        school=['保利','富祥','粤丰','新城']
        a=''
        for row in range(self.work_sheet.nrows):
            for col in range(self.work_sheet.ncols):#遍历excel有效单元格
                if str(student_name) in str(self.work_sheet.cell_value(row,col)):#判断学生名字所在单元格位置
                    for c in (account): 
                        for s in school:                                     #判断科目
                            if c in str(self.work_sheet.cell_value(row,col)) and s in str(self.work_sheet.cell_value(row,col)):
                                date=self.work_sheet.cell_value(0,col)
                                #时间
                                cellvalue1=self.work_sheet.cell(row,0).value
                                cellvalue2=xldate_as_tuple(cellvalue1,0)
                                time=[i for i in cellvalue2 if i>0]
                                if len(time)>1:
                                    hour=time[0]
                                    minute=time[1]
                                    result_time=str(hour)+':'+str(minute)+'-'+str(hour+2)+':'+str(minute)+c
                                    a=a+date+'\t'+result_time+s+'校区'+'\n'
                                else:
                                    hour=time[0]
                                    minute=':00'
                                    result_time=str(hour)+minute+'-'+str(hour+2)+minute+c
                                    a=a+date+'\t'+result_time+'\t'+s+'校区'+'\n'
        return a
        
    # wx=WeChat()
    # who=input('学生姓名:')
    # message=f'{who}家长你好，孩子这周课表按照这个\n{select_student_time(who)}'

    # WxUtils.SetClipboard(message)    # 将内容复制到剪贴板,类似于Ctrl + C
    # wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
    # wx.SendClipboard()   # 发送剪贴板的内容,类似于Ctrl + V
    # messagebox.showinfo('学生课程信息',select_student_time('朱峻希'))
if __name__=='__main__':
    #读取excel表
    work_table=xlrd.open_workbook('D:\下载\python\ichat\wxauto-main\class.xlsx')
    #选择工作簿
    work_sheet=work_table.sheet_by_index(0)
    a=Select_Student_info
    print(a(work_sheet).select_student_time('汤卉'))