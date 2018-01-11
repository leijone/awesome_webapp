from www import orm

from www.models import User, Blog, Comment


async def test():
    await orm.create_pool(user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', password='123456', image='about:blank')

    await u.save()


for x in test():
    pass
