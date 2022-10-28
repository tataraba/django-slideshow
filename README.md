# A Perfectly Simple Django Slideshow App

![GitHub repo size](https://img.shields.io/github/repo-size/tataraba/django-slideshow?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues/tataraba/django-slideshow?style=flat-square) ![GitHub](https://img.shields.io/github/license/tataraba/django-slideshow?style=flat-square) [![Twitter URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2FPythonByNight)](https://twitter.com/PythonByNight)
## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Notes](#notes)
- [Contributions?](#contributing)

## :high_brightness: About <a name = "about"></a>

This is an app that does something. That "something" is a way to organize revealjs slideshows and attach them to events where they are presented.

_NOTE: Documentation is work in progress._

## 🏁  Getting Started <a name = "getting_started"></a>

To get started, clone a copy of this repo and get going!

Here is one way to clone the project. Create a local directory and navigate to it in your terminal. Then run this command.

```
git clone https://github.com/tataraba/django-slideshow.git
```

### Requirements

Make sure you have Python 3.10 (or 3.11! ✨) installed (somewhere) in your system.

Here are the libraries we will be using (instructions below on installing them)

-   Django
-   gunicorn
-   jinja2
-   django-render-block
-   pydantic
-   pydantic-django
-   django-htmx
-   django-htmx-refresh

### 🖥️ Installing

If you use a package manager, you can install directly from the `pyproject.toml` file, which makes this process a little more straight forward. I happen to use `pdm` as my package manager, but it's not required.

If you don't use `pdm`, go about it the traditional way, like so (these instructions are for Windows PowerShell users. Use the equivalent commands if on another OS/platform):

```py
# First, Create a virtual environment
python -m venv .venv

# Activate said environment (this is the command in Windows PowerShell)
.\.venv\Scripts\activate

# Once your environment is activate, install dependencies
python -m pip install -r requirements.txt
```

Optional: If you are using `pdm`, all you would have to do instead is type:
```py
# Install dependencies
pdm install

# Activate virtual environment (created by pdm with above command)
.\.venv\Scripts\activate
```

At this point, you should have a working Django app! :balloon:

If you're not familiar with Django, you will likely need to get acquainted with some of the Django `manage.py` commands. However, if you just want to start poking around, run these two commands:

```py
# The `migrate` command turns the Django models into database tables
python manage.py migrate

# The `runserver` command runs your application locally
python manage.py runserver
```

And that's it!

You should be able to navigate to http://127.0.0.1:8000 and see the landing page for a **Perfectly Simple Django Slidshew App** (_slidjo_ for short).

## :hammer: Usage <a name = "usage"></a>

The _slidjo_ app allows you to create slideshows using [reveal.js](https://revealjs.com).

All you need to do is create an `html` file containing only the appropriate revealjs markup, and then upload that file using the "Create Slideshow" feature.

You'll be able to add a title and description for your slideshow, and later, add it to "Events" that you can also create within the app.

More details on this will be coming later, but as a quick primer, your `html` file might look like this:

```html
<!-- sample.html -->
<section>My First Slide</section>
<section>My Second Slide</section>
<section>
    <section>Let's see some vertical action</section>
    <section>Look at me down here</section>
</section>
```

Additionally, if you'd prefer to write your slides in markdown, your file can look like this:

```html
<!-- sample_with_markdown.html -->
<section data-markdown>
    <textarea data-template>

        # Heading Example

        ---

        ### New Slide

        ---

        Reveal reads the "---" as a new slide

    </textarea>
</section>
```
> Note that in neither case, you have to add `<head>` or `<body>` tags or anything like that. This is intended. Those pieces are added by templates automatically.

Obviously, the slides can get much fancier than these examples, but for more on that, you'll have to look through the [revealjs documentation](https://revealjs.com/markup/).

## :notes: Notes <a name = "notes"></a>

This is very much a work in progress. Several features are missing and I need to add a lot more documentation.

Some of the things I want to add:
-   Updating/Deleting Slideshow and Event data
-   Ability to change "themes" for revealjs slideshows (selecting alternate css styles)
-   Auto detect .html vs .md file (instead of using `<textarea>`)
-   Data validation for several fields
    -   End date > Start date
    -   Support for online-only events
    -   Ensuring the "featured" field working as expected
-   Ability to add multiple slideshows to one event (many to many relationship instead of one to many)
-   Add tests!
-   Documentation on how to use tailwind to further optimize the look and feel

## 💗 Contributions? <a name = "contributing"></a>

I am considering opening up this project for contributions. I have no idea how to manage a project, though, so for now, 🤷‍♂️...

But, if you watch this space, I may get to it sooner rather than later.