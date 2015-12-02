from sqlite import Sqlite

class Settings(Sqlite):
  
  table = "settings" #Used in sqlite for common methods (all,count)
  
  def __init__(self):
    Sqlite.__init__(self)
    #This table must be included in the default schema (see evolutions)
    
    self.load()

  def _getBoolean(self, value):
      return value == "true" or value == "True" or value == True or value == 1
  
  def load (self): 
    print "Loading settings from DB"
    
    self.voice = self._getBoolean(self.get("voice"))
    
    print self
    
  def __str__(self): 
    return """voice: {}""".format(self.voice)
              
  def put(self,key, value):
    print "Saving settings key: {}, value: {}".format(key,value)
    c = self._conn.cursor()
    c.execute("REPLACE INTO settings (key,value) VALUES (?,?)",[key,value])
    self._conn.commit()
    c.close()
    
  def get(self,key):
    c = self._conn.cursor()
    c.execute('SELECT key,value FROM settings WHERE key=? LIMIT 1',[key])
    result = c.fetchone()
    if result:
      result = result[1]
    c.close()
    return result