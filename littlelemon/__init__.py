# PyMySQL configuration for Windows/systems without mysqlclient C-extensions
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
