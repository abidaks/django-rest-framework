# Python Django rest Framework Test Project

## Installation

```
> git clone https://github.com/abidaks/django-rest-framework
> cd django-rest-framework
```


## Install dependencies

run below command to install dependencies
```
# Create a virtual environment to isolate our package dependencies locally
> python3 -m venv env
> source env/bin/activate  # On Windows use `env\Scripts\activate`

#install requirements
> pip install -r requirements.txt

#run migrations
> python manage.py migrate

#add super user
> python manage.py createsuperuser --email admin@example.com --username admin
```

## Running tests

```
> python manage.py test insurance.apps.customer.tests
> python manage.py test insurance.apps.policy.tests
```

## Running project

```
> python manage.py runserver
```

## API links

/api/v1/create_customer
/api/v1/create_policy

Other framework API's
/users/
/token/login/ (Token Based Authentication)
/token/logout/ (Token Based Authentication)

## License

* [GNU General Public License](http://www.gnu.org/licenses/)
