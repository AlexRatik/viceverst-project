from django.shortcuts import render
import re

def home(request):
	return render(request, 'home.html')

def reverse(request):
	text = request.GET['usertext']
	r_text = text[::-1]
	number_of_word = len(re.findall(r'\w+', text))
	return render(request, 'reverse.html', {'orig_text':text,'usertext':r_text,'numberW':number_of_word})