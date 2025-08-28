from django.contrib import admin
from .models import Contact
from .models import Profile, About, Resume, Education, Training , Portfolio, Summary,Contact
# Register models in the admin panel
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Training)
admin.site.register(Portfolio)
admin.site.register(Summary)
admin.site.register(Contact)
