from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm
from .models import Artist, Album, Track
from django.views.generic import DetailView


class ArtistDetailView(DetailView):

    model = Artist
    template_name = 'artists/artist_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u_form'] = SubscriberForm
        # context['albums'], context["tracks"] = self.__get_tracks_albums(self.model.pk.)
        # context['now'] = timezone.now()
        return context

    def get(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['u_form'] = SubscriberForm
        print(pk)
        context['albums'], context["tracks"] = self.__get_tracks_albums(pk)
        print(context['albums'], context["tracks"])
        return self.render_to_response(context=context)

    def post(self, request, pk, *args, **kwargs):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            self.object = self.get_object()
            context = context = super().get_context_data(**kwargs)
            context['u_form'] = SubscriberForm
            context['albums'], context["tracks"] = self.__get_tracks_albums(pk)

            messages.success(request, f'Спасибо за подписку!!!')

            return self.render_to_response(context=context)
        else:
            messages.success(request, f'Вы уже подписаны!!!')

            form = SubscriberForm()

            self.object = self.get_object()
            context = context = super().get_context_data(**kwargs)
            context['u_form'] = form
            context['albums'], context["tracks"] = self.__get_tracks_albums(pk)

            return self.render_to_response(context=context)

    def __get_tracks_albums(self, pk):
        return (
            Track.objects.filter(artist=pk),
            Album.objects.filter(artist=pk),
        )

def index(request):
    artists = Artist.objects.all()

    context = {
        "artists": artists,
    }

    return render(request, "index.html", context)
