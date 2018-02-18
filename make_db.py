import sqlite3

# items.dbに接続
connectdb = sqlite3.connect('items.sqlite3')
cdbcursor = connectdb.cursor()

# テーブルの作成
cdbcursor.execute("create table items(id,name)")

# データの挿入
cdbcursor.execute("insert into items values(1,'あいてむ')")
cdbcursor.execute("insert into items values(2,'アイテム')")
cdbcursor.execute("insert into items values(3,'item')")

# 確定
connectdb.commit()

# 閉じる
connectdb.close()
