from concurrency.thread_pool import threads
from ui.controller import display
from scanner.network import network_scan
from scanner.port import port_scan
from utils.ip import ip_range
from config.logger_config import setup_logger
from utils.decorators import time_decorator
from utils.exporter import save_result
import typer

app = typer.Typer()
logger = setup_logger()

@app.command()
@time_decorator
def sn(ip: str,
        mw: int = 100,
        color: bool = typer.Option(False, "-c/-C"),
        animation: bool= typer.Option(True, "-a/-A"),
        save: bool= typer.Option(True, "-s/-S"),
        ):

    try:

        logger.info("get ip list")
        ip_list = ip_range(ip)
        logger.info("success get ip list")

        logger.info("send tcp connect to ip list with thread")

        resulte1 = threads(network_scan,mw,ip_list)
        resulte2 = threads(network_scan,mw,ip_list)
        resulte3 = threads(network_scan,mw,ip_list)

        all_resulte = resulte1+resulte2+resulte3

        resulte = set(all_resulte)

        if save:
            logger.info("start save resulte")
            save_result("exporter",resulte,ip)
            logger.info("success save resulte")

        logger.info("success search process")

        logger.info("start display resulte")
        display(list(resulte),color,animation)
        logger.info("program finished")

    except ValueError as e:

        logger.debug(f"ValueError : {e}")
        logger.info("ValueError you enter a value not corect")

@app.command()
@time_decorator
def sp(ip: str,
       mw: int = 100,
       color: bool = typer.Option(False, "-c/-C"),
       animation: bool= typer.Option(True, "-a/-A"),
       pr: str= "1,1024",
       pl: str= "1,2",
       po: str= "1",
       save: bool= typer.Option(True, "-s/-S")
       ):

    try:

        logger.info("prepation port list")
        start, end = map(int, pr.split(","))

        list1 = list(range(start,end))
        p_list = [ int(p) for p in pl.split(",") ]

        if len(po) == 1:
            p_list.append(int(po))

        all_list = list1+p_list

        port_list =set(all_list)
        logger.info("success preparation port list")

        logger.info("setup lambda")
        port_lambda = lambda p: port_scan(ip,p)
        logger.info("lambda setup success")

        logger.info("send to ports")
        resulte = threads(port_lambda,mw,list(port_list))
        logger.info("all list port finished")

        if save:
            logger.info("start save resulte")
            save_result("exporter",resulte,ip)
            logger.info("success save resulte")

        display(list(resulte),color,animation)
        logger.info("programe success")

    except ValueError as e:

        logger.debug(f"ValueError : {e}")
        logger.info("ValueError you enter a value not corect")



app()
