import os

from python_change_parser import export_html, parse_changes, read_text_file, reset_record_id

os.chdir(os.path.dirname(os.path.realpath(__file__)))


def parse_doc_dir(doc_dir):
    print(f'Processing directory {doc_dir}')
    reset_record_id()
    for subdir in ('library', 'reference'):
        for item in os.listdir(os.path.join(doc_dir, subdir)):
            file = subdir + '/' + item
            print(f'Parsing file {file}')
            yield from parse_changes(read_text_file(os.path.join(doc_dir, subdir, item)), file)


def process_doc(version):
    export_html(list(parse_doc_dir(f'data/python-{version}-docs-html')),
                f'output/python-{version}-changes.html',
                version)


if __name__ == '__main__':
    for version in ('3.8.1', '2.7.17'):
        process_doc(version)
