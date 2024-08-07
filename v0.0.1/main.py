# -*-  coding : utf-8 -*-
# @Time : 2024/8/7 上午10:04
# @Autor : LceAn
# @File : main.py
# @Software : PyCharm


from flask import Flask, jsonify, render_template
import requests
import psutil

app = Flask(__name__)

DOCKER_API_URL = 'http://localhost:2375'


def get_container_info():
    response = requests.get(f'{DOCKER_API_URL}/containers/json?all=true')
    containers = response.json()
    container_info_list = []
    for container in containers:
        container_id = container['Id']
        container_name = container['Names'][0].lstrip('/')  # 去掉前面的斜杠
        stats_response = requests.get(f'{DOCKER_API_URL}/containers/{container_id}/stats?stream=false')

        stats = stats_response.json()
        if 'cpu_stats' in stats and 'precpu_stats' in stats:
            cpu_usage = stats['cpu_stats']['cpu_usage'].get('total_usage', 0)
            precpu_usage = stats['precpu_stats']['cpu_usage'].get('total_usage', 0)
            system_cpu_usage = stats['cpu_stats'].get('system_cpu_usage', 0)
            presystem_cpu_usage = stats['precpu_stats'].get('system_cpu_usage', 0)
            num_cpus = stats['cpu_stats'].get('online_cpus', 1)

            if system_cpu_usage > 0 and presystem_cpu_usage > 0:
                cpu_delta = cpu_usage - precpu_usage
                system_cpu_delta = system_cpu_usage - presystem_cpu_usage
                cpu_usage_percent = (cpu_delta / system_cpu_delta) * num_cpus * 100.0 if system_cpu_delta > 0 else 0.0
            else:
                cpu_usage_percent = 0.0
        else:
            cpu_usage_percent = 0.0

        memory_usage = stats['memory_stats'].get('usage', 0) / (1024 ** 2)  # 转换为MB
        memory_limit = stats['memory_stats'].get('limit', 1) / (1024 ** 2)  # 转换为MB
        memory_usage_percent = (memory_usage / memory_limit) * 100.0 if memory_limit > 0 else 0.0

        # 获取卷使用情况
        container_response = requests.get(f'{DOCKER_API_URL}/containers/{container_id}/json')
        container_details = container_response.json()
        volumes = container_details.get('Mounts', [])
        volume_usage_percent = 0  # 假设卷使用百分比
        volume_usage = 0  # 假设卷使用量
        volume_limit = 1  # 假设卷最大值

        # 获取网络信息
        network_io = stats.get('networks', {})
        rx_bytes = sum(interface['rx_bytes'] for interface in network_io.values())
        tx_bytes = sum(interface['tx_bytes'] for interface in network_io.values())
        rx_rate = rx_bytes / 1024  # 转换为KB/s
        tx_rate = tx_bytes / 1024  # 转换为KB/s

        container_info = {
            'id': container_id,
            'name': container_name,
            'cpu_usage': round(cpu_usage_percent, 2),
            'cpu_limit': num_cpus * 100,  # 假设每个CPU的最大值为100%
            'memory_usage': round(memory_usage, 2),
            'memory_limit': round(memory_limit, 2),
            'memory_usage_percent': round(memory_usage_percent, 2),
            'volume_usage': volume_usage,
            'volume_limit': volume_limit,
            'volume_usage_percent': round(volume_usage_percent, 2),
            'network_rx_rate': round(rx_rate, 2),
            'network_tx_rate': round(tx_rate, 2),
            'rx_bytes': round(rx_bytes / (1024 ** 3), 2),  # 转换为GB
            'tx_bytes': round(tx_bytes / (1024 ** 3), 2),  # 转换为GB
            'volumes': volumes
        }
        container_info_list.append(container_info)

    return container_info_list


def get_localhost_info():
    cpu_usage_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.used / (1024 ** 2)  # 转换为MB
    memory_limit = memory_info.total / (1024 ** 2)  # 转换为MB
    memory_usage_percent = memory_info.percent

    # 获取硬盘使用情况
    disk_info = psutil.disk_usage('/')
    volume_usage = disk_info.used / (1024 ** 3)  # 转换为GB
    volume_limit = disk_info.total / (1024 ** 3)  # 转换为GB
    volume_usage_percent = disk_info.percent

    # 获取网络信息
    net_io = psutil.net_io_counters()
    rx_bytes = net_io.bytes_recv
    tx_bytes = net_io.bytes_sent
    rx_rate = rx_bytes / 1024  # 转换为KB/s
    tx_rate = tx_bytes / 1024  # 转换为KB/s

    localhost_info = {
        'id': 'localhost',
        'name': 'Localhost',
        'cpu_usage': round(cpu_usage_percent, 2),
        'cpu_limit': cpu_count * 100,  # 假设每个CPU的最大值为100%
        'memory_usage': round(memory_usage, 2),
        'memory_limit': round(memory_limit, 2),
        'memory_usage_percent': round(memory_usage_percent, 2),
        'volume_usage': round(volume_usage, 2),
        'volume_limit': round(volume_limit, 2),
        'volume_usage_percent': round(volume_usage_percent, 2),
        'network_rx_rate': round(rx_rate, 2),
        'network_tx_rate': round(tx_rate, 2),
        'rx_bytes': round(rx_bytes / (1024 ** 3), 2),  # 转换为GB
        'tx_bytes': round(tx_bytes / (1024 ** 3), 2)  # 转换为GB
    }

    return localhost_info


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/localhost', methods=['GET'])
def get_localhost():
    localhost_info = get_localhost_info()
    return jsonify(localhost_info)


@app.route('/api/containers', methods=['GET'])
def list_containers():
    container_info = get_container_info()
    return jsonify(container_info)


if __name__ == '__main__':
    app.run(debug=True)
