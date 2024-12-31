import asyncpg

async def fetch_data():
    conn = await asyncpg.connect(user='user', password='password', database='dbname', host='localhost')
    data = await conn.fetch('SELECT * FROM my_table')
    await conn.close()
    return data