from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
from django.conf import settings


class ChatGPTView(APIView):
    conversation_history = []

    def post(self, request):
        user_message = request.data.get("message")

        if not user_message:
            return Response(
                {"error": "메시지가 비어있을 수 없습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 새로운 사용자 메시지를 대화 기록에 추가
        self.conversation_history.append({"role": "user", "content": user_message})

        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        system_instructions = """
                이제부터 너는 고객에게 식단과 운동정보를 제공하는 역할을 할 거야.
                대화의 문맥을 유지해줘.
                """

        try:
            # 전체 대화 기록을 모델에 전달
            messages = [
                {"role": "system", "content": system_instructions}
            ] + self.conversation_history

            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
            )
            chatgpt_response = completion.choices[0].message.content

            # GPT의 응답을 대화 기록에 추가
            self.conversation_history.append(
                {"role": "assistant", "content": chatgpt_response}
            )

            return Response({"message": chatgpt_response})

        except Exception as e:
            # 오류 로깅 (로깅 라이브러리 사용할 수 있음)
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
