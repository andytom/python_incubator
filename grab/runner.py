import logging
import spiders


#-- Constants ----------------------------------------------------------------#
SPIDERS = {
    'imdb': spiders.IMDBSpider,
    'mc': spiders.MetaCriticSpider,
}


#-- Main ---------------------------------------------------------------------#
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] %(levelname)s - %(message)s')

    logging.info("Starting to run some spiders.")
    for spider_name, spider in SPIDERS.items(): 
        logging.info("Starting to run '{}' spider.".format(spider_name))

        bot = spider(thread_number=8)
        res = bot.do_run()

        logging.info("Got {} Film(s) from '{}'.".format(len(res), spider_name))
        logging.info("Threw that data away!")
    logging.info("All Done.")
