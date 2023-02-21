import sqlite3

con=sqlite3.connect("filmler.db")

cursor=con.cursor()

def tabloolusturma(tabloAdi):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {tabloAdi}(FİLM ADI TEXT,YÖNETMEN TEXT)")
    con.commit()

def tabloyaveriekleme(filmadi,yonetmenadi):
    cursor.execute(f"INSERT INTO FİLM_KEYFİ VALUES(?,?)",(filmadi,yonetmenadi))
    con.commit()

def vericekme():
    cursor.execute("SELECT* FROM FİLM_KEYFİ")
    veriler=cursor.fetchall()
    list
    for i in veriler:
        print(i)

def veriguncelleme():
    cursor.execute("UPDATE FİLM_KEYFİ SET YÖNETMEN='YAŞO',FİLM='YAŞO' ")
    con.commit()

def verisilme():
    cursor.execute("DELETE from FİLM_KEYFİ")
    con.commit()

tabloolusturma("FİLM_KEYFİ")
tabloyaveriekleme("yenilmezler","YAŞAR gormanç")
veriguncelleme()
verisilme()
vericekme()
con.close()
