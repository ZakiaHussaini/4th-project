# QueenStore - Introduction
QueenStore is an online marketplace where users can buy online or sell online any afghan women handicrafts.This website able Users to add their own products for sale on and other users can contact and communicate to seller to buy a product. 

![Am I Responsive](/documentation/am-i-responsive.png) 


The Live Site can be found [here](https://queen-store.herokuapp.com/).

# Table of Contents
* [User Experience](#user-stories)
    * [Admin](#admin)
    * [registered User](#member-user)
    * [General User](#general-user)
* [Features](#features)
    * [Existing Features](#existing-features)
* [Future Features](#future-features)
* [Structure](#structure)
* [Databases](#databases)
    * [Post Model](#post-model)
    * [Comment Model](#comment-model)
* [Technologies Used](#technologies-used)
* [Frameworks, Libraries & Tools Used](#frameworks-libraries--tools-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

# User Experience
## Admin
* As an admin I can navigate the admin panel so that I can create, read, update and delete products on website. 

## register User
* As a registered user I can click the the inbox so that see who send me message.
* As a registered user I can click on products in my dashboard so that I can edit or delete them.
* As a registered user I can add new product so that I can sell my product.
* As a registered user I can see list of my products so that I can view a list of products added by me.
* As a registered user I can I can click on a product so that I can contact to seller and send message.


## General User
* As a general user I can clear filter that I have chosen before so that I can see all products.
* As a general user I can search items based on title and description so that I can find easily specific product.
* As a general user I can browse products based on their categories so that I can find list of products belongs to each category.
* As a general user I can view categories so that I can read how many products belongs to each category.
* As a general user I can view list of products so that I can select one to see the description.
* As a general user I can click on a product so that I can see the detail of product.
* As a general user I can register an account so that I can add products to sell.


## Design

### Color Scheme

The main colour schemes for the website are black, light gray and oranged color. The site uses black color for the background and light gray and oranged color for the text.
These colours were used throughout all the pages in such a way as to ensure adequate contrast and good user experience.

* orange color (#e74c3c)

![navbar](readme-img/orange%20color.png)


* light gray color (#d3d3d3)

![navbar](readme-img/gray.png)




### Fonts

The fonts selected were from Google Fonts, Poppins, Exo, Pacifico with sans-serif as a backup font.


### Structure

#### Website pages

Simplicity, clarity and ease of navigation between pages were the main aspects for design of this website's structure.

At the top of the page there is a recognisable type of navigation bar with website name on the left side and the navigation links to the right which collapses to hamburger icon on smaller screen sizes. At the bottom of the page there is a footer with links to a contact page and social media.

- The website consists of the following sections:
  - Home page with an overview of the content, aim of the website, new products, and categories.
  - Browse page where a user can see the product's categories,
  and search specific product based on name and description.
  -  once user choose a product user can click on it and see the detail of product like name, price, related images, descriptions and contact to seller.
  - on dashboard page user can see list of own products and can edit or delete each products.
  - the product owner can see the inbox to check who contact to buy a specific product and send message to customer.
  - registerd user can also add products to sell on new item page.
  - Login page for returning user to log in.
  - Register page allowing a new user to sign up.
  - Logout page allowing user to log out of the website.
 



# Features
## Existing Features

* **Navbar**
    * The navbar is responsive depending on whether a user is logged in or not, and the width of the screen. The navbar is fixed in place and is visible on every page and can redirect user to any page they want.
            ![navbar](readme-img/navbar.png)


* **Home Page**
    * The home page consists of a general description about the website, a list of New products added by different users. clicking on one of the products directs the user to product detail page. and also users can look how many items related to each categories.
                ![navbar](readme-img/home1.png)
                ![navbar](readme-img/home4.png)
                ![navbar](readme-img/home3.png)


* **Detail Page**
    * when user click on a specific product they will redirect to detail page. 
    * in detail page user can see the detail of product. if the user is owner then the user can edit or delete the product. 
    ![navbar](readme-img/detail%20.png)

    
    * if the user is not owner then the user can contact seller to communicate with seller.

    ![navbar](readme-img/detail2.png)

    * if user click on contact seller the coversation page appears.

    ![navbar](readme-img/contact%20seller.png)



    * and also the related items also appear in this page.

   ![navbar](readme-img/detail3.png)




   * **Browse Page**
    * In browse page user can see the categories of products and search specific product based on name and description.
    ![navbar](readme-img/browse.png)
    
   * **New Item Page**
    * In new item page registered user can add products to sell and unregistered user will redirect to login page. 
    ![navbar](readme-img/new.png)

   * **dashboard Page**
    * In dashboard users can see list of their own products. 
    ![navbar](readme-img/dashboard.png)


  * **Inbox Page**
    * In Inbox page user can see list of messages related to specific products. 
    ![navbar](readme-img/inbox.png)

    * if user click on a specific message the conversation page appear. 
    ![navbar](readme-img/conversation.png)

        
* **Sign Up**
    * Users can register and create their own account. 
    * The sign-up form checks if the username is used by someone else, alerts the user if any infomration is incorrect, such as passwords not matching or empty required fields.
    * Creating account enables access to more features. 
        
    ![navbar](readme-img/signup.png)
    
* **Sign In**
    * Users can access their account via sign-in/login feature.
   
    * Users can find login option from Menu and from home page.
    * If the user don't have an account, they can click 'sign up' link on the login page and create their account.
        
      ![navbar](readme-img/login.png)


* **Logout**
    * The user can logout from Menu and from their accounts page.
    * The logout modal asks the user if they confirm to logout.

         ![navbar](readme-img/logout.png)
 


# Database
* The backend consists of Python built with the Django framework with a database of a ElephantSQL for the deployed version.

* The following models were created to represent the database model structure for the website:

## Item Model
* The item model contains information about the item.
* The item model contains the following fields: category, name, price, image, rear_image, description, is_sold, created_by, created_at.
* The model has one-to-many relationships with User and Category Model

## Category Model
* The category model contains name of categories.


## Conversation Model
* The conversation model handles communication between users.
* conversation model contains the following fields: item, members, created_at, modified_at.
* The model has one-to-many relationships with User and Item Model


## ConversationMessage Model
This model contains the following fields: conversation, content, created_by, created_at.
The ConversationMessage model has a one-to-many relationship with Conversation Model.




## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [JShint](https://jshint.com/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)

##### Back to [top](#table-of-contents)


## Testing

### Testing Strategy
I utilised a manual testing strategy for the development of the site.
Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the criteria of the user stories listed above were met.


#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.


#### Validator Testing
All code files were validated using suitable validators for the specific language.
HTML & CSS code passed the validation.
JavaScript code produced one warning about the use of an anonymous function within a loop.
When this function was named and moved outside the loop but referenced inside the loop, it broke functionality.
After attempting a few fixes I decided that an anonymous function inside a for loop was an acceptable JavaScript practice.
All validation screenshots are included below.

All HTML validation returned the same result so I have included only 1 screenshot here.
![HTML Validation](./docs/html-validation.png)
![CSS Validation](./docs/css%20validation.png)
![JS Validation](./docs/jshint.png)


#### Lighthouse Testing
Below you can see the results of Googles Lighthouse Testing.

![Lighthouse Testing](./docs/lighthouse-testing.png)


#### Python/JavaScript Testing
All Custom Python & JavaScript code was manually tested multiple times during and after development.
This is reflected in the fact that all of the user stories below are working and have produced no errors in the terminal or the console.

## Testing User Stories


# Testing
*Unit Testing*, *Validator Testing*, and *Bugs* are documented [here](/TESTING.md).

# Deployment:
This project was deployed to Heroku. "Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps."- [Heroku.](https://www.heroku.com/)

<details>
<summary>Steps to open account in Heroku:</summary>
<br>
<ul>
    <li>
        <a href="https://signup.heroku.com/">Signup here </a>if you do not have an account already.
        <img src="documentation/signup-heroku.png">
    </li>
    <li>
        After you fill in all the information for account and sign in, you will be on <a href="https://dashboard.heroku.com/apps">Dashbord.</a> Here is where you will create an application.
    </li>
    <li>
        <p>Click on New => Create new app.</p>
        <img src="documentation/new-app.png">
    </li>
    <li>Choose a name to your application and select location that you are based.</li>
</ul>
</details>

<br>

The initial deployment was immediately after cretaing all the file directories within the repository. This is to ensure and overcome any deployment error before hand and resolve the issue before it gets more complicated.

<br>

<details>
<summary>Steps to Deployment</summary>    
I have followed Code Institute's <a href="https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf" target="_blank">Django Blog Cheat Sheet</a> steps to follow, create and deploy the project on Herokuapps.

<br>

<h2>Step 1: Installing Django and supporting libraries</h2>

<br>

<h3>In the terminal</h3>
<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Install Django and gunicorn:</td>
        <td>pip3 install django gunicorn</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Install supporting libraries: </td>
        <td>pip3 install dj_database_url psycopg2</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Install Cloudinary Libraries</td>
        <td>pip3 install dj3-cloudinary-storage</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Create requirements file</td>
        <td>pip3 freeze --local > requirements.txt</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Create Project</td>
        <td>django-admin startproject PROJ_NAME . (Don’t forget the . )</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Create App</td>
        <td>python3 manage.py startapp APP_NAME</td>
    </tr>
</table>

<br>

<h3>In the setting.py</h3>
<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>7</td>
        <td>Add to installed apps</td>
        <td>‘APP_NAME’,</td>
    </tr>
</table>

<br>

<h3>In the terminal</h3>
<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>8</td>
        <td>Migrate Changes</td>
        <td>python3 manage.py migrate</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Run Server to Test</td>
        <td>python3 manage.py runserver</td>
    </tr>
</table>

<br>

<h2>Step 2: Deploying an app to Heroku</h2>

<br>
<ul> 4 stages:
    <li> Create the Heroku app</li>
    <li>Attach the database</li>
    <li>Prepare our environment and settings.py file</li>
    <li>Get our static and media files stored on Cloudinary</li>
</ul>

<br>

<h3>2.1 Create the Heroku app</h3>

<p>1. Create new Heroku App</p>
<img src="documentation/create-app.png">

<p>2. Add Database to App Resources - Located in the Resources Tab, Add-ons, search andadd e.g. ‘Heroku Postgres’</p>
<img src="documentation/heroku-postgress.png">

<p>3. Copy DATABASE_URL - Located in the Settings Tab, in Config Vars, Copy Text</p>
<img src="documentation/config-var.png">

<br>

<h3>2.2 Attach the Database:</h3>
<h3>In Gitpod</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>4</td>
        <td>Create new env.py file on top level directory</td>
        <td>E.g. env.py</td>
    </tr>
</table>

<br>

<h3>In env.py</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>5</td>
        <td>Import os library</td>
        <td>import os</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Set environment variables</td>
        <td>os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"</td>
    </tr>
     <tr>
        <td>7</td>
        <td>Add in secret key</td>
        <td>os.environ["SECRET_KEY"] = "Make up a randomSecretKey"</td>
    </tr>
</table>

<br>

<h3>In Herkou.com</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>8</td>
        <td>Add Secret Key to Config Vars</td>
        <td>SECRET_KEY, “randomSecretKey”</td>
    </tr>
</table>
<img src = "documentation/add-config-var.png">

<br>

<h3>2.3 Prepare our environment and settings.py file:</h3>
<h3>In settings.py</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>9</td>
        <td>Reference env.py </td>
        <td><img src="documentation/import-env.png"/></td>
    </tr>
    <tr>
        <td>10</td>
        <td>Remove the insecure secret key and replace - links to the secret key variable on Heroku</td>
        <td>SECRET_KEY = os.environ.get('SECRET_KEY')</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Replace DATABASES Section (Comment out the old DataBases Section) - links to the DATATBASE_URL variable on Heroku</td>
        <td><img src="documentation/replace-database.png"/></td>
    </tr>
</table>

<br>

<h3>In the terminal</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>12</td>
        <td>Make Migrations</td>
        <td>python3 manage.py migrate</td>
    </tr>
</table>

<br>

<h3>2.4 Get our static and media files stored on Cloudinary:</h3>
<h3>In Cloudinary</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Copy your CLOUDINARY_URL e.g. API Environment Variable.</td>
        <td>From Cloudinary Dashboard</td>
    </tr>
</table>

<br>

<h3>In env.py</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>2</td>
        <td>Add Cloudinary URL to env.py - be sure to paste in the correct section of the link</td>
        <td>os.environ["CLOUDINARY_URL"] = "cloudinary://9444:ExampleCloudinaryi@dbhyuj5mc"</td>
    </tr>
</table>

<br>

<h3>In Heroku</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>3</td>
        <td>Add Cloudinary URL to Heroku Config Vars - be sure to paste in the correct section of the link</td>
        <td>Add to Settings tab in Config Vars e.g. COUDINARY_URL, cloudinary://9444:ExampleCloudinaryi@dbhyuj5mc</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, must be removed before deployment)</td>
        <td><img src="documentation/DISABLE_COLLECTSTATIC.png"></td>
    </tr>
</table>


<br>

<h3>In settings.py</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>5</td>
        <td>Add Cloudinary Libraries to installed apps (note: order is important)</td>
        <td><img src="documentation/cloudinary.png"></td>
    </tr>
    <tr>
        <td>6</td>
        <td>Tell Django to use Cloudinary to store media and static files. Place under the Static files Note</td>
        <td><img src="documentation/static.png"></td>
    </tr>
    <tr>
        <td>7</td>
        <td>Link file to the templates directory in Heroku. Place under the BASE_DIR line</td>
        <td>TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array</td>
        <td>'DIRS': [TEMPLATES_DIR]</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Add Heroku Hostname to ALLOWED_HOSTS</td>
        <td>ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]</td>
    </tr>
</table>

<br>

<h3>In Gitpod</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>10</td>
        <td>Create 3 new folders on top level directory</td>
        <td>media, static, templates</td>
    </tr>
     <tr>
        <td>11</td>
        <td>Create procfile on the top level directory</td>
        <td>Procfile</td>
    </tr>
</table>

<br>

<h3>In Procfile</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>12</td>
        <td>Add code</td>
        <td>web: gunicorn PROJ_NAME.wsgi</td>
    </tr>
</table>

<br>

<h3>In Terminal</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>13</td>
        <td>Add, Commit and Push </td>
        <td>
            <p>git add . </p>
            <p>git commit -m “Deployment Commit”</p>
            <p>git push</p>
        </td>
    </tr>
</table>

<br>

<h3>In Heroku</h3>

<table>
    <tr>
        <th>#</th>
        <th>Steps</th>
        <th>Code</th>
    </tr>
    <tr>
        <td>14</td>
        <td>Deploy Content manually through heroku/</td>
        <td>E.g Github as deployment method, on main branch</td>
    </tr>
</table>

<br>

<p>Before the final Deployement: Remove the "DISABLE_COLLECTSTATIC" from Heroku Config vars, and Change Debug to "False" in settings.py</p>

</details>

<br>

In order to make a local copy of this repository, you can type the following into your IDE terminal:
* `git clone hhttps://github.com/MerveKucukzoroglu/reading-tracker.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/MerveKucukzoroglu/reading-tracker)


# Credits
During the process of project development, there have been various sources that gave me idea how to do a particular feature or fix a bug. The following are the sources that I got knowledge from:
* [Stack Overflow](https://stackoverflow.com/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/#)
* [Django Project Documentation](https://www.djangoproject.com/)
* [Code Instiute](https://codeinstitute.net/se/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+SWE+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14660337051&hsa_grp=134087657984&hsa_ad=581817633089&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjw0PWRBhDKARIsAPKHFGgmnuTJCpzeJBqKg9fy2p-7NlU8NY95XaXmoPzBpuDdIekQWqUKxocaAso5EALw_wcB) course materials and Django Blog Walkthrough Project.
* [Bootstrap Navbar](https://getbootstrap.com/docs/5.0/components/navbar/)
* [Bootstrap Modal](https://getbootstrap.com/docs/5.1/components/modal/#tooltips-and-popovers)
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [User registration email form and views by Corey Schafer](https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6) for future email verification purposes.
    * forms.py 
        ```python
        class UserRegisterForm(UserCreationForm):
        email = forms.EmailField()

        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
        ```
    * Views.py
        ```python
            def register(request):
                if request.method == 'POST':
                    form = UserRegisterForm(request.POST)
                    if form.is_valid():
                        form.save()
                        username = form.cleaned_data.get('username')
                        messages.success(request, f'Account created for {username}!')
                        return redirect('profile')
                    else:
                        form = UserRegisterForm()
                return render(request, 'account/signup.html', {'form': form})

        ```
* [Coolors](https://coolors.co/) color palette.

    ![Coolors](/documentation/coolors.png)

* [AmIResponsive](http://ami.responsivedesign.is/) for mockup of the site.


# Acknowledgements
I would like to acknowledge and present my thanks to Tim Nelson, my mentor from Code Insitute for his guidance and constant support. It wouldn't have been possible without the amazing community in Slack, Tutors of Code insitute Tutor supports, and my friends who constantly motivated and supported me. 