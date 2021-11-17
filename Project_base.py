from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:///Projects.db')
Base = declarative_base()

class Projektai(Base):
    __tablename__ = 'Projektai'
    id = Column(Integer, primary_key=True)
    partner = Column('Partneris', String)
    address = Column('Adresas', String)
    wind_qty = Column('Langu_kiekis', Integer)
    wind_h = Column('Langu_ilgis', Float)
    wind_w = Column('Langu_plotis', Float)
    wind_sqm = Column('Langu_plotas', Float)
    door_qty = Column('Duru_kiekis', Integer)
    door_h = Column('Duru_ilgis', Float)
    door_w = Column('Duru_plotis', Float)
    door_sqm = Column('Duru_plotas', Float)
    fas_sqm = Column('Fasado_plotas', Float)
    paint_sqm = Column('Dazomas_plotas', Float)
    paint = Column('Dazai', String)
    pack_volume = Column('Pakuotes_dydis', Float)
    base_qty = Column('Grunto_kiekis', Integer)
    base_price = Column('Grunto_kaina', Float)
    paint_qty = Column('Dazu_kiekis', Float)
    paint_price = Column('Dazu_kaina', Float)
    project_price = Column('Projekto_kaina', Float)
    date = Column('Data', DateTime, default=datetime.datetime.today())

    def __init__(self, partner, address, wind_qty, wind_h, wind_w, wind_sqm, door_qty, door_h, door_w,
                 door_sqm, fas_sqm, paint_sqm, paint, pack_volume, base_qty, base_price, paint_qty,
                 paint_price, project_price):
        self.partner = partner
        self.address = address
        self.wind_qty = wind_qty
        self.wind_h = wind_h
        self.wind_w = wind_w
        self.wind_sqm = wind_sqm
        self.door_qty = door_qty
        self.door_h = door_h
        self.door_w = door_w
        self.door_sqm = door_sqm
        self.fas_sqm = fas_sqm
        self.paint_sqm = paint_sqm
        self.paint = paint
        self.pack_volume = pack_volume
        self.base_qty = base_qty
        self.base_price = base_price
        self.paint_qty = paint_qty
        self.paint_price = paint_price
        self.project_price = project_price

    def __repr__(self):
        return f'{self.id} {self.partner} {self.address}, {self.paint_sqm}, {self.paint}, {self.project_price}, {self.date}'


Base.metadata.create_all(engine)
