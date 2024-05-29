# import os
# import re
# from urllib.parse import urlparse

# # 正则表达式模式，严格匹配 URL 和 IP 地址
# url_pattern = re.compile(
#     r'\b((http|https)://'
#     r'(([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,6}|'  # 域名部分
#     r'(\d{1,3}\.){3}\d{1,3})'              # 或 IP 地址部分
#     r'(:\d+)?'                             # 端口部分（可选）
#     r'(/[a-zA-Z0-9_%./~-]*)?)\b'            # 路径部分（可选）
# )

# # 更精确的正则表达式模式，匹配发送数据的方法
# send_methods_pattern = re.compile(
#     r'\b(fetch|XMLHttpRequest|\.ajax|\.post|\.get|\.put|\.delete|axios\.post|axios\.get|axios\.put|axios\.delete|axios\.request|sendBeacon)\b', re.IGNORECASE
# )

# # 正则表达式模式，匹配变量定义
# variable_pattern = re.compile(
#     r'\b(var|let|const)?\s*(\w+)\s*=\s*["\']([^"\']+)["\']\s*;', re.IGNORECASE
# )

# # 检查 URL 是否有效
# def is_valid_url(url):
#     try:
#         result = urlparse(url)
#         return all([result.scheme, result.netloc]) and not any(keyword in url for keyword in ['getURL', 'setAtt'])
#     except ValueError:
#         return False

# def find_server_addresses(root_dir, max_depth=3):
#     server_addresses = []
#     variables = {}

#     def search_files(current_dir, depth):
#         if depth > max_depth:
#             return
#         try:
#             for entry in os.scandir(current_dir):
#                 if entry.is_dir(follow_symlinks=False):
#                     search_files(entry.path, depth + 1)
#                 elif entry.is_file(follow_symlinks=False) and entry.name.endswith('.js'): #and ('content' in entry.name or 'background' in entry.name):
#                     with open(entry.path, 'r', encoding='utf-8', errors='ignore') as file:
#                         lines = file.readlines()
#                         for i, line in enumerate(lines):
#                             line = line.strip()
#                             if line.startswith('//') or line.startswith('/*') or line.startswith('*'):
#                                 continue  # 跳过注释行

#                             # 检查变量定义
#                             var_match = variable_pattern.match(line)
#                             if var_match:
#                                 var_name = var_match.group(2)
#                                 var_value = var_match.group(3)
#                                 variables[var_name] = var_value
#                                 print(f"Captured variable: {var_name} = {var_value}")

#                             # 检查发送数据的方法是否存在于当前行
#                             if send_methods_pattern.search(line):
#                                 print(f"Found send method in line: {line}")

#                                 # 检查发送数据行中的直接地址
#                                 addresses = url_pattern.findall(line)
#                                 for address in addresses:
#                                     full_address = address[0]
#                                     if is_valid_url(full_address):
#                                         server_addresses.append(full_address)
#                                         print(f"Found direct address: {full_address}")

#                                 # 检查发送数据行中的变量
#                                 for var_name, var_value in variables.items():
#                                     if re.search(r'\b' + re.escape(var_name) + r'\b', line):
#                                         if is_valid_url(var_value):
#                                             server_addresses.append(var_value)
#                                             print(f"Variable {var_name} used in line: {line}, value: {var_value}")

#         except Exception as e:
#             print(f"Error reading {current_dir}: {e}")

#     search_files(root_dir, 1)
#     return server_addresses

# # 使用示例
# root_directory = r'C:\Users\rkw20\OneDrive\Desktop\KTH\DD2525\extension_EXP\Insecure'  # 修改为实际的根文件夹路径
# addresses = find_server_addresses(root_directory)
# print("Found server addresses used for sending data:")
# for address in addresses:
#     print(address)
import os
import re
from urllib.parse import urlparse

# 正则表达式模式，严格匹配 URL 和 IP 地址
url_pattern = re.compile(
    r'\b((http|https)://'
    r'(([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,6}|'  # 域名部分
    r'(\d{1,3}\.){3}\d{1,3})'              # 或 IP 地址部分
    r'(:\d+)?'                             # 端口部分（可选）
    r'(/[a-zA-Z0-9_%./~-]*)?)\b'           # 路径部分（可选）
)

# 更精确的正则表达式模式，匹配发送数据的方法
send_methods_pattern = re.compile(
    r'\b(fetch|XMLHttpRequest|\.ajax|\.post|\.get|\.put|\.delete|axios\.post|axios\.get|axios\.put|axios\.delete|axios\.request|sendBeacon|io)\b', re.IGNORECASE
)

# 正则表达式模式，匹配变量定义
variable_pattern = re.compile(
    r'\b(var|let|const)?\s*(\w+)\s*=\s*["\']([^"\']+)["\']\s*;', re.IGNORECASE
)

io_pattern = re.compile(
    r'io\(["\']([^"\']+)["\']\)', re.IGNORECASE
)


