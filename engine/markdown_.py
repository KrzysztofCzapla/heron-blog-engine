from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from markdown import Markdown

MD: Markdown = Markdown(
    extensions=["tables", "fenced_code", "codehilite", "meta", "footnotes"]
)


@dataclass
class PageMetadata:
    title: str = "tile"
    description: str = "description"
    date: str = "date"


@dataclass
class HTMLWithContext:
    html: str
    file_path: str  # full relative path from input folder, used to inject to output folder; contains .html
    category: str  # i.e. "blog"; can be used from main page's jinja to have different categories of subpages, i.e.: {{ blog.article1 }}
    metadata: dict
    url: Optional[str] = None

    def __post_init__(self):
        self.url = self.file_path


@dataclass
class MarkdownManager:
    input_path: str

    def get_html_with_context_list(self) -> List[HTMLWithContext]:
        return [
            self.get_single_html_with_context(filename)
            for filename in self.gather_md_files()
        ]

    def get_single_html_with_context(self, filename: Path) -> HTMLWithContext:
        html = MD.reset().convert(open(filename).read())
        metadata = {k: "\n".join(v) for k, v in MD.Meta.items()}
        file_path = filename.relative_to(self.input_path).with_suffix(".html")
        category = file_path.parts[0] if len(file_path.parts) > 1 else "unspecified"

        return HTMLWithContext(
            html=html,
            file_path=str(file_path),
            category=category,
            metadata=metadata,
        )

    def get_new_filename(self, filename: Path) -> str:
        rel = filename.relative_to(self.input_path)
        return str(rel.with_suffix(".html"))

    def gather_md_files(self):
        path = Path(self.input_path)
        return list(path.rglob("*.md"))
