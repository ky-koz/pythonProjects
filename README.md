# Python Projects
Python projects completed with the Tech Academy

## General Info
The files found in the codingDrills folder are chunks of code used to learn the basics and application of Python. The code snippets below are from a live project in which we applied SCRUM methodology in two-week sprints. With 6 other developers, we worked on web application projects together. We collaborated as a team via Slack to exchange challenges, solutions, and communications. We used Visual Studio and Azure DevOps for version control.

## Live Project
Created a web application in Python using Django to store data from an API service, a scraped web page with BeautifulSoup, and input from an admin. Created a model, index and details page, edit and delete functions and code to connect to the main app.

## Story Index
* [Build the Basic App](#build-the-basic-app)
* [Create Index Page](#create-index-page)
* [Create Details Page](#create-details-page)
* [Create Edit and Delete Functions](#create-edit-and-delete-functions)
* [Setup Beautiful Soup](#setup-beautiful-soup)
* [Parse Through HTML](#parse-through-html)


### Build the Basic App
1. Created a new app using manage.py startap
2. Registered app from within MainProject>MainProject>settings.py
3. Created base and home templates in a new template folder
4. Added function to views to render the home page
5. Registered urls with MainApp and create urls.py for art app and homepage
6. Added minimal content, such as title, image, etc, and some basic styling to home

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

[Back to Top](#general-info)

### Create Index Page
1. Created a new index page, linked it from art home page
2. Added in a function that gets all the items from the database and sends them to the template
3. Displays a list of items in the database, with some or all of the fields for that item displayed with labels/header
4. Linked art app's home page to the main home page


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
    path('AddToCollection/', views.add_artWork, name='createArtWork'),  # add new artWork
```

[Back to Top](#general-info)

### Create Details Page
Create a details page that will show the details of any single item from within the database, as selected by the user. Link this to the index page for each item.

1. Added a details template to the template folder, registered the url patterm
2. Created a views function that will find the single desires instance from the database and send it to the template
3. Added in links for each element on the index page that will direct to the details page for that item
4. Displayed all the details of the item on the details page

art_details.html
```
{% extends 'artApp/art_base.html' %}
{% load staticfiles %}
{% block templatecontent %}
<section>
    <div class="flex-container footy">
        <table>
            <tr>
                <th>Artist</th>
                <td>{{artWork.artist}}</td>
            </tr>
            <tr>
                <th>Title</th>
                <td>{{artWork.title}}</td>
            </tr>
            <tr>
                <th>Medium</th>
                <td>{{artWork.medium}}</td>
            </tr>
            <tr>
                <th>Size</th>
                <td>{{artWork.size}}</td>
            </tr>
            <tr>
                <th>Date</th>
                <td>{{artWork.year}}</td>
            </tr>
            <tr>
                <th>Location</th>
                <td>{{artWork.location}}</td>
            </tr>
        </table>
        <div class="row">
            <button class="primary-light-button col-3" type=button" onclick=" location.href='../../{{artWork.pk}}/Edit'">Edit this Art Work</button> <!-- will redirect to this items edit page -->
            <button class="primary-light-button col-3" type="button" onclick=" location.href='../../{{artWork.pk}}/Delete'">Delete this Art Work</button>
        </div>
        <hr />
        <button class="primary-bright-button" type="button" onclick=" location.href='{% url 'listArtWorks' %}'">Back to Collection</button>
    </div>
</section>
{% endblock %}
```

views.py
```
#View function to look up the details of an art work
def details_artWork(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    artWork = get_object_or_404(ArtWork, pk=pk)   #Gets single instance of the art work from the database
    context={'artWork':artWork}                   #Creates dictionary object to pass the art work object
    return render(request,'artApp/art_details.html', context)
```

art_index.html
```
<td class="col-md"><a href="{{artWork.pk}}/Details"><button class="primary-light-button">Details</button></a></td>    <!-- creates a link for that specific art work -->
```

urls.py
```
path('Collection/<int:pk>/Details/', views.details_artWork, name='artWorkDetails'), # get details for a single art work
```

[Back to Top](#general-info)

### Create Edit and Delete Functions
Allow for edit and delete functions to be done from the details page or from separate pages. Have confirmation before deleting.

1. Added an edit page to the templates (a pattern url)
2. Used model forms and instances to display the content of a single item from the database
3. Set the views function to send the information for the single item and save any changes
4. Included the option to delete an item with a confirmation that the user wants to delete

art_edit.html
```
{% extends 'artApp/art_base.html' %}
{% load staticfiles %}
{% block templatecontent %}
<section>
    <div class="flex-container footy">
        <form method="post">
            {% csrf_token %}
            <table>
                {{form.as_table}}
            </table>
            {{ form.non_field_errors}}
            <button class="primary-light-button" type="submit">Update Art Work</button>
        </form>
        <hr />
        <button class="primary-bright-button" type="button" onclick=" location.href='{% url 'listArtWorks' %}'">Back to Collection</button>
    </div>
</section>
{% endblock %}
```

art_delete.html
```
{% extends 'artApp/art_base.html' %}
{% load staticfiles %}
{% block templatecontent %}
<section>
    <div class="flex-container">
        <div class="footy"><h4>Are you sure you want to delete this art work?</h4></div>
        <div class="footy">
        <table>
            <tr>
                <th>Artist</th>
                <td>{{artWork.artist}}</td>
            </tr>
            <tr>
                <th>Title</th>
                <td>{{artWork.title}}</td>
            </tr>
            <tr>
                <th>Medium</th>
                <td>{{artWork.medium}}</td>
            </tr>
            <tr>
                <th>Size</th>
                <td>{{artWork.size}}</td>
            </tr>
            <tr>
                <th>Year</th>
                <td>{{artWork.year}}</td>
            </tr>
            <tr>
                <th>Location</th>
                <td>{{artWork.location}}</td>
            </tr>
        </table>
        <form method="post">
            {% csrf_token %}
        <button  class="primary-light-button" type="submit">Delete this Art Work</button>
        </form>
        <hr />
        <button class="primary-bright-button" type="button" onclick=" location.href='{% url 'listArtWorks' %}'">Back to Collection</button>
    </div>
    </div>
</section>
{% endblock %}
```

view.py
```
#View function to edit the details of a art work
def edit_artWork(request, pk):
    pk = int(pk)
    artWork = ArtWork.ArtWorks.get(pk=pk)          #Alternate way to get the single art work from the database
    form = ArtWorkForm(data=request.POST or None, instance=artWork)   #Creates a form filled in with the details of this art work
    if request.method == 'POST':                #If the form is being posted back with changes
        if form.is_valid():                     #Check that the form is still valid
            form.save()                         #Save the changes made to the art work details
            return redirect('artWorkDetails',pk) #Redirect to the details page for that art work
        else:                                   #Else for form not being valid
            print(form.errors)
    else:                                       #Else for request not being Post method
        return render(request,'artApp/art_edit.html', {'form':form})


#View function for deleting a art work
def delete_artWork(request, pk):
    pk = int(pk)
    artWork = ArtWork.ArtWorks.get(pk=pk)
    context = {'artWork': artWork}            #Sets the art work to a dictionary item for the template
    if request.method == 'POST':            #If the user posts a form, in this case just a delete button
        artWork.delete()                     #Deletes the art work from the database
        return redirect('listArtWorks')            #Redirects back to the index
    else:
        return render(request, 'artApp/art_delete.html', context)
```

urls.py
```
path('Collection/<int:pk>/Edit/', views.edit_artWork, name='artWorkEdit'),  # edit a single art work
path('Collection/<int:pk>/Delete/', views.delete_artWork, name='artWorkDelete'),  # delete a single art work
```

[Back to Top](#general-info)

### Setup Beautiful Soup
Pt. 1
Create a new template for displaying information sourced from another website. Use Beautiful Soup (BS) to scrape the site and find relevant information.

1. Created a new template for displaying the content
2. Used BS to get the html data from a selected site as a navigable object
3. Utilized functions of BS to find sections of data based on tags

### Parse Through HTML
Pt. 2
Parse through the html returned and display the information you wnat to display. Make sure you are getting the indivdual elements and stripping away any formatting you don't want. Add a link from your app's home page.

1. Got elements out of the BS object, send just the values desired as relevant objects to the template (nested dictionaries)
2. Displayed all objects within the data scrape template
3. Tested to ensure proper functioning, did not need to do error handling
4. Linked the data scraping page to art app's home page

art_news.html
```
{% extends 'artApp/art_base.html' %}
{% load staticfiles %}
{% block templatecontent %}
<section>
    <div class="flex-container wrapper news">
        {% for article in articles%} <!-- Iterates through the array of articles -->
            <!-- Creates a new line for each item, gives the article title and description -->
            <img src="{{article.img}}"  alt="" width=20%>
            <h4><a href="{{article.url}}">{{article.title}}</a></h4>
        {% endfor %}
    </div>
</section>
{% endblock %}
```

views.py
```
#View function for data scraping the Art Newspaper website for current news stories
def art_news(request):
    source = requests.get("https://www.theartnewspaper.com/contemporary-art")  # Get contemporaryartdaily.com//news as an html document
    print(source.status_code)  #Used for debugging to ensure a 'success' code of 200
    soup = BS(source.content, 'html.parser') #Initial processing of the html by beautiful soup, soup is now a navigatable object
    nodes = soup.find_all(class_="cp-regulars") # Search for divs with class node-title
    articles = [] #Create blank array to add articles to
    for node in nodes:  #Iterates through all the objects with class of node-title
            title = node.find('h3').get_text() #Sets title equal to the text of the a tag
            link = node.find('a').get('href') # Sets link equal to the href of the a tag
            img = node.find('div').get('data-bg')
            url = "https://www.theartnewspaper.com" + link #Modifies the link to a full url, since the links were relative
            article = {'title':title, 'url':url, 'img': img} #Creates and article object dictionary with needed elements
            articles.append(article) #Adds article dictionary item to the array before iterating through next node
    context={'articles':articles} #Creates a dictionary element for the articles to pass to the template
    return render(request, 'artApp/art_news.html', context)
```

urls.py
```
 path('artNews/', views.art_news, name='artNews'),  # data scraped news from artnews
```

[Back to Top](#general-info)
