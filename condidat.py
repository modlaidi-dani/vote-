import sqlite3


db=sqlite3.connect("bas.db")
crs=db.cursor()
class condi:
    def __init__(self,id,nom,prenom,age,niveauSC,parcourP,projetsTotal,projetsReusi,moyPReus,point) :
        self.id=id
        self.nom=nom    
        self.prenom=prenom
        self.age=age
        self.niveauSc=niveauSC
        self.parcourP=parcourP
        self.projetsTotal=projetsTotal
        self.projetsReusi=projetsReusi
        self.moyPReus=moyPReus
        self.point=point

    def set(self):
        crs.execute("INSERT INTO condidats  VALUES (?,?,?,?,?,?,?,?,?,?)",(self.id,self.nom,self.prenom,self.age,self.niveauSc,self.parcourP,self.projetsTotal,self.projetsReusi,self.moyPReus,self.point)) 
        db.commit()
        
    
    def moyenP(self):
        return (int(self.projetsReusi)/int(self.projetsTotal))*100
    
    def points(self):
        
        if int(self.age)<20:
            self.point=int(self.point)
        elif int(self.age)<35:
            self.point+=10
        elif int(self.age)<60:
            self.point+=5
        else:
            self.point=self.point
        if self.niveauSc=="licence":
            self.point+=2
        elif self.niveauSc=="master":
            self.point+=5
        elif self.niveauSc=="docteur":
            self.point+=10
        elif self.niveauSc=="profisseur":
            self.point+=15
        elif self.niveauSc=="chercheur":
            self.point+=20
        if self.parcourP=="melitent":
            self.point+=2
        elif self.parcourP=="maire":
            self.point+=5
        elif self.parcourP=="chef-daira":
            self.point+=10
        elif self.parcourP=="wali":
            self.point+=15
        elif self.parcourP=="ministre":
            self.point+=20
        elif self.parcourP=="president":
            self.point+=25
        if self.moyenP()==0:
            self.point=self.point
        elif self.moyenP()<=20:
            self.point+=2
        elif self.moyenP()<=30:
            self.point+=5
        elif self.moyenP()<=50:
            self.point+=8
        elif self.moyenP()<=70:
            self.point+=10
        elif self.moyenP()<=80:
            self.point+=15
        elif self.moyenP()<=90:
            self.point+=17
        elif self.moyenP()<=100:
            self.point+=20
        
        

    
    def insertion(self):
        
        # self.age=input("entrer votre age:\t")
        # self.niveauSc=input('entrer votre niveau scoller ("licence", "master", "docteur", "profisseur", "chercheur"):\t')
        # self.parcourP=input('entrer votre parcour politique ("melitent", "maire", "chef-daira", "wali", "ministre", "president"):\t')
        # self.projetsTotal=input("entrer le nombre de projet effecuer:\t")
        # self.projetsReusi=input("entrer le nombre de projet reusie:\t")
        self.moyPReus=self.moyenP()
        self.points()
        self.set()
        

def rec(id):
    
    crs.execute(f"select id from condidats")
    l=crs.fetchall()
    li=(int(id),)
    if li in l:
        return True
    else: return False




