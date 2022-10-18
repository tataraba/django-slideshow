# A Perfectly Simple Django Slideshow App

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Notes](#notes)

## About <a name = "about"></a>

This is an app that does something. That "something" is a way to organize my revealjs slideshows and attach them to events where they are presented.

NOTE: Documentation is work in progress. I will update with better instructions.

## Getting Started <a name = "getting_started"></a>

To get started, clone a copy of this repo and get going!

### Prerequisites

You will need Python 3.10 and Django 4.1. You will also need:

-   gunicorn
-   jinja2
-   django-render-block
-   pydantic
-   pydantic-django
-   django-htmx
-   django-htmx-refresh


### Installing

If you use a package manager, you can install directly from the `pyproject.toml` file. I happen to use `pdm` as my package manager.

After you've cloned the repo, start a virtual environment and use your preferred package manager to install your dependencies. If you're using pdm, you can use:

```
pdm install
```

I've also created a requirements file in case you want to install from that:

```
python -m pip install -r requirements.txt
```

You'll want to run the usual Django commands to get started. (Makemigrations and migrate)

## Usage <a name = "usage"></a>

You will be able to upload html files that contain the slide data (per revealjs specifications) and add basic info (such as title and description.) You can also create events and attach the slideshow to the corresponding event.

## Notes <a name = "notes"></a>

This is very much a work in progress. Several features are missing and I need to add a lot more documentation.

Some of the things I want to add:
-   Updating/Deleting Slideshow and Event data
-   Allowing more than one slide per event
-   Ability to change "themes" for revealjs slideshows
-   Auto detect .html vs .md file
-   Data validation for several fields
    -   End date > Start date
    -   Support for online-only events
    -   More pizzaz