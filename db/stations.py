from sqlite import Sqlite


class Stations(Sqlite):
  
  table = "stations" #Used in sqlite for common methods (all,count)
  
  def __init__(self):
    Sqlite.__init__(self)
    #This table must be included in the default schema (see evolutions)
