from bottle import route, run, request, redirect, template
import sqlite3


@route("/")
def index():
    return "<h1>WELCOME!!</h1>"


# アイテム一覧
@route("/list")
def view_list():
    # items.sqlite3 に接続
    connectdb = sqlite3.connect('items.sqlite3')
    concursor = connectdb.cursor()
    concursor.execute("select id,name from items order by id")
    item_list = []
    for row in concursor.fetchall():
        item_list.append({
            "id": row[0],
            "name": row[1]
        })
        connectdb.close()
    return template("list_tmpl", item_list=item_list)


@route("/add", method=["GET", "POST"])
def add_item():
    if request.method == "POST":
        # POSTアクセスならDBに登録する
        # フォームから入力(POST)されたアイテム名(データ)の取得
        item_name = request.POST.getunicode("item_name")
        connectdb = sqlite3.connect('items.sqlite3')
        concursor = connectdb.cursor()
        # 現在の最大IDの取得(fetchoneの戻り値はタプル)
        new_id = concursor.execute("select max(id)+1 from items").fetchone()[0]
        concursor.execute('insert into items values (?,?)', (new_id, item_name))
        connectdb.commit()
        connectdb.close()
        return "<br>SUCCESS</br> <a href='/list'>一覧表示</a>"
    else:
        # GETアクセスならフォームの表示
        return template("add_tmpl")


# ルーティングを数字で制限
@route("/del/<item_id:int>")
def del_item(item_id):
    connectdb = sqlite3.connect('items.sqlite3')
    concursor = connectdb.cursor()
    # 指定されたitem_idを元にDBデータを削除(delete文)
    concursor.execute("delete from items where id=?", (item_id, ))
    connectdb.commit()
    connectdb.close()
    # 削除処理後にリスト画面へ戻す
    return redirect("/list")


run(reloader=True, host='localhost', port=8080)
