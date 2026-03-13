# Heron Blog Engine
Simple Python Blog Engine for minimalistic personal page/blog

> still in development, although no one will ever use it besides me lol

This is a simple blog engine created in python, although defacto it allows to create any webpage, not necessarily a blog, but more on that later.

All the articles/pages are built using markdown files, then they are injected into customizable jinja2 templates that end up as plain html files with all the neccessary static data.

It uses compiled tailwind and pygments extension with some small changes for styling. **No j*vascript :)**, however you can add it yourself.

Live example: https://czapla.xyz/

## Usage

### Prerequisites

You need to know markdown language and jinja2 templates.

### Configuration

Use pyproject.toml to change any links, names etc. You can reference its keys directly in the jinja2 templates.

There are 3 types of pages: main page, category page and detail page. Their default jinja2 templates are inside `templates/index.html` and `templates/category.html` and `templates/detail.html` respectively. You can change both of them. They share the same header, footbar and navbar which are also customizable.

First and last pages are obvious, the `category page` is a page that lists all articles/pages within that category.

### Writing posts/articles

You need to create a folder (perhaps in another repo) and put your markdown files there.

If you put them in a subfolder they will belong to a category with that subfolder's name.
That way you can easily segregate different types of articles on your main page. For example creating a section for blog and a section for diary or something.

There are two "special" categories - `about` and `contact`. Those will only have one page and have custom HTML code in the navbar. You need to create `about/about.md` and `contact/contact.md`.

For static data inside articles (images, gifs, videos etc) create a static folder inside the input folder or its subfolders and reference them relatively (`./static/blog1_image.png`)

### Getting articles into html

1) create input folder with articles written in markdown, as described above
2) run `python engine/heron.py --input-dir <your_input_dir_path> --output-dir <your_output_dir_path>`
3) Be happy with ready to use html in the specified output folder

### Publishing your blog for free

Put the outputted files into another repo (must be public) inside /docs folder.

Then you can go to that repo's settings on github and use `Github Pages` to release your blog for free.

## Future development

I am aware that this engine is super simple so in the future I might add new stuff.

Also, it is very specific (especially the HTML/CSS) for my case, so editing the HTML is probably preferable.