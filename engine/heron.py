"""
1) header and footbar
4) Formatting etc
"""

import argparse

from jinja_ import JinjaManager
from markdown_ import MarkdownManager
from static import StaticManager


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    input_path, output_path = args.input_dir, args.output_dir

    html_with_context = MarkdownManager(input_path).get_html_with_context_list()
    JinjaManager(output_path, html_with_context).render()
    StaticManager(input_path, output_path).copy_static()


if __name__ == "__main__":
    main()
