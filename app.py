from bottle import route, run


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
    # 表示用のHTMLファイルを組み立て
    display_html = "<table border='1'>"
    for item in item_list:
        display_html += "<tr>"
        display_html += "<td>{}</td>".format(item["id"])
        display_html += "<td>{}</td>".format(item["name"])
        display_html += "</tr>"
    display_html += "</table>"
    return display_html


run(reloader=True, host='localhost', port=8080)
