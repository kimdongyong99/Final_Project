# ⚠️트러블 슈팅
    
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
    
![troble3](https://github.com/user-attachments/assets/23b86e16-e69b-4ad2-ba7f-f9fb602091b4)
    
