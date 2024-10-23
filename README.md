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
| Open AI | GPT4.0 mini |
| Server Hosting | AWS EC2 |
| HTTP Server | Gunicorn |
| Reverse Proxy | Nginx |


# 💭기술적 의사결정

- **Django REST Framework**

Django rest_framework를 사용하게 되면, view와 model 사이에 serializer라는 것을 사용하게 된다. View에서 Serializer를 가져와서 사용하게 되면 Model에서 꺼낸 데이터를 Queryset의 형태가 아니라 json형태로 데이터를 받아올 수 있다.

이렇게 Django과 DRF를 함께 사용하면 Python으로 만든 백엔드를 다른 프론트엔드에서도 사용할 수 있게 되므로 선택하였다.

- **MySQL**

 MySQL은 크로스 플랫폼 데이터베이스 서버로 설계되어 Linux, macOS 및 Windows에서 실행됩니다. 멀티플랫폼 프로젝트라면, MySQL이 적합합니다.

웹사이트에 매일 수백만 건의 쿼리가 발생하는 경우, 가장 까다로운 작업에도 최적의 속도를 보장하는 MySQL의 기능을 통해 비즈니스 또는 웹사이트가 필요에 따라 중단 없이 작동할 수 있습니다.

가동 시간, 성능, 플랫폼 간 호환성 외에도 MySQL은 진입 장벽이 거의 없는 무료 툴이기 때문에 선택하였습니다.

- **GPT API**

Open ai 에서 제공하는 API를 통해 간단하게 사용 할 수 있고  사용의 편의성과 응답의 질이 우수하다고 생각되어 사용하였다. 

- **AWS EC2**

AWS EC2는 가상 서버를 런칭하고 종료하는 것이 간단하고 빠르다.

필요에 따라 컴퓨팅 파워를 늘리거나 줄일 수 있어 작업량 변동에 따라 비용을 최적화할 수 있다.

강력한 네트워킹 및 보안 기능을 제공하여 안정적인 인프라스트럭처를 제공한다

다양한 인스턴스 유형을 제공하여 서로 다른 작업에 필요한 최적의 하드웨어 구성을 선택할 수 있다.

- **Gunicorn**

Gunicorn은 Python WSGI 애플리케이션을 위한 HTTP 서버로, Django나 Flask와 같은 프레임워크와 호환성이 뛰어나며 멀티프로세스 모델을 통해 CPU 코어를 효율적으로 활용하여 높은 성능을 제공합니다. 간단한 설정으로 빠르게 배포할 수 있고, 다양한 워커 타입을 지원하여 애플리케이션의 특성에 맞게 유연하게 사용할 수 있습니다. 특히 Nginx와 함께 사용하면 정적 파일 제공과 보안성 강화에 유리하며, 자동 워커 재시작 기능으로 안정성을 높입니다. 또한, 커뮤니티와 문서 지원이 풍부하여 확장성과 문제 해결에 유리한 서버입니다.

- **Nginx**

Nginx는 비동기 처리 방식으로 높은 성능과 낮은 리소스 사용을 자랑하는 웹 서버로, 특히 동시에 많은 요청을 처리할 때 효율적입니다. 로드 밸런싱 및 리버스 프록시 기능을 제공하여 서버 부하 분산과 보안성을 강화할 수 있으며, 정적 콘텐츠 제공에 최적화되어 있어 빠른 응답 속도를 유지합니다. SSL/TLS 처리에도 뛰어나 보안을 유지하면서도 백엔드 서버의 부하를 줄여줍니다. 설정 파일이 직관적이고 간편하며, 다양한 모듈로 기능 확장이 가능해 유연한 서버 구성이 가능합니다. 또한, 넓은 커뮤니티와 풍부한 문서 지원을 통해 문제 해결과 개발에 큰 도움을 받을 수 있는 안정적인 웹 서버입니다.

# 🧑‍🧑‍🧒‍🧒 개발팀

👑 김동용(팀장)
- 댓글 관리 기능 개발
- Chat GPT 연동 및 AI 채팅 상담 기능 개발
- 지도 연동 기능 개발
- 백엔드 및 프론트엔드 개발
- CSS 디자인
- 배포 담당
- 기획

👑 이규호 (부팀장)
- 사용자 인증 시스템을 구축 및 메일 인증을 통한 계정 활성화 기능 개발
- 뉴스크롤링 기능 개발
- 결제페이지 기능 개발
- 백엔드 및 프론트엔드 개발
- CSS 디자인
- 배포 담당
- 기획

👤 김나현
- 회원정보수정 기능 개발
- 프로필페이지 기능 개발
- 백엔드 및 프론트엔드 개발
- UX/UI 디자인
- CSS 디자인
- 배포 담당
- 기획

