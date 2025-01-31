from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, BlockedUser
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import UserSearchForm
from django.core.exceptions import PermissionDenied
from django.utils.html import escape


@login_required
def inbox(request):
    form = UserSearchForm(request.GET or None)
    requested_users = None
    users_searched = False
    if form.is_valid():
        query = form.cleaned_data.get("query")
        if query:
            requested_users = User.objects.filter(
                username__icontains=query
            ).values_list("username", flat=True)
            users_searched = True

    conversation_history = {}
    messages_history = Message.objects.filter(
        Q(sender=request.user) | Q(recipient=request.user)
    ).order_by("timestamp")

    blocked_users = BlockedUser.objects.filter(blocker=request.user).values_list(
        "blocked__username", flat=True
    )

    for message in messages_history:
        if message.sender.username == request.user.username:
            messaging_partner = message.recipient.username
        else:
            messaging_partner = message.sender.username
        if (users_searched and messaging_partner not in requested_users) or (
            messaging_partner in blocked_users
        ):
            continue
        conversation_history[messaging_partner] = {
            "sender": message.sender.username,
            "recipient": message.recipient.username,
            "content": escape(message.content),
            "timestamp": message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }

    start_conversations = []
    if users_searched:
        for username in requested_users:
            if (
                username != request.user.username
                and username not in conversation_history
                and username not in blocked_users
            ):
                start_conversations.append(username)
    return render(
        request,
        "messaging/inbox.html",
        {
            "form": form,
            "conversation_history": conversation_history,
            "start_conversations": start_conversations,
        },
    )


@login_required
def direct_messaging(request, messaging_partner_name):
    messaging_partner = get_object_or_404(User, username=messaging_partner_name)
    if messaging_partner == request.user:
        raise PermissionDenied
    blocked_users = BlockedUser.objects.filter(blocker=request.user).values_list(
        "blocked__username", flat=True
    )
    if messaging_partner.username in blocked_users:
        raise PermissionDenied
    messages_history = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=messaging_partner))
        | Q(sender=messaging_partner) & Q(recipient=request.user)
    ).order_by("timestamp")
    messages_data = [
        {
            "sender": message.sender.username,
            "recipient": message.recipient.username,
            "content": escape(message.content),
            "timestamp": message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for message in messages_history
    ]
    return render(
        request,
        "messaging/direct_messaging.html",
        {"messages": messages_data, "messaging_partner": messaging_partner.username},
    )


@login_required
@csrf_exempt
def send_message(request, recipient_username):
    recipient = get_object_or_404(User, username=recipient_username)
    if recipient == request.user:
        raise PermissionDenied
    blocked_users = BlockedUser.objects.filter(blocker=request.user).values_list(
        "blocked__username", flat=True
    )
    if recipient.username in blocked_users:
        raise PermissionDenied
    if request.method == "POST":
        content = request.POST["content"]
        if content:
            Message.objects.create(
                sender=request.user, recipient=recipient, content=content
            )
            return JsonResponse({"status": "Message sent"})
    return render(request, "messaging/send_message.html", {"recipient": recipient})


@login_required
def get_new_messages(request, messaging_partner_name):
    messaging_partner = get_object_or_404(User, username=messaging_partner_name)
    if messaging_partner == request.user:
        raise PermissionDenied
    blocked_users = BlockedUser.objects.filter(blocker=request.user).values_list(
        "blocked__username", flat=True
    )
    if messaging_partner.username in blocked_users:
        raise PermissionDenied
    messages_history = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=messaging_partner))
        | Q(sender=messaging_partner) & Q(recipient=request.user)
    ).order_by("timestamp")
    messages_data = [
        {
            "sender": message.sender.username,
            "recipient": message.recipient.username,
            "content": escape(message.content),
            "timestamp": message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for message in messages_history
    ]
    return JsonResponse({"messages": messages_data})


@login_required
def block_user(request, messaging_partner_name):
    messaging_partner = get_object_or_404(User, username=messaging_partner_name)
    if messaging_partner == request.user:
        raise PermissionDenied
    already_blocked = BlockedUser.objects.filter(
        blocker=request.user, blocked=messaging_partner
    )
    if already_blocked:
        return redirect("messaging:inbox")

    BlockedUser.objects.create(blocker=request.user, blocked=messaging_partner)
    return redirect("messaging:inbox")
