from django.db import models
from django.contrib.auth.models import User

    # Profile model
class Profile(models.Model):
    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True, blank=True)  # Made optional
    profile_image = models.ImageField(upload_to='profile', null=True, blank=True)
    mobile_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='MALE')
    address = models.TextField()
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # About section

class About(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)  
    website = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100, null=True, blank=True)  
    age = models.CharField(max_length=3, null=True, blank=True)
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance = models.CharField(max_length=100, null=True, blank=True)

    # Resume section

class Resume(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    text_area = models.TextField(max_length=200)

    # Education section

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tag = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    text_area = models.TextField(max_length=250)
    duration = models.DurationField(null=True, blank=True)
    
    # Traing models (traing 'change kiya gaya hai migrate karna hai')
class Training(models.Model):
    profile = models.ManyToManyField(Profile)
    heading = models.CharField(max_length=200,default='')
    Company = models.CharField(max_length=200,default='')  
    text_area = models.TextField()
    # Portfolio models
    
class Portfolio(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    paragraph=models.TextField()
    # Summary models
class Summary(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50, default='Sani')
    summary = models.CharField(max_length=500, default='A motivated BCA student...')
    college = models.CharField(max_length=100, default='KNIPSS College Sultanpur')
    phone = models.CharField(max_length=20, default='7755027538')
    email = models.EmailField(default='saniyadav7755@gmail.com')
    # Experience model
class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Contact models
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Optional

    def __str__(self):
        return f"{self.name} | {self.email}"

def your_view(request):
    # Your view logic here
    context = {}
    return render(request, 'index.html.html', context)