👤 이예지
- 게시물 관리 기능 개발
- 키워드 태그 기능 개발
- 백엔드 및 프론트엔드 개발
- UX/UI 디자인
- CSS 디자인
- 배포 담당
- 기획

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
- admin에서 상품을 올리면 사용자가 상품을 구매할 수 있습니다.
- 상세페이지에서 카카오페이, 토스페이로 결제할 수 있습니다.
- 테스트 결제로 구현했으므로 실제로 출금이 이뤄지지 않습니다.

## 6. Map
- 사용자가 주변의 헬스장,병원,건강 식품점 등 건강과 관련된 장소를 쉽게 찾을 수 있도록 지도 기반 검색 기능을 추가하여 사용자 편의성을 극대화할 수 있습니다

# 📃 ERD Diagram
![image](https://github.com/user-attachments/assets/bd8106f2-eeb4-4802-8846-853dc68824ac)


# 📃 와이어프레임
![image](https://github.com/user-attachments/assets/aa611206-2ea7-4b22-bdd2-ee221e6b42e9)

# 📃 architecture
![image](https://github.com/user-attachments/assets/c1fb952a-5268-451c-8ea6-e856d19567a5)

# 📃 디자인
<img width="979" alt="스크린샷 2024-10-23 오후 5 08 01" src="https://github.com/user-attachments/assets/e7a17ae3-7b82-4c84-930d-aa53e01a4a23">


# ⚠️트러블 슈팅

- 프로필 정보 수정 후 프로필 조회 페이지에 반영되지 않음
    
    작성자 : 김나현
    
    - 증상 : 사용자가 프로필 이미지를 수정했지만, 수정된 내용이 프로필 조회 페이지에 반영되지 않았습니다.
    
          페이지를 새로고침해도 프로필 이미지는 이전 상태로 유지되었습니다.
    
    - 원인 : formData.append() 메서드를 사용하여 프로필 이미지를 업데이트하는 과정에서, document.getElementById("profile_image").target.files[0] 코드의 target 속성이 잘못 사용되었습니다.
    

![troble1](https://github.com/user-attachments/assets/4f837690-271e-49ce-ba03-3a7803bb0f44)

    
    - target 을 사용한 이유: 파일 입력 요소에 대한 접근을 시도하면서 이벤트 객체를 고려해 파일 입력 요소에 대한 접근을 시도하려 했습니다.
    - 여기서는 단순히 DOM 요소에서 파일을 참조하는 것이므로, target을 사용할 필요가 없었습니다.
    
    수정 전 코드
    
    ```jsx
    formData.append("profile_image", document.getElementById("profile_image").target.files[0]);
    ```
    
    수정 후 코드
    
    ```jsx
    formData.append("profile_image", document.getElementById("profile_image").files[0]);
    ```
    
- 기사 크롤링 시 타이틀이 깨져서 나오는 인코딩 문제가 발생
    
    작성자 : 이규호
    
    - response.encoding을 utf-8로 설정해도 문자가 깨지는 것을 확인
    
    수정 전 코드
    
    ```python
    from django.http import HttpResponse
    from django.views import View
    from bs4 import BeautifulSoup
    import requests
    
    class CrawlerHealthChosun(View):
        def get(self, request, *args, **kwargs):
            url = "https://health.chosun.com/list_life.html"
            response = requests.get(url, verify=True)
            
            response.encoding = 'utf-8'
            
            soup = BeautifulSoup(response.text, "html.parser")
            article_info = self.extract_articles(soup)
            return HttpResponse(f"크롤링 시작:<br>{article_info}")
            
        def extract_articles(self, soup):
            article_info = ""
            article_list = soup.find_all('li', class_='rellist')
            for item in article_list:
                title_tag = item.find("h4").find("a")
                if title_tag:
                    href = title_tag.get("href")
                    title = title_tag.get_text(strip=True)
                    full_link = f"https://health.chosun.com{href}"
                    article_info += f'<a href="{full_link}">{title}</a><br>'
            return article_inf
    ```
    

![troble2](https://github.com/user-attachments/assets/51d300d9-34f9-4968-9819-45a1a4d5c8ed)

    
    - 문제 해결
    최종적으로 **response.encoding = 'euc-kr'**로 문제 해결
    인코딩 설정을 제대로 해줘야 문자를 정상적으로 출력할 수 있음
    
    수정 후 코드
    
    ```python
    from django.http import HttpResponse
    from django.views import View
    from bs4 import BeautifulSoup
    import requests
    
    class CrawlerHealthChosun(View):
        def get(self, request, *args, **kwargs):
            url = "https://health.chosun.com/list_life.html"
            response = requests.get(url, verify=True)
            
            # 응답의 인코딩을 euc-kr로 설정
            response.encoding = 'euc-kr'
            
            soup = BeautifulSoup(response.text, "html.parser")
            article_info = self.extract_articles(soup)
            return HttpResponse(f"크롤링 시작:<br>{article_info}")
            
        def extract_articles(self, soup):
            article_info = ""
            article_list = soup.find_all('li', class_='rellist')
            for item in article_list:
                title_tag = item.find("h4").find("a")
                if title_tag:
                    href = title_tag.get("href")
                    title = title_tag.get_text(strip=True)
                    full_link = f"https://health.chosun.com{href}"
                    article_info += f'<a href="{full_link}">{title}</a><br>'
            return article_info
    ```
    
- 회원가입 페이지에서 address 데이터가 넘어오지 않는 것을 확인
    
    작정자 : 이규호
    
    - formData.append("address", document.getElementById("address").value); 구문으로 address를 불러왔음에도 불구하고 브라우저 개발자 도구의 source에서 js코드를 확인하면 코드가 갱신되지 않는 문제가 발생
    
    ```jsx
    // 회원가입 요청
    document.getElementById("signup-form").addEventListener("submit", async function (event) {
        event.preventDefault();
    
        const formData = new FormData();
        formData.append("username", document.getElementById("username").value);
        formData.append("email", document.getElementById("email").value);
        formData.append("password", document.getElementById("password").value);
        formData.append("password_confirm", document.getElementById("password_confirm").value);
        formData.append("verification_code", document.getElementById("verification_code").value);
        formData.append("address", document.getElementById("address").value);
    ```
    
    - 문제 해결
    결과적으로는 새로고침 반영이 안되는 것이었음
    Ctrl + F5로 강력 새로고침을 통해 잘 반영되는 것을 확인할 수 있었음
    
![troble3](https://github.com/user-attachments/assets/65d55f1e-496d-4924-869b-cf4047962733)
    
- 댓글 CRUD 구현중 pk 값 설정 오류로 인한 에러
    
    작성자 : 김동용 
    
![troble4-1](https://github.com/user-attachments/assets/275dcaae-dc31-4378-ae7c-774f7e34c02f)
![troble4-2](https://github.com/user-attachments/assets/657bf1e8-e473-4902-856a-3da7ca557388)

    posts의 views.py에서 lookup_field 의 pk값 설정이 url.py에서 사용되는 경로에 지정된 pk값과 일치 하지 않아서 발생한 에러이다.
    
    두 개의 pk값을 일치 시켜주어 에러를 해결하였다.
    
- 배포 작업시 gunicorn.sevice 설정 중 생긴 에러
    
    작성자 : 김동용
    
![troble5](https://github.com/user-attachments/assets/917131a0-62de-4d5f-ab98-1c8c4991b731)
    
    gunicorn.sevice 설정을 잘못해서 삭제를 하고 다시 만들어서 실행을 했는데 오류가 발생했다.
    
    처음에 생성했던 데이터가 남아있어 충돌이 일어난것을 볼수있다
    
    ```python
    sudo systemctl daemon-reload
    ```
    
    경로에 있는 **서비스 파일**을 수정하거나 새로 만들었을 때, 시스템에 즉시 반영되지 않아 서비스 파일의 변경사항을 읽고 다시 로드 하도록 강제 해줘야 되므로  명령어를 실행시킨 후 충돌을 해결할 수 있었다.
    
- 배포 작업 시 static 파일 경로설정에 대한 에러
    
    작성자 : 김동용
    
![troble6](https://github.com/user-attachments/assets/c1eee2f2-0826-4220-9d2a-9554b2ebd0b1)
    
    ```python
    WARNING: The directory '/home/ubuntu/Final_Project_Front/static' in the STATICFILES_DIRS setting does not exist
    
    ```
    
    이 경고는 `settings.py`에서 설정된 `STATICFILES_DIRS` 경로에 해당 디렉토리가 존재하지 않는다는 의미이다. Django는 이 경로에서 정적 파일을 찾아 복사하려고 하지만, 경로가 존재하지 않아 경고가 발생한 것이다.
    
    ```python
    # 정적 파일을 서빙할 경로 (개발 중 사용할 경로)
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),  # 프로젝트의 'static' 폴더
    ]
    
    # collectstatic 명령으로 정적 파일을 모아둘 경로 (배포용)
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    ```
    
    개발 중 사용할 경로와 배포 시 사용할 경로를 다르게 지정해주어 해결할 수 있었다.

