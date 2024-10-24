# ⚠️트러블 슈팅

- 배포 작업시 gunicorn.sevice 설정 중 생긴 에러
    
    작성자 : 김동용
    
![troble5](https://github.com/user-attachments/assets/b291040d-99d9-4ef9-98df-65eda937b15e)
    
    gunicorn.sevice 설정을 잘못해서 삭제를 하고 다시 만들어서 실행을 했는데 오류가 발생했다.
    
    처음에 생성했던 데이터가 남아있어 충돌이 일어난것을 볼수있다
    
    ```python
    sudo systemctl daemon-reload
    ```
    
    경로에 있는 **서비스 파일**을 수정하거나 새로 만들었을 때, 시스템에 즉시 반영되지 않아 서비스 파일의 변경사항을 읽고 다시 로드 하도록 강제 해줘야 되므로  명령어를 실행시킨 후 충돌을 해결할 수 있었다.
    
