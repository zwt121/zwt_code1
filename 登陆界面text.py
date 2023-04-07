from tkinter import *
from tkinter import messagebox
import pymysql
import re
import webbrowser
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label1=Label(self,text='用户名')
        self.label2=Label(self,text='密码')
        self.label3=Label(self,text='登录界面')
        self.e1=StringVar()
        self.entry1=Entry(self,textvariable=self.e1)
        self.e2=StringVar()
        self.entry2=Entry(self,textvariable=self.e2,show="*")
        self.button1=Button(self,text='登录',width=15,command=self.login)
        self.button2=Button(self,text='注册账户',command=self.enroll)
        self.check=StringVar()
        self.check.set('0')
        self.checkbutton=Checkbutton(self,text='我已阅读协议内容并承诺遵守',onvalue='1',offvalue='0',variable=self.check)
        #显示组件
        #使用grid布局管理器控制位置     
        self.label1.grid(row=1,column=0)
        self.label2.grid(row=2,column=0)
        self.label3.grid(row=0,column=1)
        self.button1.grid(row=4,column=1)
        self.button2.grid(row=4,column=2,sticky=W)
        self.checkbutton.grid(row=3,column=1)
        self.entry1.grid(row=1,column=1)
        self.entry2.grid(row=2,column=1)
    def login(self):
        self.connect_sql()
        if self.entry1.get()==self.CompareAccount(): 
            if self.entry2.get()==self.ComparePassword():
                if self.check.get()=='1':
                    messagebox.showinfo('登录系统','登录成功')
                    self.close()
                    self.sihuVideo()
                else:
                    messagebox.showwarning('登录系统测试','请勾选内容')
            else:
                messagebox.showwarning('登录测试系统','密码错误')
        else:
            messagebox.showwarning('登录测试系统','用户名不存在')

            
    def enroll(self):#注册账号

        self.connect_sql()
        sql='insert into login values(%s,%s)'
        args=(self.entry1.get(),self.entry2.get())
        try:
            #执行sql
            
            #提交sql
            if self.entry1.get()!='' :
                if self.entry2.get() !='': 
                    if self.entry1.get()!=self.CompareAccount():
                        self.cursor.execute(sql,args)
                        self.connect.commit()
                        messagebox.showinfo('登录系统测试',f'注册成功\n账号为{self.entry1.get()}\n密码为{self.entry2.get()}')
                    else:
                        self.connect.rollback()
                        messagebox.showwarning('登录系统测试','用户名已存在')

                else:
                    self.connect.rollback()
                    messagebox.showwarning('登录系统测试','密码未填写')
            else:
                self.connect.rollback()
                messagebox.showwarning('登录系统测试','用户名未填写')
        except Exception as e:
            print(e)
            #回滚sql
            if self.connect:
                self.connect.rollback()
                 
        self.close()
    def connect_sql(self):
        self.connect=pymysql.connect(host='localhost',port=3306,user='root',passwd='1223',db='gui_locate')
        self.cursor=self.connect.cursor()
    def CompareAccount(self):
        try:
            sql='select admin from login where admin=%s'
            self.cursor.execute(sql,(self.entry1.get()))
            string1=self.cursor.fetchone()
            account=re.findall(pattern='\w.+\w',string=str(string1))

            return account[0]
        except Exception as e:
            print(e)
            
    def ComparePassword(self):
        try:   
            sql='select password from login where admin=%s'
            self.cursor.execute(sql,(self.entry1.get()))
            string2=self.cursor.fetchone()
            password=re.findall(pattern='\w.+\w',string=str(string2))
            return password[0]
        except Exception as e:
            print(e)
        
    def close(self):
        self.cursor.close()
        self.connect.close()
    def sihuVideo(self)
        #webbrowser.open('https://www.ven789.com/pic/toupai')

if __name__=="__main__":
    root=Tk()
    root.geometry('400x200+200+100')
    root.title('登录系统测试')
    app=Application(root)
    root.mainloop()
