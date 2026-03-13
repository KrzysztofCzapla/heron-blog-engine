from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import List

from config import HeronConfigFields, HeronConfigLoader
from jinja2 import Environment, FileSystemLoader
from markdown_ import HTMLWithContext


@dataclass
class JinjaManager:
    output_path: str
    html_with_context_list: List[HTMLWithContext]

    def render(self):
        self._render_detail_pages()
        self._render_category_pages()
        self._render_main_page()

    @staticmethod
    def _get_html_template(template: str):
        template_name = HeronConfigLoader.get_config(template)
        templates_dir = Path(__file__).parent / Path(template_name).parent
        env = Environment(loader=FileSystemLoader(str(templates_dir)))
        return env.get_template(Path(template_name).name)

    def _generate_file(self, file_content: str, filename: str):
        out_file = Path(self.output_path) / filename
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(file_content, encoding="utf-8")

    def _render_main_page(self):
        template = JinjaManager._get_html_template(HeronConfigFields.main_page_template)

        category_to_pages = defaultdict(list)
        for page in self.html_with_context_list:
            category_to_pages[page.category].append(page)

        for key, value in category_to_pages.items():
            value.sort(key=lambda page: page.metadata.get("date", "1990-01-01"), reverse=True)

        file_content = template.render(
            **category_to_pages, **HeronConfigLoader.get_config()
        )
        self._generate_file(file_content, "index.html")

    def _render_detail_pages(self):
        template = JinjaManager._get_html_template(HeronConfigFields.blog_page_template)

        for html_obj in self.html_with_context_list:
            file_content = template.render(
                detail=html_obj, **HeronConfigLoader.get_config()
            )
            self._generate_file(file_content, html_obj.file_path)

    def _render_category_pages(self):
        template = JinjaManager._get_html_template(HeronConfigFields.category_page_template)

        category_to_pages = defaultdict(list)
        for page in self.html_with_context_list:
            category_to_pages[page.category].append(page)

        for key, value in category_to_pages.items():
            value.sort(key=lambda page: page.metadata.get("date", "1990-01-01"), reverse=True)
            file_content = template.render(
                category=key, pages=value, **HeronConfigLoader.get_config()
            )
            self._generate_file(file_content, f"{key}.html")