# # 更精确的正则表达式模式，匹配发送数据的方法
# send_methods_pattern = re.compile(
#     r'\b(fetch|XMLHttpRequest|\.ajax|\.post|\.get|\.put|\.delete|axios\.post|axios\.get|axios\.put|axios\.delete|axios\.request|sendBeacon|io)\b', re.IGNORECASE
# )

# # 正则表达式模式，匹配变量定义
# variable_pattern = re.compile(
#     r'\b(var|let|const)?\s*(\w+)\s*=\s*["\']([^"\']+)["\']\s*;', re.IGNORECASE
# )

# 检查 URL 是否有效
import os
import re
from urllib.parse import urlparse

# 正则表达式模式，严格匹配 URL 和 IP 地址
url_pattern = re.compile(
    r'\b((http|https)://'
    r'(([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,6}|'  # 域名部分
    r'(\d{1,3}\.){3}\d{1,3})'              # 或 IP 地址部分
    r'(:\d+)?'                             # 端口部分（可选）
    r'(/[a-zA-Z0-9_%./~-]*)?)\b'           # 路径部分（可选）
)

# 更精确的正则表达式模式，匹配发送数据的方法
send_methods_pattern = re.compile(
    r'\b(fetch|XMLHttpRequest|\.ajax|\.post|\.get|\.put|\.delete|axios\.post|axios\.get|axios\.put|axios\.delete|axios\.request|sendBeacon|io)\b', re.IGNORECASE
)

# 正则表达式模式，匹配变量定义
variable_pattern = re.compile(
    r'\b(var|let|const)?\s*(\w+)\s*=\s*["\']([^"\']+)["\']\s*;', re.IGNORECASE
)

# 正则表达式模式，匹配 io 方法调用
io_pattern = re.compile(
    r'io\(["\']([^"\']+)["\']\)', re.IGNORECASE
)

# 检查 URL 是否有效
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc]) and not any(keyword in url for keyword in ['getURL', 'setAtt'])
    except ValueError:
        return False

def check_content_and_background_files(root_dir):
    content_found = False
    background_found = False

    for entry in os.scandir(root_dir):
        if entry.is_file(follow_symlinks=False) and entry.name.endswith('.js'):
            if 'content' in entry.name:
                content_found = True
            if 'background' in entry.name:
                background_found = True

    return content_found and background_found

def find_server_addresses(root_dir, max_depth=3):
    server_addresses = []
    variables = {}

    def search_files(current_dir, depth, content_and_background_only):
        if depth > max_depth:
            return
        try:
            for entry in os.scandir(current_dir):
                if entry.is_dir(follow_symlinks=False):
                    search_files(entry.path, depth + 1, content_and_background_only)
                elif entry.is_file(follow_symlinks=False) and entry.name.endswith('.js'):
                    if content_and_background_only and not ('content' in entry.name or 'background' in entry.name):
                        continue
                    with open(entry.path, 'r', encoding='utf-8', errors='ignore') as file:
                        lines = file.readlines()
                        for i, line in enumerate(lines):
                            line = line.strip()
                            if line.startswith('//') or line.startswith('/*') or line.startswith('*'):
                                continue  # 跳过注释行

                            # 检查变量定义
                            var_match = variable_pattern.match(line)
                            if var_match:
                                var_name = var_match.group(2)
                                var_value = var_match.group(3)
                                variables[var_name] = var_value
                                print(f"Captured variable: {var_name} = {var_value}")

                            # 检查发送数据的方法是否存在于当前行
                            if send_methods_pattern.search(line):
                                print(f"Found send method in line: {line}")

                                # 检查发送数据行中的直接地址
                                addresses = url_pattern.findall(line)
                                for address in addresses:
                                    full_address = address[0]
                                    if is_valid_url(full_address):
                                        server_addresses.append(full_address)
                                        print(f"Found direct address: {full_address}")

                                # 检查 io 方法调用中的地址
                                io_match = io_pattern.search(line)
                                if io_match:
                                    io_address = io_match.group(1)
                                    if is_valid_url(io_address):
                                        server_addresses.append(io_address)
                                        print(f"Found io address: {io_address}")

                                # 检查发送数据行中的变量
                                for var_name, var_value in variables.items():
                                    if re.search(r'\b' + re.escape(var_name) + r'\b', line):
                                        if is_valid_url(var_value):
                                            server_addresses.append(var_value)
                                            print(f"Variable {var_name} used in line: {line}, value: {var_value}")

        except Exception as e:
            print(f"Error reading {current_dir}: {e}")

    content_and_background_only = check_content_and_background_files(root_dir)
    search_files(root_dir, 1, content_and_background_only)
    return server_addresses

root_directory = r'C:\Users\rkw20\OneDrive\Desktop\KTH\DD2525\extension_EXP\Insecure'  # 修改为实际的根文件夹路径
addresses = find_server_addresses(root_directory)
print("Found server addresses used for sending data:")
for address in addresses:
    print(address)
