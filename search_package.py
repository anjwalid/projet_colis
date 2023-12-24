from tkinter import *
from tkinter import messagebox
from tkintermapview import TkinterMapView
from customtkinter import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
from database import * 


#####-----------Back to main page------#####
def admin_to_main():
    loginf.place_forget()
    image_label.place_forget()
    but.place_forget()
    image_welcome.place(x=400,y=20)
    main.place(x=10, y=30)
#============= page reclamation =========
def reclam () :
    fr.pack_forget()
    #__________suivre de reclamation__________
    def suivre_rec () : 
        frmo.pack_forget()
        frmo3 =Frame(root)
        frmo3.pack(fill=BOTH, expand=True)
        def goback2 () :
            frmo3.pack_forget()
            frmo.pack(fill = BOTH,expand =True)
        def enter(event) : 
            lent.delete(0, END)
        def  leave(event) :
            if lent.get =="" :
                 lent.insert(0,"entrez l'id de reclamation")
        def chercher() :
            id_rec =lent.get()
            db = Database("root","", "localhost","package")
            db.execute_query('select statut_rec from reclamation where id_rec = %s',(id_rec))
            test = db.fetchall()
            lob_rec = Label(frmo3,text = test[0][0],font=('Miscrosoft YaHei UI Light', 19,'bold'),bg = 'white',fg ='#59CAF5').place(x =35,y= 200)
        lobb = Label(frmo3 , image =pt_6)
        lobb.place(x = 0 , y = 0)
        lent = Entry(frmo3,width =44,font=('Miscrosoft YaHei UI Light', 18,'bold') )
        lent.insert(0,'entrez l id de reclamation')
        lent.bind('<FocusIn>',enter)
        lent.bind('<FocusOut>',leave) 
        lent.place(x = 100 , y = 140)
        but2 = Button(frmo3, text='< go back',fg='#59CAF5',bg='white', border=0, anchor='w', compound='left', font=('Calibri(Body)',15), command=goback2, cursor='hand2').place(x=20,y=26)
        bt33 =Button(frmo3, text='CHERCHER',bg='#59CAF5',fg='white', border=2, anchor='w', compound='left', font=('Calibri(Body)',13), cursor='hand2',command = chercher).place(x=700,y=140)
        Lb11 = Label(frmo3, text= 'NB : L ID DE RECLAMATION SE TROUVE DANS LE FICHIER PDF IMPRIME ',font=('Miscrosoft YaHei UI Light', 14,'bold'),fg = 'red',bg = 'white')
        lb12 =  Label(frmo3, text= 'STATUT :',font=('Miscrosoft YaHei UI Light', 19,'bold'),bg = 'white',fg ='#59CAF5')
        Lb11.place(x=120 ,y=450)
        lb12.place(x =240 ,y= 200)
            
    #__________ajouter de reclamation__________
    def ajout_rec () :
        frmo.pack_forget()
        def imp ():
            id_cls1 =entry_type_reclamation.get()       
            objet = entry_type_objet.get()
            description =entry_description.get('1.0',END)
            nom_fichier = "reclamation_{}.pdf".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            # Créer un fichier PDF avec ReportLab
            c = canvas.Canvas(nom_fichier, pagesize=letter)
            c.drawImage("logo.png", 50, 700, width=100, height=100)
            # Ajout de l'adresse de l'expéditeur
            db = Database('root','','localhost','package')
            db.execute_query('select e.PRENOM_EXP ,e.NOM_EXP from colis c , expéditeur e where id_colis = %s',(id_cls1))
            test = db.fetchall()
            c.drawString(50, 650, test[0][0] + " " +test[0][1])
            c.drawString(50, 635, "id de colis :" + " " + id_cls1)
            c.drawString(90, 615, "objet :" + " " + objet)
            # ajout title  + et date
            c.drawString(250, 720, 'RECLAMATION')
            db.execute_query('select id_rec from reclamation  where id_colis = %s',(id_cls1))
            test1 =db.fetchall()
            c.drawString(450, 690,"id de reclamation : "+str(test1[0][0]))

            c.drawString(450, 650, "date :" + " " + datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            # Ajout du corps de la lettre
            c.drawString(50, 590, "cher directeur  ")
            c.drawString(90, 560, description)
            # Ajout de la signature
            c.drawString(50, 350, "Cordialement,")
            c.drawString(50, 335, test[0][0] + " " +test[0][1])###appel base donne

            # Enregistrement du PDF
            c.save()
            messagebox.showinfo('avec succes','votre reclamation a ete imprimee')
        def goback1 () :
            frmo1.pack_forget()
            frmo.pack(fill = BOTH,expand =True)
        def vald() :
            id_cls1 = entry_type_reclamation.get()
            description =entry_description.get('1.0',END)
            db = Database('root','','localhost','package')
            db.execute_query('select id_colis from colis where id_colis = %s',(id_cls1))
            test =db.fetchall()
            if test : 
                db.execute_query('insert into reclamation(DATE_REC,DESCRIPTION_REC,ID_COLIS,STATUT_REC)  values (%s,%s,%s,%s)',(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),description,id_cls1,'non regle'))
                messagebox.showinfo("reclamation ajoutee", "votre reclmation a ete bien ajoute")
                bouton_imprimer_pdf =Button(frmo2, text="IMPRIMER EN PDF",bg ='orange',fg= 'white',font=('Miscrosoft YaHei UI Light',12,'bold'),width =17 , height= 1,command=imp).place(x = 210,y= 340)

            else :
                messagebox.showerror('erreur', 'id de colis inexistant')
                
        frmo1 =Frame(root)
        frmo1.pack(fill=BOTH, expand=True)
        lobb = Label(frmo1 , image =pt_7)
        lobb.place(x = 0 , y = 0)
        frmo2 =Frame(frmo1 , width = 400 , height = 400,bg ='#59CAF5')
        frmo2.place(x = 40 ,y = 70)
        lob1 = Label(frmo2,text = 'ID COLIS:',font=('Miscrosoft YaHei UI Light', 18,'bold'),fg ='white', bg ='#59CAF5').place(x =145 ,y = 20)
        lob2 = Label(frmo2,text = 'OBJET',font=('Miscrosoft YaHei UI Light', 18,'bold'),fg ='white', bg ='#59CAF5').place(x=155 ,y = 90)  
        lob3 = Label(frmo2,text = 'DESCRIPTION',font=('Miscrosoft YaHei UI Light', 18,'bold'),fg ='white', bg ='#59CAF5').place(x =120 ,y = 160) 
        entry_type_reclamation = Entry(frmo2, width=40,bd = 1)
        entry_type_reclamation.place(x =80 ,y = 60)
        entry_type_objet = Entry(frmo2, width=40,bd = 1)
        entry_type_objet.place(x =80 ,y = 130)
        entry_description = Text(frmo2, width=40, height=7)
        entry_description.place( x = 40, y =200 )
        bouton_validation =Button(frmo2, text="VALIDER",bg ='green',fg= 'white',font=('Miscrosoft YaHei UI Light', 12,'bold'),width =17 , height= 1,command =vald).place(x = 20,y= 340)
        but1 = Button(frmo1, text='< go back',fg='#59CAF5',bg='white', border=0, anchor='w', compound='left', font=('Calibri(Body)',15), command=goback1, cursor='hand2').place(x=20,y=26)


    def goback () :
        frmo.pack_forget()
        fr.pack(fill = BOTH,expand =True)
        
    frmo =Frame(root)
    frmo.pack(fill=BOTH, expand=True)
    lob = Label(frmo , image =pt_6)
    lob.place(x = 0 , y = 0)
    lbb =Label(frmo ,text ='BIENVENUE AU PAGE DE RECLAMATION ',fg = '#59CAF5',bg = 'white',font =('CALIBRI',30,'bold'))
    lbb.place(x = 135, y = 100)
    bt_rec = Button(frmo , text = 'AJOUTER UNE RECLAMATION',bg ='#59CAF5',fg = 'white',font = ('Miscrosoft YaHei UI Light', 10,'bold'),width=40,height = 4,cursor = 'hand2',command =ajout_rec )
    bt_rec.place(x = 100 , y = 240)
    bt_rec1 = Button(frmo , text = 'SUIVRE VOTRE RECLAMATION',bg ='#59CAF5',fg = 'white',font = ('Miscrosoft YaHei UI Light', 10,'bold'),width=40,height = 4,cursor = 'hand2',command =suivre_rec)
    bt_rec1.place(x = 500 , y = 240)
    but1 = Button(frmo, text='< go back',fg='#59CAF5',bg='white', border=0, anchor='w', compound='left', font=('Calibri(Body)',15), command=goback, cursor='hand2').place(x=20,y=26)





