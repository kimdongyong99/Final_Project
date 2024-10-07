# 💪🏻 핏한 하루 🏃‍♂️

# 🗓️ 개발 기간 
2024.09.23 ~ 2024.10.24

# 👩🏻‍💻 프로젝트 개요
핏한 하루는 스파르타 코딩클럽 부트캠프의 최종 팀 프로젝트입니다.
AI 기반의 맞춤형 식단 및 운동 계획을 제공하는 다이어트 관리 플랫폼으로 건강한 라이프스타일을 쉽게 실천할 수 있도록 돕습니다.

## 🤖 주요 기능
- 맞춤형 추천 : 이용자는 챗봇을 통해 자신의 몸무게, 키, 골격근량, 체지방량 등 정보를 입력하면 개인에 맞는 식단과 운동 계획을 추천받을 수 있습니다.
- 건강 뉴스 제공 : 이용자는 최신 건강 관련 뉴스를 확인할 수 있으며, 관심 있는 뉴스에 좋아요를 눌러 자신의 관심사를 표현할 수 있습니다.
- 자유게시판 : 이용자는 자유게시판을 통해 다른 이용자들과 소통하고 경험을 나누는 공간을 제공합니다.

# 💻 개발 환경
[🔗 종합병원-notion](https://teamsparta.notion.site/fff2dc3ef514811e9f89dc2cfad3ea37)
|Programming Language| python 3.10|
|:----------------:|:----------------:|
| Web Framework | Django 4.2|
| Database | SQLite|
| IDE | PyCharm, Vs code |
| Version Control | Git, Github |
| Communication | Zep, Notion, Slack|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap, JS |
| Database | Django ORM, SQLite |

# 🧑‍🧑‍🧒‍🧒 개발팀

👑 김동용(팀장)
- 댓글기능 구현
- Chat GPT 구현
- 백엔드 및 프론트엔드 구현

👤 김나현
- 프로필기능 구현
- 소셜로그인 구현
- 백엔드 및 프론트엔드 구현

👤 이규호
- 회원기능 및 이메일 인증 구현
- 뉴스크롤링 구현
- 결제페이지 구현
- 백엔드 및 프론트엔드 구현

👤 이예지
- 게시글 기능구현
- 결제페이지 구현
- 백엔드 및 프론트엔드 구현

# 🧬 디펙토리 구조
| Structure| Function|
|:----------------:|----------------|
| A_FIT_DAY | 프로젝트 설정 및 초기화 파일 |
| accounts | 사용자 인증 . 및 계정 관리 기능 |
| articles | main page 뉴스기사 |
| chatgpt | ChatGPT 검색기능 |
| media | 이미지 저장 |
| posts |  게시물 생성, 수정, 삭제, 검색 |

# 📌 프로젝트 특징
## 1. 계정[멤버십 기능]
- 회원가입 : 사용자는 자신의 ID와 비밀번호로 계정을 만들 수 있습니다.
- 로그인 : 기존 사용자는 등록된 ID와 비밀번호로 로그인할 수 있습니다.
- 로그아웃 : 사용자는 로그아웃을 통해 안전하게 계정을 종료할 수 있습니다.
- 소셜로그인 : 사용자는 카카오등 사용하는 소셜로 로그인을 할 수 있습니다.
- 회원 정보 수정: 사용자는 자신의 계정 정보를 업데이트 할 수 있습니다.
- 프로필 : 사용자는 프로필 기능에서 자신이 좋아하는 게시물, 기사, 작성한 게시물을 확인할 수 있습니다.
- 프로필 수정 : 사용자는 프로필 정보를 업데이트 할 수 있습니다. 


## 2. Articles 
- 뉴스 크롤링 : 사용자는 서비스 제공자가 추천한 기사를 확인할 수 있습니다.
- 검색 기능 : 서비스 제공자가 추천한 기사글을 검색할 수 있습니다.


## 3. post (자유게시판)
- 쓰기 및 등록: 사용자는 객체에 대한 설명을 작성하고 게시할 수 있습니다.
- 텍스트 수정: 등록된 텍스트의 내용을 수정할 수 있습니다.
- 텍스트 삭제: 사용자는 자신의 게시물을 삭제할 수 있습니다.
- 개별 세부 정보 페이지(글쓰기 조회): 사용자는 특정 게시물의 세부 정보를 조회할 수 있습니다.
- 조회수: 게시물이 얼마나 많이 조회되었는지 볼 수 있습니다.
- 스팀(좋아요): 사용자는 관심 있는 게시물을 스팀할 수 있습니다.
- 검색 기능: 다양한 기준으로 게시물을 검색할 수 있습니다.

## 4. Chat Bot
- 사용자는 AI 서비스를 이용해 원하는 정보를 검색할 수 있습니다.
- 사용자는 AI 서비스를 이용해 원하는 정보의 결과를 받을 수 있습니다.


# 📃 ERD 다이어그램
![image](https://github.com/user-attachments/assets/bd8106f2-eeb4-4802-8846-853dc68824ac)


# 📃 와이어프레임
![image](https://github.com/user-attachments/assets/aa611206-2ea7-4b22-bdd2-ee221e6b42e9)

