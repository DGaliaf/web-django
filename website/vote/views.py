from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .forms import ArtistUpdateForm, TrackUpdateForm, AlbumUpdateForm
# from .models import VoteArtist, VoteAlbum, VoteTrack



@login_required()
def vote(request):
    # if request.method == 'POST':
    #     artist_form = ArtistUpdateForm(request.POST, instance=request.user)
    #     track_form = TrackUpdateForm(request.POST, instance=request.user)
    #     album_form = AlbumUpdateForm(request.POST, instance=request.user)
    #
    #     if artist_form.is_valid():
    #         artist_form.save()
    #     elif track_form.is_valid():
    #         track_form.save()
    #     elif album_form.is_valid():
    #         album_form.save()
    #
    #     messages.success(request, f"Благодарим за ваш голос")
    #
    #     return redirect('vote:vote_page')
    #
    # else:
    #     artist_votes = VoteArtist.objects.all()
    #     track_votes = VoteTrack.objects.all()
    #     album_votes = VoteAlbum.objects.all()
    #
    #     artist_form = ArtistUpdateForm(instance=request.user)
    #     track_form = TrackUpdateForm(instance=request.user)
    #     album_form = AlbumUpdateForm(instance=request.user)
    #
    # context = {
    #     'artist_form': artist_form,
    #     'track_form': track_form,
    #     'track_form_err': track_form.errors,
    #     'album_form': album_form,
    #     'album_votes': album_votes,
    #     'track_votes': track_votes,
    #     'artist_votes': artist_votes,
    # }

    return render(request, 'vote_page.html')
