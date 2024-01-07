from django.contrib import admin

from .models import Track, Album, Artist, SubscribeForm

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(SubscribeForm)
admin.site.register(Track)

fields = ['image_tag']
readonly_fields = ['image_tag']
