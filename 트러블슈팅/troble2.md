# ⚠️트러블 슈팅

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
    
![troble2](https://github.com/user-attachments/assets/eed97575-277e-4a52-9b6e-19c60bbc799f)
    
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
