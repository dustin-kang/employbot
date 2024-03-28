<center>
<img src="https://github.com/f-lab-edu/employbot/assets/55238671/45e8bb0b-7a2f-4c0d-a940-a88622635c24" width=600>
</center>

# Slack API를 이용한 취업봇 만들기
취업봇은 개발하는 개발자분들이 자주 이용하는 Slack 채널에서 취업 및 이직 준비를 빠르고 쉽게 도와드리기 위해 만들어진 봇입니다.

취업봇을 통해 **구직 정보를 빠르게 찾아볼 수 있습니다.**

## 💻 기술 스택
- Python
- FAST API, uvicorn
- Slack API
- AWS EC2 (Ubuntu 22.04, Nginx

## ⚒️ 기능
- 잡코리아, 사람인, 원티드, 인디드 등의 구직 사이트내 직업 검색
- 클라이언트와 양방향을 실시간 통신을 위해 Uvicorn 웹 프레임워크 사용
- AWS EC2 Ubuntu 22.04로 배포 구현 **현재 종료**

<center>
<img src="https://user-images.githubusercontent.com/55238671/277393027-d771b39d-0dfc-4ac3-b1fb-d4a569a868c5.gif" width=300>
</center>

- 세부적인 포지션을 이용해 검색하는 방법과 간단한 통합 검색으로 다양한 취업 정보 사이트 URL를 연결해주는 기능이 있습니다.
- Slack API를 이용함으로써 BlockKit을 이용할 수 있어 부족한 프론트엔드 부분의 시간 비용을 덜어줄 수 있었다는 점입니다. 

## 🏗️ 아키텍처
<center>
<img width="800" alt="image" src="https://github.com/dustin-kang/employbot/assets/155930071/0a143c6c-ba11-412b-b3f7-bde563763b5a">
</center>

## 👨‍💻 피드백
### 후기
이번 프로젝트를 통해 Django 프레임워크와 다른 경량 프레임워크를 사용함으로 써 비교적 간결하게 코드를 작성할 수 있었고 중복된 코드를 제거하거나 함수를 재구성할 때 복잡함을 덜할 수 있었습니다.

## 📝 개발 일지
https://dongwooblog.tistory.com/124
