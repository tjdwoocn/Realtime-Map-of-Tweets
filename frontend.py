from flask import Flask, jsonify, request, Response, render_template
from pykafka import KafkaClient
import json

# 로컬에서 실행되는 카프카 클라이언트 호출하는 함수 
def get_kafka_client():
    return KafkaClient(hosts = '127.0.0.1:9092')

# Flask 실행하는 app
app = Flask(__name__)

@app.route("/")
def index():
    return('LEAFLET MAP')

@app.route('/topic/<topicname>')
# 바로 위에서 가져온 topicname 넣어주기
def get_messages(topicname):
    client = get_kafka_client()
    def events():
        for 


if __name__ =='__main__':
    # debug 부분을 True라고 해주면 위의 index 부분을 수정해줬을때 
    # 서버를 따로 재실행 하지 않고도 실시간으로 update 가능함 
    app.run(debug=True, port=5001)