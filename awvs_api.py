#!/usr/bin/env python3
#coding:utf-8
#Author:se55i0n
#Awvs 11 API利用脚本

import json
import time
import requests
import urllib.parse
import setting
import traceback
import requests.packages.urllib3


class awvs(object):
	def __init__(self,target,rule):
		self.task = []
		# self.server = 'https://127.0.0.1:13443/api/v1'
		self.server = setting.awvs_server
		self.apikey = setting.awvs_apikey
		self.header = {'X-Auth':self.apikey,'content-type':'application/json'}
		self.target = target
		self.rule = rule
		#前6个为系统默认扫描策略，后面为自定义
		self.scan_rule = {
				"FS": "11111111-1111-1111-1111-111111111111",
				"HR": "11111111-1111-1111-1111-111111111112",
				"XSS": "11111111-1111-1111-1111-111111111116",
				"SQL": "11111111-1111-1111-1111-111111111113",
				"WP": "11111111-1111-1111-1111-111111111115",
				"CO": "11111111-1111-1111-1111-111111111117"
				}
		self.W = '\033[0m'
		self.G = '\033[1;32m'
		self.O = '\033[1;33m'
		self.R = '\033[1;31m'
		self.B = '\033[1;34m'
		requests.packages.urllib3.disable_warnings()

	def request(self, path):
		try:
			return requests.get(url=self.server+path, timeout=10, 
					verify=False, headers=self.header)
		except Exception as e:
			print(e)

	def scan_type(self):
		#扫描策略选择
		try:
			l = '[0] 全扫描\n'
			l += '[1] 高风险漏洞\n'
			l += '[2] 跨站点脚本漏洞\n'
			l += '[3] SQL注入漏洞\n'
			l += '[4] 脆弱的密码\n'
			l += '[5] 仅爬行'
			print(self.G+l+self.W)
			rule = input(self.O+'[Awvs_Api/Set_Rule]>> '+self.W)
			if rule == '0':
				return self.scan_rule['FS']
			elif rule == '1':
				return self.scan_rule['HR']
			elif rule == '2':
				return self.scan_rule['XSS']
			elif rule == '3':
				return self.scan_rule['SQL']
			elif rule == '4':
				return self.scan_rule['WP']
			elif rule == '5':
				return self.scan_rule['CO']
			else:
				print(self.R+'[-] Ops, 输入有误...'+self.W)
		except Exception as e:
			pass

	
	def scan_type_(self):
    		#扫描策略选择
		try:
			# l = '[0] 全扫描\n'
			# l += '[1] 高风险漏洞\n'
			# l += '[2] 跨站点脚本漏洞\n'
			# l += '[3] SQL注入漏洞\n'
			# l += '[4] 弱口令\n'
			# l += '[5] 仅爬行'
			# print(self.G+l+self.W)
			# rule = input(self.O+'[Awvs_Api/Set_Rule]>> '+self.W)
			rule = self.rule
			if rule == '0':
				return self.scan_rule['FS']
			elif rule == '1':
				return self.scan_rule['HR']
			elif rule == '2':
				return self.scan_rule['XSS']
			elif rule == '3':
				return self.scan_rule['SQL']
			elif rule == '4':
				return self.scan_rule['WP']
			elif rule == '5':
				return self.scan_rule['CO']
			else:
				print(self.R+'[-] Ops, 输入有误...'+self.W)
		except Exception as e:
			pass

	def check_id(self):
		#扫描任务ID选择
		try:
			r = self.request('/scans')
			response = json.loads(r.text)
			text = response['scans']
			if len(text)>0:
				for i in range(len(text)):
					self.task.append(text[i]['scan_id'])
					print(self.G+'['+str(i)+']',text[i]['target']['address']+self.W)
				task_id = input(self.O+'[Awvs_Api/Set_Task_Id]>> '+self.W)
				return self.task[int(task_id)]
			else:
				print(self.R+'[-] Ops, 当前无扫描任务...'+self.W)
				return
		except Exception as e:
			print(self.R+'[-] Ops, 输入有误...'+self.W)
		finally:
			#清空获取的任务列表
			del self.task[:]


	# def check_id_(self):
	# 	#扫描任务ID选择
	# 	try:
	# 		r = self.request('/scans')
	# 		response = json.loads(r.text)
	# 		text = response['scans']
	# 		if len(text)>0:
	# 			for i in range(len(text)):
	# 				self.task.append(text[i]['scan_id'])
	# 				print(self.G+'['+str(i)+']',text[i]['target']['address']+self.W)
	# 			# task_id = input(self.O+'[Awvs_Api/Set_Task_Id]>> '+self.W)
	# 			task_id = i
	# 			return self.task[int(task_id)]
	# 		else:
	# 			print(self.R+'[-] Ops, 当前无扫描任务...'+self.W)
	# 			return
	# 	except Exception as e:
	# 		print(self.R+'[-] Ops, 输入有误...'+self.W)
	# 	finally:
	# 		#清空获取的任务列表
	# 		del self.task[:]


	def add(self):
		#添加扫描对象
		try:
			target = input(self.O+'[Awvs_Api/Set_Target]>> '+self.W)
			# target = self.target
			if target:
				data = {'address':target,'description':'','criticality':10}
				r = requests.post(url=self.server+'/targets', timeout=10, 
					verify=False, headers=self.header, data=json.dumps(data))
				if r.status_code == 201:
					return json.loads(r.text)['target_id']
			else:
				return False
		except Exception as e:
			print(e)

	def add_(self):
    		#添加扫描对象
		try:
			# target = input(self.O+'[Awvs_Api/Set_Target]>> '+self.W)
			target = self.target
			if target:
				data = {'address':target,'description':'','criticality':10}
				r = requests.post(url=self.server+'/targets', timeout=10, 
					verify=False, headers=self.header, data=json.dumps(data))
				if r.status_code == 201:
					return json.loads(r.text)['target_id']
			else:
				return False
		except Exception as e:
			print(e)

	def scan(self):
		#启动扫描任务
		data = {'target_id':self.add(),'profile_id':self.scan_type(),
		'schedule':{'disable':False,'start_date':None, 'time_sensitive':False}}
		try:
			r = requests.post(url=self.server+'/scans', timeout=10, 
				verify=False, headers=self.header, data=json.dumps(data))
			if r.status_code == 201:
				print(self.G+'[-] OK, 扫描任务已经启动...'+self.W)
		except Exception as e:
			print(e)


	def scan_(self):
    		#启动扫描任务
		data = {'target_id':self.add_(),'profile_id':self.scan_type_(),
		'schedule':{'disable':False,'start_date':None, 'time_sensitive':False}}
		try:
			r = requests.post(url=self.server+'/scans', timeout=10, 
				verify=False, headers=self.header, data=json.dumps(data))
			if r.status_code == 201:
				print(self.G+'[-] OK, 扫描任务已经启动...'+self.W)
		except Exception as e:
			print(e)


	def stop(self):
		#停止扫描任务
		try:
			r = requests.post(url=self.server+'/scans/'+self.check_id()+'/abort',
			 timeout=10, verify=False, headers=self.header)
			if r.status_code == 204:
				print(self.G+'[-] OK, 扫描已经停止...'+self.W)
		except Exception as e:
			pass

	def view(self):
		#查看任务状态
		try:
			r = self.request('/scans/'+self.check_id())
			response = json.loads(r.text)
			addr = response['target']['address']
			high = response['current_session']['severity_counts']['high']
			medium = response['current_session']['severity_counts']['medium']
			low = response['current_session']['severity_counts']['low']
			status = response['current_session']['status']
			print(self.G+'[-] 扫描目标: {}'.format(addr))
			print('[-] 扫描状态: {}'.format(status))
			print('[-] 高危漏洞: {}'.format(high))
			print('[-] 中危漏洞: {}'.format(medium))
			print('[-] 低危漏洞: {}'.format(low)+self.W)
		except Exception as e:
			pass

	def report(self):
		#生成报告
		try:
			data = {'template_id':'11111111-1111-1111-1111-111111111111',
			'source':{'list_type':'scans','id_list':[self.check_id()]}}
			r = requests.post(url=self.server+'/reports',timeout=10, 
				verify=False, headers=self.header, data=json.dumps(data))
			if r.status_code == 201:
				self.download(r.headers['Location'])
		except Exception as e:
			print(e)

	def download(self, path):
		#下载报告
		try:
			r = requests.get(url=self.server.replace('/api/v1','')+path,
				timeout=10, verify=False, headers=self.header)
			response = json.loads(r.text)
			report_id = response['report_id']
			target = response['source']['description']
			url = self.server.replace('/api/v1','')+'/reports/download/'
			print(self.G+'[-] 报告生成中...'+self.W)
			#等待报告生成
			while True:
				time.sleep(5)
				_r = self.request('/reports/'+report_id)
				if json.loads(_r.text)['status'] == 'completed':
					res = requests.get(url=url+report_id+'.pdf',verify=False,timeout=10)
					if res.status_code == 200:
						name = urllib.parse.urlparse(target).netloc.replace(';','')
						print(self.G+'[-] OK, 报告下载成功.'+self.W)
						with open(name +'.pdf', 'wb') as f:
							f.write(res.content)
						break
		except Exception as e:
			print(e)

	def delete(self):
		#删除扫描任务
		try:
			r = requests.delete(url=self.server+'/scans/'+self.check_id(), 
				timeout=10, verify=False, headers=self.header)
			if r.status_code == 204:
				print('url = ',self.server+'/scans/'+self.check_id())
				print('status_code = ',r.status_code)
				print(self.G+'[-] OK, 已经删除任务...'+self.W)
		except Exception as e:
			pass



	def delete_(self):
		c = 0
		print("[*]开始清除任务")
		while True:
			result = requests.get(self.server+"/targets?c="+str(c),headers=self.header,timeout=30,verify=False)
			results = json.loads(result.content)
			c = c + 100
			if results['targets'] == []:
				return print("[*]任务全部清除完毕")
			for s in results["targets"]:
				r = requests.delete(url=self.server+'/targets/'+s['target_id'], timeout=10, verify=False, headers=self.header)
				print("[-]当前删除 target_id:%s"%s['target_id'])


	def handle(self):
		#任务调度
		try:
			self.banner()
			self.usage()
			print('-'*43)
			while True:
				show = input(self.O+'[Awvs_Api]>> '+self.W)
				if show == 'view':
					self.view()
				elif show == 'scan':
					self.scan()
				elif show == 'stop':
					self.stop()
				elif show == 'del':
					self.delete()
				elif show == 'report':
					self.report()
				elif show == 'help' or show == '?':
					self.usage()
				elif show == 'exit':
					break
				elif show == '':
					pass
				else:
					print(self.R+'[-] Ops, 输入错误...'+self.W)
		except KeyboardInterrupt:
			pass


	# def main(self):
	# 	pass


	def usage(self): 
		s = '帮助:\n'
		s += '    scan     开始扫描任务\n'
		s += '    stop     停止扫描任务\n'
		s += '    del      删除扫描任务\n'
		s += '    report   任务扫描报告\n'
		s += '    view     查看扫描任务\n'
		s += '    ?、help  查看扫描帮助\n'
		s += '    exit     退出扫描任务'
		print(self.B+s+self.W)


	def banner(self):
		flag = '''
    ___                      ___          _
   /   |_      ___   _______/   |  ____  (_)
  / /| | | /| / / | / / ___/ /| | / __ \/ /
 / ___ | |/ |/ /| |/ (__  ) ___ |/ /_/ / /
/_/  |_|__/|__/ |___/____/_/  |_/ .___/_/
                               /_/'''
		
		print(self.O+flag+self.W+'\n')
		print('-'*43)


# if __name__ == '__main__':
# 	mywvs = awvs()
# 	mywvs.handle()
	
