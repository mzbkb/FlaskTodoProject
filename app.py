from flask import Flask, request, redirect
import pymysql
from flask import render_template

app = Flask("代办项目网站")

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',  # 用户名
    password='root',  # 密码
    port=3306,  # MySQL服务端口
    db='todo',  # 连接的数据库
    charset='utf8mb4'  # 字符集
)


def insert_to_db(description, deadline):
    """新增待办项"""
    sql = f"""
        insert into todo_list
        (description, deadline)
        values ('{description}', '{deadline}')
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def update_db(id, description, deadline):
    """更新待办项"""
    sql = f"""
        update todo_list
        set description ='{description}', deadline = '{deadline}'
        where id={id}
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def query_data():
    """查询所有当前待办事项"""
    sql = """
        select * 
        from todo_list
        order by deadline asc
    """
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()


def query_keyword_data(keyword):
    """依据关键词查询待办事项"""
    sql = f"""
        SELECT * 
        FROM todo_list
        WHERE description LIKE '%{keyword}%'
        ORDER BY deadline ASC
    """
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()


def query_single_data(id):
    """查询单条待办数据"""
    sql = f"""
        select * 
        from todo_list
        where id = {id}
    """
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchone()


def delete_db(id):
    """删除待办项"""
    sql = f"""
        delete 
        from todo_list
        where id={id}
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


@app.route("/edit", methods=["GET", "POST"])
def edit():
    # url内部的东西由 request.args.get 取得
    id = request.args.get("id")
    data = query_single_data(id)

    if request.method == "POST":
        description = request.form.get("description")
        deadline = request.form.get("deadline")
        update_db(id, description, deadline)
        # 更新完数据后，重定向至首页，展示新的列表
        return redirect("/")

    return render_template("edit.html", data=data)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        description = request.form.get("description")
        deadline = request.form.get("deadline")
        insert_to_db(description, deadline)

    datas = query_data()
    return render_template("index.html", datas=datas)


@app.route("/delete", methods=["GET"])
def delete():
    id = request.args.get("id")
    delete_db(id)
    datas = query_data()
    return render_template("index.html", datas=datas)


@app.route("/select", methods=["GET", "POST"])
def select():
    keyword = request.args.get("keyword")
    keyword_datas = query_keyword_data(keyword)
    return render_template("select.html", keyword_datas=keyword_datas)


app.run(debug=True)
