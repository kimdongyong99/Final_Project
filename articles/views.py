from django.shortcuts import render

# Create your views here.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Article
from bs4 import BeautifulSoup
import requests
from openai import OpenAI
from django.conf import settings
import chromedriver_autoinstaller



client = OpenAI(api_key=settings.OPENAI_API_KEY)

class CrawlerHealthChosun(View):
    def get(self, request, *args, **kwargs):
        # 헬스 조선 기사 리스트 페이지 URL
        url = "https://health.chosun.com/list_life.html"
        response = requests.get(url, verify=True)

        # 응답의 인코딩을 euc-kr로 설정, 인코딩 안하면 깨짐
        response.encoding = 'euc-kr'

        soup = BeautifulSoup(response.text, "html.parser")

        # 기사 제목, 링크, 이미지 URL 추출
        article_info = self.extract_articles(soup)

        # HttpResponse로 크롤링된 기사 정보를 반환
        return HttpResponse(f"크롤링 시작:<br>{article_info}")

    def extract_articles(self, soup):
        article_info = ""  # 반환할 정보를 저장할 변수

        # 제목과 링크 추출
        article_list = soup.find_all('li', class_='rellist')

        for item in article_list:
            title_tag = item.find("h4").find("a")
            image_tag = item.find("img")  # 조선헬스에서 img 확인

            if title_tag:
                href = title_tag.get("href")
                title = title_tag.get_text(strip=True)
                full_link = f"https://health.chosun.com{href}"

                # 이미지 URL이 있을 경우 추출
                if image_tag:
                    image_url = image_tag.get("src")
                else:
                    image_url = None

                # 중복 체크 후 DB에 저장
                if not Article.objects.filter(link=full_link).exists():
                    Article.objects.create(
                        title=title, link=full_link, image_url=image_url)

                # 반환할 정보에 제목, 링크, 이미지, 요약 추가
                if image_url:
                    article_info += f'<a href="{full_link}">{title}</a><br><img src="{image_url}" alt="{title}" style="width:300px;"><br><br>'
                else:
                    article_info += f'<a href="{full_link}">{title}</a><br><br>'

        # 반환할 기사 정보가 없으면 기본 메시지 반환
        if not article_info:
            article_info = "No articles found."

        return article_info


class WebDriverManager:
    def __enter__(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--remote-debugging-port=9222")
        path = chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome(
            service=ChromeService(path),
            options=chrome_options,
        )
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()


class ArticleSummarizer(View):
    def get(self, request, *args, **kwargs):
        url = request.GET.get("url")

        if not url:
            return JsonResponse({"error": "URL이 제공되지 않았습니다."}, status=400)

        try:
            with WebDriverManager() as driver:
                driver.get(url)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "NewsEndMain_comp_article_content__PZYoE")
                    )
                )
                html_content = driver.page_source
        except Exception as e:
            return JsonResponse(
                {"error": f"웹 크롤링 중 오류 발생: {str(e)}"}, status=500
            )

        soup = BeautifulSoup(html_content, "html.parser")
        content = self.extract_main_content(soup)

        if not content:
            return JsonResponse({"error": "기사를 찾을 수 없습니다."}, status=404)

        try:
            summary = self.summarize_content(content)
        except Exception as e:
            return JsonResponse(
                {"error": f"요약 생성 중 오류 발생: {str(e)}"}, status=500
            )

        return JsonResponse({"summary": summary})

    def extract_main_content(self, soup):
        article_div = soup.find(
            "article", class_="NewsEndMain_comp_news_article__wMpnW _article_body"
        )
        if article_div:
            content_div = article_div.find("div", class_="_article_content")
            if content_div:
                text = content_div.get_text(strip=True)
                if len(text) > 200:
                    return text
        return None

    def summarize_content(self, content):
        """추출한 기사를 요약하는 함수"""
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "이 기사를 간단히 요약해 주세요."},
                {"role": "user", "content": content},
            ],
        )
        return response.choices[0].message.content.strip()