import sqlite3

mail = [('1', 'siddharth.sulur@gmail.com'),
 ('2', 'gokulrajtvm05@gmail.com'),
 ('3', 'madhavan86776@gmail.com'),
 ('4', 'siddharth.sulur@gmail.com'),
 ('5', 'madhavan07vk@gmail.com'),
 ('6', 'siddharth.sulur@gmail.com'),
 ('7', 'siddharthsridhar2006@gmail.com'),
 ('8', 'siddharthsridhar2006@gmail.com'),
 ('9', 'gokulrajtvm05@gmail.com'),
 ('10', 'aravindhnov05@gmail.com'),
 ('11', 'madhavan07vk@gmail.com'),
 ('12', 'laravindakrishnan@gmail.com'),
 ('13', 'arav302005@gmail.com'),
 ('14', 'siddharthsridhar2006@gmail.com'),
 ('15', 'arav302005@gmail.com'),
 ('16', 'siddharth.sulur@gmail.com'),
 ('17', 'siddharth.sulur@gmail.com'),
 ('18', 'gokulrajtvm05@gmail.com'),
 ('19', 'gokulrajtvm05@gmail.com'),
 ('20', 'laravindakrishnan@gmail.com'),
 ('21', 'laravindakrishnan@gmail.com'),
 ('22', 'aravindhnov05@gmail.com'),
 ('23', 'arav302005@gmail.com'),
 ('24', 'siddharth.sulur@gmail.com'),
 ('25', 'siddharthsridhar2006@gmail.com'),
 ('26', 'madhavan07vk@gmail.com'),
 ('27', 'madhavan86776@gmail.com'),
 ('28', 'madhavan07vk@gmail.com'),
 ('29', 'siddharthsridhar2006@gmail.com'),
 ('30', 'laravindakrishnan@gmail.com'),
 ('31', 'siddharthsridhar2006@gmail.com'),
 ('32', 'aravindhnov05@gmail.com'),
 ('33', 'madhavan07vk@gmail.com'),
 ('34', 'madhavan86776@gmail.com'),
 ('35', 'madhavan07vk@gmail.com'),
 ('36', 'madhavan07vk@gmail.com'),
 ('37', 'arav302005@gmail.com'),
 ('38', 'laravindakrishnan@gmail.com'),
 ('39', 'siddharthsridhar2006@gmail.com'),
 ('40', 'laravindakrishnan@gmail.com'),
 ('41', 'gokulrajtvm05@gmail.com'),
 ('42', 'aravindhnov05@gmail.com'),
 ('43', 'arav302005@gmail.com'),
 ('44', 'siddharth.sulur@gmail.com'),
 ('45', 'arav302005@gmail.com'),
 ('46', 'madhavan86776@gmail.com'),
 ('47', 'laravindakrishnan@gmail.com'),
 ('48', 'siddharthsridhar2006@gmail.com'),
 ('49', 'laravindakrishnan@gmail.com'),
 ('50', 'arav302005@gmail.com')]

conn = sqlite3.connect('mail.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE items (
    id TEXT PRIMARY KEY,
    mail TEXT
)
""")


cur.executemany("""
INSERT OR REPLACE INTO items (id, mail)
VALUES (?, ?)
""", mail)

conn.commit()
conn.close()