#! /usr/bin/env python3
# -*- coding: utf-8

import javalang
import sys
from javalang.tree import MethodDeclaration, ReturnStatement, FieldDeclaration, LocalVariableDeclaration

def read_file(filename):
  with open(filename, 'r') as f:
    ret = f.read()
  return ret

def analysis_ret_empty_array_rather_than_null(ast):
  """
  see https://pmd.github.io/latest/pmd_rules_java_errorprone.html#returnemptyarrayratherthannull
  """
  # print(ast.types[1])
  for cls in ast.types:
    cls_var_record = {}
    for member in cls.body:
      if isinstance(member, MethodDeclaration):
        ret_arr_flag = False
        local_var_record = {}
        if member.return_type != None and len(member.return_type.dimensions) > 0:
          ret_arr_flag = True
        else:
          continue # no need to check
        for stmt in member.body:
          if isinstance(stmt, LocalVariableDeclaration):
            var_type = stmt.type
            for var in stmt.declarators:
              local_var_record[var.name] = var_type
          elif isinstance(stmt, ReturnStatement):
            if ret_arr_flag:
              try:
                if stmt.expression.value == 'null':
                  print('catches an error')
              except AttributeError:
                pass
        print('vars in method', member.name, local_var_record)
      elif isinstance(member, FieldDeclaration): 
        var_type = member.type
        for var in member.declarators:
         cls_var_record[var.name] = var_type
    print('vars in class', cls_var_record)


if __name__ == '__main__':
  ast = javalang.parse.parse(read_file(sys.argv[1]))
  analysis_ret_empty_array_rather_than_null(ast)

