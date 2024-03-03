import sqlite3

db=sqlite3.connect("bas.db")
cr=db.cursor()

def veriffier(id):
    
        cr.execute(f"select id,nom,prenom from users where (id={id}) ")
        return cr.fetchall()
def verifier(i,n,p):
    cr.execute("select id from users")
    l=cr.fetchall()

    idl=(i,)

    if idl in l:
        a=veriffier(i)
        id,nom,prenom=a[0][0],a[0][1],a[0][2]
        if i==id and n==nom and p==prenom:
            return True

    


