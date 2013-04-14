

class Router(object):
  def __init__(self):
    self.urls = (
      '/', 'HomeHandler',
      '/login/', 'LoginHandler',
      '/user/', 'UserHandler'
    )
  
  def get_routes(self):
    return self.urls