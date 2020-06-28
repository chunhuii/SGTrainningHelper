from selenium import webdriver
from selenium.webdriver.common import action_chains
import time

#登陆网站的用户名
userName='abc'
#登陆网站的密码
userPass='abc'
#你参与的项目ID（在地址栏找到）
projectID='11111111111111111111111'
#操作时间间隔
contSplitSec=5

driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
action = action_chains.ActionChains(driver)
while True:
    driver.get(r'http://jmhaotong.kttx.cn/pc/index.do')
    driver.set_window_size(1366,768)
    time.sleep(contSplitSec)
    driver.execute_script(r"$('#mobile').val('%s');$('#password').val('%s');dologin();"%(str(userName),str(userPass)))
    time.sleep(contSplitSec)
    driver.get(r'http://jmhaotong.kttx.cn:80/pc/project/projectInfo.do?projectId=%s' % str(projectID))
    time.sleep(contSplitSec)
    driver.execute_script(r'$(".details_center ul li.active")[0].click();var L=$("ul#stageTable li.actives").length;var O=$("ul#stageTable li.actives")[L-1];window.open($(O).find("a").attr("href"),"_self")')
    time.sleep(contSplitSec)
    while(str(driver.current_url).find("courseInfo.do") > -1 or str(driver.current_url).find("viewCourseVideoTemple.do") > -1):
        print("进入下一课程...")
        driver.get(driver.current_url.replace('courseInfo.do','viewCourseVideoTemple.do'))
        print("课程视频获取中...")
        time.sleep(contSplitSec)
        p = int(driver.execute_script(r'var i=$(".duration,.pv-time-duration").text().split(":").length;return $(".duration,.pv-time-duration").text().split(":")[0]*60+$(".duration,.pv-time-duration").text().split(":")[1]*(i==3?60:1)+(i==3?$(".duration,.pv-time-duration").text().split(":")[2]*1:0);'))
        itime=int(p+30) if type(p)!="NoneType" else 10
        print("获取播放总时间...%s秒+30秒"% str(p))
        time.sleep(contSplitSec*3)
        try:
            action.click(driver.find_element_by_css_selector('.prism-big-play-btn')).perform()
        except:
            pass
        print("开始学习...")
        time.sleep(itime)
        print("完成本课程学习。")
        input=driver.find_element_by_id('evaluationComment')
        input.send_keys('good!')
        driver.execute_script('courseDetailEvaluation()')
        print("自动评论本课程。")
        time.sleep(contSplitSec)
        driver.execute_script(r'nextCourse()')
