dev-start:
	python manage.py runserver --settings=config.settings.dev

dev-install:
	pip install -r requirements/dev.txt

dev-showmigrations:
	python manage.py showmigrations --settings=config.settings.dev

dev-makemigrations:
	python manage.py makemigrations --settings=config.settings.dev

dev-makemigrations-app:
	python manage.py makemigrations $(app) --settings=config.settings.dev

dev-migrate:
	python manage.py migrate  --settings=config.settings.dev

dev-migrate-app:
	python manage.py migrate $(app) --settings=config.settings.dev

dev-migrate2:
	python manage.py migrate $(app) $(m) --settings=config.settings.dev

dev-sqlmigrate:
	python manage.py sqlmigrate $(app) $(m) 

dev-shell:
	python manage.py shell --settings=config.settings.dev
    
dev-dbshell:
	python manage.py dbshell --settings=config.settings.dev

#dev-test:
#	python manage.py test $(route) --settings=config.settings.dev
#--verbosity=2

# Definiere den Basis-Pfad für Tests
APPS_PATH=apps

dev-test:
	python manage.py test apps --settings=config.settings.dev

dev-test-app:
	python manage.py test $(APPS_PATH).$(route) --settings=config.settings.dev 

dev-delete_users:
	python manage.py delete_users --settings=config.settings.dev

dev-create_users:
	python manage.py create_users --settings=config.settings.dev

dev-flush:
	python manage.py flush --settings=config.settings.dev

dev-coverage-report:
	coverage erase--settings=config.settings.dev
	#coverage run manage.py test apps --settings=config.settings.dev
	coverage run manage.py test apps config/test_middleware --settings=config.settings.dev
	coverage report -m

dev-coverage-html:
	coverage erase
	#coverage run manage.py test apps --settings=config.settings.dev
	coverage run manage.py test apps config.tests.test_middleware --settings=config.settings.dev
	coverage html

dev-coverage-file:
	coverage erase
	coverage run manage.py test apps.$(app).tests.test_$(file) --settings=config.settings.dev
	coverage report -m --include=apps/$(app)/$(file).py

dev-coverage-file1:
	coverage erase
	coverage run manage.py test config.test_middleware --settings=config.settings.dev
	coverage report -m