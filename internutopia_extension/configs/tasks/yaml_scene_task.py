# internutopia_extension/configs/tasks/yaml_scene_task.py

from typing import Optional
from internutopia.core.config.task import TaskCfg
import yaml

class YamlSceneTaskCfg(TaskCfg):
    type: Optional[str] = 'SingleInferenceTask'  # 复用已有Task逻辑
    scene_yaml_path: Optional[str] = None        # 新增：yaml文件路径

    def model_post_init(self, __context):
        """YAML解析后自动填充父类字段"""
        if self.scene_yaml_path is None:
            return
        
        with open(self.scene_yaml_path, 'r') as f:
            raw = yaml.safe_load(f)
        
        scene = raw.get('scene', {})
        spawn = scene.get('spawn', {})
        
        # 把YAML里的scene信息映射到父类已有字段
        if spawn.get('usd_path') and self.scene_asset_path is None:
            self.scene_asset_path = spawn['usd_path']
        
        if spawn.get('scale') and self.scene_scale == (1.0, 1.0, 1.0):
            s = spawn['scale']
            self.scene_scale = (s[0], s[1], s[2])
        
        if spawn.get('translation') and self.scene_position == (0, 0, 0):
            t = spawn['translation']
            self.scene_position = (t[0], t[1], t[2])
        
        if spawn.get('orientation') and self.scene_orientation == (1.0, 0, 0, 0):
            o = spawn['orientation']
            self.scene_orientation = (o[0], o[1], o[2], o[3])