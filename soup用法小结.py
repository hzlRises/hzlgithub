#coding:utf-8
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
#   http://cuiqingcai.com/1319.html
html = '''
<div id="abc">
<tbody><tr>
            	<th rowspan="2"><i>装修前</i><br>准备阶段</th>
                <td><b>收房验房：</b></td>
                <td><a class = "one" target="_blank" href="http://home.fang.com/zhishi/liucheng/list01/">交房手续及流程</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list02/">验房流程</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list03/">毛坯房验收</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list04/">精装房验收</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list05/">二手房验收</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list06/">收房常识必备</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list07/">资金准备</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list116/">公积金知识</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list117/">房贷/房产契税</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list118/">买房知识</a></td>
            </tr>
            <tr>
            	<td><b>装修准备：</b></td>
                <td><a class = "two" target="_blank" href="http://home.fang.com/zhishi/liucheng/list08/">装修基础概念</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list09/">装修方式</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list10/">选择装修风格</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list11/">制定设计方案</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list12/">装修预算制定</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list13/">基础装修报价单</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list14/">100平简约报价</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list15/">小户型报价参考</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list16/">报价注意事项</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list17/">装修公司选择</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list18/">资质考察</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list19/">设计师选择</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list20/">施工队选择</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list21/">家装洽谈</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list22/">签订装修合同</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list23/">合同范本参考</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list24/">装修付款</a></td>
            </tr>
            <tr>
            	<th style="background:#f1f1f1;" rowspan="7"><i>装修中</i><br>施工阶段</th>
                <td><b>开工准备：</b></td>
                <td><a class = "three" target="_blank" href="http://home.fang.com/zhishi/liucheng/list25/">物业登记事项</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list26/">建材清单参考</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list27/">装修工期安排</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list28/">材料进场验收</a></td>
            </tr>
            <tr>
            	<td><b>拆改工程：</b></td>
                <td><a class = "one" target="_blank" href="http://home.fang.com/zhishi/liucheng/list29/">结构拆改</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list30/">承重墙改造</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list31/">燃气管道改造</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list32/">水电改造</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list33/">水路施工</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list34/">电路施工</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list35/">强弱电施工</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list36/">地板基层施工</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list37/">护墙基层施工</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list38/">门窗套安装</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list39/">吊顶基层施工</a></td>
            </tr>
            <tr>
            	<td><b>木工工程：</b></td>
                <td><a class = "one" class="dsf" target="_blank" href="http://home.fang.com/zhishi/liucheng/list40/">木工施工流程</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list41/">板材</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list42/">龙骨</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list43/">顶角/踢脚线</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list44/">石膏板</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list45/">胶黏剂/胶水</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list46/">玻璃</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list47/">扣板</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list48/">门窗</a></td>
            </tr>
            <tr>
            	<td><b>中期验收：</b></td>
                <td><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list49/">中期验收内容</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list50/">中期验收标准</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list51/">隐藏工程验收</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list52/">木工验收</a></td>
            </tr>
            <tr>
            	<td><b>泥瓦工程：</b></td>
                <td><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list53/">泥瓦施工流程</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list54/">地面防水</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list55/">地面找平</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list56/">地暖铺设</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list57/">瓷砖铺贴</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list58/">石材铺装</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list59/">泥瓦工程验收</a></td>
            </tr>
            <tr>
            	<td><b>油漆工程：</b></td>
                <td><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list60/">油漆施工工艺</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list61/">油漆施工流程</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list62/">油漆工程验收</a></td>
            </tr>
            <tr>
            	<td><b>硬装收尾：</b></td>
                <td><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list63/">贴壁纸/墙纸</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list64/">地板铺贴</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list65/">洁具安装</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list66/">五金安装</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list67/">灯具安装</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list68/">家电安装</a></td>
            </tr>
        	<tr>
            	<th rowspan="2"><i>装修后</i><br>入住阶段</th>
                <td><b>监理验收：</b></td>
                <td><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list69/">装修监理流程</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list70/">完工验收</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list71/">核算装修款</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list72/">家装保修服务</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list73/">污染检测</a></td>
            </tr>
            <tr>
            	<td><b>软装家电：</b></td>
                <td><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list74/">软装搭配原则</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list75/">窗帘布艺选购</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list76/">家电选购</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list77/">家具选购</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list78/">地毯选购搭配</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list79/">装饰画选择</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list80/">花卉选择摆放</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list81/">搬家搬场</a><a target="_blank" href="http://home.fang.com/zhishi/liucheng/list82/">装修保洁</a></td>
            </tr>
        </tbody>
		
		
		
		<ol>
        	<li><b>建材：</b><span><a target="_blank" href="http://home.fang.com/zhishi/daogou/list83/">灯具</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list84/">卫浴</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list85/">油漆</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list86/">瓷砖</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list87/">门窗</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list88/">五金</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list89/">橱柜</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list90/">地板</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list91/">暖气设备</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list92/">壁纸</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list93/">水龙头</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list94/">天花板/吊顶</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list95/">建筑构件</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list96/">装修材料</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list97/">厨房用具</a></span></li>
        	<li><b>家具：</b><span><a target="_blank" href="http://home.fang.com/zhishi/daogou/list98/">家具</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list99/">儿童家具</a></span></li>
        	<li><b>软装：</b><span><a target="_blank" href="http://home.fang.com/zhishi/daogou/list100/">地毯</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list101/">床上用品</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list102/">窗帘</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list103/">日杂用品</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list104/">饰品</a></span></li>
        	<li><b>电器：</b><span><a target="_blank" href="http://home.fang.com/zhishi/daogou/list105/">办公用品</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list106/">家用电器</a><a target="_blank" href="http://home.fang.com/zhishi/daogou/list107/">厨卫电器</a></span></li>
        </ol>
		
		
		<ol class = "dd">
        	<li><b>家居风水布局：</b><span><a target="_blank" href="http://home.fang.com/zhishi/fengshui/list108/">客厅风水</a><a target="_blank" href="http://home.fang.com/zhishi/fengshui/list109/">卧室风水</a><a target="_blank" href="http://home.fang.com/zhishi/fengshui/list110/">厨房风水</a><a target="_blank" href="http://home.fang.com/zhishi/fengshui/list111/">卫生间风水</a></span></li>
        	<li><b>装修风水学：</b><span><a target="_blank" href="http://home.fang.com/zhishi/fengshui/list112/">装修风水</a><a target="_blank" href="http://home.fang.com/zhishi/fengshui/list113/">桃花运风水</a><a target="_blank" href="http://home.fang.com/zhishi/fengshui/list114/">财运风水</a><a target="_blank" href="http://home.fang.com/zhishi/fengshui/list115/">办公室风水</a></span></li>
        </ol>
    </div>
    <div id ="efg">
        myid=efg
    </div>
    <div id ="h" class="bbbbb">
        myid=h
    </div>
    <div id ="h">
        myid=h
    </div>
    <div id ="i">
        myid=i
    </div>
'''
s = BeautifulSoup(html,"lxml")

