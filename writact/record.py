from typing import Union, TypedDict
from datetime import datetime
from decimal import Decimal
import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class IRecord(TypedDict):
  timestamp: str
  action: str
  source: str
  base: str
  volume: str
  price: str
  counter: str
  fee: str
  feeccy: str
  comment: str

class Record:
  def __init__(self)->None:
    self.action:str = ''
    self.source:str = ''
    self.base:str = ''
    self.volume:Union[float,Decimal,str] = 0
    self.price:Union[float,Decimal,str] = ''
    self.counter:str = ''
    self.fee:Union[float,Decimal,str] = 0
    self.feeccy:str = ''
    self.comment:str = ''

  def __str__(self)->str:
    return self.get_cryptact_line()

  def fill_blank_non_use(self)->None:
    self.counter = 'JPY'
    self.fee = 0
    self.feeccy = 'JPY'

  @property
  def timestamp(self)->str:
    # YYYY/MM/DD HH:mm:ss
    timestamp_str = self._timestamp.strftime('%Y/%m/%d %H:%M:%S')
    return timestamp_str

  @timestamp.setter
  def timestamp(self,value:Union[int,str])->None:
    if(type(value) == str):
      try:
        self._timestamp = datetime.strptime('%Y/%m/%d %H:%M:%S')
      except(Exception) as e:
        raise(e)
    elif(type(value) == int):
      if(len(value)==13):
        value = value/1000
      self._timestamp = datetime.fromtimestamp(value)
    else:
      raise(Exception,"not supported value")

  @property
  def price(self)->str:
    return self._price

  @property
  def volume(self)->str:
    return self._volume

  @property
  def fee(self)->str:
    return self._fee

  @price.setter
  def price(self,value:int|str|Decimal):
    self._price = str(value)

  @volume.setter
  def volume(self,value:int|str|Decimal):
    self._volume = str(value)

  @fee.setter
  def fee(self,value:int|str|Decimal):
    self._fee = str(value)

  def get_datetime_from_timestamp(self)->datetime:
    return self._timestamp

  def insert_timestamp_from_iso(self,value)->None:
    self._timestamp = datetime.fromisoformat(value)

  def to_dict(self)->TypedDict[IRecord]:
    result = {'timestamp':self.timestamp,'action':self.action,'source':self.source,'base':self.base,'volume':self.volume,'price':self.price,'counter':self.counter,'fee':self.fee,'feeccy':self.feeccy,'comment':self.comment}
    return result

  def get_cryptact_line(self,demilita = ',')->str:
    result = demilita.join([self.timestamp,self.action,self.source,self.base,self.volume,self.price,self.counter,self.fee,self.feeccy,self.comment])
    return result