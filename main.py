from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interfaceM import Ui_MainWindow 
from interface1 import Ui_Form as f1
from interfaceRes import Ui_Form as fr
from interfaceInsc import Ui_Form as fi
from siser1 import Ui_Form as s1
from siser2 import Ui_Form as s2
from siser3 import Ui_Form as s3
from siser4 import Ui_Form as s4
from siser5 import Ui_Form as s5
from vote1 import Ui_Form as v1
from vote2 import Ui_Form as v2
from vote3 import Ui_Form as v3
from vote4 import Ui_Form as v4
from vote5 import Ui_Form as v5
from admin import Ui_Form as ad



from intnon import Ui_Form as fn
import result as resul
import connection1 as con
import condidat as condid
import liste_projets as lis
import vote as vo
import bddadmin as add 

def adm(): 
    if uiad.radioButton.isChecked():
        afi=1
    if uiad.radioButton_2.isChecked():
        afi=2
    if uiad.radioButton_3.isChecked():
        afi=3
    add.inserer(afi)


def close():
    internon.close()
    interIns.close()
    interRes.close()
def afichef1():
    inter1.show()
    MainWindow.close()
    interIns.close()
    internon.close()
    interRes.close()
    ints5.close()
    intv5.close()
def connex():
    id=ui.id.text()
    nom=ui.nom.text().lower().replace(" ","")
    prenom=ui.prenom.text().lower().replace(" ","")
    try:
        if type(int(id))!="int":
            
            if id=="1" and nom=="admin" and prenom=="admin":
                
                intad.show()
                MainWindow.close()
            else:    
                a=con.verifier(int(id),nom,prenom)
                if a==True:
                    afichef1()
                else:  
                    QMessageBox.warning(intv1,"erreur", "Verifiez vos coordonnèes ")

    except Exception:
        QMessageBox.warning(intv1,"erreur", "Voutre Identificateur dois etre un entier  ")

def enp():
    
    id=ui.id.text()
    a=uis1.lineEdit.text()
    b=uis2.lineEdit.text()
    c=uis3.lineEdit.text()
    d=uis4.lineEdit.text()
    e=uis5.lineEdit.text()
    ed=uis1.textEdit.toPlainText()
    ec=uis2.textEdit.toPlainText()
    jn=uis3.textEdit.toPlainText()
    st=uis4.textEdit.toPlainText()
    af=uis5.textEdit.toPlainText()
    try:
        p=(pourcentpaf()-int(e))
        if p>=0:
            lis.inser(int(id),ed,int(a),ec,int(b),jn,int(c),st,(d),af,int(e))
            ints5.close()
        else:QMessageBox.warning(ints5,"Erreur","Le pourcentage sisé est superieur au rest")
    except Exception:   QMessageBox.warning(ints5,"Erreur","Vous devez remplir votre projet et son pourcentage")
    

def pourcentpeco():
    ped1=uis1.lineEdit.text()
    z=100-(int(ped1))
    return z
# zed=pourcentped(ped)

def pourcentpjs():
    pec1=uis1.lineEdit.text()
    pec2=uis2.lineEdit.text()
    
    z=100-(int(pec2)+int(pec1))
    return z
# zec=pourcentpeco(zed,pec)    
def pourcentpsan():
    pec1=uis3.lineEdit.text()
    pec2=uis2.lineEdit.text()
    pec3=uis1.lineEdit.text()

    z=100-(int(pec3)+int(pec1)+int(pec2))
    return z
def pourcentpaf():
    pec1=uis1.lineEdit.text()
    pec2=uis2.lineEdit.text()
    pec3=uis3.lineEdit.text()
    pec4=uis4.lineEdit.text()
    
    z=100-(int(pec2)+int(pec3)+int(pec4)+int(pec1))
    return z



