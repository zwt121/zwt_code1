from tkinter import *
from tkinter import messagebox
from get_data_exl import *
from login_student import *
class  Send_info(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_grid()
    def create_grid(self):
        #创建学生姓名文本
        self.label1=Label(self,text='学生姓名:')
       
        #创建输入学生姓名的输入框
        self.e1=StringVar()
        self.entry1=Entry(self,textvariable=self.e1)
        self.text1=Text(self,width=40,height=12,bg='white')
        #创建查询按键
        self.button1=Button(self,text='查询',command=self.select_student)
        self.button2=Button(self,text='发送',command=self.send_message,width=20)
        #显示组件
        #使用grid布局管理器控制位置 
        self.label1.grid(row=1,column=0)
        self.text1.grid(row=3,column=0,columnspan=3)
        self.entry1.grid(row=1,column=1)
        self.button1.grid(row=1,column=2)
        self.button2.grid(row=2,column=1)
        
    def select_student(self):
        student_name=self.entry1.get()
        information=ssi.select_student_time(student_name)
        messagebox.showinfo('测试',information)
        self.text1.delete(1.0,END)
        self.text1.insert(END,information)
    def send_message(self):
        student_name=self.entry1.get()
        
        if student_name in student_list:
            messagebox.showwarning('学生课程信息','课表重复发送')
        else:
            student_list.append(student_name)
            who=f'识才教育{self.entry1.get()}学习交流群'
            message=ssi.select_student_time(student_name)
            WxUtils.SetClipboard(message)    # 将内容复制到剪贴板,类似于Ctrl + C
            wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
            wx.SendClipboard()   # 发送剪贴板的内容,类似于Ctrl + V  
        
if __name__=="__main__":
    wx=WeChat()
    student_list=[]
    student_name_list=[]
    work_table=xlrd.open_workbook('D:\下载\python\ichat\wxauto-main\class.xlsx')
    work_sheet=work_table.sheet_by_index(0)
    work_table2=xlrd.open_workbook('D:\下载\python\ichat\wxauto-main\student_names.xlsx')
    work_sheet2=work_table2.sheet_by_index(0)
    for row in range(work_sheet2.nrows):
        student_name_list.append(work_sheet2.cell_value(row,0))
    print(student_name_list)

    ssi=Select_Student_info(work_sheet)
    root=Tk()
    root.geometry('1960x1080+0+0')
    root.title('学生课表查询')
    app=Send_info(root)
    root.mainloop()