# import re, csv
# from time import sleep, time
# from random import uniform, randint
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException    

# def write_stat(loops, time):
# 	with open('stat.csv', 'a', newline='') as csvfile:
# 		spamwriter = csv.writer(csvfile, delimiter=',',
# 								quotechar='"', quoting=csv.QUOTE_MINIMAL)
# 		spamwriter.writerow([loops, time])  	 
	
# def check_exists_by_xpath(xpath):
#     try:
#         driver.find_element_by_xpath(xpath)
#     except NoSuchElementException:
#         return False
#     return True
	
# def wait_between(a,b):
# 	rand=uniform(a, b) 
# 	sleep(rand)
 
# def dimention(driver): 
# 	d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1]);
# 	return d if d else 3  # 默认情况下，Dimention为3
	
# # ***** 识别和提交图片解决方案的主要程序
# def solve_images(driver):	
# 	WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID ,"rc-imageselect-target"))
#         ) 		
# 	dim = dimention(driver)	
# 	# ****************** 检查是否有单击的图块******************
# 	if check_exists_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr/td[@class="rc-imageselect-tileselected"]'):
# 		rand2 = 0
# 	else:  
# 		rand2 = 1 

# 	# 等待，然后单击平铺 	
# 	wait_between(0.5, 1.0)		 
# 	# ****************** 点击瓷砖 ****************** 
# 	tile1 = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH ,   '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim )))) 
# 		)   
# 	tile1.click() 
# 	if (rand2):
# 		try:
# 			driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim))).click()
# 		except NoSuchElementException:          		
# 		    print('\n\r No Such Element Exception for finding 2nd tile')
   
	 
# 	#****************** 点击提交按钮****************** 
# 	driver.find_element_by_id("recaptcha-verify-button").click()

# start = time()	 
# url='...'
# driver = webdriver.Firefox()
# driver.get(url)

# mainWin = driver.current_window_handle  

# # 将驱动程序移动到第一个iframe
# driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])

# # *************  查找复选框  **************
# CheckBox = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))
#         ) 

# # *************  单击复选框  ***************
# wait_between(0.5, 0.7)  
# # 单击验证码复选框
# CheckBox.click() 
 
# #***************** 返回主窗口 **************************************
# driver.switch_to_window(mainWin)  

# wait_between(2.0, 2.5) 

# # ************ 按标记名切换到第二个iframe******************
# driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1])  
# i=1
# while i<130:
# 	print('\n\r{0}-th loop'.format(i))
# 	# ******** 检查第一帧是否选中复选框 ***********
# 	driver.switch_to_window(mainWin)   
# 	WebDriverWait(driver, 10).until(
#         EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME , 'iframe'))
#         )  
# 	wait_between(1.0, 2.0)
# 	if check_exists_by_xpath('//span[@aria-checked="true"]'): 
#         import winsound
# 		winsound.Beep(400,1500)
# 		write_stat(i, round(time()-start) - 1 ) # 将结果保存到stat文件中
# 		break 
		
# 	driver.switch_to_window(mainWin)   
# 	# ********** 到第二帧解图 *************
# 	wait_between(0.3, 1.5) 
# 	driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1]) 
# 	solve_images(driver)
# 	i=i+1

