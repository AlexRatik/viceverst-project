from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	text = request.GET['usertext']
	r_text = text[::-1]
	return render(request, 'reverse.html', {'orig_text':text,'usertext':r_text})