def enter(event) : 
    entry_pack.delete(0, END)
def  leave(event) :
    if entry_pack.get =="" :
        entry_pack.insert(0,"entrez l id de colis")
def reussie() :
    id_colis = entry_pack.get()
    db = Database('root','','localhost','package')
    db.execute_query('select e.Nom_EXP,d.NOM_DEST,C.DATE_LIVRAISON,c.ID_STATUT,a.address_agence from colis c , expéditeur e , destinataire d ,agence a  where e.CIN_exp = c.CIN_exp and d.CIN_des =c.CIN_dest and a.id_agence = c.id_agence and id_colis = %s',(id_colis))
    test = db.fetchall()
    if test :
        lb2 = Label(inf,text=test[0][0],font=('Miscrosoft YaHei UI Light', 12,'bold'),bg ='#59CAF5',fg ='white').place(x = 165 ,y = 20)
        lb3 = Label(inf,text=test[0][1],font=('Miscrosoft YaHei UI Light', 12,'bold'),bg ='#59CAF5',fg ='white').place(x = 165 ,y = 60)
        lb4=Label(inf,text = test[0][2],font=('Miscrosoft YaHei UI Light', 12,'bold'),bg ='#59CAF5',fg ='white').place(x = 209 ,y = 100)
        lb5=Label(inf,text = test[0][4] ,font=('Miscrosoft YaHei UI Light', 12 ,'bold'),bg ='#59CAF5',fg ='white').place(x = 203 ,y = 140)
        maps.set_address(test[0][4],marker=True)
        lb_p2.pack_forget() 
        if test[0][3] == 1 :
            lb_p1 = Label(fr, image = pt_1,bg = 'white').place(x = '200', y = '120')
        elif test[0][3] == 2 :
            lb_p1 = Label(fr, image = pt_2,bg = 'white').place(x = '200', y = '120')
        elif test[0][3] == 3 :
            lb_p1 = Label(fr, image = pt_3,bg = 'white').place(x = '200', y = '120')
        elif test[0][3] == 4 :
            lb_p1 = Label(fr, image = pt_4,bg = 'white').place(x = '200', y = '120')

    else :
        messagebox.showerror('ERROR','ID COLIS INTROUVABLE')
