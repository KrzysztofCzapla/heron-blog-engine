import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass
class StaticManager:
    input_path: str
    output_path: str

    def copy_static(self):
        # copy static from input folder
        src_static = Path(self.input_path)
        dest_static = Path(self.output_path)

        # this looks for all static folders and copies them to the output folder
        # this way we can have relative paths of static files for each subfolder
        static_dirs = [
            p for p in src_static.rglob("*") if p.is_dir() and p.name == "static"
        ]
        for static_dir in static_dirs:
            if static_dir.is_dir():
                relative_path = static_dir.relative_to(src_static)
                dest_dir = dest_static / relative_path
                shutil.copytree(static_dir, dest_dir, dirs_exist_ok=True)

        # copy static from templates folder
        src_templates_static = Path(__file__).parent / Path("templates") / "static"
        if src_templates_static.exists():
            shutil.copytree(
                src_templates_static, dest_static / "static", dirs_exist_ok=True
            )
