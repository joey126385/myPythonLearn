
"""
什么是编码？
    编码是将信息、数据、信号等转换成某种标准形式的过程。
    在计算机科学和信息技术领域，编码特指将信息（如文本、图片、音频、视频等）转换为计算机可以识别和处理的形式。
    这通常涉及到将原始信息转换为一系列的二进制代码（0和1），这些二进制代码可以被计算机硬件和软件解释和执行。

什么是编码规则？
    编码规则是指在进行信息或数据编码时所遵循的一系列标准和原则。
    这些规则确保了编码的一致性和准确性，从而方便数据的存储、传输和处理。

编码规范发展历史：
    1、ASCII编码，表示 127 个英文字符。刚开始只支持英语，其它语言不能够在计算机上存储和显示。
    2、GBK编码，中国编码。随着计算机普及，各国家语言不同，文字多少更是不同，127个根本不够用。各国都要为自己的语言编码
    3、Unicode规范，为了使国际间信息交流更加方便，国际组织制定了UNICODE 字符集，
      为各种语言中的每一个字符设定了统一并且唯一的数字编号，以满足跨语言、跨平台进行文本转换、处理的要求。
      目前90%的网站使用的是UTF-8编码。UTF-8 把unicode进行优化。减小了硬盘存储空间浪费与传输效率低下。
"""


"桃花坞里桃花庵，桃花庵里桃花仙。"
str1 = "桃花"
# 要求查看编码后的数据？
# 提示：使用 .encode(编码) 进行编码方法, 必填参数 encoding （编码集）

# 如何解码编码后的数据？
# 提示：使用 .decode(编码) 进行解码, 必填参数 encoding （编码集）
# 注意：用什么加密就用什么解密，解铃还须系铃人。
