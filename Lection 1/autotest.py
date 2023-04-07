from unittest.mock import patch
from os import walk
import time


from jobs2 import test as program
test_dir="31"
ShowPrint=False
def fakeInput():
    global data
    global data_index
    result = data[data_index]
    data_index+=1
    return result
def fakePrint(s):
    global result_program
    result_program.append(str(s))

def showResult(file_name,data,result_program,result,errorIndex,time_running):
    print('-' * 200)
    print(f'Тестовый файл:{file_name}')
    if len(data)>20:
        print(f'Входные данные: {len(data)} строк')
    else:
        print(f'Входные данные:\n{data}')
    if len(result_program)>0:

        if len(result_program)>20 and len(errorIndex)==0:
            print(f'Результат программы: {len(result_program)} строк')
        else:
            print(f'Результат программы:\n{result_program}')
    else:
        print("результатов нет!")
    if len(result) > 0:

        if len(result) > 20 and len(errorIndex)==0:
            print(f'Результат должен быть: {len(result)} строк')
        else:
            print(f'Результат должен быть:\n{result}')
    else:
        print("Ожидаемых результатов нет!")
    if (len(errorIndex)>0):
        print('Ошибки:')
        for i in errorIndex:
            print(f'{i}:Ожидаем |{result[i]}| - получено |{result_program[i]}|')
    else:
        print('Ошибок нет!')
    print(f'Время выполнения программы:{time_running/1000000}')



data_files = []
result_program=[]
result_files = {}
f=[]
errorIndex=[]
for (dirpath, dirnames, filenames) in walk(f'.\\{test_dir}'):
        f.extend(filenames)
        break
data_files=[x for x in filenames if '.a' not in x]
result_files={x[:-2]:x for x in filenames if '.a' in x}

for file_name in data_files:
    with open(f'.\\{test_dir}\\{file_name}', "r") as f:
        data = []
        result=[]
        errorIndex = []
        result_program=[]
        data_index = 0
        for line in f:
            data.append(line.replace('\n',''))
        with patch.object(__builtins__, 'input', fakeInput):
            if ShowPrint:
                start = time.perf_counter_ns()
                program()
                time_running=time.perf_counter_ns()-start
            else:
                with patch.object(__builtins__, 'print', fakePrint):
                    start = time.perf_counter_ns()
                    program()
                    time_running=time.perf_counter_ns()-start
        if file_name in result_files:
            result_fileName=result_files[file_name]
            with open(f'.\\{test_dir}\\{result_fileName}', "r") as r:
                for line in r:
                    result.append(line.replace('\n',''))
                if len(result) == len(result_program):
                    for i in range (len(result)):

                        if result[i]!=result_program[i]:
                            errorIndex.append(i)
                else:
                    print (f'Ответов должно быть {len(result)}, а их {len(result_program)}')

        showResult(file_name, data, result_program, result, errorIndex,time_running)





