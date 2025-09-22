import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass
class StaticManager:
    input_path: str
    output_path: str

    def copy_static(self):
        if Path(self.input_path + "/static").exists():
            shutil.copy(Path(self.input_path) / "static", Path(self.output_path) / "static")