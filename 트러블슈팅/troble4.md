# ⚠️트러블 슈팅

- 댓글 CRUD 구현중 pk 값 설정 오류로 인한 에러
    
    작성자 : 김동용 
    
![troble4-1](https://github.com/user-attachments/assets/06e5941b-9eff-4976-9427-ee46041754ca)

![troble4-2](https://github.com/user-attachments/assets/d0a153ce-ba6c-4a55-bc0c-3bff86215b8c)
    
    posts의 views.py에서 lookup_field 의 pk값 설정이 url.py에서 사용되는 경로에 지정된 pk값과 일치 하지 않아서 발생한 에러이다.
    
    두 개의 pk값을 일치 시켜주어 에러를 해결하였다.
    
