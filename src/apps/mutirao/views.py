from django.shortcuts import render, redirect
from django.views import View
from .models import Emenda, Review
from .forms import MutiraoForm
from django.db.models import Count

class MutiraoView(View):
    def post(self, request, *args, **kwargs):

        form = MutiraoForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.emenda = Emenda.objects.get(pk=form.cleaned_data['emenda_id'])
            obj.save()
            return redirect('mutirao', tipo=self.kwargs['tipo'], ano=self.kwargs['ano'], numero=self.kwargs['numero'])

    
    def get(self, request, *args, **kwargs):
        emenda = Emenda.objects.filter(pl__tipo=self.kwargs['tipo'],pl__numero=self.kwargs['numero'],pl__ano=self.kwargs['ano']).annotate(r_count=Count('review'))
        emenda = emenda.filter(r_count__lt=2).order_by('r_count')
        count = len(emenda)
        if not emenda:
            return render(request, 'mutirao/obrigado.html', { 'tipo' : self.kwargs['tipo'], 'numero' : self.kwargs['numero'], 'ano' : self.kwargs['ano']})
        
        form = MutiraoForm({'emenda_id' : emenda[0].id, 'apoiar':False})
        context = {
            'emenda' : emenda[0],
            'form' : form,
            'count' : count
        }
        return render(request, 'mutirao/emenda.html', context)