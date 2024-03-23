import re
import os
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph


SOURCE_CODE_DIR = "./source_code"
SPLITTED_CODE_DIR = "./splitted_code"
FUNCTION_DECLARATION_PATTERN = r"\nvoid ([a-z]+)(?:[a-z(*)]+)"
STRUCT_DECLARATION_PATTERN = r"\nstruct ([a-z]+) {\n"


def get_files_from_dir():
    files = [val.replace("\\","/") for sublist in [[os.path.join(i[0],j) for j in i[2]] for i in os.walk(SOURCE_CODE_DIR)] for val in sublist]
    return files


def get_file_content(file):
    f = open(file, "r")
    return f.read()


def get_all_function_names(content):    
    function_names = re.findall(FUNCTION_DECLARATION_PATTERN, content)
    return list(set(function_names))


def find_end_of_function_index(function_str):
    start_fun_char = "{"
    end_fun_char = "}"
    new_start = 0
    for index in range(len(function_str)):
        c = function_str[index]        
        if c == end_fun_char:
            new_start -= 1
        elif c == start_fun_char:
            new_start += 1    
        if new_start == 0 and c == end_fun_char:            
            return (index + 1)
    print("No Index")


def write_file(file, data):
    print(f"Creating function file: {file}")
    f = open(file, "w")
    f.write(data)
    f.close


def get_function_content(reg_ex, content, function_name):      
    match = re.search(reg_ex, content)
    if match == None: return None
    start_index = match.start()
    end_of_str = match.end()
    print(f"{function_name}: {start_index}:{end_of_str}")
    # print(content[end_of_str:])
    end_index = end_of_str + find_end_of_function_index(content[end_of_str:])    
    return content[start_index:end_index]


def split_functions(function_names, content):
    # function_names = ["person","display","checkbalance","afterlogin"]
    for function_name in function_names:        
        FUNCTION_START_PATTERN = rf"\nvoid {function_name}(?:[0-9a-z(*), \[\]]*)[\n]+"        
        function_content = get_function_content(FUNCTION_START_PATTERN, content, function_name)
        if function_content == None: continue
        # print("Final Function:::")
        write_file(f"{SPLITTED_CODE_DIR}/{function_name}.c", function_content.strip())
        # break


def create_main_function(content):
    #Get all structures
    struct_names = re.findall(STRUCT_DECLARATION_PATTERN, content)
    print(struct_names)
    global_text = ""
    for struct_name in struct_names:        
        STRUCT_START_PATTERN = rf"\nstruct {struct_name} "
        function_content = get_function_content(STRUCT_START_PATTERN, content, struct_name)
        if function_content == None: continue
        global_text+= function_content + "\n"
    write_file(f"{SPLITTED_CODE_DIR}/global.c", global_text.strip())
    
    MAIN_START_PATTERN = rf"\nint main()"
    function_content = get_function_content(MAIN_START_PATTERN, content, "main")    
    write_file(f"{SPLITTED_CODE_DIR}/main.c", function_content.strip())
        # break


def create_call_graph(function_names):
    function_names.append("global")
    function_names.append("main")
    call_map = {}
    for functiion_name in function_names:
        f = open(f"./{SPLITTED_CODE_DIR}/{functiion_name}.c", "r")
        content = f.read()  
        called_functions = []
        for called_function in function_names: 
            if functiion_name == called_function: continue     
            regx = fr"{called_function}"
            match = re.search(regx, content)
            if match: called_functions.append(called_function)
        if len(called_function) > 0: call_map[functiion_name] = called_functions
    return call_map


def render_graph(edge_list, function_name):  
    if len(edge_list) == 0: return 
    graph = Digraph('G', filename='cluster.gv',node_attr={'color': 'lightblue2', 'style': 'filled'}, engine ="circo")
    for edge in edge_list:
        graph.edge(edge[0], edge[1])
    # graph.view()
    graph.render(f"./graphs/{function_name}")


def traverse_node(call_map, function_name, visited, edge_list):
    if function_name in visited:
        return
    visited.append(function_name)
    if function_name in call_map:
        for called_function in call_map[function_name]:
            edge_list.append([function_name, called_function])
            traverse_node(call_map, called_function, visited, edge_list)


def generate_call_graph(call_map):     
    for function_name in function_names:
        visited =[]
        edge_list = [] 
        traverse_node(call_map, function_name, visited, edge_list)
        render_graph(edge_list, function_name)



files = get_files_from_dir()
for file in files:
    content = get_file_content(file)
    function_names = get_all_function_names(content)
    print(function_names)
    # split_functions(function_names, content)    
    # create_main_function(content)
    call_map = create_call_graph(function_names)
    print(call_map)
    generate_call_graph(call_map)