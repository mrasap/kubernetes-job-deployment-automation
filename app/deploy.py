from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['yaml'])
)

template = env.get_template('job.yaml')

if __name__ == "__main__":
    print(template.render(item="two"))