#la fenetre
root =  Tk()
root.geometry('925x500+300+120')
root.title('SEARCH PACKAGE')
root['bg'] ='white'

#ajouter les images 

photo1 = PhotoImage(file = 'projet_colis/images/rec.png')
pt_1 = PhotoImage(file = 'projet_colis/images/E4.png')
pt_2 = PhotoImage(file = 'projet_colis/images/E3.png')
pt_3 = PhotoImage(file = 'projet_colis/images/E2.png')
pt_4 = PhotoImage(file = 'projet_colis/images/E1.png')
pt_5 = PhotoImage(file = 'projet_colis/images/E5.png')
pt_6 = PhotoImage(file = 'projet_colis/images/coco.png')
pt_7 =PhotoImage(file = 'projet_colis/images/recm1.png')

#ajoutant les frames
fr = Frame(root,bg = 'white')
fr.pack(fill = BOTH,expand =True)
inf =Frame (root, bg ='#59CAF5',width =400 , height = 200)
inf.place(x =480 , y = 250)
#ajoutant background
lbb = Label(fr,image= pt_6)
lbb.place(x = 0, y = 0)
# ajouter_Map
maps =TkinterMapView(fr,width = 400 , height = 200,corner_radius=0)
maps.place(relx=0.03,rely=0.5)
maps.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=20)
#ajouter un arriere-plan 
maps.set_address("Maroc")
#ajouter_Label_pour photo
lb_p2 = Label(fr, image = pt_5,bg = 'white')
lb_p2.pack(anchor=NW, padx=200, pady=120)

#ajouter_Label_pour_resultat
lb1=Label(inf,text = 'EXPEDITEUR :',font=('Miscrosoft YaHei UI Light', 12,'bold'),fg ='white',bg ='#59CAF5').place(x = 40 ,y = 20)
lb1=Label(inf,text = 'DESTINATAIRE :',font=('Miscrosoft YaHei UI Light', 12,'bold'),fg ='white',bg ='#59CAF5').place(x = 40 ,y = 60)
lb1=Label(inf,text = 'DATE DE LIVRAISON:',font=('Miscrosoft YaHei UI Light', 12,'bold'),fg ='white',bg ='#59CAF5').place(x = 40 ,y = 100)
lb1=Label(inf,text = 'ADRESSE AGENCE :',font=('Miscrosoft YaHei UI Light', 12,'bold'),fg ='white',bg ='#59CAF5').place(x = 40 ,y = 140)

#AJOUTER L ENTREE 
entry_pack = Entry(fr,font=('Miscrosoft YaHei UI Light', 14),width = 38 , bd = 1  )
entry_pack.insert(0,'entrez l id de votre colis')
entry_pack.bind('<FocusIn>',enter)
entry_pack.bind('<FocusOut>',leave)
entry_pack.place(x = '220',y = '30')
#ajouter_bouton_pour_barre_search
bt = Button(fr,text = 'RECHERCHER',font =('Arial',9),bg = '#59CAF5' ,fg = 'white',cursor ='hand2',command = reussie)
bt.place(x ='650', y = '28.53')
but = Button(fr, text='< Back to Main',fg='#59CAF5',bg='white', border=0, anchor='w', compound='left', font=('Calibri(Body)',15), command=admin_to_main, cursor='hand2').place(x=20,y=26)

bt2=Button(fr,image =photo1, cursor ='hand2',bd =0.3,bg= 'white',command = reclam)
bt2.place(x = 850 ,y = 26)


root.mainloop()







 