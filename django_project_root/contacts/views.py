# from django.shortcuts import render
# from django.core.mail import send_mail
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from rest_framework.permissions import AllowAny

# class ContactView(APIView):
#     permission_classes = [AllowAny]  # 👈 Allow unauthenticated users

#     def post(self, request):
#         message = request.data.get('message')
#         if not message:
#             return Response({"error": "Message is required."}, status=status.HTTP_400_BAD_REQUEST)

#         send_mail(
#             subject="New Contact Message",
#             message=message,
#             from_email=None,
#             recipient_list=['tarasjulieproject@yahoo.com'],
#             fail_silently=False,
#         )
#         return Response({"success": "Message sent successfully!"}, status=status.HTTP_200_OK)


from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class ContactView(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated users

    def post(self, request):
        # Get message from the request data
        message = request.data.get('message')
        
        # If message is not provided, return a bad request error
        if not message:
            return Response({"error": "Message is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Send the email
        try:
            send_mail(
                subject="New Contact Message from Frontend: About Us section",
                message=message,
                from_email= "amchosen@yahoo.com",  # Use the default email from settings if needed
                recipient_list=["amchosen@yahoo.com"],
                fail_silently=True,
            )
            return Response({"success": "Message sent successfully!"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
