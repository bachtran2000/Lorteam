from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import sqlite3

app = Flask(__name__)
api = Api(app)

#
# conn = sqlite3.connect('chinook.db')
# phải có dòng KHỞI TẠO CON TRỎ này trước khi .fetchall()
# cursor = conn.cursor()
# query = cursor.execute("select * employees")
# print({'employees': [i[0] for i in query.fetchall()]})

# conn = sqlite3.connect('Xanh.db')
# cursor = conn.cursor()
# query = cursor.execute("select SoPhongNgu,SoToilet from tripdata where SoToilet = '2 (phòng)' ")
# print(query.fetchall())

AA = 90
conn = sqlite3.connect('Xanh.db')
cursor = conn.cursor()
query = cursor.execute(
    "select DiaChi from tripdata where DienTich = 90 and  SoPhongNgu = 3 and SoToilet = 2 ")  # Dòng này thực hiện truy vấn và trả về json
#     return jsonify({'employees': [i[0] for i in query.fetchall()]})  # Tìm và thêm cột đầu tiên là Employee ID
# c = conn.cursor()
# em =  c.execute('SELECT top')ỉ
# import pandas as pd
ok = query.fetchall()
print(ok)


@app.route('/<dientich>/<sophongngu>/<sotoilet>')
def get(dientich=None, sophongngu=None, sotoilet=None):
    conn = sqlite3.connect('Xanh.db')
    cursor = conn.cursor()

    query = cursor.execute(
        f"select DiaChi from tripdata where DienTich = 90   and SoPhongNgu = {sophongngu} and SoToilet = {sotoilet} ")  # Dòng này thực hiện truy vấn và trả về json
    #     return jsonify({'employees': [i[0] for i in query.fetchall()]})  # Tìm và thêm cột đầu tiên là Employee ID
    # c = conn.cursor()
    # em =  c.execute('SELECT top')ỉ
    # import pandas as pd
    ok = query.fetchall()
    return jsonify(ok)


@app.route('/<ho>/<ten>', methods=['GET'])
def test(ho=None, ten=None):
    # em =  c.execute('SELECT top')ỉ
    # import pandas as pd

    return jsonify(ok)


if __name__ == '__main__':
    app.run(debug=True)
