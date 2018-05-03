import www.orm

from www.models import User, Blog, Comment
import asyncio


async def test(loop,**kw):
    await www.orm.create_pool(loop=loop,user='root', password='andy123', db='awesome')
    u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'))
    await u.save()
    await www.orm.destory_pool()

data=dict(name='ayjk', email='andy5759520@gmail.com', passwd='andy123', image='about:blank')
loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop,**data))
loop.close()