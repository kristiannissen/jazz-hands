import os
import yaml

class Config(object):
  def __init__(self):
    file_path = os.path.join(os.path.dirname(__file__), 'settings.yaml')
    with open(file_path) as f:
      self.yaml_data = yaml.load(f)

  def get_settings(self):
    return self.yaml_data

  def get_settings_for(self, name):
    if self.yaml_data.has_key(name):
      return self.yaml_data.get(name)
    return None
