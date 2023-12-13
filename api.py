from flask import Flask, request
from flask_restful import Api, Resource
import requests
import config
from main import get_token

app = Flask(__name__)
api = Api(app)

class getApi(Resource):

    def get(self):
        method = request.args.get('method')

        if method == "getReporter":
            id = request.args.get('id')
            testr = True
            data = requests.get(f"https://api.vk.com/method/bugtracker.getReportersById?access_token={config.main_token}&reporter_ids={id}&v=5.163").json()
            if data.get('error') is not None:
                config.main_token = get_token()
                data = requests.get(
                    f"https://api.vk.com/method/bugtracker.getReportersById?access_token={config.main_token}&reporter_ids={id}&v=5.163").json()
            if len(data['response']['items']) == 0:
                return {"message": "user not found"}
            if data['response']['items'][0]['status_text'] in ['Обычный пользователь', 'Не учавствует в программе VK Testers', 'Исключён из программы VK Testers', 'Вышел из программы VK Testers', 'Отклонил приглашение в программу', "Во вступлении в программу отказано", 'Вышла из программы VK Testers']:
                testr = False
            if data['response']['items'][0]['status_text'] not in ['Обычный пользователь', 'Не учавствует в программе VK Testers', 'Исключён из программы VK Testers', 'Вышел из программы VK Testers', 'Отклонил приглашение в программу', "Во вступлении в программу отказано", 'Вышла из программы VK Testers']:
                testr = True
            return {"response": {"reporter": {"id": id, "status_text": data['response']['items'][0]['status_text'], "reports_count": data['response']['items'][0]['reports_count'], "top_position": data['response']['items'][0]['top_position'], "tester": testr}}}
        else:
            return {"message": "method not passed or found"}


api.add_resource(getApi, "/vk-bugs-api/")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='3551', debug=False)

