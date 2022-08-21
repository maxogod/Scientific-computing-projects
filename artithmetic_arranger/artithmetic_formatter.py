def arithmetic_arranger(problems, solve=False):
  
  if len(problems) > 5:
    return 'Error: Too many problems.'
    
  arranged_problems = ''
  frst_line = ''
  scnd_line = ''
  dashes_line = ''
  result = ''
  
  for i in range(len(problems)):
    prob_lst = problems[i].split()
    
    if not prob_lst[0].isnumeric() or not prob_lst[2].isnumeric():
      return 'Error: Numbers must only contain digits.'
    if len(prob_lst[0]) > 4 or len(prob_lst[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    if prob_lst[1] not in ('+', '-'):
      return "Error: Operator must be '+' or '-'."
      
    if i == len(problems) - 1:
      extra_spaces = ''
    else:
      extra_spaces = '    '

    if len(prob_lst[0]) >= len(prob_lst[2]):
      space = ' ' * (len(prob_lst[0]) - len(prob_lst[2]))
      frst_line += f'  {prob_lst[0]}{extra_spaces}'
      scnd_line += f'{prob_lst[1]} {space}{prob_lst[2]}{extra_spaces}'
      dashes = '-' * (len(prob_lst[0]) + 2)
      dashes_line += f'{dashes}{extra_spaces}'
      if prob_lst[1] == '+':
        result_num = int(prob_lst[0]) + int(prob_lst[2])
        result += f'{" " * (len(dashes) - len(str(result_num)))}{result_num}{extra_spaces}'
      elif prob_lst[1] == '-':
        result_num = int(prob_lst[0]) - int(prob_lst[2])
        result += f'{" " * (len(dashes) - len(str(result_num)))}{result_num}{extra_spaces}'
      
    else:
      space = ' ' * (len(prob_lst[2]) - len(prob_lst[0]))
      frst_line += f'  {space}{prob_lst[0]}{extra_spaces}'
      scnd_line += f'{prob_lst[1]} {prob_lst[2]}{extra_spaces}'
      dashes = '-' * (len(prob_lst[2]) + 2)
      dashes_line += f'{dashes}{extra_spaces}'
      if prob_lst[1] == '+':
        result_num = int(prob_lst[0]) + int(prob_lst[2])
        result += f'{" " * (len(dashes) - len(str(result_num)))}{result_num}{extra_spaces}'
      elif prob_lst[1] == '-':
        result_num = int(prob_lst[0]) - int(prob_lst[2])
        result += f'{" " * (len(dashes) - len(str(result_num)))}{result_num}{extra_spaces}'
  if solve:
    arranged_problems += f'{frst_line}\n{scnd_line}\n{dashes_line}\n{result}'
  else:
    arranged_problems += f'{frst_line}\n{scnd_line}\n{dashes_line}'
  return arranged_problems

print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']))
