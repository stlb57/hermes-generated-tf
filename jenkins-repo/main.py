# In jenkins-repo/main.py
import json
import os
import sys # Import the 'sys' module to read from standard input
from jinja2 import Environment, FileSystemLoader, select_autoescape

jinja_env = Environment(loader=FileSystemLoader("templates"))

def build_template(node_data, name):
    template = jinja_env.get_template(f"{name}.tf.j2")
    return template.render(node_data)

if __name__ == "__main__":
    # This line reads the JSON data piped in from the Jenkins 'sh' command.
    request_data = json.load(sys.stdin)

    with open("main.tf", "w") as fd:
        provider_config = 'provider "aws" { region = "us-east-1" }\n\n'
        fd.write(provider_config)
        for node in request_data["nodes"]:
            tf_code = build_template(node, node["type"])
            fd.write(tf_code + "\n\n")
    
    print("✅ Successfully generated main.tf from Jenkins parameter!")
