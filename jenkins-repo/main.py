#help from - https://softwaredefined.pl/?templating-terraform-using-python-and-jinja2
import json
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
import git
import shutil

jinja_env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

def build_template(node_data, name):
    template = jinja_env.get_template(f"{name}.tf.j2")
    # This line ensures the template gets the full node object
    return template.render(node_data)

if __name__ == "__main__":
    with open("data.json", "r") as file:
        request_data = json.load(file)

    with open("main.tf", "w") as fd:
        # This block adds the required AWS provider configuration
        provider_config = """
provider "aws" {
  region = "us-east-1"
}

"""
        fd.write(provider_config)

        # This part of your code remains the same
        for node in request_data["nodes"]:
            name = node["type"]
            tf_code = build_template(node, name)
            fd.write(tf_code)
            fd.write("\n\n")
    
    print("✅ Successfully generated main.tf!")
