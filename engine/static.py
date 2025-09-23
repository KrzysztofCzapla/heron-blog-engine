import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass
class StaticManager:
    input_path: str
    output_path: str

    def copy_static(self):
        # copy static from input folder
        src_static = Path(self.input_path) / "static"
        dest_static = Path(self.output_path) / "static"
        if src_static.exists():
            shutil.copytree(src_static, dest_static, dirs_exist_ok=True)

        # copy static from templates folder
        src_templates_static = Path("templates") / "static"
        if src_templates_static.exists():
            shutil.copytree(src_templates_static, dest_static, dirs_exist_ok=True)
