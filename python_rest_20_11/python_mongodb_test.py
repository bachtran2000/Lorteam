
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Apartment'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Apartment'

mongo = PyMongo(app)

data = pd.read_csv("data_model_20_11.csv", index_col=None)



model = pickle.load(open('random_forest_model.pkl', 'rb'))


@app.route('/apartment', methods=['GET'])
def get_all_stars():

    apartment = mongo.db.Apartment
    output = []
    dodai = apartment.count()
    for h in apartment.find({'DienTich': 74.5}):
        output.append({'title': h['TieuDe'], 'Giá': h['GiaTien'], 'Diện tích': h['DienTich'],
                       'Số Phòng Ngủ': h['SoPhongNgu'], 'Số Toilet': h['SoToilet']})
    return jsonify(output)


@app.route('/apartment/', methods=['GET'])
def get_one_star():
    input = request.args.to_dict()
    
    if 'DienTich' in input:
        DienTich = input['DienTich']
        print(DienTich)
        DienTich = float(DienTich)
    if 'SoPhongNgu' in input:
        SoPhongNgu = input['SoPhongNgu']
        SoPhongNgu = int(SoPhongNgu)
    if 'SoToilet' in input:
        SoToilet = input['SoToilet']
        SoToilet = int(SoToilet)
    if 'HuongNha' in input:
        HuongNha = input['HuongNha']
        if HuongNha == 'Đông':
            HuongNha = int(1)
        if HuongNha == 'Tây':
            HuongNha = int(2)
        if HuongNha == 'Nam':
            HuongNha = int(3)
        if HuongNha == 'Bắc':
            HuongNha = int(4)
        if HuongNha == 'Đông-Bắc':
            HuongNha = int(5)
        if HuongNha == 'Đông-Nam':
            HuongNha = int(6)
        if HuongNha == 'Tây-Bắc':
            HuongNha = int(7)
        if HuongNha == 'Tây-Nam':
            HuongNha = int(8)
    else:
        HuongNha = data['HuongNha'].mean()
    if 'HuongBanCong' in input:
        HuongBanCong = input['HuongBanCong']
        if HuongBanCong == 'Đông':
            HuongBanCong = int(1)
        if HuongBanCong == 'Tây':
            HuongBanCong = int(2)
        if HuongBanCong == 'Nam':
            HuongBanCong = int(3)
        if HuongBanCong == 'Bắc':
            HuongBanCong = int(4)
        if HuongBanCong == 'Đông-Bắc':
            HuongBanCong = int(5)
        if HuongBanCong == 'Đông-Nam':
            HuongBanCong = int(6)
        if HuongBanCong == 'Tây-Bắc':
            HuongBanCong = int(7)
        if HuongBanCong == 'Tây-Nam':
            HuongBanCong = int(8)
    else:
        HuongBanCong = data['HuongBanCong'].mean()
    if 'NoiThat' in input:
        NoiThat = input['NoiThat']
        NoiThat = int(NoiThat)
    else:
        NoiThat = data['NoiThat'].mean()
    if 'ChuDauTu' in input:
        ChuDauTu = input['ChuDauTu']
        ChuDauTu_DB = mongo.db.ChuDauTu
        for c in ChuDauTu_DB.find():
            ChuDauTu = c[ChuDauTu]
            print(ChuDauTu)
    else:
        ChuDauTu = data['ChuDauTu'].mean()
    if 'Quan' in input:
        Quan = input['Quan']
        Quan_DB = mongo.db.Quan
        for q in Quan_DB.find():
            Quan = q[Quan]
            print(Quan)
    else:
        Quan = data['Quan'].mean()
    if 'KinhDo' in input:
        KinhDo = input['KinhDo']
        KinhDo = float(KinhDo)
    else:
        KinhDo = data['KinhDo'].mean()
    if 'ViDo' in input:
        ViDo = input['ViDo']
        ViDo = float(ViDo)
    else:
        ViDo = data['ViDo'].mean()
    if 'LoaiTin' in input:
        LoaiTin = input['LoaiTin']
        LoaiTin = int(LoaiTin)
    else:
        LoaiTin = data['LoaiTin'].mean()
    

    apartment = mongo.db.Apartment
    output = []

    ThongTin = [DienTich, SoPhongNgu, SoToilet,ChuDauTu,ViDo,KinhDo,NoiThat,LoaiTin,Quan,HuongNha,HuongBanCong]

    ThongTin = np.array(ThongTin)

    ThongTin = ThongTin.reshape(1, -1)

    dudoan = model.predict(ThongTin).tolist()

    return jsonify(dudoan)


@app.route('/star', methods=['POST'])
def add_star():
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({'name': name, 'distance': distance})
    new_star = star.find_one({'_id': star_id})
    output = {'name': new_star['name'], 'distance': new_star['distance']}
    return jsonify({'result': output})


if __name__ == '__main__':
	app.run(host='18.139.111.217', port:5000, debug= True)
    app.run(debug=True)
