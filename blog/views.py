from django.shortcuts import render

from .models import Holiday, Image


def home(request):
    news = Holiday.objects.all()   
     

    context = {
        "new" : news[0],
        "new_one" : news[1],
        "new_3" : news[2],
        "new_uzim" : news[3],
        "new_uzim_about" : news[19],
        "commint" : news[20]
    }
 
    return render (request, 'index.html', context)



def tabriklar(request):
    return render(request, 'tabrik.html')




def images(request):
    img = Image.objects.all()
    
    context = {
        "img_2" : img[1],
        "img_3" : img[2],
        "img_4" : img[0],
        "img_5" : img[4],
        "img_6" : img[5],
        "img_7" : img[6],
        "img_8" : img[7],
        "img_9" : img[8],
        "img_10" : img[9],
        "img_11" : img[10],
        "img_12" : img[11],
        "img_13" : img[12],
        "img_14" : img[13],
        "img_15" : img[14],
        "img_16" : img[15],
        "img_17" : img[16],
        "img_18" : img[17],
     
    }
    return render (request, 'rasm.html', context)