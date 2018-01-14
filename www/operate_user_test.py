import asyncio

import sys

from www import orm

from www.models import User, Blog, Comment


# async def test():
#     await orm.create_pool(user='www-data', password='www-data', database='awesome')
#
#     u = User(name='Test', email='test@example.com', password='123456', image='about:blank')
#
#     await u.save()
#
#
# for x in test():
#     pass
async def test():
    await orm.create_pool(loop=loop, user='root', password='leihai', db='awesome')
    u = User(name='test22', email='test123@test.com', passwd='test', image='about:blank')
    await u.save()
    await orm.destory_pool()


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
