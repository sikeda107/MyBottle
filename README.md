# MyBottle
Bottle official site: https://bottlepy.org/docs/dev/  
## INSTALLATION
`wget  https://bottlepy.org/bottle.py`  
or  
`sudo pip install bottle`

## References：
bottleで始めるWEBアプリの最初の一歩  
<https://www.slideshare.net/satoshiyamada71697/bottleweb>


## About Files：
bottle.py - bottleを使うために必要なもの  
app.py - アプリ本体  
make_db.py - sqlite3にデータを入れるためのもの  

## DB Operation：
1. `$python make_db.py` -- データの初期化
1. `$sqlite3 -- sqliteの起動`
1. `sqlite> .table`-- テーブルの一覧表示
1. `sqlite> .schema items` -- テーブルのスキーマを表示
1. `sqlite> SELECT * FROM items;` -- 全てのレコードを取得
1. `sqlite> .exit` -- sqliteの終了
