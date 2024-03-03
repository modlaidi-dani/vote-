import sqlite3 as sql

bdd = sql.connect("bas.db")
cr = bdd.cursor()

def recup():
    cr.execute("select * from idmin")
    return cr.fetchall()[0][0]
    

def inserer(v):

    cr.execute(f"update idmin Set adm={v}  ")
    bdd.commit()

def reset():
    cr.execute("delete from projets")
    bdd.commit()
    cr.execute("delete from condidats")
    bdd.commit()
    cr.execute("update users set pointVote=1 ")
    bdd.commit()


