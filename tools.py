from krita import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

_tools = []

class Tool:
    def __init__(self, uid, name, func):
        self.uid = uid
        self.name = name
        self.func = func
    
    def __call__(self):
        self.func()

def registerTools(window):
    for tool in tools:
        log.write("Register Tools: uid " + tool.uid + " name " + tool.name)
        action = window.createAction(tool.uid, tool.name, "tools/scripts")
        action.triggered.connect(tool)

def tool(func, uid, name):
    log.write("Tool Decorator: uid " + uid + " name " + name)
    toolCls = Tool(uid, name, func)
    _tools.append(toolCls)
    return toolCls

@tool("smoosh-hello", "Hello")
def tool_hello():
    QMessageBox.information(QWidget(), "Test", "Hello World")