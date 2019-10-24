#! /usr/bin/env python3
# -*- coding: utf-8

import javalang
import sys
from javalang.tree import MethodDeclaration, ReturnStatement, FieldDeclaration, LocalVariableDeclaration

def read_file(filename):
  with open(filename, 'r') as f:
    ret = f.read()
  return ret

def analysis_ret_empty_array_rather_than_null(filename):
  """
  see https://pmd.github.io/latest/pmd_rules_java_errorprone.html#returnemptyarrayratherthannull
  """
  ast = javalang.parse.parse(read_file(filename))
  for cls in ast.types:
    for member in cls.body:
      if isinstance(member, MethodDeclaration):
        # ret type
        if member.return_type != None and len(member.return_type.dimensions) > 0:
          ret_arr_flag = True
        else:
          continue # no need to check
        # function body
        if member.body == None: continue
        for stmt in member.body:
          if isinstance(stmt, ReturnStatement):
            if ret_arr_flag:
              try:
                if stmt.expression.value == 'null':
                  print('catches an error')
              except AttributeError:
                pass


def analysis_track_vars(filename):
  """
  see https://pmd.github.io/latest/pmd_rules_java_errorprone.html#returnemptyarrayratherthannull
  """
  # print(ast.types[1])
  ast = javalang.parse.parse(read_file(filename))
  for cls in ast.types:
    cls_var_record = {}
    for member in cls.body:
      if isinstance(member, MethodDeclaration):
        local_var_record = {}
        # function body
        if member.body == None: continue
        for stmt in member.body:
          if isinstance(stmt, LocalVariableDeclaration):
            var_type = stmt.type
            for var in stmt.declarators:
              local_var_record[var.name] = var_type
        # print('vars in method', member.name, local_var_record)
      elif isinstance(member, FieldDeclaration): 
        # member variable in class
        var_type = member.type
        for var in member.declarators:
         cls_var_record[var.name] = var_type
    # print('vars in class', cls_var_record)

def is_string(tokens, i, string_set):
    if type(tokens[i]) == javalang.tokenizer.String:
        return True
    if type(tokens[i]) == javalang.tokenizer.Identifier and tokens[i].value in string_set:
        return True
    return False


def is_operator(tokens, i):
    return type(tokens[i]) == javalang.tokenizer.Operator


def analysis_string_cmp(fname):
    result = list()
    string_set = set()
    with open(fname, 'r') as file:
        data = file.read()
        tokens = list(javalang.tokenizer.tokenize(data))
        for i in range(len(tokens)):
            # print(tokens[i])
            if type(tokens[i]) == javalang.tokenizer.Identifier and tokens[i].value == "String":
                string_set.add(tokens[i+1].value)
            if i < len(tokens) - 2 and is_string(tokens, i, string_set) and is_operator(tokens, i+1)\
                    and is_string(tokens, i + 2, string_set):
                if tokens[i].position[0] != tokens[i+1].position[0] or \
                        tokens[i+1].position[0] != tokens[i + 2].position[0]:
                    continue
                if javalang.tokenizer.Operator.is_infix(tokens[i+1]):
                    result.append(tokens[i+1].position)

    print("There are {} bad string comparison in the program.".format(len(result)))
    print(result)


if __name__ == '__main__':
  analysis_ret_empty_array_rather_than_null(sys.argv[1])

