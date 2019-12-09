from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger


def demo(request):
    queryset  = demo.dobjects.filter
    paginator = Paginator(queryset,2)
    page_request_var = 'page'
    page      = request.GET.get(page_request_var)

 try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)         

context = {
        'queryset': paginated_queryset,
        'Page_request_var' : page_request_var
    }
    return render(request,"file.html",context)



  
