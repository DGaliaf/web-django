from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm
from .models import Artist
from django.views.generic import DetailView


class ArtistDetailView(DetailView):

    model = Artist
    template_name = 'artists/artist_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u_form'] = SubscriberForm
        # context['now'] = timezone.now()
        return context

    def post(self, request, *args, **kwargs):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            self.object = self.get_object()
            context = context = super().get_context_data(**kwargs)
            context['u_form'] = SubscriberForm
            messages.success(request, f'Спасибо за подписку!!!')

            return self.render_to_response(context=context)
        else:
            messages.success(request, f'Вы уже подписаны!!!')

            form = SubscriberForm()

            self.object = self.get_object()
            context = context = super().get_context_data(**kwargs)
            context['u_form'] = form

            return self.render_to_response(context=context)

def index(request):
    artists = Artist.objects.all()

    context = {
        "artists": artists,
    }

    return render(request, "index.html", context)
