import os
import importlib
from keyword import iskeyword
import threading, queue,time

def call_plugin(p_name,method,state=None,text=None,filepath=None,propath=None):
    #package='plugins.'+p_name 根据路径引入对应的插件模块
    obj = importlib.import_module('.' + p_name, package='plugins.'+p_name)
    c = getattr(obj,p_name)
    obj = c(state,text,{},filepath,propath) # new class
    mtd = getattr(obj,method)
    return mtd()
def getAllPlugin(filepath):
    plg_ls=[]
    files=os.listdir(filepath)
    for f in files:
        #过滤_开头、关键字模块，且为文件夹
        if not f.startswith('_') and not iskeyword(f) and os.path.isdir(filepath+'/'+f):
            #判断插件主模块是否存在，即插件文件夹名.py文件是否存在
            if os.path.exists(filepath+'/'+f+'/'+f+'.py') and f!='BasePlugin':
                plg_ls.append(f)

    # print(plg_ls)
    # for f in files:
    #     if f.endswith('.py') and not f.startswith('_') and not iskeyword(f):
    #         # print(os.path.splitext(f)[0])
    #         plg_ls.append(os.path.splitext(f)[0])
    # plgs={}.fromkeys(plg_ls)
    # for plugin in plgs:
    #     # obj = __import__(plugin)  # import module (同级目录)
    #     #importlib.import_module导入一个模块。参数 name 指定了以绝对或相对导入方式导入什么模块 (比如要么像这样 pkg.mod 或者这样 ..mod)。如果参数 name 使用相对导入的方式来指定，那么那个参数 packages 必须设置为那个包名，这个包名作为解析这个包名的锚点 (比如 import_module('..mod', 'pkg.subpkg') 将会导入 pkg.mod)。
    #     obj =importlib.import_module('.'+plugin,package='plugins')
    #     c = getattr(obj, plugin)
    #     obj=c()
    #     r=re.compile('(?!__)')#匹配非__开头
    #     plgs[plugin]=list(filter(r.match, dir(obj)))#dir(obj)列出obj所有方法，返回list，python3中filter默认返回filter类
    # return plgs
    return plg_ls


