from django.shortcuts import render,HttpResponse
from itertools import product

# Create your views here.
def index(request):
    return HttpResponse('hello')

def robots(request):
    return HttpResponse("there are many routes how much will you check!! try searching the route of what you want")
l=[]
for i in product('abcdefghjklmnpqrtuvwyz',repeat=4):
    l.append(i)

for j in l:
    i=''.join(j)
    if i=='flag':
        code = f"def {i}(request):\n  return HttpResponse('flag you got')"
        exec(code)
    else:
        code = f"def {i}(request):\n  return HttpResponse('Nope!')"
        try:
            exec(code)

        except:
            continue

print

