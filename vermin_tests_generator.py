import ast

module_test_template = '''\
def test_{test_name}(self):
{indentation}self.assertOnlyIn({version}, self.detect("import {name}"))
'''

class_test_template = '''\
def test_{item}_of_{test_module}(self):
{indentation}self.assertOnlyIn({version}, self.detect("from {module} import {item}"))
'''

function_test_template = '''\
def test_{item}_from_{test_module}(self):
{indentation}self.assertOnlyIn({version}, self.detect("import {module}\\n{module}.{item}()"))
'''

method_test_template = '''\
def test_{method}_from_{test_module}_{item}(self):
{indentation}self.assertOnlyIn({version},
{indentation}                  self.detect("from {module} import {item}\\n"
{indentation}                              "{item}().{method}()"))
'''

data_test_template = class_test_template

attribute_test_template = '''\
def test_{attribute}_from_{test_module}_{item}(self):
{indentation}self.assertOnlyIn({version},
{indentation}                  self.detect("from {module} import {item}\\n"
{indentation}                              "{item}().{attribute}"))
'''

function_kwarg_test_template = '''\
def test_{kwarg}_of_{item}_from_{test_module}(self):
{indentation}self.assertOnlyIn({version},
{indentation}                  self.detect("from {module} import {item}\\n"
{indentation}                              "{item}({kwarg}=None)"))
'''

method_kwarg_test_template = '''\
def test_{kwarg}_of_{method}_from_{test_module}_{item}(self):
{indentation}self.assertOnlyIn({version},
{indentation}                  self.detect("from {module} import {item}\\n"
{indentation}                              "x = {item}()\\n"
{indentation}                              "x.{method}({kwarg}=None)"))
'''

all_rule_types = [x[:-14] for x in globals().keys() if x.endswith('_test_template')]

DEFAULT_INDENTATION = 2


def parse_rule(rule):
    rule = rule.strip().rstrip(',')
    name, version = rule.split(':')
    return ast.literal_eval(name), eval(version, {'bp': lambda name: False})  # eval is evil, but just do it


def simplify_version(version):
    version = tuple(filter(bool, version))
    if not version:
        raise ValueError('version cannot be (None, None)')
    return version[0] if len(version) == 1 else version


def gen_module_test(rule, indentation=DEFAULT_INDENTATION):
    name, version = parse_rule(rule)
    return module_test_template.format(test_name=name.replace('.', '_'),
                                       indentation=' ' * indentation,
                                       version=simplify_version(version),
                                       name=name)


def gen_class_test(rule, indentation=DEFAULT_INDENTATION):
    name, version = parse_rule(rule)
    module, item = name.rsplit('.', 1)
    return class_test_template.format(item=item,
                                      test_module=module.replace('.', '_'),
                                      indentation=' ' * indentation,
                                      version=simplify_version(version),
                                      module=module)


def gen_function_test(rule, indentation=DEFAULT_INDENTATION):
    name, version = parse_rule(rule)
    module, item = name.rsplit('.', 1)
    return function_test_template.format(item=item,
                                         test_module=module.replace('.', '_'),
                                         indentation=' ' * indentation,
                                         version=simplify_version(version),
                                         module=module)


def gen_method_test(rule, indentation=DEFAULT_INDENTATION):
    name, version = parse_rule(rule)
    module, item, method = name.rsplit('.', 2)
    return method_test_template.format(method=method,
                                       test_module=module.replace('.', '_'),
                                       item=item,
                                       indentation=' ' * indentation,
                                       version=simplify_version(version),
                                       module=module)


gen_data_test = gen_class_test


def gen_attribute_test(rule, indentation=DEFAULT_INDENTATION):
    name, version = parse_rule(rule)
    module, item, attribute = name.rsplit('.', 2)
    return attribute_test_template.format(attribute=attribute,
                                          test_module=module.replace('.', '_'),
                                          item=item,
                                          indentation=' ' * indentation,
                                          version=simplify_version(version),
                                          module=module)


def gen_function_kwarg_test(rule, indentation=DEFAULT_INDENTATION):
    name, version = parse_rule(rule)
    name, kwarg = name
    module, item = name.rsplit('.', 1)
    return function_kwarg_test_template.format(kwarg=kwarg,
                                               item=item,
                                               test_module=module.replace('.', '_'),
                                               indentation=' ' * indentation,
                                               version=simplify_version(version),
                                               module=module)


def gen_method_kwarg_test(rule, indentation=DEFAULT_INDENTATION):
    name, version = parse_rule(rule)
    name, kwarg = name
    module, item, method = name.rsplit('.', 2)
    return method_kwarg_test_template.format(kwarg=kwarg,
                                             method=method,
                                             test_module=module.replace('.', '_'),
                                             item=item,
                                             indentation=' ' * indentation,
                                             version=simplify_version(version),
                                             module=module)


def gen_multi(rules, rule_type, indentation=DEFAULT_INDENTATION):
    if rule_type not in all_rule_types:
        raise ValueError(f'invalid rule type {rule_type}')
    return '\n'.join(globals()[f'gen_{rule_type}_test'](rule, indentation) for rule in rules.splitlines())
