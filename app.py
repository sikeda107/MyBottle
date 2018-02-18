from bottle import route, run, template
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


run(reloader=True, host='localhost', port=8080)
