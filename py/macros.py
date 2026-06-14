# This is the hook for defining variables, macros and filters
import os
from pathlib import Path


def define_env(env):

    @env.macro
    def local_folder(page_url, rootdir):
        page_path = os.path.join('docs', page_url)
        rel_parent_path = Path(page_path).parent
        HTML = '<ul>\n'
        target_path = os.path.join(rel_parent_path, rootdir)
        for subdir, dirs, files in os.walk(target_path, topdown=False):
            for file in sorted(files):
                file_path = '../'+ rootdir + '/' + file
                HTML += '\t<li>\n'
                HTML += '\t<a href="{}" target="_blank">{}</a>\n'.format(file_path,file)
                HTML += '\t</li>\n'
        HTML += '</ul>\n'
        return HTML

    @env.macro
    def copy_url_login_mdp(input_category, input_key):
        return '''<a href=\"#\" onclick=\"openPage(event, \'{input_category}\', \'{input_key}\',\'url\')\">{input_key}</a>
             ( <a onclick="copySecret(\'{input_category}\', \'{input_key}\', \'login\', this)">login</a>
             : <a onclick="copySecret(\'{input_category}\', \'{input_key}\', \'password\', this)">password</a> )
             '''.format(input_category=input_category, input_key=input_key)

    @env.macro
    def secret_field(input_category, input_key, input_property='password'):
        uid = '{}-{}-{}'.format(
            input_category.replace(' ', '_'),
            input_key.replace(' ', '_'),
            input_property.replace(' ', '_'),
        )
        js = (
            "getAndCopySecret('{cat}', '{key}', '{prop}')"
            ".then(v => {{"
            "document.getElementById('secret-label-{uid}').textContent = v;"
            "document.getElementById('secret-btn-{uid}').hidden = true;"
            "}})"
            ".catch(() => {{"
            "document.getElementById('secret-btn-{uid}').classList.add('md-button--secondary');"
            "}})"
        ).format(cat=input_category, key=input_key, prop=input_property, uid=uid)
        icon = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24"'
            ' fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>'
            '<circle cx="12" cy="12" r="3"/>'
            '</svg>'
        )
        return (
            '<span id="secret-label-{uid}"></span>'
            ' <button class="md-button" id="secret-btn-{uid}" onclick="{js}"><p>{icon}</p></button>'
        ).format(uid=uid, js=js, icon=icon)