import sqlite3
db=sqlite3.connect("bas.db")
cr=db.cursor()
def afiche():
    cr.execute("select id from projets order by PVote desc ")
    l=cr.fetchall()
    ll1,ll2,ll3,ll4,ll5=l[0][0],l[1][0],l[2][0],l[3][0],l[4][0]
    lll1,lll2,lll3=test(ll1,ll2,ll3,ll4,ll5)
    cr.execute(f"select nom,prenom from condidats where id={lll1}")
    g=cr.fetchall()
    g1=g[0]
    cr.execute(f"select nom,prenom from condidats where id={lll2}")
    g=cr.fetchall()    
    g2=g[0]
    cr.execute(f"select nom,prenom from condidats where id={lll3}")
    g=cr.fetchall()
    g3=g[0]
    g11=str(g1[0]).upper()
    g12=str(g1[1]).capitalize()
    g21=str(g2[0]).upper()
    g22=str(g2[1]).capitalize()
    g31=str(g3[0]).upper()
    g32=str(g3[1]).capitalize()
    gg1="A la première place       :\t"+g11+"  "+g12
    gg2="A la deuxièmme place  :\t"+g21+"  "+g22
    gg3="A la troisièmme place :\t"+g31+"  "+g32

    return gg1,gg2,gg3
 
def test(id1, id2, id3, id4, id5):
    # Retrieve PVote values for the provided IDs
    cr.execute(f"SELECT id,PVote FROM projets WHERE id IN ({id1}, {id2}, {id3}, {id4}, {id5}) ORDER BY PVote DESC")
    k = cr.fetchall()
    kk1, kk2, kk3, kk4, kk5 = k[0][0], k[1][0], k[2][0], k[3][0], k[4][0]
    pv1,pv2,pv3,pv4,pv5=k[0][1], k[1][1], k[2][1], k[3][1], k[4][1]
    # Retrieve points values for the provided IDs
    cr.execute(f"SELECT id, points FROM condidats WHERE id IN ({kk1}) ")
    pp1 = cr.fetchall()[0]+(pv1,)
    cr.execute(f"SELECT id, points FROM condidats WHERE id IN ({kk2}) ")
    pp2 = cr.fetchall()[0]+(pv2,)
    cr.execute(f"SELECT id, points FROM condidats WHERE id IN ({kk3}) ")
    pp3 = cr.fetchall()[0]+(pv3,)
    cr.execute(f"SELECT id, points FROM condidats WHERE id IN ({kk4}) ")
    pp4 = cr.fetchall()[0]+(pv4,)
    cr.execute(f"SELECT id, points FROM condidats WHERE id IN ({kk5}) ")
    pp5 = cr.fetchall()[0]+(pv5,)

    
    return pp1[0], pp2[0], pp3[0]

def per(v1,v2):
    a=v1
    b=v2
    v1,v2=b,a
    return v1,v2        
def condition():    
    cr.execute("select id from  projets")
    bb=cr.fetchall()
    return len(bb)




