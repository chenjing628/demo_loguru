from loguru import logger

#  需求：实现一个假发的操作
def add(a,b,*args):
    sum = 0
    if not isinstance(a,int):
        logger.error('输入的参数a的类型不正确')
        return
    if not isinstance(b,int):
        logger.error('输入的参数b的类型不正确')
        return
    for x in args:
        if not isinstance(x,int):
            logger.warning('输入的数据类型错误，请检查')
            continue
        sum += x
    sum = sum + a + b
    return sum
add(3,4)
print('*'*20)
add(3,'g')
add(2,5,8)
add(3,5,'k',2)
