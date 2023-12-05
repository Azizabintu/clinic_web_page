from landing_page.models import Company

def company_data_func(request):
    return {
        'company_data': Company.objects.get(id=1)
    }