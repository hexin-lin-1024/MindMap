## Markdown 规范
换行：行尾打出两个空格后留一个空行再开始下一行。  

表格，强调，代码块后不加两个空格且空一行再开始，在此前的正文需空一行且不加两个空格。  

正文不同段落之间空两行。  

正文与强调之间空一行。  

## 抽象机制

### 消息抽象
`Mail` 对象，每一个邮件都封装在一个对象中。

```Python
class Mail():
    def __init__(self):
        pass

    #发件人（可能代发）

    #收件人（可能抄送）

    #附件

    #卫星数据：尽量列出

    @property #题目
    def TITLE(self):
        pass

    @TITLE.setter
    def TITLE(self, TITLE):
        pass
    
    @property #纯文本正文
    def TEXT(self):
        pass

    @TEXT.setter
    def TEXT(self, TEXT):
        pass

    @property #富文本正文
    def RICH_TEXT(self):
        pass
    
    @RICH_TEXT.setter
    def RICH_TEXT(self, RICH_TEXT):
        pass
```


## 插件机制
在 ./plugins 下，每一个插件占一个文件夹。

### 同步插件抽象



### 分类插件抽象


