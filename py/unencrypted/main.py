def define_env(env):
    password_key = 'mot de passe'
    login_key = 'login'
    name_key = 'name'
    url_key = 'url'

    @env.macro
    def copy_login(key):
        value = env.variables[key][login_key]
        value_with_html_entities = value.encode('ascii', 'xmlcharrefreplace').decode("utf-8")
        HTML = """<a data-clipboard-text="%s" href="#">%s</a>"""
        return HTML % (value_with_html_entities, value_with_html_entities)

    @env.macro
    def copy_password(key):
        value = env.variables[key][password_key]
        value_with_html_entities = value.encode('ascii', 'xmlcharrefreplace').decode("utf-8")
        HTML = """<a data-clipboard-text="%s" href="#">mot de passe</a>"""
        return HTML % (value_with_html_entities)

    @env.macro
    def url_link(key):
        name = env.variables[key][name_key]
        url = env.variables[key][url_key]
        HTML = """<a href="%s" target="_blank">%s</a>"""
        return HTML % (url, name)