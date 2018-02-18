from bottle import route, run, request, template
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
        return "SUCCESS"
    else:
        # GETアクセスならフォームの表示
        return template("add_tmpl")


run(reloader=True, host='localhost', port=8080)
