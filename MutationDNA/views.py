from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from . import functions
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from ast import literal_eval
from stats.models import DNAStrings

@method_decorator(csrf_exempt, name='dispatch')
def hasMutation(request):

    if request.method == 'POST':
        dna = literal_eval(request.POST['dna'])
        DNAS = DNAStrings.objects.create(dnaString=dna)
        if(functions.hasMutation(dna)):
            DNAS.mutation = True;
            DNAS.save()
            return HttpResponse()
        else:
            DNAS.save()
            return HttpResponseForbidden()
    
    return HttpResponse()

def stats(request):
    allDNAs = DNAStrings.objects.all()
    total = allDNAs.count()
    count_mutations = allDNAs.filter(mutation=True).count()
    count_no_mutations = allDNAs.filter(mutation=False).count()
    ratio = (count_mutations * 100) / total

    obj = {
        'count_mutations': count_mutations,
        'count_no_mutations': count_no_mutations,
        'ratio': ratio
    }

    return JsonResponse(obj)

    