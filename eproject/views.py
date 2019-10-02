from django.shortcuts import render, redirect
from django.http import HttpResponse
from  django.http import HttpResponseRedirect
from  datetime import datetime
from .models import Regtable
from .models import Stafftasks
from .models import Classname
from .forms import AlltaskForm

# Create your views here.

def home(request):
	
	"""b = SecondTable1(name='Beatles Blog', username='muguyman', email='tunde@yahoo.com')
	b.save()"""
	try:
		context = {"firstname": "therapy", "lastname": "theman"}
		return render(request, "home.html", {"name": context})
	except:
		return render(request, "home.html", {'allitem': "error"})
	#return HttpResponse(ditems)

	
def deletedata(request, getid):
	
	ditems = SecondTable1.objects.get(id=getid)
	ditems.delete()

	return redirect('home')
	#return HttpResponse(ditems)	

def login(request):
	
	if request.method == 'POST':
		name = request.POST["username"]
		passwrd = request.POST["password"]

		raw_query = 'SELECT * FROM Regtable where username = %s AND password = %s'
		ditems = Regtable.objects.raw(raw_query, [name, passwrd])
		if (ditems):
				request.session['username'] = ditems[0].firstname + " " + ditems[0].lastname
				if(ditems[0].logintype == 1):
					request.session['staffid'] = ditems[0].id
					return redirect('staffpage')
				elif(ditems[0].logintype == 2):
					request.session['stuclass'] = ditems[0].class_field
					return redirect('studentpage')
		else:
			return render(request, "login.html", {'error': "THIS USER DOES NOT EXIST"})
		
	else:
		
		return render(request, "login.html", {'error': "none"})
		
		
def staffpage(request):
	
	staffid = request.session['staffid'] 
	staffname = request.session['username']
	
	id = int(staffid)
	raw_query = 'SELECT * FROM Stafftasks where staffid = %s'
	ditems = Stafftasks.objects.raw(raw_query, [id])
	if(ditems):
		return render(request, "staffpage.html", {'allitem': ditems, 'name': staffname})
	else:
		return render(request, "staffpage.html", {'error': "YOU DO NOT HAVE ANY ASSIGNMENTS"})
	
	return render(request, "staffpage.html", {'name': staffname})
	#return HttpResponse(ditems)
	
	
def deleteitem(request, getid):
	
	ditems = Stafftasks.objects.get(id=getid)
	ditems.delete()

	return redirect('staffpage')
	#return HttpResponse(ditems)	
	
		
	
def staffinput(request):

	staffname = request.session['username']
	
	if request.method == 'POST':
		staffid = request.session['staffid']
		nowtime = datetime.now().strftime("%Y-%m-%d") #%H:%M:%S"
	    #datenow = time.

		form = AlltaskForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.staffid = staffid
			obj.date =  nowtime
			
			obj.save()
			
			return redirect('staffpage')
		else:
			return redirect('staffinput')
		
	else:
		
		return render(request, "staffinput.html", {'name': staffname})



def studentpage(request):

	staffname = request.session['username'] 
	stuclass = request.session['stuclass']
	
	raw_query = 'SELECT * FROM Stafftasks where classname = %s'
	ditems = Stafftasks.objects.raw(raw_query, [stuclass])
	
	if(ditems):
		return render(request, "studentpage.html", {'allitem': ditems, 'name': staffname})
	else:
		return render(request, "studentpage.html", {'error': "NO AVAILABLE ASSIGNMENTS"})
	
		
	return render(request, "staffinput.html", {'name': staffname})
	