import os.path
from dataclasses import dataclass
from typing import List

from jinja2 import Template

from config import HeronConfigLoader, HeronConfigFields
from markdown_ import HTMLWithContext


@dataclass
class JinjaManager:
    output_path: str
    html_with_context_list: List[HTMLWithContext]

    @staticmethod
    def get_html_template():
        with open(HeronConfigLoader.get_config(HeronConfigFields.blog_page_template)) as f:
            return Template(f.read())

    def render(self):
        template = JinjaManager.get_html_template()

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        for html_obj in self.html_with_context_list:
            file_content = template.render(content=html_obj.html)

            with open(self.output_path + "/" + html_obj.filename, "w", encoding="utf-8") as f:
                f.write(file_content)