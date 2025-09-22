from dataclasses import dataclass
from pathlib import Path
from typing import List

from markdown import Markdown

MD: Markdown = Markdown(extensions=["tables", "fenced_code", "codehilite", "meta", "footnotes"])

@dataclass
class HTMLWithContext:
    html: str
    filename: str


@dataclass
class MarkdownManager:
    input_path: str

    def get_html_with_context(self) -> List[HTMLWithContext]:
        return [HTMLWithContext(MarkdownManager.render_md_to_html(filename), self.get_new_filename(filename)) for filename in self.gather_md_files()]

    def get_new_filename(self, filename: Path) -> str:
        return filename.with_suffix(".html").name

    @staticmethod
    def render_md_to_html(filename: Path):
        return MD.reset().convert(open(filename).read())

    def gather_md_files(self):
        path = Path(self.input_path)
        return list(path.rglob("*.md"))

    @staticmethod
    def validate_md_file(md_file: Path):
        return md_file