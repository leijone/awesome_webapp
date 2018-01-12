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
async def test(loop):
    await orm.create_pool(loop=loop, user='ubuntu', password='ubuntu', db='personalblog')
    u = User(name='test22', email='test22@test.com', password='test', image='about:blank')
    await u.save()
    await orm.destory_pool()


data=dict(name='gaf', email='235123345@qq.com', passwd='1312345', image='about:blank')
loop=asyncio.get_event_loop()
# loop.run_until_complete(test(loop,**data))
loop.run_until_complete(test(loop))
loop.close()
