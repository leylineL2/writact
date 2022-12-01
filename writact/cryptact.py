from typing import List
from .record import Record
from decimal import Decimal
import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class CryptactTool:
	def __init__(self) -> None:
		self.records:List[Record] = []


	def print_records(self) -> str:
		print('Timestamp,Action,Source,Base,Volume,Price,Counter,Fee,FeeCcy')
		for record in self.records:
			print(record)


	def mining(self,timestamp:int|str,base:str,volume:float,source:str='',price:float|None=None,counter:str='JPY',fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'MINING'
		r.source = source
		r.base = base
		r.volume = volume
		if (price != None):
			r.price = price
		r.counter = counter
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)


	def sendfee(self,timestamp:int|str,base:str,volume:float,source:str='',price:float|None=None):
		r = Record()
		r.timestamp = timestamp
		r.action = 'SENDFEE'
		r.source = source
		r.base = base
		r.volume = volume
		if (price != None):
			r.price = price
		r.fill_blank_non_use()
		self.records.append(r)



	def bonus(self,timestamp:int|str,base:str,volume:float,source:str='',price:float|None=None):
		r = Record()
		r.timestamp = timestamp
		r.action = 'BONUS'
		r.source = source
		r.base = base
		r.volume = volume
		if (price != None):
			r.price = price
		r.fill_blank_non_use()
		self.records.append(r)


	def lend(self,timestamp:int|str,base:str,volume:float,source:str='',price:float|None=None,fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'LEND'
		r.source = source
		r.base = base
		r.volume = volume
		if (price != None):
			r.price = price
		r.fill_blank_non_use()
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)


	def lending(self,timestamp:int|str,base:str,volume:float,source:str='',price:float|None=None,fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'LEND'
		r.source = source
		r.base = base
		r.volume = volume
		if (price != None):
			r.price = price
		r.fill_blank_non_use()
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)


	def recover(self,timestamp:int|str,base:str,volume:float,source:str='',price:float|None=None,fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'RECOVER'
		r.source = source
		r.base = base
		r.volume = volume
		if (price != None):
			r.price = price
		r.fill_blank_non_use()
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)


	def staking(self,timestamp:int|str,base:str,volume:float,source:str='',price:float|None=None,fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'STAKING'
		r.source = source
		r.base = base
		r.volume = volume
		if (price != None):
			r.price = price
		r.fill_blank_non_use()
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)


	def loss(self,timestamp:int|str,base:str,volume:float,source:str='',feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'LOSS'
		r.source = source
		r.base = base
		r.volume = volume
		r.price = 0
		r.fill_blank_non_use()
		r.fee = 0
		r.feeccy = feeccy
		self.records.append(r)


	def borrow(self,timestamp:int|str,base:str,volume:float,source:str='',counter:str='JPY',fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'BORROW'
		r.source = source
		r.base = base
		r.volume = volume
		r.counter = counter
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)

	def return_(self,timestamp:int|str,base:str,volume:float,source:str='',counter:str='JPY',fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'RETURN'
		r.source = source
		r.base = base
		r.volume = volume
		r.counter = counter
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)		


	def reduce(self,timestamp:int|str,base:str,volume:float,source:str='',counter:str='JPY',fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'REDUCE'
		r.source = source
		r.base = base
		r.volume = volume
		r.counter = counter
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)		

	
	def cash(self,timestamp:int|str,counter:str,fee:float=float(0),source:str=''):
		r = Record()
		r.timestamp = timestamp
		r.action = 'CASH'
		r.source = source
		r.base = counter
		r.volume = 0
		r.price = 0
		r.counter = counter
		r.fee = fee
		r.feeccy = counter
		self.records.append(r)


	def buy(self,timestamp:int|str,base:str,volume:float,counter_amount:float,source:str='',counter:str='JPY',fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'BUY'
		r.source = source
		r.base = base
		r.volume = volume
		r.price = Decimal(f'${counter_amount}')/Decimal(f'${volume}')
		r.counter = counter
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)


	def sell(self,timestamp:int|str,base:str,volume:float,counter_amount:float,source:str='',counter:str='JPY',fee:float=float(0),feeccy:str='JPY'):
		r = Record()
		r.timestamp = timestamp
		r.action = 'SELL'
		r.source = source
		r.base = base
		r.volume = volume
		r.price = Decimal(f'${counter_amount}')/Decimal(f'${volume}')
		r.counter = counter
		r.fee = fee
		r.feeccy = feeccy
		self.records.append(r)
		

	def defifee(self,timestamp:int|str,base:str,volume:float,source:str='',price:float|None=None):
		r = Record()
		r.timestamp = timestamp
		r.action = 'DEFIFEE'
		r.source = source
		r.base = base
		r.volume = volume
		if (price != None):
			r.price = price
		r.fill_blank_non_use()
		self.records.append(r)
