# ⚠️트러블 슈팅

- 배포 작업 시 static 파일 경로설정에 대한 에러
    
    작성자 : 김동용
    
![troble6](https://github.com/user-attachments/assets/16cba0e0-36c4-4db2-a60c-8c0c47373067)
    
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

