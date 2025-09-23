# Heron Blog Engine
Simple Python Blog Engine for minimalistic personal page/blog

> still in development, also this README is shit lol

This is a simple blog engine created in python.
It allows to create different categories of articles so you are not bind to just a blog.

### Purpose

This engine is easy to use and customizable for creating simple, minimalistic websites using markdown and jinja2 that are outputted into html files ready for live site.

### Usage

for simpliest usage:
1) create input folder with articles written in markdown.
2) run `python heron.py --input-dir <your_input_dir_path> --output-dir <your_output_dir_path>`
3) Be happy with ready to use html in the specified output folder

You can also use subfolders to create categories of pages.

For example, if, inside your input folder, you create a `blog` subfolder and put markdown files there - then you can access them in jinja2 tempalte using `{% for article in blog %}`

Further and better instructions for usage will be given later, too tired for that now lol