from django.shortcuts import render


def view_bag(request):
    """ view that returns contents of the bag page """

    return render(request, 'bag/bag.html')
