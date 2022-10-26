import json
import threading
import time

from flask_apscheduler import APScheduler

from conn.bot import bot
from conn.bot.getUpdate import GetUpdate
from conn.gheaders.Inspector import Check
from conn.gheaders.conn import read_yaml
from conn.ql import ql
from conn.gheaders import logger
from conn.ql.ql_token import token_main
from conn.sql.addsql import dele_datati
from conn.txt.txt_zli import tx_revise
from conn.web.ql_web import run_web
from conn.fo.core import adaptation

scheduler = APScheduler()
yml = read_yaml()


@scheduler.task('interval', id='ti_ck', days=1)
def ti_ck():
    """
    定时清空数据库
    :return:
    """
    dele_datati()


@scheduler.task('interval', id='timing_ck', days=15)
def timing_ck():
    """
    设置每半个月获取一次新的ck,青龙作者是的是一个月保质期，不过这里设置为半个月
    :return: 0 or -1
    """
    for i in range(3):
        ck = token_main()
        if ck == 0:
            logger.write_log("新的Bearer添加成功token_main")
            return 0
        logger.write_log("新的Bearer添加失败, 30s后再次获取")
        time.sleep(30)
    logger.write_log("新的Bearer添加失败停止执行后面步骤")
    return -1


@scheduler.task('interval', id='list', minutes=30)
def ql_crons():
    """
    获取青龙任务列表
    :return: 0 or -1
    """
    try:
        js = ql.crons()
        with open(yml['json'], mode='wt', encoding='utf-8') as f:
            json.dump(js, f, ensure_ascii=False)
            f.close()
        return 0
    except Exception as e:
        logger.write_log(f'获取列表异常,{e}')
        return -1


@bot.message_handler(func=lambda m: True)
def ordinary(message):
    """
    私聊群聊消息
    :param message:
    :return:
    """
    # print(message)
    tx_revise(message.text)


# @bot.channel_post_handler()
# def ordi(message):
#     """
#     频道消息
#     :param message:
#     :return:
#     """
#     print(message)


def mai():
    """
    执行主要程序
    :return:
    """
    tf = True
    while tf:
        ym = read_yaml()
        if ym['ip'] != '' and ym['Client ID'] != '' and ym['Client Secret'] != '':
            # 创建一些路径和数据库
            Check().cpath()
            # 把版本号传递给青龙
            ql.Version = adaptation()
            # 获取必备青龙参数
            ck = timing_ck()
            cr = ql_crons()
            if ck == 0 and cr == 0:
                logger.write_log("连接青龙端成功")
                # 结束循环
                tf = False
            else:
                logger.write_log("连接青龙端失败,定时任务不启动,请重新输入")
                # n秒检测一次
                time.sleep(20)
        else:
            logger.write_log("没有检测到青龙必要参数存在不继续向下执行后续功能")
            # n秒检测一次
            time.sleep(20)
    # 启动定时任务
    scheduler.start()


if __name__ == '__main__':
    # 使用多线程防止任务阻塞
    t1 = threading.Thread(target=run_web)
    t1.start()
    mai()
    # 用来检测用户用什么方式
    yml = read_yaml()
    if yml['TG_API_HOST'] == '' or yml['Proxy']:
        logger.write_log("你调用了官方封装的TG机器人方法库")
        # 如果用户没有填写反代或没有设置代理将调用第三方封装机器人
        bot.infinity_polling()
    else:
        logger.write_log("调用了开发者自己写的TG接口")
        tg_mes = GetUpdate()
        while True:
            try:
                tg_ms = tg_mes.get_long_link()
                # 消息不为空和没有异常
                if tg_ms['ok']:
                    if tg_ms["result"]:
                        # 确认收到消息
                        tg_mes.data['offset'] = tg_ms["result"][len(tg_ms["result"]) - 1]['update_id'] + 1
                        for result in tg_ms["result"]:
                            # message 一般是 私聊 群消息 加入群组 and 是消息而非加入群组
                            if 'message' in result and "chat" in result['message']:
                                # 私聊消息
                                if result['message']['chat']['type'] == 'private':
                                    if 'text' in result['message']:
                                        logger.write_log(f"收到私聊消息内容 {result['message']['text']}")
                                        tx_revise(result['message']['text'])
                                # 群消息
                                elif result['message']['chat']['type'] == 'supergroup':
                                    if 'text' in result['message']:
                                        tx_revise(result['message']['text'])
                            # 频道消息
                            elif 'channel_post' in result:
                                if result['channel_post']['chat']['type'] == 'channel':
                                    if 'text' in result['channel_post']:
                                        tx_revise(result['channel_post']['text'])
                            else:
                                pass
                                # print(result)
                    # else:
                    #     print("收到消息为空")
                else:
                    logger.write_log(f"异常消息 {tg_ms['result']} 触发异常停止10秒")
                    time.sleep(10)
            except Exception as e:
                logger.write_log(f"个人开发类异常: {e}")

