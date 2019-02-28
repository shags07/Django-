# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import textwrap
from django.views.generic.base import View

# Create your views here.
class HomePageView(View):
	def dispatch(request,*args,**kwargs):
		response_text = textwrap.dedent('\
				      	       <html>\
				               <body>\
				               <h2>Patching </h2>\
					       <form>\
 					       HostName:<br>\
					       <input type="text" name="HostName" value="">\
					       <br>\
                                               Search package:<br>\
 					       <input type="text" name="SearchPackage" value="">\
 					       <br><br>\
  					       <input type="submit" value="Submit">\
				               </form>\
					       </body>\
					       </html>\
					       ')
		return HttpResponse(response_text)
