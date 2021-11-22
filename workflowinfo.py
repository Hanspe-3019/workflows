'''
Dies ist ein kleines Modul, das eine Tabelle mit Informationen aus
den enthaltenen Workflows generiert und die <table>…</table> in README.md
ersetzt.
Ausführen mit
  python3 workflowinfo.py
'''
import zipfile
from pathlib import Path
import plistlib
from collections import Counter
from datetime import date

INTEND_4 = '&nbsp;' * 4
DOCFILE = './README.md'

def get_info(alfredworkflow):
    ''' alfredworkflow: zipped workflow directory
    extract info.plist and return as dict
    extract icon.png to ./doc/name.png
    '''
    with zipfile.ZipFile(alfredworkflow, 'r') as archive:

        with archive.open('info.plist') as plist:
            workflow_info = plistlib.load(plist)

        try:
            icon = archive.getinfo('icon.png')
            icon.filename = f"{workflow_info['name']}.png"
            archive.extract(icon, path='./doc')
        except KeyError:
            pass

    return workflow_info

def build_doc(info):
    ''' Get name, description, version and counts of objects
    '''
    its_obj_types = ( obj['type'] for obj in info['objects'] )
    types_counter = Counter(its_obj_types)
    type_infos = (
        f"{obj_type.removeprefix('alfred.workflow.')} : "
        f"{count}"
        for obj_type, count in types_counter.items()
        if obj_type != 'alfred.workflow.utility.debug'
    )
    name = info['name']
    description = info['description']
    docfile = Path(f'./doc/{name}.md')
    if docfile.exists():
        more = f'<br>{INTEND_4*3}<a href="{docfile.as_posix()}">Read more...</a>'
    else:
        more = ''

    return '\n'.join([
        '<tr>',
        f'<td><img src="./doc/{name}.png" width="128">',
        f"<td><strong>{name}</strong><br>{INTEND_4}{description}{more}",
        f"<td>{info['version']}",
        f"<td>{'<br>'.join(sorted(type_infos))}",
    ])

def ignore_caps(posixpath):
    ''' little helper to sort PosisPath ignoring capitalisation.
    '''
    return posixpath.as_posix().lower()

def main():
    ''' Read *.alfredworkflow files from current directory
    and replace <table> in DOCFILE with new <table>
    '''
    with open(DOCFILE, 'r') as docfile:
        olddoc = docfile.read()

    before_table = olddoc.split('<table>')[0]
    after_table = olddoc.split('/table>')[-1]

    with open(DOCFILE, 'w') as docfile:

        today = date.today().isoformat()
        docfile.write(before_table)
        docfile.write('<table>')
        docfile.write(f'<caption><small>Generated at {today}</small></caption>')
        docfile.write('<table><tr><th><th>Workflow<th>Version<th>contains')

        for workflow in sorted(
                Path('.').glob('*.alfredworkflow'),
                key=ignore_caps
        ):
            info = get_info(workflow)
            docfile.write(f'\n{build_doc(info)}')

        docfile.write('</table>')
        docfile.write(after_table)

if __name__ == '__main__':
    main()
