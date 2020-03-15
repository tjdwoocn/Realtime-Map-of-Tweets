var mymap = L.map('mapid').setView([51.512, -0.104], 2);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoidGpkd29vY24iLCJhIjoiY2s3NGY5YzhiMDZkYjNsbnlodTM0NXkxbCJ9.EF87PivkJWkL5jOiE8cYww'
}).addTo(mymap);

// 새로운 event source 생성, busdata_seoul 이라는 topic 사용
var source = new EventSource('/topic/twitterdata');
// 새로운 메세지가 생성 될때마다 업데이트 해주기 위한 event listener 추가
source.addEventListener('message', function(e){
    // console에 메세지가 어떻게 전달되는지 보기위해 log 추가
    console.log('message');
    // 받은 log 데이터 json 형태로 파싱 후 log 기록
    obj = JSON.parse(e.data);
    console.log(obj);
    // 원하는 정보 변수에 저장
    lat = obj.place.bounding_box.coordinates[0][0][1];
    long = obj.place.bounding_box.coordinates[0][0][0];
    username = obj.user.name;
    time = obj.user.created_at;
    tweet = obj.text;
    
    // 마커 생성하기 (마커에 Username, Tweet, Time 정보 추가)
    marker - L.karker([lat, long],).addTo(mymap).bindPopup('Username: <strong>' + username + '</strong><br>Tweet: <strong>' + tweet + '</strong><br>Time: <strong>' + time + '</strong>')

},  false);