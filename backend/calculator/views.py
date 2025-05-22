from django.shortcuts import render
import math

def index(request):
    result = None
    if request.method == "POST":
        expression = request.POST.get("expression")
        try:
            result = eval(expression, {"__builtins__": None}, vars(math))
        except Exception as e:
            result = f"Erreur : {e}"
    return render(request, "calculator/index.html", {"result": result})

