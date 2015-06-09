# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from models import Reals, db_connect, create_reals_table


class StackPipeline(object):
    """ Stack Exchange pipeline for storing scraped items in the database """
    def __init__(self):
        """ Initialize database connection and sessionmaker """
        engine = db_connect()
        create_reals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save reals in database.
        This method is called for every item pipeline componenet."""
        session = self.Session()
        real = Reals(**item)

        try:
            session.add(real)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item
