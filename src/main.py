import os
import yaml
from jinja2 import Environment, FileSystemLoader


class YamlParser:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def parse_yaml(self):
        with open(self.yaml_file, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        return data

    def generate_html(self, template_file, output_file):
        data = self.parse_yaml()
        env = Environment(loader=FileSystemLoader(os.path.join("src", "jinja")))
        template = env.get_template(template_file)

        # Read styles from CSS file
        with open(os.path.join("src", "jinja", "styles.css"), "r") as file:
            styles = file.read()

        html_content = template.render(data=data, styles=styles)

        output_path = os.path.join(output_file)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(html_content)


if __name__ == "__main__":
    yaml_parser = YamlParser(os.path.join("resume.yaml"))

    # Generate HTML
    yaml_parser.generate_html("template.html", "index.html")
