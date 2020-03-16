# 필요한 패키지들 임포트
# key 와 token 값 저장되어 있는 credentials 파일도 호출
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import credentials
from pykafka import KafkaClient
import json
import sys

# 카프카 클라이언트(broker)를 리턴하는 함수
def get_kafka_client():
    return KafkaClient(hosts = '127.0.0.1:9092')

# override tweepy.StreamListener to add logic to on_status
words = ['python', 'corona']
# 오버라이딩 함
class MyStreamListener(StreamListener):
    # 모든 메세지를 가져오는 'on_data' method 사용
    def on_data(self, data):
        print(data)
        # data 를 json 포맷으로 변경
        message = json.loads(data)
        print(message)
        # Place 태그에 데이터가 있는것만 가져오기
        if message['place'] is not None:
            # 카프카 클라이언트를 client 변수에 리턴
            client = get_kafka_client()
            # 'twitterdata' 토픽 호출
            topic = client.topics['twitterdata'] 
            # 해당 토픽에 데이터 produce 해주는 producer 생성
            producer = topic.get_sync_producer()
            # message 말고 data를 가져온 이유는 json형태로 load 된 것 말고 오리지널 데이터를 가져오기 위해
            producer.produce(data.encode('utf8')) # 카프카 데이터는 byte로 나오기 떄문에 encode 필요
        return True


    # 오류메세지 출력
    def on_error(self, status):
        print(status)


# 언제든지 이 파일을 실행하면 auth 객체 불러오기
if __name__ == "__main__":    
    auth = OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY )
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

    # Listener 호출
    listener = MyStreamListener()
    Stream = Stream(auth, listener)
    # 해당 단어가 들어가는 tweet들 stream
    # 아래의 locations 옵션은 전세계의 모든 tweets 를 확인하는 방법
    # Stream.filter(locations=[-180,-90,180,90])
    Stream.filter(track=['python'])