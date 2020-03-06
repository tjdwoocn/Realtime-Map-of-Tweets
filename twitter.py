# 필요한 패키지들 임포트
# key 와 token 값 저장되어 있는 credentials 파일도 호출
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import credentials

# override tweepy.StreamListener to add logic to on_status
# 오버라이딩 함
class MyStreamListener(StreamListener):
    # 모든 메세지를 가져오는 'on_data' method 사용
    def on_data(self, data):
        print(data)
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
    Stream.filter(track=['PythonSJ'])
