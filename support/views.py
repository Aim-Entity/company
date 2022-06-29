from django.shortcuts import render
from .models import SupportCard


def support(request):
    bullying = SupportCard.objects.filter(topic="Bullying")
    mental_illness = SupportCard.objects.filter(topic="Mental Illness")
    stress = SupportCard.objects.filter(topic="Stress")
    disability = SupportCard.objects.filter(topic="Disability")
    depression = SupportCard.objects.filter(topic="Depression")

    # print(bullying.count())
    context = {
        "bullying": bullying,
        "mental_illness": mental_illness,
        "stress": stress,
        "disability": disability,
        "depression": depression,

        "bull_count": bullying.count(),
        "mental_count": mental_illness.count(),
        "stress_count": stress.count(),
        "dis_count": disability.count(),
        "dep_count": depression.count(),
    }
    return render(request, "support/support.html", context)
