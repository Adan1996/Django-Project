from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    email = models.EmailField(default='nama@mail.com') # default adalah options untuk memasukan nilai default email, karena field email tidak boleh kosong
    alamat = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.title)