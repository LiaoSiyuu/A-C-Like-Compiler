"""
@ Author: 2054435 廖偲宇
@ Date: 2023-04-29
@ Version: 1.0
@ Description: 编译器-词法分析器类
"""

import re
import sys


class Lexical_Analyzer():
    # @ 函数名：__init__
    # @ 函数功能：初始化
    def __init__(self):
        self.CURRENT_LINE = 0
        self.pInputStr = 0
        # 保留字
        self.reserved = {
            'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
            'int': 'INT',
            'return': 'RETURN',
            'void': 'VOID'
        }
        # 类别
        self.type = ['seperator', 'operator', 'identifier', 'int']
        # 词法分析所使用的正则表达式
        self.regex = [
            '\{|\}|\[|\]|\(|\)|,|;',  # 界符
            '\+|-|\*|/|==|!=|>=|<=|>|<|=',  # 操作符
            '[a-zA-Z][a-zA-Z0-9]*',  # 标识符
            '\d+'  # 整数
        ]

    # 函数名：remove_comments
    # 函数功能：去除注释
    def tool_remove_comments(self, text):
        comments = re.findall('//.*?\n', text, flags=re.DOTALL)
        if len(comments) > 0:
            text = text.replace(comments[0], "")
        comments = re.findall('/\*.*?\*/', text, flags=re.DOTALL)
        if len(comments) > 0:
            text = text.replace(comments[0], "")
        return text.strip()

    # @ 函数名：tool_scan
    # @ 函数功能：扫描一行(经行一次扫描，返回得到的token以及剩余的字符串)
    def tool_scan(self, line):
        tmp_max = ''
        target_regex = self.regex[0]
        index_sub = 0
        match = False
        for regex in self.regex:
            result = re.match(regex, line)
            if result:
                result = result.group(0)
                if len(result) > len(tmp_max):
                    match = True
                    tmp_max = result
                    target_regex = regex
        # 出错处理
        if not match:
            print(u"非法字符：" + line[0])
            return {"data": line[0], "regex": None, "remain": line[1:]}
        else:
            return {"data": tmp_max, "regex": target_regex, "remain": line[index_sub + len(tmp_max):]}

    # @ 函数名：tool_scan_line
    # @ 函数功能：重复扫描一行，并返回一组token
    def tool_scan_line(self, line):
        tokens = []
        result = line.strip().strip('\t')
        origin = result
        while True:
            if result == "":
                break
            before = result
            result = self.tool_scan(result)
            if result['regex']:
                token = {
                    'class': "T",
                    'row': self.CURRENT_LINE,
                    'colum': origin.find(before) + 1,
                    'name': self.type[self.regex.index(result['regex'])].upper(),
                    'data': result['data']
                }
                token['type'] = token['name']

                # 保留字，对应文法中->不加引号，认定为终结符
                if result['data'] in self.reserved:
                    token['name'] = self.reserved[result['data']].lower()
                    token['type'] = token['name']

                # 操作符或者界符，对应文法中->加引号，认定为终结符
                if token['name'] == "operator".upper() or token['name'] == "seperator".upper():
                    token['type'] = token['data']

                if token['name'] == "INT":
                    token['data'] = token['data']  # 如果是int(token['data'])，词法分析表就显示不出来，因为要str
                tokens.append(token)

            result = result['remain'].strip().strip('\t')
            if result == "":
                return tokens
        return tokens

    # @ 函数名：genTokensFromInputBox
    # @ 函数功能：从输入框生成token
    def genTokensFromInputBox(self, input_str):
        lines = self.tool_remove_comments(input_str).split('\n')
        tokens = []
        for line in lines:
            tokens_temp = self.tool_scan_line(line)
            tokens += tokens_temp
            self.CURRENT_LINE += 1
        return tokens

    # @ 函数名：getTokensOfOneLine
    # @ 函数功能：从一行中获取token
    def getTokensOfOneLine(self, input_str):
        if self.pInputStr >= len(input_str):
            return []
        while True:
            idx = input_str.find('\n', self.pInputStr)
            if idx == -1:
                idx = len(input_str) - 1
            line = input_str[self.pInputStr:idx + 1].strip()
            self.pInputStr = idx + 1
            if line == '':
                continue
            else:
                break

        tokens = self.tool_scan_line(line)
        sys.stdout.flush()
        return tokens
