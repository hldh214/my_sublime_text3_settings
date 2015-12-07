import sublime, sublime_plugin
#import webbrowser
import os

class OpenBrowserCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		host = 'http://localhost/' #主机名
		local = 'C:\\xampp\\htdocs\\' #本地服务器路径,注意每一个反斜杠之后要加一个反斜杠用于转义
		browser = 'C:\\Users\\hldh214\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe ' #浏览器路径,注意每一个反斜杠之后要加一个反斜杠用于转义
		url = host + self.view.file_name().split(local)[1].replace('\\', '/') #构造最终URL
		os.popen(browser + url) #使用CMD打开浏览器进行浏览
		#webbrowser.open(url)