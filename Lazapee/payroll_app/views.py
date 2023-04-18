from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request, 'payroll_app/home_page.html')
