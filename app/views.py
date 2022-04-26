from queue import Empty
from xml.dom.minidom import Identified
from django.shortcuts import render, redirect
from numpy import require
from app.models import Employee, Blog
from app.forms import BlogForm
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db import connection
import subprocess, shlex
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "app/index.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "User Created Successfully! You can login now!.")
            return redirect('app:index')
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form":form})

@login_required
def home(request):
    return render(request, "app/home.html")

@login_required
def employees(request):
    if request.method == "POST":
        id = request.POST.get("id")
        cust_id = request.POST.get("cust_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        address = request.POST.get("address")
        contactno = request.POST.get("contactno")

        # Saving to DB using Django ORM - the best way
        Employee.objects.create(first_name=first_name, last_name=last_name, cust_id=cust_id,
        age=age, sex=sex, address=address, contactno=contactno)

        # # Direct SQL Queries - the wrong way
        # cursor = connection.cursor()
        # query = "INSERT INTO app_employee (cust_id, first_name, last_name, age, sex, address, contactno) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (cust_id, first_name, last_name, age, sex, address, contactno)
        # cursor.execute(query)

        # # Direct SQL Queries - the correct way
        # cursor = connection.cursor()
        # cursor.execute("INSERT INTO app_employee (cust_id, first_name, last_name, age, sex, address, contactno) VALUES (%s, %s, %s, %s, %s, %s, %s)", [cust_id, first_name, last_name, age, sex, address, contactno])

        return redirect("app:employees")
    else:
        # Fetch all employees using Django ORM
        employees = Employee.objects.all()

        return render(request, 'app/customers.html',
        {"employees":employees})

def delrec(request,id):
    delemployee = Employee.objects.filter(id=id)
    delemployee.delete()
    result = Employee.objects.all()
    #return render(request, 'app/customers.html',{"employees":result})
    return redirect("app:employees")


@login_required
@csrf_exempt
def search_employees(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_term = request.POST.get('searchTerm')

        # Searching employees using Django ORM - the best way
        employees = Employee.objects.filter(first_name__icontains=search_term)

        # # Searching employees using raw() - the wrong way
        # query = "SELECT * FROM app_employee WHERE first_name ILIKE '%s';" % search_term
        # employees = Employee.objects.raw(query)

        # # Searching employees using raw() - the correct way
        # employees = Employee.objects.raw('SELECT * FROM app_employee WHERE first_name ILIKE %s;',[search_term])

        # # Searching employees using extra() - the wrong way
        # employees = Employee.objects.extra(where=["first_name ILIKE '%s'" % search_term])

        # # Searching employees using extra() - the correct way
        # employees = Employee.objects.extra(where=['first_name ILIKE %s'], params=[search_term])

        html = render_to_string('app/search_customers.html',
        {'employees':employees})

        return HttpResponse(html)

