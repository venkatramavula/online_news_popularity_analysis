from django.shortcuts import render
import joblib

def home(request):
    return render(request , "home.html")

def result(request):
    cls = joblib.load('CART.sav')
    lr = joblib.load('LR.sav')
    lis = []
    lis.append(request.GET['Mon'])
    lis.append(request.GET['Tues'])
    lis.append(request.GET['Wed'])
    lis.append(request.GET['Thurs'])
    lis.append(request.GET['Fri'])
    lis.append(request.GET['Sat'])
    lis.append(request.GET['Sunday'])
    lis.append(request.GET['weekend'])
    lis.append(request.GET['avg_max_shares'])
    lis.append(request.GET['avg_min_share'])
    lis.append(request.GET['avg_shares'])
    if request.GET['Model'] == "DecesionTree":
        name = "Decesion Tree Classifier"
        data_model = cls
    else:
        name = "Logistic Regression"
        data_model = lr

    ans = data_model.predict([lis])

    print("Ansssss",ans)
    return render(request,'result.html',{"ans":ans.mean() ,"model_name":name})
