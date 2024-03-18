import json
from string import Template
import re

# 根据参数匹配内容
def find(data):
    # 判断data类型是否为字典
    if isinstance(data, dict):
        # 对象格式化为str
        data = json.dumps(data)
        # 定义正则匹配规则
        pattern = "\\${(.*?)}"
        # 按匹配进行查询，把查询的结果返回
        return re.findall(pattern, data)

# 进行参数替换
def replace(ori_data, replace_data):
    # 对象格式化为str
    ori_data = json.dumps(ori_data)
    # 处理字符串的类，实例化并初始化原始字符
    s = Template(ori_data)
    # 使用新的字符，替换
    return s.safe_substitute(replace_data)

# 根据var，逐层获取json格式的值
def parse_relation(var, resdata):
    # 判断变量var是否存在
    if not var:
        # 如果变量var不存在，则直接返回resdata
        return resdata
    else:
        # 如果变量var存在，则获取数组第一个类容
        resdata = resdata.get(var[0])
        # 从数组中删除第一个类容
        del var[0]
        # 递归
        return parse_relation(var, resdata)

# 测试代码
if __name__ == '__main__':
    ori_data = {"admin-token":"${token}"}
    replace_data = {'token':'x015k878'}
    print(replace(ori_data, replace_data))
