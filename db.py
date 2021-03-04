from pymysql import connect


db = connect(
    "localhost",
    "root",
    "1234",
    "clientes"
)


