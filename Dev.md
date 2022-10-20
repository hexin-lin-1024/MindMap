## Markdown 规范
换行：行尾打出两个空格后留一个空行再开始下一行。  
表格，强调，代码块后不加两个空格且空一行再开始，在此前的正文需空一行且不加两个空格。  
正文不同段落之间空两行。  
正文与强调之间空一行。  
正文中加入代码块两端空格。  

## 抽象机制

### 消息抽象
`Mail` 对象，每一个邮件都封装在一个对象中。
```Python
class Mail:
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
发送操作（接受一个Mail对象）  
同步机制： 
启动之后，在初始化阶段收取历史信息，同时初始化实时队列。  
任务反馈：每次创建新任务时分配TASK ID，执行完后放入完成队列中，可以调用 `status(id)` 来查询任务是否成功。
实现以下功能：  
1. 对于客户端（有状态）  
实现：发送代理、接收绑定：如果收到新消息，调用触发客户端刷新  
2. 对于插件（无状态）  
实现：客户端的发送任务代理；收到新消息时放入队列并且触发客户端刷新  

```Python
class Sync:
    def __init__(self, config): #config 为用户配置
        self.description = "" #简短条件描述
        self.detail = "" #说明细节

    def send(self, mail):
        pass
```

### 分类插件抽象
包含多个 `Judge` 对象。

```Python
class Judge:
    def __init__(self, config): #config 为用户配置
        self.description = "" #简短条件描述
        self.detail = "" #说明细节

    def judge(self, mail):
        pass
        #返回真或者假
```

For Example:

```Python
class Judge:
    def __init__(self, config):
        self.description = "是垃圾邮件" #简短条件描述
        self.detail = "通过关键词判断是否为垃圾邮件" #说明细节
        self.keywords = config["keywords"]
        
    def judge(self, mail):
        for i in self.keywords:
            if i in mail.TEXT:
                return True
        return False
```

改进：  
有没有可能存在非布尔值判断的需求？如何对此类进行抽象?
`config` 的可视化机制：`config["vis"]` 中存储可视化模板？