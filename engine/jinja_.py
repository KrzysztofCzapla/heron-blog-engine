from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import List

from config import HeronConfigFields, HeronConfigLoader
from jinja2 import Environment, FileSystemLoader, Template
from markdown_ import HTMLWithContext


@dataclass
class JinjaManager:
    output_path: str
    html_with_context_list: List[HTMLWithContext]

    @staticmethod
    def get_html_template(template: str = HeronConfigFields.blog_page_template):
        template_name = HeronConfigLoader.get_config(template)
        templates_dir = Path(__file__).parent / Path(template_name).parent
        env = Environment(loader=FileSystemLoader(str(templates_dir)))
        return env.get_template(Path(template_name).name)

    def generate_file(self, file_content: str, filename: str):
        out_file = Path(self.output_path) / filename
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(file_content, encoding="utf-8")

    def render(self):
        template = JinjaManager.get_html_template()

        for html_obj in self.html_with_context_list:
            file_content = template.render(
                content=html_obj.html, **HeronConfigLoader.get_config()
            )
            self.generate_file(file_content, html_obj.file_path)

        self.render_main_page()

    def render_main_page(self):
        template = JinjaManager.get_html_template(HeronConfigFields.main_page_template)

        category_to_pages = defaultdict(list)
        for page in self.html_with_context_list:
            category_to_pages[page.category].append(page)

        for key, value in category_to_pages.items():
            value.sort(key=lambda page: page.metadata.get("date", "1990-01-01"), reverse=True)

        file_content = template.render(
            **category_to_pages, **HeronConfigLoader.get_config()
        )
        self.generate_file(file_content, "index.html")
