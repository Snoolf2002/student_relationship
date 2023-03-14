from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Student, Contact

# Create your views here.

def get_student(request: HttpRequest) -> JsonResponse:
    data = Student.objects.all()

    res = []
    for dat in data:
        contact = dat.contact
        res.append(
            {
                "firstname": dat.first_name,
                "lastname": dat.last_name,
                "phone": contact.phone,
                "adress": contact.adress
            }
        )
    
    return JsonResponse({'students': res})