def aficheRes():
    afic=add.recup()
    if afic==3:
        a=resul.condition()
        if a==5:
            interRes.show()
            inter1.close()
        else: QMessageBox.warning(inter1,"Erreur","La liste des condidats n'est pas encore remplie ")
    else: QMessageBox.warning(inter1,"Erreur","Acces impossible actuellement!! ")

def afichInsc():
    afi=add.recup()
    id=ui.id.text()
    if afi==2:   
        l=condid.rec(id)
        if l==False :
            interIns.show()
            inter1.close()
        else: QMessageBox.warning(inter1,"Erreur","Vous avez deja inscrit")
    else: QMessageBox.warning(inter1,"Erreur","Acces impossible actuellement!! ")

def afichNon():
    internon.show()


def info():
    id=ui.id.text()
    nom=ui.nom.text()
    prenom=ui.prenom.text()
    age=uiIn.age.text()
    nv=uiIn.comboBox_sc.currentText()
    pp=uiIn.comboBox_par.currentText()
    tp=uiIn.Tprojets.text()
    pr=uiIn.projetsRes.text()
    try:
        condid.condi(id,nom,prenom,age,nv,pp,tp,pr,0,0).insertion()
        a=lis.selection()
        if a==False:
            afichs1()
            # afichNon()
        elif a==True:
            p1,p2,idmi=lis.sel(id)
            if int(p1)>int(p2):
                lis.supp(id,idmi)
                afichs1()
            else:  afichNon()
    except Exception:
        QMessageBox.warning(interIns,"Erreur","Vous devez siser vos informations")

def afichs1():
    uis1.label_3.setText( f" il  vous reste : 100% a consomer ")
    ints1.show()
    interIns.close()
    ints2.close()
    


def afichs2():
    try:
        p=pourcentpeco()
        if p>=0:
            uis2.label_3.setText(f" il  vous reste : {p}% a consomer ")

            ints2.show()
            ints1.close()
            ints3.close()
        else: QMessageBox.warning(ints1,"Erreur","Le pourcentage sisé est superieur au rest")
    except Exception: QMessageBox.warning(ints1,"Erreur","Vous devez remplir votre projet et son pourcentage ")

def afichs3():
    try:
        p=pourcentpjs()
        if p>=0:
            uis3.label_3.setText(f" il  vous reste : {p}% a consomer ")

            ints3.show()
            ints2.close()
            ints4.close()
        else: QMessageBox.warning(ints1,"Erreur","Le pourcentage sisé est superieur au rest")

    except Exception: QMessageBox.warning(ints1,"Erreur","Vous devez remplir votre projet et son pourcentage ")

def afichs4():
    try:
        p=pourcentpsan()
        if p>=0:
            uis4.label_3.setText(f" il  vous reste : {p}% a consomer ")

            ints4.show()    
            ints3.close()
            ints5.close()
        else: QMessageBox.warning(ints2,"Erreur","Le pourcentage sisé est superieur au rest")

    except Exception: QMessageBox.warning(ints2,"Erreur","Vous devez remplir votre projet et son pourcentage ")

def afichs5():
    try:
        p=pourcentpaf()
        if p>=0:
            uis5.label_3.setText(f" il  vous reste : {p}% a consomer ")
            ints5.show()
            ints4.close()
        else: QMessageBox.warning(ints3,"Erreur","Le pourcentage sisé est superieur au rest")

    except Exception: QMessageBox.warning(ints3,"Erreur","Vous devez remplir votre projet et son pourcentage ")

def afichv1():
    afi=add.recup()
    if afi==1:
        if vo.check()==True:
            id=ui.id.text()
            a=vo.debV(id)
            if a==True:
                intv1.show()
                inter1.close()
                intv2.close()
            else:    
                QMessageBox.warning(inter1,"Erreur", "Vous avez dejà voté ")
        else:            QMessageBox.warning(inter1,"Erreur", "La liste des condidats n'est pas encore remplé ")
    else:            QMessageBox.warning(inter1,"Erreur", " Acces impossible actuellement!! ")


