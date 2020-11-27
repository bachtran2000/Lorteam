from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import sqlite3
import pandas as pd
from pymessenger.bot import Bot
import requests

app = Flask(__name__)
api = Api(app)
ACCESS_TOKEN = 'EAAR9Xg2Dnu4BAN4eotC3Ol7WY5VAbEN550s1vh63NbhhIzGBgZBZAmHbgJ6QbldoD2FGJ5UZCAWZByQVB4nVLkpsfBx2fz3bk1s8jZAWBEcLFQALICvdo1EoEkidOc8zv3IyzxlK4mUjKs1xxtnALZCwtZC6HmZAKUZB29CGYQiHPnAsBvZCVW5SMg'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

# We will receive messages that Facebook sends our bot at this endpoint
negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop", '0')
count = 0
requestND = ''


@app.route('/timthongtin')
def timthongtin(one=False):
    input = request.args.to_dict()
    sql_query = ''



    if 'DienTich' in input:
        print(input['DienTich'])
        if input['DienTich'] != '':
            DienTich = input['DienTich']
            dau = int(int(DienTich) * 0.85)
            cuoi = int(int(DienTich) * 1.15)
            sql_query = f"select  * from data01 where ({DienTich} > {dau} and {DienTich} < {cuoi})"
            print(sql_query)
    if 'Quan' in input:
        if input["Quan"] != "":
            Quan = input['Quan']
            add_Quan = f" and Quan = \'{Quan}\'  "
            sql_query += add_Quan
    if 'SoPhongNgu' in input:
        if input['SoPhongNgu'] != '':
            SoPhongNgu = input['SoPhongNgu']
            add_SoPhongNgu = f" and SoPhongNgu = \'{SoPhongNgu}\' "
            sql_query += add_SoPhongNgu
    if 'SoToilet' in input:
        if input["SoToilet"] != "":
            SoToilet = input['SoToilet']
            add_SoToilet = f" and SoToilet = \'{SoToilet}\' "
            sql_query += add_SoToilet
    if 'HuongNha' in input:
        if input["HuongNha"] != "":
            HuongNha = input['HuongNha']
            add_HuongNha = f" and HuongNha = \'{HuongNha}\' "
            sql_query += add_HuongNha
    if 'HuongBanCong' in input:
        if input["HuongBanCong"] != "":
            HuongBanCong = input['HuongBanCong']
            add_HuongBanCong = f" and HuongBanCong = \'{HuongBanCong}\' "
            sql_query += add_HuongBanCong
    if 'NoiThat' in input:
        if input["NoiThat"] != "":
            NoiThat = input['NoiThat']
            add_NoiThat = f" and NoiThat = \'{NoiThat}\' "
            sql_query += add_NoiThat
    if 'ChuDauTu' in input:
        if input["ChuDauTu"] != "":
            ChuDauTu = input['ChuDauTu']
            add_ChuDauTu = f" and ChuDauTu = \'{ChuDauTu}\' "
            sql_query += add_ChuDauTu
    sql_query += " limit 10"
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


@app.route('/fb', methods=['GET', 'POST'])
def receive_message():
    global count
    print('BẮT ĐẦU REQUEST MỚI')
    # if request.method == 'GET':
    #     """Before allowing people to message your bot, Facebook has implemented a verify token
    #     that confirms all requests that your bot receives came from Facebook."""
    #     token_sent = request.args.get("hub.verify_token")
    #     return verify_fb_token(token_sent)
    # # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    # else:
    # get whatever message a user sent the bot
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        output = request.get_json()
        print(output)
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                print(message.get('message'))
                if message.get('message'):
                    recipient_id = message['sender']['id']

                    if message['message'].get('text'):
                        print(" trước khi vào vog if >>>>>>>>>>>>>>>>>>>>>>>")
                        print(message['message'].get('text'))
                        Tin_nhan = message['message'].get('text')
                        CHECK = Tin_nhan.find('DienTich=', 0, len(Tin_nhan))
                        if CHECK == 0:
                            response_sent_text = get_message_after(message['message'].get('text'))
                            send_message(recipient_id, response_sent_text)
                        else:
                            response_sent_text = get_message(message['message'].get('text'))
                            send_message(recipient_id, response_sent_text)
                        # if user sends us a GIF, photo,video, or any other non-text item
                        # if message['message'].get('attachments'):
                        #     response_sent_nontext = get_message(user_response='a')
                        #     send_message(recipient_id, response_sent_nontext)

    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


# chooses a random message to send to the user


def get_message(user_response):
    global count

    print("get_message000000000000000")
    print("COUNT = %d" % count)
    print('user_response = %s' % user_response)
    # return selected item to the user
    if user_response in negative_responses:
        # return "cảm ơn, chúc bạn một ngày tốt lành!!!"

        return user_response
    elif user_response in exit_commands:
        count = 0
        return "tạm biệt, hẹn gặp lại!!!"
    elif user_response.find('DienTich', 0, len(user_response)) == -1 and user_response[0] != '1':
        count = 0
        return "xin chào, đây là Chatbot dự đoán giá. Nhập 1 để chọn dự đoán, nhập 0 để thoát"
    elif user_response[0] == "1":
        count = 1
        print('1 xuat hiện ở trong vòng if')
        print(count)
        return 'Nhập theo mẫu sau để dự đoán: DienTich=..., SoPhongNgu=..., Quan=..., SoToilet= ...'




    else:
        return "Sửa lại code đi :v "
    # if count == 1:
    #     if user_response.find('apartment/?', 0, len(user_response)) != -1:
    #         rq = requests.get("http://18.139.111.217:5000/apartment/?DienTich=90&SoToilet=2&SoPhongNgu=3")
    #         print('ccccccccccccccccc')
    #         print(count)
    #         gia_nha = rq.json()
    #         return "Cho nay la cua json"
    print("bbbbbb")
    print(count)
    return "Co loi xay ra"


def get_message_after(user_response):
    global count
    print("count after = %s" % count)
    # return selected item to the user
    print('get_message_after11111111111111111')
    print("COUNT = %d" % count)
    print('user_response = %s' % user_response)

    link = 'http://18.139.111.217:5000/apartment/?'
    input = user_response
    input = input.replace(" ", "")
    input = input.replace(",", "&")
    input = input.replace("HaiBàTrưng", "Hai Bà Trưng")
    input = input.replace("ĐốngĐa", "Đống Đa")



    link_rq = link + input

    print(" link nhu sau: ><")
    print(link_rq)
    rq = requests.get(link_rq)

    print('ccccccccccccccccc')
    print(link_rq)
    print(count)
    gia_nha = rq.json()
    gia = gia_nha[0:len(gia_nha) - 8]
    return 'Giá dự đoán là: %s triệu/m2' % gia


# uses PyMessenger to send response to user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


@app.route("/quan")
def quan():
    df = pd.read_csv("ToaDoQuan.csv")
    return df.to_json()


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0',port=5002,debug=True)
