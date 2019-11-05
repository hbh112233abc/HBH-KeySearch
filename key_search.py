import sublime
import sublime_plugin

import webbrowser
import urllib.parse

class KeySearchCommand(sublime_plugin.TextCommand):
    def run(self, edit,driver=""):
        # 配置信息
        #print('input driver:',driver)
        conf = sublime.load_settings("HBH-KeySearch.sublime-settings")
        if not driver:
            driver = conf.get('default_driver','baidu')
        #print('select driver:',driver)
        search_format_conf = conf.get('search_format',{})
        #print('search_format_conf:',search_format_conf)
        search_format = search_format_conf.get(driver,'https://www.baidu.com/s?wd={key}')
        #print('search_format:',search_format)
        # 选中的字符串
        sels = self.view.sel()
        sel = sels[0]
        #print(sel)
        keywords = self.view.substr(sels[0])
        keywords = urllib.parse.quote(keywords)
        #print('keywords:',keywords)
        # 打开浏览器搜索引擎 搜索该文本
        url = search_format.replace('{key}',keywords)
        #print('url:',url)
        webbrowser.open_new_tab(url)
