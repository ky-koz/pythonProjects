# Python Projects
Python projects completed with the Tech Academy

## General Info
The files found in the codingDrills folder are chunks of code used to learn the basics and application of Python. The code snippets below are from a live project in which we applied SCRUM methodology in two-week sprints. With 6 other developers, we worked on web application projects together. We collaborated as a team via Slack to exchange challenges, solutions, and communications. We used Visual Studio and Azure DevOps for version control.

## Live Project
Created a web application in Python using Django to store data from an API service, a scraped web page with BeautifulSoup, and input from an admin. Created a model, index and details page, edit and delete functions and code to connect to the main app.

## Story Index
* [Build the Basic App](#build-the-basic-app)


### Build the Basic App
1. Create a new app using manage.py startap
2. Register app from within MainProject>MainProject>settings.py
3. Create base and home templates in a new template folder
4. Add function to views to render the home page
5. Register urls with MainApp and create urls.py for your app and homepage
6. Add minimal content, such as title, image, etc, and some basic styling to home

settings.py
```
INSTALLED_APPS = [
     'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
     'FootyDemo',
+    'artApp',
     'RecipeNomad',
     'GotDemo',
]
```

art_base.html
```
{% extends 'base.html' %}
{% load staticfiles %} <!-- must load static files on every template, even though it extends another template -->
{% block appcontent %}
    <section>
        <div class="flex-container wrapper">
            <h5>Square Post Art Application</h5>
            <hr />
            <a class= 'tabNav' href="{% url 'art' %}">Square Post Home Page</a>
            <a class= 'tabNav'  href="{% url 'listArtWorks' %}">Art Collection</a>
            {% comment %}<a class= 'tabNav'  href="#">Square Post API Service</a>{% endcomment %}
            <a class= 'tabNav'  href="{% url 'artNews' %}">Contemporary Art News</a>
        </div>
    </section>
    {% block templatecontent %}{% endblock %} <!-- section that all the template specific content will render within -->
{% endblock %}
```

art_home.html
```
{% extends 'artApp/art_base.html' %}
{% load staticfiles %}
{% block templatecontent %}
<section>
    <div id="footyPic">
        <img src="{% static 'images/arthome.jpg' %}">
        <span class="footy_center"><strong>Welcome to the Square Post Art App</strong><br />
        A collection manager app for lovers of our contemporary, post postmodern art world! There's a database to manage a
        collection of artworks, an API for new artists and works, and articles featuring recent exhibitions scraped from
        the Contemporary Art Daily website. Take a look.</span>
        <br />
        <a class="footy_caption" href="http://www.contemporaryartdaily.com/2019/11/gili-tal-at-eth-zurich/" target="_blank" rel="noopener noreferrer" title="artwork by Gili Tal at ETH Zurich"><span>Gili Tal, photo by Nelly Rodriguez</span></a>
    </div>
</section>
{% endblock %}

<!-- Gili_Tal_gta©NellyRodriguez -->
```

views.py
```
#View function that renders the home page - no context needed
def home(request):
    return render(request, 'artApp/art_home.html')
```

urls.py
```
urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('HomePage.urls')),
     path('footy/', include('FootyDemo.urls')),
+    path('art/', include('artApp.urls')),
     path('RecipeNomad/', include('RecipeNomad.urls')),
     path('got/', include('GotDemo.urls')),
]
```

### Create Index Page
1. Create a new index page, link it from your home page
2. Add in a function that gets all the items from the database and sends them to the template
3. Display a list of items in the database, with some or all of the fields for that item displayed with labels/header
4. Link your app's home page to the main home page


art_index.html
```
{% extends 'artApp/art_base.html' %}
{% load staticfiles %}
{% block templatecontent %}
<section >
    <div class="flex-container" id="jerseyCollectionPage">
        <table class="table-striped">
            <tr>
                <th class="col-md">Artist</th>
                <th class="col-md">Title</th>
                <th class="col-md">Medium</th>
                <th class="col-md">Size</th>
                <th class="col-md">Year</th>
                <th class="col-md">Location</th>
            </tr>
            {% for artWork in artWorks %}     <!-- creates a new row for each art work in the collection -->
                <tr>
                    <td class="col-md">{{artWork.artist}}</td>
                    <td class="col-md">{{artWork.title}}</td>
                    <td class="col-md">{{artWork.medium}}</td>
                    <td class="col-md">{{artWork.size}}</td>
                    <td class="col-md">{{artWork.year}}</td>
                    <td class="col-md">{{artWork.location}}</td>
                    <td class="col-md"><a href="{{artWork.pk}}/Details"><button class="primary-light-button">Details</button></a></td>    <!-- creates a link for that specific art work -->
                </tr>
            {% endfor %}
        </table>
        <button class="primary-bright-button" type="button" onclick=" location.href='{% url 'createArtWork' %}'">Add to Collection</button>
    </div>
</section>
{% endblock %}
```

views.py
```
#View function that controls the main index page - list of jerseys
def index(request):
    get_artWorks = ArtWork.ArtWorks.all()      #Gets all the current art works from the database
    context = {'artWorks': get_artWorks}      #Creates a dictionary object of all the art works for the template
    return render(request, 'artApp/art_index.html', context)

#View function to add a new art work to the database
def add_artWork(request):
    form = ArtWorkForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/art work to the database
        return redirect('listArtWorks')			 # Redirects to the index page, which is named 'art' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = ArtWorkForm()                     #Creates a new blank form
    return render(request, 'artApp/art_create.html', {'form':form})
```

urls.py
```
urlpatterns = [
    path('', views.home, name='art'),                                #home page
    path('Collection/', views.index, name='listArtWorks'),  # index of art works
```

