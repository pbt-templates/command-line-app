organization: python
name: {{cookiecutter.app_name}}
version: {{cookiecutter.version}}
description: a simple command line app
url: https://github.com/{{cookiecutter.author}}/{{cookiecutter.app_name}}

license:
    name: {{cookiecutter.license}}
    url: http://url-to/{{cookiecutter.license}}

authors:
    - {{cookiecutter.author}} <{{cookiecutter.author_mail}}>

dependencies:

entry_point: ["{{cookiecutter.app_name}}", "main"]