print s.find(id="h")
print s.find_all("div",attrs={"id":"h"})

'''
print s.find(id="i").stripped_strings
for li in s.find(id="i").stripped_strings:
    print li
'''

'''
传方法
def has_class_id(s):
    return s.has_attr('class') and  s.has_attr('id')

print s.find_all(has_class_id)
'''



'''
遍历文档树
.content 属性可以将tag的子节点以列表的方式输出
print s.ol.contents

for li in s.ol.contents:
    print li

输出方式为列表，可以用列表索引来获取它的某一个元素
print s.ol.contents[1]
'''

'''
print s.find_all('a')获取所有a标签
print s.find_all("a", attrs={"class": "one"})获取所有class为one的a标签
print s.find_all("div",attrs={"id":"abc"})#获取所有id为abc的div
for li in s.find_all("a", attrs={"class": "one"},):
    print li
for li in s.find_all("div",attrs={"id":"abc"}):
    print li
'''

'''
print s.find(id="abc").string
print s.find(id="efg").string
关于string属性，如果超过一个标签的话，那么就会返回None，否则就返回具体的字符串
超过一个标签的话，可以试用strings
'''

'''
print s.find(id="abc").get_text()获取id为abc的div下所有文本内容，不包含html标签

print s.find(id="abc").strings
 返回list 生成器对象
<generator object _all_strings at 0x0185D058>

for li in s.find(id="abc").strings:
    print li
'''
'''
.stripped_strings 
输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
for li in s.find(id="abc").stripped_strings :
    print li
'''



