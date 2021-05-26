from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter.font as TkFont
from tkinter import filedialog
from tkinter import messagebox
from Os_file_manipulation import Os_file_manipulation
from Comparing_data import Comparing_values
from Automation_of_code import Automation_of_code
code_upload=outputuploads=testcasesuploads=""
var = 0
sts = 0
passvalues = Os_file_manipulation()
class USERINTERFACE:  
    @staticmethod
    def Gui():
        root =Tk()
        root.geometry("900x800")
        root.resizable(width=False,height= False)
        #Custom Font 
        bigFont =TkFont.Font(family="Helvetica",size=17)
        root.option_add("*TCombobox*Listbox*Font",bigFont)
        root.option_add("*Font",bigFont)
        #logo
        root.title('AUTOMATED SOFTWARE TESTING AND TESTCASES GENERATOR')
        root.iconbitmap('images\logo_ico.ico')

        #background Image
        bg1 = Image.open('images\moroccan-flower.png')
        #resize
        resize_bg=bg1.resize((900,800),Image.ANTIALIAS)
        #define 
        new_bg = ImageTk.PhotoImage(resize_bg)
        compileImg = ImageTk.PhotoImage(Image.open('images\logo.png'))

        #Create canvas
        mycanvas = Canvas(root,width=900,height=800)
        mycanvas.pack(fill='both',expand=True)
        #set image
        mycanvas.create_image(0,0,image=new_bg,anchor=NW)


        def frontPage():
            global qsimg
            # global case_entry
            #constants
            def constants():
                outputuploadBtn.destroy()
                testcasesuploadBtn.destroy()
                uploadBtn.destroy()
                droptype.destroy()
                case_entry.destroy()
                qsBtn.destroy()
                helpBtn.destroy()
                gtrBtn.destroy()
                mycanvas.create_image(0,0,image=new_bg,anchor=NW)
                mycanvas.create_text(300,50,text= 'Automated Software Testing ' ,fill='black',font=("Blod",20) )
                mycanvas.create_text(300,80,text= 'and Testcase Generator' ,fill='black',font=("Blod",20) )
                mycanvas.create_image(50,40,image=compileImg,anchor=NW)

            ###########       Header    ########################
            mycanvas.create_image(50,40,image=compileImg,anchor=NW)
            mycanvas.create_text(300,50,text= 'Automated Software Testing ' ,fill='black',font=("Blod",20) )
            mycanvas.create_text(300,80,text= 'and Testcase Generator' ,fill='black',font=("Blod",20) )
            def help():
                constants()
                helpPage()
            #button HELP
            helpBtn = Button(root, text='help',command=help,font=("Blod",20),bd=0,fg='green')
            qsimg = ImageTk.PhotoImage(Image.open('images\help_32.png')) 
            qsBtn = Button(root,image=qsimg,bd=0,command=help)
            mycanvas.create_window(750,40,anchor=NW,window=helpBtn,width=50)
            mycanvas.create_window(800,50,anchor=NW,window=qsBtn,width=50)
            ########################         Header       ##################

            #TEXT
            mycanvas.create_text(40,200,text= 'No.of testcases to be generated: ' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(40,250,text= 'Select type: ' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(40,350,text= 'Choose Code: ' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(40,450,text= 'Custom testcases and output(optional): ' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(40,500,text= 'TestCases:  ' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(500,500,text= 'Outputs: ' ,fill='black',font=("Blod",20),anchor=NW )

            # num
            global var
            var = IntVar()
            case_entry = Entry(root,font=("Helvetica",17),width=20,fg='black',bd=0,textvariable =var)
            case_canvas = mycanvas.create_window(450,200,anchor=NW,window=case_entry,width=100)
            
            #drop type
            types = ['INT', 'STR']
            def show(event):
                global sts
                mycanvas.create_text(200,200,fill='blue',font=("Blod",20) )
                if droptype.get() == 'STR':
                    sts = 1  
                else:
                    sts = 0 
            droptype= ttk.Combobox(root,value= types,state='readonly',font=("Blod",17),width=100)
            # droptype.current(0)
            droptype.bind("<<ComboboxSelected>>", show)
            mycanvas.create_window(200,250,anchor=NW,window=droptype,width=100)
            
            #button upload
            def upload():
                global code_upload
                #file location giver
                root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("text files","*.txt")))
                code_upload = root.filename
                if code_upload == '':
                    uploadBtn['fg'] = 'red'
                else:
                    uploadBtn['fg'] = 'green'
            uploadBtn = Button(root, text='Upload',command=upload,font=("Blod",15),bd=1,fg='black')
            mycanvas.create_window(250,350,anchor=NW,window=uploadBtn,width=100)
            #button upload for testcases
            def testcasesupload():
                global testcasesuploads
                root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
                testcasesuploads =root.filename
                if testcasesuploads == '':
                    testcasesuploadBtn['fg'] = 'red'
                else:
                    testcasesuploadBtn['fg'] = 'green'
            testcasesuploadBtn = Button(root, text='Upload',command=testcasesupload,font=("Blod",15),bd=1,fg='black')
            mycanvas.create_window(250,500,anchor=NW,window=testcasesuploadBtn,width=100)

            #button upload for output
            def outputupload():
                global outputuploads
                root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
                outputuploads =root.filename
                print(outputuploads)
                if outputuploads == '':
                    outputuploadBtn['fg'] = 'red'
                else:
                    outputuploadBtn['fg'] = 'green'        
            outputuploadBtn = Button(root, text='Upload',command=outputupload,font=("Blod",15),bd=1,fg='black')
            mycanvas.create_window(700,500,anchor=NW,window=outputuploadBtn,width=100)
            
            #button Generator
            def gtr():
                try:
                    int(var.get())
                    constants()
                    if(int(var.get())<=1000 and int(var.get())>=0):
                        if code_upload !="":
                            Automation_of_code.get_code_path(code_upload)
                            passvalues.append_in_txt(var.get(),sts)
                        else:                       
                            data = messagebox.showerror("Code Error","Please Upload The code")
                            tryAgain()
                            raise Exception("Code should be uploaded!!")
                        if testcasesuploads!="" and outputuploads!="":
                            Automation_of_code.execute_code(testcasesuploads)
                            passvalues.getpath(testcasesuploads,outputuploads)
                            Comparing_values.comparing_values()
                        else:
                            Automation_of_code.execute_code("")
                        successpage()
                    else:
                        tryAgain()
                    # hello.openFiless(upload)
                    # if(var.get()==1):
                    #     successpage()
                    # else:
                    #     tryAgain()
                except TclError:
                    case_entry["fg"] = 'red'
                    data = messagebox.showerror("Value Error","Please enter Number Inputs")
                    if data=="ok":
                        case_entry["fg"] = 'black'
                    
                    
                    
                #print("upload1")
                #print("testcasesuploads")
                #print("outputuploads")
                #print(entry.get())
            gtrBtn = Button(root, text='Generate',command=gtr,font=("Blod",20),bd=3,fg='black')
            mycanvas.create_window(325,600,anchor=NW,window=gtrBtn,width=200)


        frontPage()


        ###############################Successful page###################################

        def successpage():
            global refreshBtn
            def refreshdes():
                refreshBtn.destroy()
            def refreshfun():
                refreshdes()
                mycanvas.create_image(0,0,image=new_bg,anchor=NW)
                frontPage()
                mycanvas.create_text(300,50,text= 'Automated Software Testing ' ,fill='black',font=("Blod",20) )
                mycanvas.create_text(300,80,text= 'and Testcase Generator' ,fill='black',font=("Blod",20) )
                
            #img
            global img
            img = ImageTk.PhotoImage(Image.open('images\success256.png'))
            mycanvas.create_image(350,150,anchor=NW,image=img)
            mycanvas.create_text(450,400,text= 'TESTCASES AND OUTPUTS ' ,fill='black',font=("Blod",30) )
            mycanvas.create_text(450,450,text= 'SUCCESSFULLY GENERATED ' ,fill='black',font=("Blod",30) )
            refreshBtn = Button(root, text='Refresh',command=refreshfun,font=("Blod",20),bd=3,fg='black')
            mycanvas.create_window(350,550,anchor=NW,window=refreshBtn,width=200)
            #mycanvas.create_text(450,450,text= str(text) ,fill='black',font=("Blod",30) )

        ###############################Try again page###################################

        def tryAgain():
            def againdes():
                againBtn.destroy()
            def againfun():
                againdes()
                mycanvas.create_image(0,0,image=new_bg,anchor=NW)
                frontPage()

            #img
            global new_imgEmj
            imgEmj = Image.open('images\emoji.png')
            #resize
            resize_emj=imgEmj.resize((200,200),Image.ANTIALIAS)
            #define 
            new_imgEmj = ImageTk.PhotoImage(resize_emj)
            mycanvas.create_image(350,150,anchor=NW,image=new_imgEmj)
            mycanvas.create_text(450,400,text= 'Something went wrong ' ,fill='black',font=("Blod",30) )
            mycanvas.create_text(450,450,text= ' please try again ' ,fill='black',font=("Blod",30) )
            againBtn = Button(root, text='Try Again',command=againfun,font=("Blod",20),bd=3,fg='black')
            mycanvas.create_window(350,550,anchor=NW,window=againBtn,width=200)    

        ###############################Help Page###################################
        def helpPage():
            anscolor = '#505050'
            def backdes():
                backBtn.destroy()
            def backfun():
                backdes()
                mycanvas.create_image(0,0,image=new_bg,anchor=NW)
                frontPage()

            mycanvas.create_text(60,150,text= 'Welcome to the help page ' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(60,200,text= 'FAQ' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(60,250,text= 'Q-1)Can we choose any type of code?' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(60,300,text= 'A)yes,you can as long as code has single input' ,fill=anscolor,font=("Blod",20),anchor=NW )
            mycanvas.create_text(60,400,text= 'Q-2)Where can i find my code testcases and output?' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(60,450,text= 'A)The testcases and outputs will be stored in a text file' ,fill=anscolor,font=("Blod",20),anchor=NW )
            mycanvas.create_text(60,500,text= 'which will be in same directory as this program' ,fill=anscolor,font=("Blod",20),anchor=NW )
            mycanvas.create_text(60,600,text= 'Q-3)Upto how many testcases can i generate?' ,fill='black',font=("Blod",20),anchor=NW )
            mycanvas.create_text(60,650,text= 'A)you can generate upto 1000 testcases' ,fill=anscolor,font=("Blod",20),anchor=NW )
            global imgback
            imgback = ImageTk.PhotoImage(Image.open('images\Back42.png'))
            backBtn = Button(root, image=imgback,command=backfun,bd=0,)
            mycanvas.create_window(750,40,anchor=NW,window=backBtn)


        root.mainloop()
