#### 根据变量运行自动运行对应任务
没有代理的填写下面反代
## 特别声明
```text
有问题可以加InteIJ外部群 https://t.me/InteIJ (已经在封群的InteIJ的请不要加入,外部群只能使用活动参数的权限)
需要其他功能的可以反馈添加，或者反馈脚本BUG问题
有如果有其他获取参数的可以反馈给我添加
本项目所有活动来自TG各大频道,本项目偷免单助力介意勿用
害怕偷CK的勿用,不接受任何形式甩锅,不对任何行为负责
本脚本优先适配船长和M系列脚本,如果有其他相同脚本但是参数不同将优先适配为准
```

### 容器构建命令
```shell
docker run -dit \
  -p 5008:5008 \
  -e TZ=Asia/Shanghai \
  --name qlva \
  --restart unless-stopped \
  xgzk/qlvariable:latest
```
```http
http://IP:5008/
```
需要 定时任务 配置文件 权限
容器里面没有代码需要等待1-4分钟让程序跑起来
获取最新线报请重启项目
#### 青龙那边操作
```text
进入青龙容器
青龙10版本执行
touch /ql/config/qlva.sh
青龙11以后执行
touch /ql/data/config/qlva.sh

青龙面板 修改配置文件 config.sh
10添加 source /ql/config/qlva.sh
11以后添加 source /ql/data/config/qlva.sh
可以在配置文件的文件看到qlva.sh文件
```
#### 机器人指令
```text
机器人指令
机器人所在群组发送 /id 机器人会返回群组ID (转发线报的机器人别拉自己群会循环发送)
频道消息转发给机器人会返回 频道信息和个人信息
下面是私聊消息指令
    /forward ID 会把东西转发到这个频道或者群组 暂时只能使用一个ID
    /prohibit 名称 脚本加入黑名单会不执行
    /quit 频道ID或者@唯一名称 退出群聊或频道
    /putk 别名@青龙URL@Client_ID@Client_Secret 提交青龙相关执行参数 别名不能相同否则无法提交成功(提交的无法被执行)
    /start 启动提交的青龙，如果任务异常会被删除,也可以同步青龙任务
机器人交互设置
    找 https://t.me/BotFather 发送 /setprivacy 选择自己使用的机器人名称 选择D开头的
    怎么申请机器人自己百度
没有代理的把下面连接填写反代里 (反代不能转发，会乱码)
https://thingproxy.freeboard.io/fetch/https://api.telegram.org
```
### 对一些链接黑处理机制
```text
https://cjhydz-isv.isvjcloud.com 提取的是cj
lz cj ji pr sh tx wq 对非链接类型统一使用 no
export NOT_TYPE="lz";
别的怎么根据链接筛掉黑号自己解决
上面的会被自动当成链接变量添加到参数中
```

### 非adm64系统的问题
```text
因为不能测试adm64外的版本不清楚其他版本是否正常
如果拉取三次容器都显示相同错误的
请手动构架
第一步 下载docker目录下的所有文件
全部上传到Linux系统进入上传文件的目录执行
docker build -t xgzk/qlvariable:latest .
就行,然后重新执行容器构建命令
```

## 更新说明

