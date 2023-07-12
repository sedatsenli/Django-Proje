from django.shortcuts import render
from .forms import OrderForm

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.save()
            return render(request, 'order_created.html')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

