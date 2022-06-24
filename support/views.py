from django.shortcuts import render


def support(request):

    context = {}
    return render(request, "support/support.html", context)