def a():

    l1,l2,l3,l4,l5=vo.returPeduc()
    if uiv1.radioButton.isChecked():
        l=l1

    elif uiv1.radioButton_2.isChecked():
        l=l2
        

    elif uiv1.radioButton_3.isChecked():
        l=l3
        

    elif uiv1.radioButton_4.isChecked():
        l=l4
        

    elif uiv1.radioButton_5.isChecked():
        l=l5
    return l
def b():
    l1,l2,l3,l4,l5=vo.returPecon()
    if uiv2.radioButton.isChecked():
        l=l1

    elif uiv2.radioButton_2.isChecked():
        l=l2

    elif uiv2.radioButton_3.isChecked():
        l=l3

    elif uiv2.radioButton_4.isChecked():
        l=l4

    elif uiv2.radioButton_5.isChecked():
        l=l5
    return l
def c():
    l1,l2,l3,l4,l5=vo.returPjun()
    if uiv3.radioButton.isChecked():
        l=l1

    elif uiv3.radioButton_2.isChecked():
        l=l2

    elif uiv3.radioButton_3.isChecked():
        l=l3

    elif uiv3.radioButton_4.isChecked():
        l=l4

    elif uiv3.radioButton_5.isChecked():
        l=l5
    return l
def d():
    l1,l2,l3,l4,l5=vo.returPsan()
    if uiv4.radioButton.isChecked():
        l=l1

    elif uiv4.radioButton_2.isChecked():
        l=l2

    elif uiv4.radioButton_3.isChecked():
        l=l3

    elif uiv4.radioButton_4.isChecked():
        l=l4

    elif uiv4.radioButton_5.isChecked():
        l=l5
    return l
def e():
    l1,l2,l3,l4,l5=vo.returPaf()
    l=0
    if uiv5.radioButton.isChecked():
        l=l1
    elif uiv5.radioButton_2.isChecked():
        l=l2

    elif uiv5.radioButton_3.isChecked():
        l=l3

    elif uiv5.radioButton_4.isChecked():
        l=l4

    elif uiv5.radioButton_5.isChecked():
        l=l5
    return l
def some():
    aa=a()
    bb=b()
    cc=c()
    dd=d()
    ee=e()
    vo.educ1(aa)
    vo.econ1(bb)
    vo.junn1(cc)
    vo.sant1(dd)
    vo.affaire1(ee)
    

def afichv2():
    if not uiv1.radioButton.isChecked() and not uiv1.radioButton_2.isChecked() and not uiv1.radioButton_3.isChecked() and not uiv1.radioButton_4.isChecked() and not uiv1.radioButton_5.isChecked():
        QMessageBox.warning(intv1,"erreur", "Vous devez choisir un projet ")
    else:
        intv2.show()
        
        intv1.close()
        intv3.close()

def afichv3():
    if not uiv2.radioButton.isChecked() and not uiv2.radioButton_2.isChecked() and not uiv2.radioButton_3.isChecked() and not uiv2.radioButton_4.isChecked() and not uiv2.radioButton_5.isChecked():
        QMessageBox.warning(intv2,"erreur", "Vous devez choisir un projet ")
    else:

        intv3.show()


        intv2.close()
        intv4.close()

def afichv4():
    if not uiv3.radioButton.isChecked() and not uiv3.radioButton_2.isChecked() and not uiv3.radioButton_3.isChecked() and not uiv3.radioButton_4.isChecked() and not uiv3.radioButton_5.isChecked():
        QMessageBox.warning(intv3,"erreur", "Vous devez choisir un projet ")
    else:

        intv4.show()


        intv3.close()
        intv5.close()

def afichv5():
    if not uiv4.radioButton.isChecked() and not uiv4.radioButton_2.isChecked() and not uiv4.radioButton_3.isChecked() and not uiv4.radioButton_4.isChecked() and not uiv4.radioButton_5.isChecked():
        QMessageBox.warning(intv4,"erreur", "Vous devez choisir un projet ")
    else:
   
   
        intv5.show()

        intv4.close()

