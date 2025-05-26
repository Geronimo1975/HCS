from apps.base.models import Service

def services_processor(request):
    services = Service.objects.all()
    return {"services": services}
