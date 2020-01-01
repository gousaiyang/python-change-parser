import json
import re

from bs4 import BeautifulSoup

record_id = 0


def read_text_file(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as file:
        return file.read()


def write_text_file(filename, content, encoding='utf-8'):
    with open(filename, 'w', encoding=encoding) as file:
        file.write(content)


def may_be_argument_change(description):
    description = description.lower()
    return 'parameter' in description or 'argument' in description


def parse_arguments(element):
    return ([str(s.string) for s in element.parent.find_all('em')] +
            [str(s.string) for s in element.parent.select('span[class="pre"]')])


def parse_changes(text, file):
    soup = BeautifulSoup(text, 'html.parser')
    for element in soup.find_all(class_='versionmodified'):
        # only find elements with class "versionmodified added" or "versionmodified changed"
        element_class = element['class']
        if 'deprecated' in element_class:
            continue
        if 'added' in element_class:
            type_ = 'added'
        elif 'changed' in element_class:
            type_ = 'changed'
        else:
            if 'deprecated' not in str(element.parent).lower():
                raise ValueError('found a "versionmodified" element which is none of added/changed/deprecated')
            continue

        description = element.parent.get_text()
        version = re.findall(r'in version (\d+(?:.\d+)+)', element.string, re.ASCII)[0]

        for parent in element.parents:
            parent_class = parent.get('class')
            if parent.name == 'dl':
                category = parent_class[0] if parent_class else 'unknown object'
                name = parent.find('dt').get('id')
                anchor = name
                if may_be_argument_change(description):
                    category = 'argument'
                    name = (name, parse_arguments(element))
                break
            if parent_class == ['section']:
                section = parent.get('id')
                anchor = section
                if section.startswith('module-'):
                    category = 'module'
                    name = section[7:]
                else:
                    category = 'unknown section'
                    name = section
                break
        else:
            raise ValueError('failed to extract information from parent nodes')

        global record_id
        record_id += 1

        yield {
            'id': record_id,
            'type': type_,
            'version': version,
            'category': category,
            'name': name,
            'file': file,
            'anchor': anchor,
            'description': description
        }


def reset_record_id():
    global record_id
    record_id = 0


def export_html(data, output_file, version):
    py_major_version = int(version.split('.')[0])
    if py_major_version not in (2, 3):
        raise ValueError('invalid Python version')
    template = read_text_file('template.html')
    js_data = {
        'changes': data,
        'py_major_version': py_major_version,
        'py_version': version
    }
    output = template.replace('var data = {"changes": [], "py_major_version": null, "py_version": null}; // To be generated.',
                              'var data = {};'.format(json.dumps(js_data, separators=(',', ':'))))
    write_text_file(output_file, output)
