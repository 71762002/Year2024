from django.db import models



class Holiday(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
    
    def get_new_image(self):
        return Image.objects.filter(holiday_id=self.id).first().image
    

class AboutUs(models.Model):
    image = models.ImageField(upload_to='newyear/image')
    description = models.CharField(max_length = 200)
    

    def __str__(self):
        return self.image
    

class Image(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=200, blank=True, null=True)
    holiday = models.ForeignKey(Holiday, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.image} - {self.name}"
    
    
    
