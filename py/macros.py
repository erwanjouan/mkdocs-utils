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
        HTML = (
            f"""<a href=\"#\" onclick=\"openPage(event, '{category}', '{key}','url')\">{key}</a>
             ( <a onclick="copySecret(\'{category}\', \'{key}\', \'login\', this)">login</a>
             : <a onclick="copySecret(\'{category}\', \'{key}\', \'password\', this)">password</a> )
             """
        )
        return HTML.format(category= input_category, key=input_key)
