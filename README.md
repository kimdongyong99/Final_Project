# 💪🏻 핏한 하루 🏃‍♂️

# 🗓️ 개발 기간 
2024.09.23 ~ 2024.10.24

# 👩🏻‍💻 프로젝트 개요
핏한 하루는 스파르타 코딩클럽 부트캠프의 최종 팀 프로젝트입니다.
AI 기반의 맞춤형 식단 및 운동 계획을 제공하는 다이어트 관리 플랫폼으로 건강한 라이프스타일을 쉽게 실천할 수 있도록 돕습니다.

# 💡아이디어, 기획

현대 사회에서 바쁜 일상 속에서도 건강한 라이프스타일을 유지하는 것은 매우 중요해졌습니다.
'핏한 하루'는 AI 기반의 맞춤형 식단 및 운동 계획을 통해, 사용자가 쉽고 편리하게 건강 관리를 실천할 수 있도록 돕기 위해 기획되었습니다.
단순한 다이어트가 아닌, 지속 가능한 건강 습관을 형성하고 이를 통해 더 나은 삶의 질을 추구하는 것이 목표입니다.개인의 신체 상태와 목표에 맞춘 맞춤형 솔루션으로, 누구나 쉽게 건강한 하루를 만들 수 있는 플랫폼을 제공합니다.

## 🤖 주요 기능
- AI 맞춤형 식단 및 운동 추천 : AI를 활용하여 사용자의 건강 데이터(나이, 성별, 신체 정보, 활동 수준, 식습관, 건강 목표 등)를 기반으로 개인 맞춤형 식단 및 운동 계획을 제공합니다.
- 커뮤니티 및 사용자 피드백 시스템 : 사용자들이 서로의 경험을 공유 할 수 있는 커뮤니티를 운영합니다.
- 건강 정보 및 뉴스 피드 :사용자에게 최신 건강 정보 및 뉴스를 제공하여 건강 트렌드를 쉽게 따라갈 수 있도록 돕습니다.
- 소셜 로그인 및 간편 회원가입 : 소셜 로그인 기능을 제공하여 사용자가 쉽게 가입하고 접근할 수 있게 합니다.
- 지도로 장소 찾기 : 지도 검색기능을 제공해 주변의 필요한 장소에 대한 정보를 얻을 수 있는 페이지를 제공합니다.

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
| Open AI| GPT4.0 mini |

# 🧑‍🧑‍🧒‍🧒 개발팀

👑 김동용(팀장)
- 댓글 관리 기능 개발
- Chat GPT 연동 및 AI 채팅 상담 기능 개발
- 지도 연동 기능 개발
- 백엔드 및 프론트엔드 개발

👑 이규호 (부팀장)
- 사용자 인증 시스템을 구축 및 메일 인증을 통한 계정 활성화 기능 개발
- 뉴스크롤링 기능 개발
- 결제페이지 기능 개발
- 백엔드 및 프론트엔드 개발

👤 김나현
- 회원정보수정 기능 개발
- 프로필페이지 기능 개발
- 백엔드 및 프론트엔드 개발
- UX/UI 디자인

👤 이예지
- 게시물 관리 기능 개발
- 키워드 태그 기능 개발
- 백엔드 및 프론트엔드 개발
- UX/UI 디자인

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

## 5. Payment service
-   

# 🏗️서비스 아키텍처
![핏한하루 SA](https://github.com/user-attachments/assets/5255d356-9807-45b6-810f-18af8b5439eb)

# 📃 ERD Diagram
![image](https://github.com/user-attachments/assets/bd8106f2-eeb4-4802-8846-853dc68824ac)


# 📃 와이어프레임
![image](https://github.com/user-attachments/assets/aa611206-2ea7-4b22-bdd2-ee221e6b42e9)

# 📃 architecture
![image](https://github.com/user-attachments/assets/c1fb952a-5268-451c-8ea6-e856d19567a5)
