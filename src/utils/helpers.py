from src import config


def render_message(template_name, *args, **kwargs):
    template = config.jinja2_env.get_template(template_name)
    return template.render(*args, **kwargs)
