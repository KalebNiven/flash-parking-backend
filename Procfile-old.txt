heroku buildpacks:clear
heroku buildpacks:add --index heroku/python
web: python app.py
heroku ps:scale web=1