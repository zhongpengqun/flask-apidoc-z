# flask-apidoc

Write API document when you coding, Test your API when you press last word immediately



### Installation

​    $sudo pip install flask_doc

### Useage

We suppose there's a Flask project in /var/www/app

#### 1. command line

    $cd /var/www/app
    $fkapidoc manager.py app

This will generate all docstring in view functions to a markdown string print on screen, or you can save it to a file

    $fkapidoc manager.py app > doc.md

If you don't need generate all view functions (return html not api), you can add an external parameter to set filters.

We suppose you there's a blueprint in project like below:

    api = Blueprint('api', __name__, template_folder='templates', url_prefix='/api')

It contains all API view functions, we'd like to only generate documentation in the blueprint.

    $fkapidoc manager.py app api. > doc.md

We can generate multi blueprint, just use "," to split.

    $fkapidoc manager.py app api.,xxx.,yyy. > doc.md


#### 2. Embedded in project

   first step: import:

    from flask_doc import Generator

   second step: init generator

    generator = Generator(app)

   or use filter

    generator = Generator(app, filters=["api."])

   put line after in the last file before start server

    generator.prepare()

   then, when you start server, open

    open: http://domain/api-doc

   It will show you a web page contains API specification, Toc Index and Test Fly client

   ![显示效果](http://ww3.sinaimg.cn/large/578b198bgw1fb7tz5of27j21kw0lfn0h.jpg)

   Click the paper plane will show you a form to invoke api, you can run it and see what happened immediately.

   ![显示效果](http://ww3.sinaimg.cn/large/578b198bgw1fb7u2y3vn5j21kw0jkdij.jpg)












