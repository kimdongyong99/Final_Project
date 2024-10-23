# ⚠️트러블 슈팅

- 프로필 정보 수정 후 프로필 조회 페이지에 반영되지 않음
    
    작성자 : 김나현
    
    - 증상 : 사용자가 프로필 이미지를 수정했지만, 수정된 내용이 프로필 조회 페이지에 반영되지 않았습니다.
    
          페이지를 새로고침해도 프로필 이미지는 이전 상태로 유지되었습니다.
    
    - 원인 : formData.append() 메서드를 사용하여 프로필 이미지를 업데이트하는 과정에서, document.getElementById("profile_image").target.files[0] 코드의 target 속성이 잘못 사용되었습니다.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/e15247bf-7d2e-46c9-a4e2-2461ad1b10b4/image.png)
    
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
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/72142cf2-8841-4012-857e-603287183f46/image.png)
    
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
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/72a37088-1391-47bf-a5e1-80b6f9f3aead/image.png)
    
- 댓글 CRUD 구현중 pk 값 설정 오류로 인한 에러
    
    작성자 : 김동용 
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/3e25f693-ebdc-473f-9b5b-a3652b0c5e04/image.png)
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/61a071b7-f0e1-44e5-bb76-e2b3b40716ec/image.png)
    
    posts의 views.py에서 lookup_field 의 pk값 설정이 url.py에서 사용되는 경로에 지정된 pk값과 일치 하지 않아서 발생한 에러이다.
    
    두 개의 pk값을 일치 시켜주어 에러를 해결하였다.
    
- 배포 작업시 gunicorn.sevice 설정 중 생긴 에러
    
    작성자 : 김동용
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/c14b3412-54c5-4e3f-b9a2-8a78b67328f2/image.png)
    
    gunicorn.sevice 설정을 잘못해서 삭제를 하고 다시 만들어서 실행을 했는데 오류가 발생했다.
    
    처음에 생성했던 데이터가 남아있어 충돌이 일어난것을 볼수있다
    
    ```python
    sudo systemctl daemon-reload
    ```
    
    경로에 있는 **서비스 파일**을 수정하거나 새로 만들었을 때, 시스템에 즉시 반영되지 않아 서비스 파일의 변경사항을 읽고 다시 로드 하도록 강제 해줘야 되므로  명령어를 실행시킨 후 충돌을 해결할 수 있었다.
    
- 배포 작업 시 static 파일 경로설정에 대한 에러
    
    작성자 : 김동용
    
    ![스크린샷(134).png](https://prod-files-secure.s3.us-west-2.amazonaws.com/83c75a39-3aba-4ba4-a792-7aefe4b07895/b904f8cb-bcbf-44e0-a4b3-5d375a440213/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7(134).png)
    
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
