import sqlite3
db=sqlite3.connect("bas.db")
cr=db.cursor()
def returPeduc():
    cr.execute("select education from projets ")
    l=cr.fetchall()
    try:
        l1,l2,l3,l4,l5=l[0][0],l[1][0],l[2][0],l[3][0],l[4][0]
        return l1,l2,l3,l4,l5
    except Exception: return "","","","",""
def returPecon():
    cr.execute("select economie from projets ")
    l=cr.fetchall()
    try:
        l1,l2,l3,l4,l5=l[0][0],l[1][0],l[2][0],l[3][0],l[4][0]
        return l1,l2,l3,l4,l5
    except Exception: return "","","","",""
def returPjun():
    cr.execute("select junesse from projets ")
    l=cr.fetchall()
    try:
        l1,l2,l3,l4,l5=l[0][0],l[1][0],l[2][0],l[3][0],l[4][0]
        return l1,l2,l3,l4,l5
    except Exception: return "","","","",""
def returPsan():
    cr.execute("select sante from projets ")
    l=cr.fetchall()
    try:
        l1,l2,l3,l4,l5=l[0][0],l[1][0],l[2][0],l[3][0],l[4][0]
        return l1,l2,l3,l4,l5
    except Exception: return "","","","",""
def returPaf():
    cr.execute("select afaireEtrang from projets ")
    l=cr.fetchall()
    try:
        l1,l2,l3,l4,l5=l[0][0],l[1][0],l[2][0],l[3][0],l[4][0]
        return l1,l2,l3,l4,l5
    except Exception: return "","","","",""

def check():
    cr.execute("select count(*) from projets")
    cont=cr.fetchall()[0][0]
    if cont==5:
        return True
    else: return False





# procidure radio education
def educ1(l):
    cr.execute("SELECT id FROM projets WHERE (education= ?)",(l,))
    id=cr.fetchall()[0][0]
    cr.execute(f"UPDATE projets SET NVeduc = NVeduc+1 WHERE (id={id})")
    db.commit()
    cr.execute(f"update projets set PVote= PVote + Peducation where id={id}")
    db.commit()
    
    
# procidure economie 
def econ1(l):
    cr.execute("SELECT id FROM projets WHERE (economie= ?)",(l,))
    id=cr.fetchall()[0][0]
    cr.execute(f"UPDATE projets SET NVeco = NVeco+1 WHERE (id={id})")
    db.commit()
    cr.execute(f"update projets set PVote= PVote + Peconomie where id={id}")
    db.commit()
    
# procidure jeunnes
def junn1(l):
    cr.execute("SELECT id FROM projets WHERE (junesse= ?)",(l,))
    id=cr.fetchall()[0][0]
    cr.execute(f"UPDATE projets SET NVjun = NVjun+1 WHERE (id={id})")
    db.commit()
    cr.execute(f"update projets set PVote= PVote + Pjeunesse where id={id}")
    db.commit()

# sante
def sant1(l):
    cr.execute("SELECT id FROM projets WHERE (sante= ?)",(l,))
    id=cr.fetchall()[0][0]
    cr.execute(f"UPDATE projets SET NVsan = NVsan+1 WHERE (id={id})")
    db.commit()
    cr.execute(f"update projets set PVote= PVote + Psante where id={id}")
    db.commit()
# affaire etrangere
def affaire1(l):
    cr.execute("SELECT id FROM projets WHERE (afaireEtrang= ?)",(l,))
    id=cr.fetchall()[0][0]
    cr.execute(f"UPDATE projets SET NVaf = NVaf+1 WHERE (id={id})")
    db.commit()
    cr.execute(f"update projets set PVote= PVote + PafaireEtrang where id={id}")
    db.commit()

    

def pV(idT):
    cr.execute(f"update users set pointVote= pointVote-1 where id={idT} ")
    db.commit()
def rid():
    cr.execute("select id from projets")
    id=cr.fetchall()
    id1=id[0]
    id2=id[1]
    id3=id[3]
    id4=id[3]
    id5=id[4]
    return id1[0],id2[0],id3[0],id4[0],id5[0]
def debV(id):
    cr.execute(f"select pointVote from users where(id={id})")
    l=cr.fetchall()
    l1=l[0]
    l2=l1[0]
    if l2==1:
        return True
    else: return False




