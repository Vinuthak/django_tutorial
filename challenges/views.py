from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "january challenge",
    "february": "february challenge",
    "march": "march challenge",
    "april": "april challenge",
    "may": "may challenge",
    "june": "june challenge",
    "july": "july challenge",
    "august": "august challenge",
    "september": "september challenge",
    "october": "october challenge",
    "november": "november challenge",
    "december": None,
}


# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_string(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month": month.capitalize()},
        )
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

    except:
        return HttpResponseNotFound("<h3>Not allowed for this month!</h3>")
    return HttpResponse(f"<h3>{challenge_text}</h3>")


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month number!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
