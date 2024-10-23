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
    
