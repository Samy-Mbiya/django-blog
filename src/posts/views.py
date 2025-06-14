from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from posts.models import BlogPost


# Affichage de la Liste des posts
class BlogHome(ListView):
    model = BlogPost # on affiche toute la liste
    context_object_name = "posts" #a utiliser dans le template

    def get_queryset(self):
        queryset = super().get_queryset() # on recupere la requette
        if self.request.user.is_authenticated:# on verifie si l'utilisateur est connecté
            return queryset # on affiche tout

        return queryset.filter(published=True)  # on que le publication qui on un valeur true

# creation du post
@method_decorator(login_required, name='dispatch') # etre connecté avant de crée
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content',]
    # le redirectionement est fait a partire de la methode dans le fichier models.py dans la clase BlogPost


# Mise à jour
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published',]

# Detail du Post
class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

#Suppression du Post
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_delete_confirm.html"  # 🔹 Template requis
    success_url = reverse_lazy("posts:home")











