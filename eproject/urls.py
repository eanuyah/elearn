from django.urls import path
from .import views 
#from .homepage import homeviews

urlpatterns = [

    path('' ,views.home, name = 'home'),
	
	path('deletedata/<getid>' ,views.deletedata, name = 'deletedata'),
	
	path('login/' ,views.login, name = 'login'),
	
	path('staffpage/' ,views.staffpage, name = 'staffpage'),
	
	path('staffinput/' ,views.staffinput, name = 'staffinput'),
	
	path('deleteitem/<getid>' ,views.deleteitem, name = 'deleteitem'),
	
	path('studentpage/' ,views.studentpage, name = 'studentpage'),
	

]
