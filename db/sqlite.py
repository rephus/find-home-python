#https://docs.python.org/2/library/sqlite3.html
import sqlite3

#TODO: This class must be a singleton (1 connection)
class Sqlite:

  _db = "/var/sqlite/find-home-python.db"

  def __init__(self):
    print "Loading db ", Sqlite._db
    self._conn = sqlite3.connect(self._db, check_same_thread=False)
    self._evolutions()

  def version(self):
    c = self._conn.cursor()
    c.execute("SELECT key,value FROM settings WHERE key = 'version'")
    result = c.fetchone()
    c.close()
    return result[1]

  def _evolutions(self):
    try:
      version = self.version()
      #print "Rows in settings ", self._count("settings")
      if version < 0: # Replace 0 with next version
        pass #_schema_v1() should appear here
      else:
        #Last case (db is updated)
        print "Database is updated, version: {}".format(version)

    except Exception as error:
      print "Database exception: ",error
      self._schema_v0()
      print "Database successfully created"

  def _schema_v0(self):
    c = self._conn.cursor()
    c.execute("CREATE TABLE settings (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT,value TEXT)")
    c.execute("INSERT INTO settings (key,value) VALUES (?,?)",["version","0"])

    c.execute("""CREATE TABLE stations (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, zone NUMBER,
                 postal_code TEXT, lat NUMBER, lon NUMBER)""")

    self._conn.commit()
    c.close()

  def all(self, limit = 100):
    c = self._conn.cursor()
    c.execute('SELECT * FROM {}  order by id desc LIMIT {}'.format(self.table, limit))
    result = c.fetchall()
    c.close()
    return result

  def delete(self, id):
    c = self._conn.cursor()
    c.execute('DELETE FROM {} WHERE id = {}'.format(self.table, id))
    c.close()

  def last(self):
    c = self._conn.cursor()
    c.execute('SELECT * FROM {} ORDER BY id DESC LIMIT 1'.format(self.table))
    result = c.fetchone()
    c.close()
    return result

  def count(self):
    c = self._conn.cursor()
    c.execute('SELECT COUNT(*) FROM {}'.format(self.table))
    result = c.fetchone()
    c.close()
    return result[0]

  def destroy(self):
    self._conn.close()
