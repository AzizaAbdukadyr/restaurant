from django.shortcuts import render
from .models import Menu, Booking


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})


def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, "book.html", context)

# def about(request):
#     about_content = {'about':'This is restaurant Little lemon'}
#     return render(request, "about.html", about_content)

# def menu(request):
#     menuitem = {'mains': [
#         {'name': 'Greek salad', "price":"12"},
#         {'name': 'shaurma', "price":"20"},
#         {'name': 'plov', "price":"10"},
#     ]}
#     return render(request, 'menu.html', menuitem)

# def menu_by_id(request):
#     new_menu = Menu.objects.all()
#     new_menu_dict = {'menu': new_menu}
#     return render(request, "menu_card.html", new_menu_dict)
