"""
自定义路由转换器
注册自定义的路由转换器, 在总路由注册
"""


class MobileConverter:
    """自定义路由转换器去匹配手机号 """
    # 定义匹配手机号的正则表达式: 18500001111
    regex = r'1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
