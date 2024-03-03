import sqlite3 
db=sqlite3.connect("bas.db")
cr=db.cursor()
def selection():
    cr.execute("select id from condidats ORDER BY points desc")
    lg=cr.fetchall()
    cr.execute("select count(*) from projets")
    t=cr.fetchall()[0]
    taille=t[0]
    if taille==5: return True
    else: return False

def sel(id):
    cr.execute(f"select points from condidats where id = {id}")
    pointID=cr.fetchall()[0]
    kvid=pointID[0]
    cr.execute("select id from projets ")
    idMIN=cr.fetchall()
    l1=idMIN[0]
    le1=l1[0]
    l2=idMIN[1]
    le2=l2[0]
    l3=idMIN[2]
    le3=l3[0]
    l4=idMIN[3]
    le4=l4[0]
    l5=idMIN[4]
    le5=l5[0]
    cr.execute(f"select id from condidats where id={le1} or id={le2} or id={le3} or id={le4} or id={le5} order by points desc")
    lis=cr.fetchall()
    lmi=lis[-1]
    idmi=lmi[0]
    cr.execute(f"select points from condidats where id={idmi}")
    k=cr.fetchall()
    kv=k[0]
    kvm=kv[0]
    return kvid,kvm,idmi
def supp(id,idm):
    id,idm=int(id),int(idm)
    cr.execute(f"delete from projets where id={idm}")
    db.commit()

##  def inser(a,e,pe,ec,pec,j,pj,s,ps,af,paf):   

#      cr.execute(f"insert into projets (id,education,Peducation,economie,Peconomie,junesse,Pjeunesse,sante,Psante,afaireEtrang,PafaireEtrang) values ({a},{e},{pe},{ec},{pec},{j},{pj},{s},{ps},{af},{paf})")
#     db.commit()


def inser(a, e, pe, ec, pec, j, pj, s, ps, af, paf):
    cr.execute("INSERT INTO projets (id, education, Peducation, economie, Peconomie, junesse, Pjeunesse, sante, Psante, afaireEtrang, PafaireEtrang) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(a, e, pe, ec, pec, j, pj, s, ps, af, paf))
    db.commit()