def voteterm():
    if not uiv5.radioButton.isChecked() and not uiv5.radioButton_2.isChecked() and not uiv5.radioButton_3.isChecked() and not uiv5.radioButton_4.isChecked() and not uiv5.radioButton_5.isChecked():
        QMessageBox.warning(intv5,"erreur", "Vous devez choisir un projet ")
    else:

        some()
        id=ui.id.text()
        vo.pV(id)
        intv5.close()
def mainaffiche():
    adm()
    MainWindow.show()
    intad.close()

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

inter1 = QtWidgets.QWidget()
uif1 = f1()
uif1.setupUi(inter1)

interRes= QtWidgets.QWidget()
uiRes = fr()
uiRes.setupUi(interRes)

interIns= QtWidgets.QWidget()
uiIn = fi()
uiIn.setupUi(interIns)

internon= QtWidgets.QWidget()
uino = fn()
uino.setupUi(internon)

ints1= QtWidgets.QWidget()
uis1 = s1()
uis1.setupUi(ints1)

ints2= QtWidgets.QWidget()
uis2 = s2()
uis2.setupUi(ints2)

ints3= QtWidgets.QWidget()
uis3 = s3()
uis3.setupUi(ints3)

ints4= QtWidgets.QWidget()
uis4 = s4()
uis4.setupUi(ints4)

ints5= QtWidgets.QWidget()
uis5 = s5()
uis5.setupUi(ints5)

intv1= QtWidgets.QWidget()
uiv1 = v1()
uiv1.setupUi(intv1)

intv2= QtWidgets.QWidget()
uiv2 = v2()
uiv2.setupUi(intv2)

intv3= QtWidgets.QWidget()
uiv3 = v3()
uiv3.setupUi(intv3)

intv4= QtWidgets.QWidget()
uiv4 = v4()
uiv4.setupUi(intv4)

intv5= QtWidgets.QWidget()
uiv5 = v5()
uiv5.setupUi(intv5)

intad= QtWidgets.QWidget()
uiad = ad()
uiad.setupUi(intad)


MainWindow.show()
uif1.pushButton_2.clicked.connect(afichInsc)
uiIn.pushButton_3 .clicked.connect(afichef1)
uiIn.suivant.clicked.connect(info)
uiIn.annuler.clicked.connect(close)
uif1.pushButton.clicked.connect(aficheRes)
ui.connection.clicked.connect(connex)
uino.pushButton_2.clicked.connect(afichef1)
uino.pushButton.clicked.connect(close)
uiRes.pushButton.clicked.connect(close)
uiRes.pushButton_2.clicked.connect(afichef1)
uis1.suivant.clicked.connect(afichs2)
uis2.suivant.clicked.connect(afichs3)
uis2.pre.clicked.connect(afichs1)
uis3.suivant.clicked.connect(afichs4)
uis3.pre.clicked.connect(afichs2)
uis4.suivant.clicked.connect(afichs5)
uis4.pre.clicked.connect(afichs3)
uis5.suivant.clicked.connect(enp)
uis5.pre.clicked.connect(afichs4)

uif1.pushButton_3.clicked.connect(afichv1)
uiv1.pushButton.clicked.connect(afichv2)
uiv2.pushButton.clicked.connect(afichv3)
uiv2.pushButton_2.clicked.connect(afichv1)
uiv3.pushButton.clicked.connect(afichv4)
uiv3.pushButton_2.clicked.connect(afichv2)
uiv4.pushButton.clicked.connect(afichv5)
uiv4.pushButton_2.clicked.connect(afichv3)
uiv5.pushButton_2.clicked.connect(afichv4)
uiv5.pushButton.clicked.connect(voteterm)
uiad.pushButton_2.clicked.connect(mainaffiche)
uiad.pushButton.clicked.connect(add.reset)



sys.exit(app.exec_())