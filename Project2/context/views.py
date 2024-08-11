from django.shortcuts import render

def home(request):
    d={'age':20 ,'lst':[1,2,3,4,5,6],'courses':[
        {'id': 1,
         "Name":'python',
         'fee':400,
        },
        {'id': 2,
         "Name":'python2',
         'fee':200,
        },
        {'id': 3,
         "Name":'python3',
         'fee':600,
        }
    ]
    }
    return render(request,'context/context.html',d)
