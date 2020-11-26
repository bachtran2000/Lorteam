from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
import sqlite3
import pandas as pd
from pymessenger.bot import Bot
import requests

app = Flask(__name__)
api = Api(app)
ACCESS_TOKEN = 'EAAR9Xg2Dnu4BAJf1j8YCObxHac5aW2l61UZCs9w52iCzTTkTEJxc0Uh6dLQIXJgOPaW0lhdvcTJv0YK84QuMMI6rFmOex5Olk6jtNn2b5jIJ9Qm9MqnnSzGVUtSwRPcZC36rP3UdXuaEq0pbik4ar1Is5a5BrH9MhU3iyzEPBtRpegWylI'
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
        DienTich = input['DienTich']
        dau = int(int(DienTich) * 0.98)
        cuoi = int(int(DienTich) * 1.02)
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
                        CHECK = Tin_nhan.find('apartment/?', 0, len(Tin_nhan))
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
    elif user_response.find('apartment/?', 0, len(user_response)) == -1 and user_response[0] != '1':
        count = 0
        return "xin chào, đây là Chatbot dự đoán giá. Nhập 1 để chọn dự đoán, nhập 0 để thoát"
    elif user_response[0] == "1":
        count = 1
        print('1 xuat hiện ở trong vòng if')
        print(count)
        return 'Nhập theo mẫu sau để dự đoán: apartment/?DienTich=...&SoPhongNgu=...&Quan=...'




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

    link = 'http://18.139.111.217:5000/'
    link_rq = link + user_response
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
    app.run(host='0.0.0.0',port=5001,debug=True)
