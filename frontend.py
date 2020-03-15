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
    # 웹화면에 보여줄 front (index.html) 작업 후 호출
    return(render_template('index.html'))

@app.route('/topic/<topicname>')
# 바로 위에서 가져온 topicname 넣어주기
def get_messages(topicname):
    client = get_kafka_client()
    # events 가 생성될 때 마다 client(broker)가 새로운 메세지를 consume 하도록
    def events():
        for message in client.topics[topicname].get_simple_consumer():
            # return 말고 generate 사용해야함 (yield)
            yield 'data:{0}\n\n'.format(message.value.decode())
    return (Response(events(), mimetype='text/event-stream'))

if __name__ =='__main__':
    # debug 부분을 True라고 해주면 위의 index 부분을 수정해줬을때 
    # 서버를 따로 재실행 하지 않고도 실시간으로 update 가능함 
    app.run(debug=True, port=5001)