from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render


def contact_view(request):
    return render(request, 'contact/contact.html')


def contact_submit(request):
    if request.method == "POST":
        if "message" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            full_message = f"From: {name} <{email}>\n\n{message}"
            subject = "[Portfolio] New Work Proposal"
        else:
            nickname = request.POST.get("nickname")
            feedback = request.POST.get("feedback")
            full_message = f"From: {nickname}\n\n{feedback}"
            subject = "[Portfolio] Feedback"

        send_mail(
            subject=subject,
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
        )
        return JsonResponse({"ok": True})
    return JsonResponse({"error": "Invalid request"}, status=400)
