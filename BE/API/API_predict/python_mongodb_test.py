
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import pandas as pd
import numpy as np
import pickle
import locale
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Apartment'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Apartment'

mongo = PyMongo(app)

data = pd.read_csv("data_model_20_11.csv", index_col=None)


model = pickle.load(open('random_forest_model.pkl', 'rb'))


@app.route('/house/', methods=['GET'])
def get_all_stars():
	input = request.args.to_dict()
	
	if 'DienTich' in input:
		DienTich = input['DienTich']
		print(DienTich)
		DienTich = float(DienTich)
	if 'SoPhongNgu' in input:
		SoPhongNgu = input['SoPhongNgu']
		if(SoPhongNgu == ''):
			SoPhongNgu = data['SoPhongNgu'].mean()
		else:
			SoPhongNgu = int(SoPhongNgu)
	if 'SoToilet' in input:
		SoToilet = input['SoToilet']
		if(SoToilet == ''):
			SoToilet = data['SoToilet'].mean()
		else:
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
		if HuongNha == '':
			HuongNha = data['HuongNha'].mean()
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
		if HuongBanCong == '':
			HuongBanCong = data['HuongBanCong'].mean()
	else:
		HuongBanCong = data['HuongBanCong'].mean()
	if 'NoiThat' in input:
		NoiThat = input['NoiThat']
		if(NoiThat == ''):
			NoiThat = data['NoiThat'].mean()
		else:
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
		if(KinhDo == ''):
			KinhDo = data['KinhDo'].mean()
		else:
			KinhDo = int(KinhDo)
	else:
		KinhDo = data['KinhDo'].mean()
	if 'ViDo' in input:
		ViDo = input['ViDo']
		if(ViDo == ''):
			ViDo = data['ViDo'].mean()
		else:
			ViDo = int(ViDo)
	else:
		ViDo = data['ViDo'].mean()
	if 'LoaiTin' in input:
		LoaiTin = input['LoaiTin']
		if(LoaiTin == ''):
			LoaiTin = data['LoaiTin'].mean()
		else:
			LoaiTin = int(LoaiTin)
	else:
		LoaiTin = data['LoaiTin'].mean()
	
	find_one = data[(data['DienTich']== DienTich)&(data['Quan']==Quan )&(data['ChuDauTu']==ChuDauTu)]

	find_one.drop(columns = {'Index','TieuDe','url','HinhAnh','MoTa','NgayDang','DienThoai'},axis=1,inplace=True)
	find_one = find_one.to_json()
	return jsonify(find_one)

@app.route('/apartment/', methods=['GET'])
def get_predict():
	input = request.args.to_dict()
	
	if 'DienTich' in input:
		DienTich = input['DienTich']
		print(DienTich)
		DienTich = float(DienTich)
	if 'SoPhongNgu' in input:
		SoPhongNgu = input['SoPhongNgu']
		if(SoPhongNgu == ''):
			SoPhongNgu = data['SoPhongNgu'].mean()
		else:
			SoPhongNgu = int(SoPhongNgu)
	else:
		SoPhongNgu = data['SoPhongNgu'].mean()
	if 'SoToilet' in input:
		SoToilet = input['SoToilet']
		if(SoToilet == ''):
			SoToilet = data['SoToilet'].mean()
		else:
			SoToilet = int(SoToilet)
	else:
		SoToilet = data['SoToilet'].mean()
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
		if HuongNha == '':
			HuongNha = data['HuongNha'].mean()
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
		if HuongBanCong == '':
			HuongBanCong = data['HuongBanCong'].mean()
	else:
		HuongBanCong = data['HuongBanCong'].mean()
	if 'NoiThat' in input:
		NoiThat = input['NoiThat']
		if(NoiThat == ''):
			NoiThat = data['NoiThat'].mean()
		else:
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
		if(KinhDo == ''):
			KinhDo = data[data['Quan'] == Quan]['KinhDo'].mean()
		else:
			KinhDo = float(KinhDo)
	else:
		KinhDo = data['KinhDo'].mean()
	if 'ViDo' in input:
		ViDo = input['ViDo']
		if(ViDo == ''):
			ViDo = data[data['Quan'] == Quan]['ViDo'].mean()
		else:
			ViDo = float(ViDo)
	else:
		ViDo = data['ViDo'].mean()
	if 'LoaiTin' in input:
		LoaiTin = input['LoaiTin']
		if(LoaiTin == ''):
			LoaiTin = data['LoaiTin'].mean()
		else:
			LoaiTin = int(LoaiTin)
	else:
		LoaiTin = data['LoaiTin'].mean()
	

	ThongTin = [DienTich, SoPhongNgu, SoToilet,ChuDauTu,ViDo,KinhDo,NoiThat,LoaiTin,Quan,HuongNha,HuongBanCong]

	ThongTin = np.array(ThongTin)

	ThongTin = ThongTin.reshape(1, -1)

	dudoan = model.predict(ThongTin).tolist()

	dudoan = float(dudoan[0])/(DienTich*1e6)

	dudoan = round(dudoan,2)*1e6

	return jsonify(f"{dudoan:,}")


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
	app.run(host='0.0.0.0', port=5000, debug=True)
