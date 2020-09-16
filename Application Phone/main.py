from tkinter import *
import MySQLdb
from tkinter import messagebox

conn=MySQLdb.connect("localhost","root","12345","test")
cr=conn.cursor()

class Application(object):
    def __init__(self,master):
        self.master=master

        self.top=Frame(master,height=200,bg="white")
        self.top.pack(side=TOP,fill=X)

        self.bottom=Frame(master,height=600,bg="#0e91e3")
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image=PhotoImage(file="phone.png")
        self.top_image_label=Label(self.top,image=self.top_image)
        self.top_image_label.place(x=150,y=35)

        #top heading
        self.heading=Label(self.top,text="My Phonebook",font="Verdana 20 bold",bg="white",fg="#2412c9")
        self.heading.place(x=300,y=75)


    #open window for add people
        def add_people_window():
            top2=Toplevel()
            top2.title("My People")
            top2.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(),self.master.winfo_screenheight()))

            self.top_addcontact_window_frame=Frame(top2,height=200,bg="white")
            self.top_addcontact_window_frame.pack(side=TOP,fill=X)

            self.bottom_addcontact_window_frame=Frame(top2,height=600,bg="#dbfc00")
            self.bottom_addcontact_window_frame.pack(fill=X)

            self.top_addcontact_image=PhotoImage(file="addcontacts.png")
            self.top_addcontact_image_label=Label(top2,image=self.top_addcontact_image)
            self.top_addcontact_image_label.place(x=150,y=35)

            self.addcontact_heading=Label(top2,text="Add new Person",font="Verdana 20 bold",bg="white",fg="#2412c9")
            self.addcontact_heading.place(x=300,y=75)


        #Adding labels and entries on add contact window
            self.name=Label(self.bottom_addcontact_window_frame,text="Name :",font="Verdana 20 bold",fg="#2412c9",bg="#dbfc00",width=15)
            self.name.place(x=200,y=50)
            self.name_entry=Entry(self.bottom_addcontact_window_frame,width=20,bd=4,font="Verdana 20 bold")
            self.name_entry.insert(0,"name")
            self.name_entry.place(x=600,y=50)

            self.surname=Label(self.bottom_addcontact_window_frame,text="Surname :",font="Verdana 20 bold",fg="#2412c9",bg="#dbfc00",width=15)
            self.surname.place(x=200,y=110)
            self.surname_entry=Entry(self.bottom_addcontact_window_frame,width=20,bd=4,font="Verdana 20 bold")
            self.surname_entry.insert(0,"surname")
            self.surname_entry.place(x=600,y=110)

            self.email=Label(self.bottom_addcontact_window_frame,text="Email :",font="Verdana 20 bold",fg="#2412c9",bg="#dbfc00",width=15)
            self.email.place(x=200,y=170)
            self.email_entry=Entry(self.bottom_addcontact_window_frame,width=20,bd=4,font="Verdana 20 bold")
            self.email_entry.insert(0,"email")
            self.email_entry.place(x=600,y=170)

            self.phone=Label(self.bottom_addcontact_window_frame,text="Mobile :",font="Verdana 20 bold",fg="#2412c9",bg="#dbfc00",width=15)
            self.phone.place(x=200,y=230)
            self.phone_entry=Entry(self.bottom_addcontact_window_frame,width=20,bd=4,font="Verdana 20 bold")
            self.phone_entry.insert(0,"mobile")
            self.phone_entry.place(x=600,y=230)

            self.address=Label(self.bottom_addcontact_window_frame,text="Address :",font="Verdana 20 bold",fg="#2412c9",bg="#dbfc00",width=15)
            self.address.place(x=200,y=290)
            self.address_entry=Text(self.bottom_addcontact_window_frame,width=20,height=4,bd=4,font="Verdana 20 bold")
            self.address_entry.place(x=600,y=290)


            #Add person to database
            def add_person():
                name=self.name_entry.get()
                surname=self.surname_entry.get()
                email=self.email_entry.get()
                phone=self.phone_entry.get()
                address1=self.address_entry.get(1.0,END)
                
                if(name and surname and email and phone and address1!=""):
                    cr.execute("""insert into detail(per_name,per_surname,per_email,per_phone,per_add) values("%s","%s","%s","%s","%s")"""%(name,surname,email,phone,address1))
                    conn.commit()
                    messagebox.showinfo("Success","Contact Added")
                    
                else:
                    messagebox.showerror("Error","Fill all the fields",icons="warning")

            self.add_contact_button=Button(self.bottom_addcontact_window_frame,text="Add Person",font="Verdana 20 bold",command=add_person,bg="white")
            self.add_contact_button.place(x=450,y=500)

        #Update Window
        def update_window():
            top3=Toplevel()
            top3.title("Update Persons")
            top3.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(),self.master.winfo_screenheight()))

            self.top_update_window_frame=Frame(top3,height=200,bg="white")
            self.top_update_window_frame.pack(side=TOP,fill=X)

            self.bottom_update_window_frame=Frame(top3,height=600,bg="#fcca03")
            self.bottom_update_window_frame.pack(fill=X)

            self.top_update_image=PhotoImage(file="C:/Users/Akshay/Desktop/contacts.png")
            self.top_update_image_label=Label(top3,image=self.top_update_image)
            self.top_update_image_label.place(x=150,y=35)

            self.update_heading=Label(top3,text="Update Person",font="Verdana 20 bold",bg="white",fg="#2412c9")
            self.update_heading.place(x=300,y=75)


            select_item=self.listbox.curselection()
            person_value=self.listbox.get(select_item)
            person_id=person_value.split(" . ")[0]

                
            cr.execute("select * from detail where per_id = '{}'".format(person_id))
            result=cr.fetchone()
            print(result)
            person_name=result[1]
            person_surname=result[2]
            person_email=result[3]
            person_phone=result[4]
            person_address=result[5]

            #Adding labels and entries on add Update window
            self.name1=Label(self.bottom_update_window_frame,text="Name :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.name1.place(x=200,y=50)
            self.name1_entry=Entry(self.bottom_update_window_frame,width=20,bd=4,font="Verdana 20 bold")
            self.name1_entry.insert(0,person_name)
            self.name1_entry.place(x=600,y=50)

            self.surname1=Label(self.bottom_update_window_frame,text="Surname :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.surname1.place(x=200,y=110)
            self.surname1_entry=Entry(self.bottom_update_window_frame,width=20,bd=4,font="Verdana 20 bold")
            self.surname1_entry.insert(0,person_surname)
            self.surname1_entry.place(x=600,y=110)

            self.email1=Label(self.bottom_update_window_frame,text="Email :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.email1.place(x=200,y=170)
            self.email1_entry=Entry(self.bottom_update_window_frame,width=20,bd=4,font="Verdana 20 bold")
            self.email1_entry.insert(0,person_email)
            self.email1_entry.place(x=600,y=170)
    
            self.phone1=Label(self.bottom_update_window_frame,text="Mobile :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.phone1.place(x=200,y=230)
            self.phone1_entry=Entry(self.bottom_update_window_frame,width=20,bd=4,font="Verdana 20 bold")
            self.phone1_entry.insert(0,person_phone)
            self.phone1_entry.place(x=600,y=230)

            self.address1=Label(self.bottom_update_window_frame,text="Address :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.address1.place(x=200,y=290)
            self.address1_entry=Text(self.bottom_update_window_frame,width=20,height=4,bd=4,font="Verdana 20 bold")
            self.address1_entry.insert(1.0,person_address)
            self.address1_entry.place(x=600,y=290)


            def update_btn():
                name=self.name1_entry.get()
                surname=self.surname1_entry.get()
                email=self.email1_entry.get()
                phone=self.phone1_entry.get()
                address=self.address1_entry.get(1.0,END)
                cr.execute("update detail set per_name='{}',per_surname='{}',per_email='{}',per_phone='{}',per_add='{}' where per_id={}".format(name,surname,email,phone,address,person_id))
                conn.commit()
                messagebox.showinfo("Success","Contact Updated")

            self.add_contact_button=Button(self.bottom_update_window_frame,text="Update Person",font="Verdana 20 bold",command=update_btn)
            self.add_contact_button.place(x=450,y=500)
   
        
        def display_person():
            top4=Toplevel()
            top4.title("Update Persons")
            top4.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(),self.master.winfo_screenheight()))

            self.top_display_window_frame=Frame(top4,height=200,bg="white")
            self.top_display_window_frame.pack(side=TOP,fill=X)

            self.bottom_display_window_frame=Frame(top4,height=600,bg="#dbfc00")
            self.bottom_display_window_frame.pack(fill=X)

            self.top_display_image=PhotoImage(file="contacts.png")
            self.top_display_image_label=Label(top4,image=self.top_display_image)
            self.top_display_image_label.place(x=150,y=35)

            self.display_heading=Label(top4,text="Person Information",font="Verdana 20 bold",bg="white",fg="#2412c9")
            self.display_heading.place(x=300,y=75)

            select_item=self.listbox.curselection()
            person_value=self.listbox.get(select_item)
            person_id=person_value.split(" . ")[0]

                
            cr.execute("select * from detail where per_id = '{}'".format(person_id))
            result=cr.fetchone()
            print(result)
            person_name=result[1]
            person_surname=result[2]
            person_email=result[3]
            person_phone=result[4]
            person_address=result[5]

            self.id2=Label(self.bottom_display_window_frame,text="Person Id :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.id2.place(x=200,y=50)
            self.id2_entry=Label(self.bottom_display_window_frame,text=person_id,width=20,bd=4,font="Verdana 20 bold")
            self.id2_entry.place(x=600,y=50)

            self.name2=Label(self.bottom_display_window_frame,text="Name :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.name2.place(x=200,y=50)
            self.name2_entry=Label(self.bottom_display_window_frame,text=person_name,width=20,bd=4,font="Verdana 20 bold")
            self.name2_entry.place(x=600,y=50)

            self.surname2=Label(self.bottom_display_window_frame,text="Surname :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.surname2.place(x=200,y=110)
            self.surname2_entry=Label(self.bottom_display_window_frame,text=person_surname,width=20,bd=4,font="Verdana 20 bold")
            self.surname2_entry.place(x=600,y=110)

            self.email2=Label(self.bottom_display_window_frame,text="Email :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.email2.place(x=200,y=170)
            self.email2_entry=Label(self.bottom_display_window_frame,text=person_email,width=20,bd=4,font="Verdana 20 bold")
            self.email2_entry.place(x=600,y=170)
    
            self.phone2=Label(self.bottom_display_window_frame,text="Mobile :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.phone2.place(x=200,y=230)
            self.phone2_entry=Label(self.bottom_display_window_frame,text=person_phone,width=20,bd=4,font="Verdana 20 bold")
            self.phone2_entry.place(x=600,y=230)

            self.address2=Label(self.bottom_display_window_frame,text="Address :",font="Verdana 20 bold",fg="#2412c9",bg="white",width=15)
            self.address2.place(x=200,y=290)
            self.address2_entry=Label(self.bottom_display_window_frame,text=person_address,width=20,height=4,bd=4,font="Verdana 20 bold")
            self.address2_entry.place(x=600,y=290)
            


        #Delete Person
        def delete_person():
            select_item=self.listbox.curselection()
            person_value=self.listbox.get(select_item)
            person_id=person_value.split(" . ")[0]
            cr.execute("delete from detail where per_id = '{}'".format(person_id))
            conn.commit()
            messagebox.showinfo("Success","Contact Deleted")




    #Open1 Window
        def open_window():
            top1=Toplevel()
            top1.title("My People")
            top1.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(),self.master.winfo_screenheight()))

            self.top_window_frame1=Frame(top1,height=200,bg="white")
            self.top_window_frame1.pack(side=TOP,fill=X)

            self.bottom_window_frame2=Frame(top1,height=600,bg="#dbfc00")
            self.bottom_window_frame2.pack(fill=X)

            self.top_image1=PhotoImage(file="contacts.png")
            self.top_image_label1=Label(top1,image=self.top_image1)
            self.top_image_label1.place(x=150,y=35)

            self.heading1=Label(top1,text="My Phonebook",font="Verdana 30 bold",bg="white",fg="#2412c9")
            self.heading1.place(x=300,y=75)

            self.scroll=Scrollbar(self.bottom_window_frame2,orient=VERTICAL)
            self.scroll.grid(row=0,column=1,sticky=N+S,pady=50)

            self.listbox=Listbox(self.bottom_window_frame2,width=34,height=15,font="Verdana 20 bold")
            self.listbox.grid(row=0,column=0,padx=60,pady=20)
            self.scroll.config(command=self.listbox.yview)
            self.listbox.config(yscrollcommand=self.scroll.set)

            cr.execute("select * from detail")
            rows=cr.fetchall()
            count=0
            for row in rows:
                self.listbox.insert(count,str(row[0])+" . "+row[1]+" . "+row[4])
                count+=1



            #add buttons on my contacts
            self.btn_add_people=Button(self.bottom_window_frame2,text="Add Contacts",font="Verdana 20 bold",bg="white",fg="black",width=15,command=add_people_window)
            self.btn_add_people.grid(row=0,column=2,padx=200,pady=10,sticky=N)

            self.btn_update_people=Button(self.bottom_window_frame2,text="Update",font="Verdana 20 bold",bg="white",fg="black",width=15,command=update_window)
            self.btn_update_people.grid(row=0,column=2,padx=200,pady=100,sticky=N)

            self.btn_display_people=Button(self.bottom_window_frame2,text="Display",font="Verdana 20 bold",bg="white",fg="black",width=15,command=display_person)
            self.btn_display_people.grid(row=0,column=2,padx=200,pady=210,sticky=N)
    
            self.btn_delete_people=Button(self.bottom_window_frame2,text="Delete",font="Verdana 20 bold",bg="white",fg="black",width=15,command=delete_person)
            self.btn_delete_people.grid(row=0,column=2,padx=200,pady=290,sticky=N)




        def about_us():
            top5=Toplevel()
            top5.title("Update Persons")
            top5.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(),self.master.winfo_screenheight()))
            
            self.top_about_us_window_frame=Frame(top5,height=self.master.winfo_screenheight(),bg="#fcca03")
            self.top_about_us_window_frame.pack(fill=BOTH)

            self.text=Label(self.top_about_us_window_frame,text="Hey this is About us page."
                            "\nThis Application is made for Educational purpose"
                            "\nYou can Contact us on"
                            "\nFacebook : Akshay patil"
                            "\nInstagram : patilakshay345",font="Verdana 25 bold",bg="#fcca03",fg="black")
            self.text.place(x=300,y=250)



        #Add buttons
        #View people
        self.view_btn=Button(self.bottom,text="My People",font="Verdana 20 bold",width=15,bg="white",command=open_window)
        self.view_btn.place(x=550,y=150)

        #add people
        self.add_btn=Button(self.bottom,text="Add contact",font="Verdana 20 bold",width=15,bg="white",command=add_people_window)
        self.add_btn.place(x=550,y=240)


        #View people
        self.about_btn=Button(self.bottom,text="About Us",font="Verdana 20 bold",width=15,bg="white",command=about_us)
        self.about_btn.place(x=550,y=330)
        

        
def main():
    root=Tk()
    app=Application(root)
    root.title("Phonebook App")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
    root.mainloop()


if __name__=='__main__':
    main()
