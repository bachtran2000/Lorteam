
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import sqlite3

app = Flask(__name__)
api = Api(app)

@app.route('/timthongtin')
def timthongtin(one = False):
    input = request.args.to_dict()
    sql_query = ''

    if 'DienTich' in input:
        DienTich = input['DienTich']
        dau = int(int(DienTich)*0.98)
        cuoi = int(int(DienTich)*1.02)
        sql_query = f"select * from data01 where (DienTich > {dau} and DienTich < {cuoi})"
    if 'Quan' in input:
        Quan = input['Quan']
        if Quan != '-1':
            add_Quan = f" and Quan = \'{Quan}\'  "
            sql_query += add_Quan
    if 'SoPhongNgu' in input:
        SoPhongNgu = input['SoPhongNgu']
        if SoPhongNgu != '-1':
            add_SoPhongNgu = f" and SoPhongNgu = \'{SoPhongNgu}\' "
            sql_query += add_SoPhongNgu
    if 'SoToilet' in input:
        SoToilet = input['SoToilet']
        if SoToilet != '-1':
            add_SoToilet = f" and SoToilet = \'{SoToilet}\' "
            sql_query += add_SoToilet
    if 'HuongNha' in input:
        HuongNha = input['HuongNha']
        if HuongNha != '-1':
            add_HuongNha = f" and HuongNha = \'{HuongNha}\' "
            sql_query += add_HuongNha
    if 'HuongBanCong' in input:
        HuongBanCong = input['HuongBanCong']
        if HuongBanCong != '-1':
            add_HuongBanCong = f" and HuongBanCong = \'{HuongBanCong}\' "
            sql_query += add_HuongBanCong
    if 'NoiThat' in input:
        NoiThat = input['NoiThat']
        if NoiThat != '-1':
            add_NoiThat = f" and NoiThat = \'{NoiThat}\' "
            sql_query += add_NoiThat
    if 'ChuDauTu' in input:
        ChuDauTu = input['ChuDauTu']
        if ChuDauTu != '-1':
            add_ChuDauTu = f" and ChuDauTu = \'{ChuDauTu}\' "
            sql_query += add_ChuDauTu

# ### CONNECT DATA
    conn = sqlite3.connect('xa01.db')
    cur = conn.cursor()
    query = cur.execute(sql_query)
    r = [dict((cur.description[i][0], value) \
              for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    kq = (r[0] if r else None) if one else r
    ok = dumps(kq)
    return ok


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
