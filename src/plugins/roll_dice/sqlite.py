import sqlite3

db_file="nodice.db"

def create_db():
    conn=sqlite3.connect(db_file)
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS qq_info (
                qq_id INTEGER PRIMARY KEY NOT NULL,
                is_ban INTEGER DEFAULT 0,
                ban_reason TEXT,
                ban_time INTEGER,
                is_admin INTEGER DEFAULT 0,
                admin_time INTEGER,
                is_white INTEGER DEFAULT 0,
                white_time INTEGER,
                jrrp_value INTEGER,
                jrrp_date TEXT,
                bot_on INTEGER DEFAULT 1,
                card_chosen TEXT DEFAULT \"default\",
                nick_name TEXT,
                default_dice INTEGER NOT NULL DEFAULT 100,
                success_rule INTEGER NOT NULL DEFAULT 0 CHECK (success_rule >= 0 AND success_rule <= 5))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS character_cards (
                qq_id INTEGER NOT NULL,
                card_name TEXT NOT NULL,
                property TEXT NOT NULL,
                value INTEGER NOT NULL,
                PRIMARY KEY (qq_id, card_name, property))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS group_info (
                group_id INTEGER NOT NULL,
                bot_on INTEGER DEFAULT 1,
                help_on INTEGER DEFAULT 1,
                jrrp_on INTEGER DEFAULT 1,
                is_ban INTEGER DEFAULT 0,
                ban_reason TEXT,
                ban_time INTEGER,
                is_white INTEGER DEFAULT 0,
                white_time INTEGER,
                default_dice INTEGER NOT NULL DEFAULT 100,
                success_rule INTEGER NOT NULL DEFAULT 0 CHECK (success_rule >= 0 AND success_rule <= 5), PRIMARY KEY(group_id))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS group_user_info (
                qq_id INTEGER NOT NULL,
                group_id INTEGER NOT NULL,
                type INTEGER NOT NULL,
                nick_name TEXT,
                card_chosen TEXT DEFAULT \"default\",
                PRIMARY KEY(qq_id, group_id, type))''')
    conn.commit()
    conn.close()

def insert_group_info(group_id):
    create_db()
    with sqlite3.connect(db_file) as conn:
        cur=conn.cursor()
        cur.execute(f"INSERT INTO group_info (group_id) VALUES ({group_id})")

def get_bot_on(group_id):
    try:
        with sqlite3.connect(db_file) as conn:
            cur=conn.cursor()
            cur.execute(f"SELECT bot_on FROM group_info WHERE group_id = {group_id}")
            return True if cur.fetchone()[0]==1 else False
    except:
        set_bot_on(group_id,True)
        return True

def set_bot_on(group_id,is_bot_on):
    try:
        insert_group_info(group_id)
    except:
        pass
    with sqlite3.connect(db_file) as conn:
        cur=conn.cursor()
        cur.execute(f"UPDATE group_info SET bot_on={1 if is_bot_on else 0} WHERE group_id = {group_id}")
        conn.commit()

def get_jrrp_on(group_id):
    try:
        with sqlite3.connect(db_file) as conn:
            cur=conn.cursor()
            cur.execute(f"SELECT jrrp_on FROM group_info WHERE group_id = {group_id}")
            return True if cur.fetchone()[0]==1 else False
    except:
        set_bot_on(group_id,True)
        return True

def set_jrrp_on(group_id,is_jrrp_on):
    try:
        insert_group_info(group_id)
    except:
        pass
    with sqlite3.connect(db_file) as conn:
        cur=conn.cursor()
        cur.execute(f"UPDATE group_info SET jrrp_on={1 if is_jrrp_on else 0} WHERE group_id = {group_id}")
        conn.commit()

def get_default_dice(group_id):
    try:
        with sqlite3.connect(db_file) as conn:
            cur=conn.cursor()
            cur.execute(f"SELECT default_dice FROM group_info WHERE group_id = {group_id}")
            return cur.fetchone()[0]
    except:
        insert_group_info(group_id)
        return 100

def set_default_dice(group_id,default_dice):
    try:
        insert_group_info(group_id)
    except:
        pass
    with sqlite3.connect(db_file) as conn:
        cur=conn.cursor()
        cur.execute(f"UPDATE group_info SET default_dice={default_dice} WHERE group_id = {group_id}")
        conn.commit()
        

if __name__=='__main__':
    print(get_bot_on(666))
    


