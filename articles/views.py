from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Article, Comment
from bs4 import BeautifulSoup
import requests
from openai import OpenAI
from django.urls import reverse
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentListSerializer, CommentCreateSerializer
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.paginator import Paginator

client = OpenAI(api_key=settings.OPENAI_API_KEY)

from django.http import JsonResponse


class CrawlerNewsList(View):
    def get(self, request, *args, **kwargs):
        # 헬스 조선 기사 리스트 페이지 URL
        url = "https://health.chosun.com/list.html"
        response = requests.get(url, verify=True)

        # 응답의 인코딩을 euc-kr로 설정
        response.encoding = 'euc-kr'
        soup = BeautifulSoup(response.text, "html.parser")

        # 검색어가 있으면 필터링
        search = request.GET.get('search', '')
        page_number = request.GET.get('page', 1)  # 요청된 페이지 번호, 기본값은 1

        # 기사 제목과 링크 추출
        news_data = self.extract_news(soup)

        # 추가: 각 뉴스 데이터에 대해 ArticleSerializer로 직렬화된 정보를 가져옴
        for news_item in news_data:
            article = Article.objects.get(id=news_item["id"])
            news_item["total_likes"] = article.total_likes()

        # 검색어가 있으면 필터링
        if search:
            news_data = [news_item for news_item in news_data if search.lower() in news_item['title'].lower()]

        # 페이지네이션 적용 (한 페이지에 9개씩)
        paginator = Paginator(news_data, 9)
        page_obj = paginator.get_page(page_number)

        # JSON 형식으로 반환 (페이지네이션 정보와 함께 반환)
        return JsonResponse({
            'news': list(page_obj),  # 뉴스 데이터 리스트
            'has_next': page_obj.has_next(),  # 다음 페이지 여부
            'has_previous': page_obj.has_previous(),  # 이전 페이지 여부
            'page_number': page_obj.number,  # 현재 페이지 번호
            'total_pages': paginator.num_pages,  # 전체 페이지 수
        }, safe=False)
    
    def extract_news(self, soup):
        news_list = []
        article_list = soup.find_all('li', class_='rellist')

        for item in article_list:
            title_tag = item.find("h4").find("a")
            image_tag = item.find("img")
            if title_tag:
                href = title_tag.get("href")
                title = title_tag.get_text(strip=True)
                full_link = f"https://health.chosun.com{href}"

                image_url = image_tag.get("src") if image_tag else None

                # 기존에 같은 링크가 있는지 확인하고 없으면 저장
                article, created = Article.objects.get_or_create(
                    link=full_link,
                    defaults={
                        'title': title,
                        'image_url': image_url,
                    }
                )

                # JSON 형식으로 뉴스 데이터 저장 (article.id 추가)
                news_list.append({
                    "id": article.id,  # 이 부분에서 id를 반환
                    "title": title,
                    "link": full_link,
                    "image_url": image_url,
                })

        return news_list


class WebDriverManager:
    def __enter__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(
            service=ChromeService(executable_path="C:\\Users\\noaet\\chromedriver-win64\\chromedriver.exe"),
            options=chrome_options,
        )
        return self.driver
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()


class CrawlerNewsSummary(View):
    def get(self, request, *args, **kwargs):
        # 헬스 조선 기사 리스트 페이지 URL
        url = "https://health.chosun.com/list.html"
        response = requests.get(url, verify=True)

        # 응답의 인코딩을 euc-kr로 설정
        response.encoding = 'euc-kr'
        soup = BeautifulSoup(response.text, "html.parser")

        # 기사 제목과 링크 추출
        news_info = self.extract_news(soup)

        return HttpResponse(
            f"""
            크롤링 시작:<br>
            {news_info}
        """
        )
    
    def extract_news(self, soup):
        news_list = soup.find('ul', class_='tab-contents board-list')  # 헬스 조선의 뉴스 리스트 태그와 클래스명
        news_info = ""
        if news_list:
            for item in news_list.find_all("li", class_="rellist"):
                title_tag = item.find("h4").find("a")
                if title_tag:
                    href = title_tag.get("href")
                    title = title_tag.get_text(strip=True)
                    full_link = f"https://health.chosun.com{href}"  # 상대 경로를 절대 경로로 변환
                    news_info += (
                        f'<a href="{reverse("summarize")}?url={full_link}">{title}</a><br>'
                    )
        return news_info
    

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
                        (By.CLASS_NAME, "news_body_all")
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
        article_div = soup.find("div", class_="news_body_all")
        if article_div:
            text = article_div.get_text(strip=True)
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
    

class ArticleDetailAPIView(View):
    def get(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)

        # 요약이 DB에 없을 경우 OpenAI로 요약 생성
        if not article.summary:
            article.summary = self.get_summary(article)
            article.save()  # 새 요약을 DB에 저장

        return JsonResponse({
            "title": article.title,
            "link": article.link,
            "image_url": article.image_url,
            "summary": article.summary,  # 저장된 요약을 반환
            "total_likes": article.total_likes(),
        })

    def get_summary(self, article):
        content = article.title  # 기사의 제목을 요약에 사용
        try:
            summary = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "이 기사를 간단히 요약해 주세요."},
                    {"role": "user", "content": content},
                ],
            ).choices[0].message.content.strip()
        except Exception as e:
            summary = "요약 생성 중 오류 발생"
        
        return summary


class ArticleLikeView(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def post(self, request, article_id, *args, **kwargs):
        article = get_object_or_404(Article, pk=article_id)
        user = request.user  # 현재 로그인한 사용자

        if article.likes.filter(id=user.id).exists():
            # 이미 좋아요를 누른 경우 -> 좋아요 취소
            article.likes.remove(user)
            return Response({"message": "Like removed", "total_likes": article.total_likes()}, status=status.HTTP_200_OK)
        else:
            # 좋아요를 아직 누르지 않은 경우 -> 좋아요 추가
            article.likes.add(user)
            return Response({"message": "Article liked", "total_likes": article.total_likes()}, status=status.HTTP_200_OK)


class CommentListCreateView(ListCreateAPIView):
    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        article_id = self.kwargs['article_pk']  # URL에서 article_pk 가져오기
        return Comment.objects.filter(article_id=article_id)  # 해당 article의 댓글만 반환

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentListSerializer

    def perform_create(self, serializer):
        article = get_object_or_404(Article, pk=self.kwargs['article_pk'])
        serializer.save(author=self.request.user, article=article)  # 댓글 작성


class CommentUpdateDeleteView(UpdateAPIView, DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentCreateSerializer
    lookup_field = 'pk'