```text
版本1.1 
 > 修复不同版本数据库差异问题
 > 添加去重功能
版本1.1.1
    > 修复重复提示不清楚问题
    > 增加请求次数，由原来一次请求失败，现在可以最多请求三次，只要成功一次，就不再请求了
    > 优化活动参数重复提醒
版本1.1.2
    > 适配了特别10.2版本，把10.2之前包括10.2定义为9版本
版本1.2
    > 更新可以保留conn.yml文件
    > 对一些获取进行不去重处理
    > 建议之前版本拉取最新脚本
版本1.3
    > 添加了配置文件检测
    > 修补了缺少的文件
    > 添加了10版本以上数据库表的检测
版本2
    > 正式启用容器版本
    > 取消了复杂的配置,改用程序自动适配
    > 有了自动更新省去了更新繁琐的步骤
版本2.1
    > 添加了库优先级,可以指定所有活动脚本走特定库,当库没有才走ID前面的脚本
    > 添加禁用活动脚本
    > 添加对相同活动去重复功能,只要其他脚本执行过将不再执行
版本2.2
    > 对页面进行美化
版本3.0
        > 使用tg官方机器人监控进行监控群组
        > 支持使用反代域名
        > 完美与爬虫端融合
        > 修改了对比去重复的标记物问题
        > 优化了对比数据执行时间缓慢问题
        > 不需要科学环境的正在开发还不支持使用(因公益服务器被攻击暂停开发这个部分)
    > 2022-11-1 修复当前版本出现BUG问题
        > 取消了官方TG库改成统一长连接请求
    > 2022-11-6 添加转发消息功能正式版本即将开始发布使用
        > 频道消息转发给机器人返回频道ID 群组发送 /id 机器人发给用户频道ID
    > 2022-11-7 修复多个参数漏掉问题
        > 支持获取链接变量类型 export NOT_TYPE 用户可以自己更改后筛掉黑CK
    > 2022-11-8
        > 修复没有过滤自己频道线报问题
        > 频道消息转发给机器人异常问题
        > 转发失败没有提示问题
        > 超时线报没有清理问题
    > 2022-11-9 13:07
        > 超时线报没有清理问题
        > 支持单参数活动变量转成伪活动链接(不清楚有没有问题)
        > 重复线报不再提示
    > 2022-11-9 17:21
        > 修复匹配船长库中 jd_wxCompleteInfo.py jd_joinCommon_opencard.py 的活动链接参数缺少问题
    > 2022-11-10 19:03
        > 添加脚本黑名单 /prohibit 名称
        > 修复链接转换参数 https_txt,异常问题: missing ), unterminated subpattern at position 0 报错
    > 2022-11-11 16:46
        > 修复重复参数标记物和线报出现 https://cjhydz-isv.isvjcloud.com&a7de573f565848dab15be18bae764aedexport 问题
版本3.1
        > 取消自动适配改用对任务列表解包统一json文件格式
        > 减少循环次数,优化了程序执行所需要的时间损耗
        > 同步脚本更改每12个小时同步一次
        > 清理重复参数更改12个小时清理一次
        > 合并清理和获取为一个函数
    > 2022-11-16 18:00
        > 修复禁用活动任务
    > 2022-11-16 21:00
        > 添加禁用重复任务
        > 修补 task 脚本 这种没有库的无法匹配问题
        > 不支持中文(此问题后期不会修复)
    > 2022-11-16 22:30
        > 修复NOT开头重复执行参数不执行问题
        > Administrator 用户ID正式启用 自己去配置文件填写,填写Administrator 的用户需要重启容器，暂时不能动态获取Administrator的值
        > 添加 Administrator 的用户遇到 NOT重复执行参数将会发送TG消息通知,一般七日签到等长期活动
    > 2022-11-16 23:10
        > 修复去重复关键字为空问题
    > 2022-11-17 12:00
        > 填充活动参数反转链接的数据库支持数量
    > 2022-11-18 11:00
        > 添加机器人退出群聊
        > 所有交互命令全部在设置Administrator的前提下触发
    > 2022-11-18 18:30
        > 修改数据库表
        > 优化了之前无脑使用查询sql
    > 2022-11-18 21:00
        > 修补export yhyauthorCode 转换链接引起的https_txt,异常问题
    > 2022-11-18 21:40
        > 新增加对 jd_lzkj_loreal_invite.js == 邀请入会有礼（lzkj_loreal）和 jd_jinggeng_showInviteJoin.js == 邀请入会赢好礼（京耕）脚本支持
    > 2022-11-19 21:00
        > 因多任务并发出现493问题暂时在零点设置延迟90秒(后面会优化)
        > 添加管理员权限请出群聊(未启用,只是开放了接口)
    > 2022-11-20 13:30
        > 弃用judge
        > 修改获取脚本的sql执行逻辑
        > 不清楚什么原因造成卡任务添加无关紧要输出
        > 卡任务未知
    > 2022-11-20 19:30
        > main_core方法使用多线程,不阻塞tg机器人交互
    > 2022-11-21 10:30
        > 对长连接以知异常明细划分 [Errno -3] Try again 异常不会再暂停10s
3.2版本(重新拉镜像)
        > 支持多容器
        > 修改青龙存储密钥方式
        > 前端页面提交修改
        > 添加提交青龙指令
        > 添加自动删除异常青龙功能
        > 登陆页面(暂时借用代理的登陆页面)
        > 更换容器和启动文件名称容器自动编译
        > 修复log显示不出来问题和js和css部分404问题
        > 493问题暂时没有修复
        > 修复在任务不执行而标记物添加问题
    2022-11-24 20:30
        > 修复群聊下非Administrator用户发送/id触发异常问题
        > 零点延迟 23秒 平常延迟 3秒
    2022-12-01 03:40(不保留文件更新)
        > 添加动态日志
        > 修复一些BUG
        > 检测用户提交的是否为ID
        > 更新数据库内容
    2022-12-01 14:00
        > 对 jd_wdz.js jd_wdzfd.js jd_wdz.py 进行不去重复处理
        > 修复线报jd_wdzfd.js中掺杂export问题
    2022-12-01 16:00(不保留文件更新)
        > 适配保护环境库脚本
    2022-12-02 20:00
        > 添加云端数据库，本次重启项目都会获取新的数据库
        > 修复日志500错误
    2022-12-07 18:30
        > 支持微定制转换URL
    2022-12-08 00:30
        > 修复微定制转换URL
    2022-12-08 02:00
        > 对多个相同参数值同一行只能识别一个问题
    2022-12-08 03:00
        > 修复sh类型链接跳过问题
    2022-12-10 02:00
        > 重启后保留1200秒之前的线报
    2022-12-20 00:40
        > 修补数据库和转换链接和船长脚本店铺抽豆
        > 转发线报的保留更新非转发的重启就行
    2022-12-20 21:21
        > 对接 jd_convert_json.py 店铺签到 https://github.com/XgzK/JD_annex/blob/master/jd_convert_json.py
        > 12个小时自动清理一次日志
    > 2022-12-30 03:51
        > 更换容器使用 python10 + nodejs
        > 使用 nuitka3 编译加密
    > 2023-1-4 1:09
        > 取消添加参数重启无法同步问题
        > 前端代码分离出来单独Web文件夹
3.3版本(不保留配置文件更新)
        解决493问题
        对同一脚本增加延迟时间
        不再直接修改配置文件,改成引入qlva.sh文件
        对 https://shop.m.jd.com/shop/lottery?shopId=585437 自动获取 venderId值
    23/1/12 10:08
        尝试修补队列任务不释放问题
```
### 插件
```text
添加解析 店铺抽豆 解析插件 com.Plugin.lottery
```