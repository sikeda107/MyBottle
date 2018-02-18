from bottle import route, run, template


@route("/")
def index():
    return "<h1>WELCOME!!</h1>"


# アイテム一覧
@route("/list")
def view_list():
    item_list = [
        {"id": 1, "name": "あいてむ"},
        {"id": 2, "name": "アイテム"},
        {"id": 3, "name": "item"},
    ]
    return template("list_tmpl", item_list=item_list)


run(reloader=True, host='localhost', port=8080)
