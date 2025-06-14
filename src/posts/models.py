from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu") #verbose_name c'est comme le label
    thumbnail = models.ImageField(blank=True, null=True , upload_to='blog')

    class Meta:
        ordering = ['-create_on']
        verbose_name = "Article" #Permet d'afficher  l'information dans les getionnaire des utilisateurs

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): #Enregistrement du slug
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property #Permet de metre la methode au templates
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"

    def get_absolute_url(self):
        return reverse('posts:home') # on redirige ve la liste (posts est la valeure qu'on recupere dans urls app_name ="posts" et home est le nom du lien de blog)