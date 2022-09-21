# Web Todo List 项目

## 1.项目背景

​		本项目提供了待办事项的新增、删除、更改以及查询服务，方便使用者完成日常事项的记录与查看。本项目基于Python语言开发，采用Flask后端框架，通过MySQL数据库存储待办事项描述及其截止时间。

## 2.项目部署

### 项目开发环境

| 名称   | 所需版本 |
| ------ | -------- |
| MySQL  | 8.0.24   |
| Python | 3.8.5    |
| Flask  | 2.0.3    |

### MySQL数据库初始化

打开CreateDatabaseAndTable.sql，运行其中SQL语句，实现建库建表，以完成数据库初始化。

### Python后端连接本地MySQL

请根据本地MySQL配置，修改app.py中的如下代码：

```python
conn = pymysql.connect(
    host='127.0.0.1',  
    user='root',  # 用户名
    password='root', # 密码
    port=3306,   # MySQL服务端口
    db='todo',   # 连接的数据库
    charset='utf8mb4'  # 字符集
)
```

### 项目运行方式

运行app.py，在浏览器键入网址进入项目：http://127.0.0.1:5000

## 3.项目结构说明

文件CreateDatabaseAndTable.sql提供了建库、建表的基本SQL语句。

文件app.py提供了Flask框架的Python语言后端服务。

\FlaskTodoProject\templates\index.html为项目主页，内有新增代办功能、检索框以及当前所有待办列表。

\FlaskTodoProject\templates\edit.html为待办事项更改页，能够修改待办事项的描述或者截止日期。

\FlaskTodoProject\templates\select.html为检索功能结果页面，能够显示精确查询结果，暂不提供模糊查询。

## 4.后续更新计划

1.模糊查询功能：采用搜索引擎Elasticsearch以提供良好的模糊查询性能。

2.单元测试。

3.已过期事项添加删除线：~~这是演示已被删除的事项。~~

4.按时间段查询功能。

5.添加事项时，前段添加滑轮选择时间。





