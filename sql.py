import sqlite3 as sq

# conn = sq.connect(':memory:')
conn = sq.connect("info.db")
exc = conn.cursor()
# theme = exc.execute("SELECT current_theme from theme").fetchone()[0]
# print(theme)


exc.execute("INSERT INTO path VALUES ('/home/', 'true', 1)")
conn.commit()


