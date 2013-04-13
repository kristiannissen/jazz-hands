

class Router(object):
  def __init__(self):
    self.urls = (
      '/', 'HomeHandler',
      '/(\d+)', 'DocumentHandler'
    )
  
  def get_routes(self):
    return self.urls