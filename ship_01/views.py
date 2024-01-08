from django.shortcuts import render, redirect
from .forms import NameForm
from .models import ShipList,UserList
from django.core.paginator import Paginator # 페이징 기능이 있는 함수를 import!

# Create your views here.
def form_basic(request):#클래스 가져옴
    form = NameForm()#인스턴스 객채를 만듬
    return render(
        {'form':form}
    )

def Ship_List(request):#클래스 가져옴
    info = ShipList.objects.all()#info 라는 값으로~
    # p=Paginator(info,4)#Paginator를 통해서 4개씩 담아줌
    return render(
        request, 'ship_01/ship_list.html',
        {'info':info}#info 해서 받아온 값을 Dictionary로 전송을 해줌
    )

def main(request):

    return render(request,"ship_01/main.html")

def select(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        
        search = request.GET.get('search', '')
    
        
        shiplist = ShipList.objects.filter(name__icontains = search)
        p = Paginator(shiplist, 10)

        info = p.page(page)

        start_page = (int(page) - 1) // 10 * 10 + 1
        end_page = start_page + 9
        if end_page > p.num_pages:
            end_page = p.num_pages



        context = {
        'shiplist' : info,
        'page_range' : range(start_page, end_page + 1),
        'search' : search
        }
        return render(request, 'ship_01/select.html', context)
    
def insert(request):
    if request.method == 'POST':
        code = ShipList.objects.order_by('-code').first().code + 1
        name = request.POST.get('name')
        owner = request.POST.get('owner')
        type = request.POST.get('type')
        length = request.POST.get('length')
        height = request.POST.get('height')
        width = request.POST.get('width')
        waterline = request.POST.get('waterline')
        # pubs = BookStore.objects.filter(name__icontains = publisher)        
        
        # if publisher == '':
        #     publisher_id = 0
        # elif not pubs:
        #     bscode = BookStore.objects.order_by('-bscode').first().bscode + 1
        #     BookStore.objects.create(bscode=bscode,
        #                              name=publisher)
        #     publisher_id = bscode
        # elif len(pubs) >= 2:
        #     # 2개 이상일때 선택하는 코드
        #     publisher_id = pubs[0].bscode
        # else:

        #     publisher_id = pubs[0].bscode

        # year_of_publication = request.POST.get('year_of_publication')
        # price = request.POST.get('price')
        # if price == '':
        #     price = 0
        

        ShipList.objects.create(code=code,
                                name=name,
                                owner=owner,
                                type=type,
                                length=length,
                                height=height,
                                width=width,
                                waterline=waterline)

        
        return redirect('/')
        # return render(request, 'book_list/main.html')
    else:
        return render(request, 'ship_01/insert.html')
    
def update(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        shiplist = ShipList.objects.all()
        p = Paginator(shiplist, 10)

        info = p.page(page)

        start_page = (int(page) - 1) // 10 * 10 + 1
        end_page = start_page + 9
        if end_page > p.num_pages:
            end_page = p.num_pages



        context = {
        'shiplist' : info,
        'page_range' : range(start_page, end_page + 1)
        }
        return render(request, 'ship_01/update.html', context)
    elif request.method == 'POST':
        code = ShipList.objects.order_by('-code').first().code + 1
        name = request.POST.get('name')
        owner = request.POST.get('owner')
        type = request.POST.get('type')
        length = request.POST.get('length')
        height = request.POST.get('height')
        width = request.POST.get('width')
        waterline = request.POST.get('waterline')        
        # pubs = BookStore.objects.filter(name__icontains = publisher)

        # if not pubs:
        #     bscode = BookStore.objects.order_by('-bscode').first().bscode + 1
        #     BookStore.objects.create(bscode=bscode,
        #                              name=publisher)
        #     publisher_id = bscode
        # elif len(pubs) >= 2:
        #     # 2개 이상일때 선택하는 코드
        #     publisher_id = pubs[0].bscode
        # else:

        #     publisher_id = pubs[0].bscode

        # year_of_publication = request.POST.get('year_of_publication')
        # price = request.POST.get('price')

        update_data = ShipList.objects.get(code = code)
        if name != '':
            update_data.name = name
        if owner != '':
            update_data.owner = owner
        # if publisher != '':
        #     update_data.publisher_id = publisher_id
        # if year_of_publication != '':
        #     update_data.year_of_publication = year_of_publication
        # if price != '':
        #     update_data.price = price

        update_data.save()

        return redirect('/')

def delete(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        shiplist = ShipList.objects.all()
        p = Paginator(shiplist, 10)

        info = p.page(page)

        start_page = (int(page) - 1) // 10 * 10 + 1
        end_page = start_page + 9
        if end_page > p.num_pages:
            end_page = p.num_pages



        context = {
        'shiplist' : info,
        'page_range' : range(start_page, end_page + 1)
        }
        return render(request, 'ship_01/delete.html', context)
    elif request.method == 'POST':
        code = request.POST.get('code')
        ShipList.objects.get(code = code).delete()
        
        return redirect('/')



