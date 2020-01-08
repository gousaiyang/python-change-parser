import ast
import collections
import re


def read_text_file(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as file:
        return file.read()


def parse_version_requirement(text, expect_major):
    version = text.split('.')
    if not all(re.fullmatch(r'[0-9]+', x) for x in version):
        raise ValueError(f'invalid version {text!r}')
    if len(version) not in (2, 3):
        raise ValueError(f'invalid version {text!r}, should be major.minor or major.minor.micro')
    major = int(version[0])
    minor = int(version[1])
    micro = int(version[2]) if len(version) > 2 else None
    if major not in (1, 2, 3):
        raise ValueError(f'invalid major version {major}')
    if major == 2 and (minor > 7 or minor < 0):
        raise ValueError(f'minor version {minor} out of range for major version 2')
    if micro is not None and (micro >= 20 or micro < 0):
        raise ValueError(f'micro version {micro} out of range')
    if major == 1:
        major = 2
        minor = 0
    if major != expect_major:
        raise ValueError(f'major version {major} does not match expected major version {expect_major}')
    return (major, minor)


def is_removed_in_py3(name):
    name_parts = name.split('.')
    return any(name_parts[:len(x)] == x for x in removed_in_py3_list)


def validate_identifier_name(name):
    parts = name.split('.')
    if not all(re.fullmatch('[_A-Za-z][_0-9A-Za-z]*', x) for x in parts):
        raise ValueError('invalid identifier name')


py3_rules = read_text_file('py3_rules.txt').rstrip('\n').split('\n\n')[1:]
py2_rules = read_text_file('py2_rules.txt').rstrip('\n').split('\n\n')[1:]
removed_in_py3_list = [x.split('.') for x in read_text_file('removed_in_py3.txt').splitlines() if not x.startswith('#')]

modules_rules = collections.defaultdict(lambda: [None, None])
classes_rules = collections.defaultdict(lambda: [None, None])
exceptions_rules = collections.defaultdict(lambda: [None, None])
functions_rules = collections.defaultdict(lambda: [None, None])
variables_and_constants_rules = collections.defaultdict(lambda: [None, None])
decorators_rules = collections.defaultdict(lambda: [None, None])
kwargs_rules = collections.defaultdict(lambda: [None, None])

for ruleset, major_version in ((py2_rules, 2), (py3_rules, 3)):
    for part in ruleset:
        rules = part.split('\n')
        rule_type = rules[0]
        if not rule_type.endswith(':'):
            raise ValueError('rule type line should end with ":"')
        rule_type = rule_type[:-1]
        if rule_type == 'misc':  # skip misc part
            continue
        elif rule_type == 'module':
            target = 'modules_rules'
        elif rule_type in ('data', 'attribute'):
            target = 'variables_and_constants_rules'
        elif rule_type == 'class':
            target = 'classes_rules'
        elif rule_type == 'exception':
            target = 'exceptions_rules'
        elif rule_type in ('function', 'method'):
            target = 'functions_rules'
        elif rule_type == 'decorator':
            target = 'decorators_rules'
        elif rule_type == 'argument':
            target = 'kwargs_rules'
        else:
            raise ValueError(f'unknown rule type {rule_type!r}')
        rules = rules[1:]
        for rule in rules:
            rule_version, rule_content = rule.split(' ', 1)
            rule_version = parse_version_requirement(rule_version, major_version)
            if target == 'kwargs_rules':
                func, kwargs = ast.literal_eval(rule_content)
                validate_identifier_name(func)
                for kwarg in kwargs:
                    validate_identifier_name(kwarg)
                    kwargs_rules[(func, kwarg)][major_version - 2] = rule_version
            else:
                validate_identifier_name(rule_content)
                globals()[target][rule_content][major_version - 2] = rule_version


modules_rules = sorted(modules_rules.items())
classes_rules = sorted(classes_rules.items())
exceptions_rules = sorted(exceptions_rules.items())
functions_rules = sorted(functions_rules.items())
variables_and_constants_rules = sorted(variables_and_constants_rules.items())
decorators_rules = sorted(decorators_rules.items())
kwargs_rules = sorted(kwargs_rules.items())

with open('vermin_rules_generated.py', 'w', encoding='utf-8') as rulefile:
    for rule_type in ('modules_rules', 'classes_rules', 'exceptions_rules', 'functions_rules', 'variables_and_constants_rules', 'decorators_rules'):
        rulefile.write(f'{rule_type} = {{\n')
        for name, versions in globals()[rule_type]:
            if not any(versions):
                raise ValueError('invalid versions tuple')
            if versions[1] is None and not is_removed_in_py3(name):
                versions[1] = (3, 0)
            rulefile.write(f'    "{name}": {tuple(versions)!r},\n')
        rulefile.write('}\n\n')
    rulefile.write('kwargs_rules = {\n')
    for name, versions in kwargs_rules:
        if not any(versions):
            raise ValueError('invalid versions tuple')
        if versions[1] is None and not is_removed_in_py3(name[0]):
            versions[1] = (3, 0)
        rulefile.write(f'    ("{name[0]}", "{name[1]}"): {tuple(versions)!r},\n')
    rulefile.write('}\n')
