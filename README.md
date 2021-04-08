**please fork and make pull requests to learn from eachother.**

# Intro

There is nothing better and simpller to add to your resume then twetter clone. But in this app I compine more things which is notions.so clone. I really hate the menu bar where you have to go the the menu bar and selecte insert then select image, but if you can just say `/image` and hit anter that would be much easer, and I beilive that this will be the future of docs even goodl docs may switch to this new way of interacting with docs.

# please visit the [projects section](https://github.com/aliscie/notion-so-clone-api/projects/1)

# please visit the [fotonend repo](https://github.com/aliscie/Notion-so-clone)

---

## Waht is `graphene-django`(django graphql api)

- The app is a graphql api based on [this tutorial](https://www.youtube.com/watch?v=kP7wQoFXUSc&list=PLOLrQ9Pn6caxz00JcLeOR-Rtq0Yi01oBH)
- If you are femular with `django-rest-api` frame work then it is easy to under stand `djgango-graphql`
- django graphql is an is api frame work where you can query data instead of `GET`
  - query in graphql api means to spesfy the field that you want to get instead of requesting all the avaliable fields which may save your internt speed.

## Get started to use:

0. go to the master branch
1. \$`git clone https://github.com/aliscie/autodox-backend.git`
2. \$`cd autodox-backend-master`
3. \$ `virtualenv env --python=python3`
4. \$ `source env/binactivate`
5. \$`pip install -r requirements.txt`
6. make sure to have `PyJWT==1.7.0` in `requirements.txt`,
7. in case you installed `PyJWT==2.0.0` or any other versions not equal to `1.7.0` please
8. you should `pip uninstall PyJWT` then `pip install PyJWT==1.7.0`
9. Somtimes you need to delete the `migrations` files and the `db.sqlite3` file so please be aware of that in case you got some errors like `field not found`...

- if you don't know how to delete migrations files
- go to a folder called `migrations`
- then inside it delete all the files expet `__init__.py` file which is important for django to recognize which fold is which.

8. \$`python3 manage.py createsuperuser`

- do add username email and password
- you should know this by your self.

9. \$ `python3 manage.py makemigrations`
10. \$ `python3 manage.py migrate`

## My repo strecture

1. `backend/settings.py`

- E

2. `api/models.py`

- it is probably easy for you to understand this
- But you may need to understand `class Component(models.Model):`
  - this is a reusable class
  - I used it in `class Style(Component):` and in this case its create the same fields strecture with a new model called `Style`
  - Reusable component enable you to create reusable feids strecture, but that does not mean the content of the fields wil be the same every time you use the reusable class model. It is share only the strecture not the content.
  - there are tow fields `who_can_see` and `who_can_edite` in each component
    - Here I using the same fiels every time I create a new model that may need these two, and repetitiveness is a problem
    - I do that because of this `kwarg` `related_name='who_can_see_style', in which if I created in`class Component(models.Model):`it will create this field with the same`related_name`each time I use it, which confuse django and somtimes id don't show the field of`who_can_see`
    - also I don't understand what is related_name do, and if I can just get rid of it.

3. `api/pipline.py`

- to understant the folloing code in `settings.py`

```

SOCIAL_AUTH_PIPELINE = (

  'api.pipline.save_profile' #<= this line of code talls where SOCIAL_AUTH app where is our function that should be activated every time the user sing in or sing up.
)
```

- then go back to thi `api/pipline.py`
- the `save_profile` function try to add the image url for the image field when the user sing up, or it is update it when the user change it and login.
- Hover, I need this function because by defualt the social auth app can detecte the first name, last name and email to add them to my `ExtendUser` model but it can't do that for the other fields so I need to do it by my self.
- So, `social_django` responsable on handling social singin/up.

4. `api/views.py`
5. `api/schema.py`
6. `api/tests.py`

### Comments

1. `# TODO`

- you will find `# TODO` before each comment that expline there is some work and code need to be dont
- usally I need this when I am stuck in somthing that I don't know how to do.
- Also I am using an extention called TODOs in my VScode.

2. Comented code

- sometimes I add some code and imports and comment them just in case I need them in the future
- other time I do that in case I finde a code that I cen comment it and the app still work, but I don't konw if i should delete it or if I will need it in the future.

### Branches

1. `mater` branch only for code
2. `main` branch only for `readme` fiel
3. in the future I man create branches that has names start with `experment` for expermenting with my code

- for example I may create a branch called `experment-personal-profiel` in order to try to make personal profiles in few ways and after I finsih I will copy the code and add it to my code in my `master` branch and then I will delete `experment-personal-profiel` branch.

## The purpose of this app

This is a graphql api used as a backend for the app [notion-so clone](https://github.com/aliscie/Notion-so-clone) which is a clone app for [notion so](https://www.notion.so/).

## [Demo](https://autodox-backend.herokuapp.com/graphql)

- open
- TODO in the delpied app I have a problem, in which the data base is deleted automatcly each 2 or 3 hourse., Maybe I have problmes in my `settings.py`

## Database

- I am still using sqlite3, and I will switch to `postgresql`
- I will use `aws` database as will for static files
- I will also use local files to enable user to save their fiels on their computers
- I also want to know if i can use google drive and link it to django in order to sive the data files in it.
