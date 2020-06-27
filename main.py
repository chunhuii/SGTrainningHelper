from selenium import webdriver
from selenium.webdriver.common.by import By
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
while True:
    try:
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
            driver.execute_script(r"location.assign(location.href.replace('courseInfo.do','viewCourseVideoTemple.do'));")
            time.sleep(contSplitSec)
            p = driver.execute_script(r'var i=($(".duration,.pv-time-duration").text().split(":")[0]*60)+($(".duration,.pv-time-duration").text().split(":")[1]*60)+(($(".duration,.pv-time-duration").text().split(":").length==3)?($(".duration,.pv-time-duration").text().split(":")[2]*60):0);return i;')
            itime=int(p+30) if type(p)!="NoneType" else 10
            driver.execute_script(r'setTimeout(function(){ $("#evaluationComment").text("good!");courseDetailEvaluation();setTimeout(function(){ nextCourse(); },(%s*1000),0);},(%s*1000),0);' % (str(contSplitSec+10),str(itime+10)))
            time.sleep(5)
            driver.execute_script(r'try{ setTimeout(player.play(),%s*1000,0); }catch(exception){ setTimeout($(".pv-playpause").click(),%s*1000,0); }'%(str(contSplitSec),(contSplitSec)))
            time.sleep(itime+20)
    except:
        driver.refresh()
