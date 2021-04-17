from django.shortcuts import render
from django.http import HttpResponse
from nsetools import Nse


def home(request):
	nse = Nse()
	nifty_bank = nse.get_index_quote("nifty bank")
	nifty_50 = nse.get_index_quote("nifty 50")
	india_vix = nse.get_index_quote("india vix")
	contaxt = {
		'nifty_bank':nifty_bank,
		'nifty_50':nifty_50,
		'india_vix':india_vix
	}
	return render(request, 'stockinfo/base.html',contaxt)

def profile(request):
	return render(request, 'stockinfo/profile.html')