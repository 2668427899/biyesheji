# coding: utf-8
__author__ = 'ila'
import configparser
# 通过 configparser 模块读取配置文件 config.ini，获取 HDFS 的主机地址。
from hdfs.client import Client
def upload_to_hdfs(filename):
    try:
        port = 50070
        cp = configparser.ConfigParser()
        cp.read('config.ini',encoding="utf-8")

        client = Client(f"http://{cp.get('sql','host')}:{port}/")
        user_dir = "tmp"
        client.upload(hdfs_path=f'/{user_dir}/{filename}', local_path=filename, chunk_size=2 << 19, overwrite=True)
    except Exception as e:
        print(f'upload_to_hdfs eror : {e}')