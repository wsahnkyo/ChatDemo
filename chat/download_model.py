#模型下载，复制代码到上述文件
from modelscope import snapshot_download
model_dir = snapshot_download('qwen/Qwen-1_8B-Chat',local_dir=r"E:\model\Qwen-1_8B-Chat")