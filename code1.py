from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id_publ = Column('id_publ', Integer, primary_key=True)
    name = Column('name', String(length=50))

    def __init__(self, id_publ, name):
        self.id_publ = id_publ
        self.name = name

    def __repr__(self):
        return f'({self.id_publ}) {self.name}'


class Book(Base):
    __tablename__ = 'book'
    id_book = Column('id_book', Integer, primary_key=True)
    title = Column('title', String(length=100))
    id_publ = Column('id_publ', Integer, ForeignKey('publisher.id_publ'))

    def __repr__(self):
        return f'{self.title}'


    def __init__(self, id_book, title, id_publ):
        self.id_book = id_book
        self.title = title
        self.id_publ = id_publ


class Shop(Base):
    __tablename__ = 'shop'
    id_shop = Column('id_shop', Integer, primary_key=True)
    name = Column('name', String(length=50))

    def __init__(self, id_shop, name):
        self.id_shop = id_shop
        self.name = name

    def __repr__(self):
        return f'{self.name}'



class Stock(Base):
    __tablename__ = 'stock'
    id_stock = Column('id_stock', Integer, primary_key=True)
    id_book = Column('id_book', Integer, ForeignKey('book.id_book'))
    id_shop = Column('id_shop', Integer, ForeignKey('shop.id_shop'))
    count = Column('count', Integer)

    def __init__(self, id_stok, id_book, id_shop, count):
        self.id_stock = id_stok
        self.id_book = id_book
        self.id_shop = id_shop
        self.count = count


class Sale(Base):
    __tablename__ = 'sale'
    id_price = Column('id_price', Integer, primary_key=True)
    price = Column('price', Integer)
    date_sale = Column('date_sale', Date)
    id_stock = Column('id_stock', Integer, ForeignKey('stock.id_stock'))
    count = Column('count', Integer)

    def __init__(self, id_price, price, date_sale, id_stock, count):
        self.id_price = id_price
        self.price = price
        self.date_sale = date_sale
        self.id_stock = id_stock
        self.count = count

    def __repr__(self):
        return f'{self.price} | {self.date_sale}'



engine = create_engine('postgresql://postgres:Polina3108@localhost:5432/dbalchemy')
# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
#
# publ_1 = Publisher(1,'Пушкин')
# publ_2 = Publisher(2,'Чехов')
# publ_3 = Publisher(3, 'Толстой')
#
# session.add(publ_1)
# session.add(publ_2)
# session.add(publ_3)
# session.commit()
#
# book_1 = Book(1, 'Капитанская дочка', 1)
# book_2 = Book(2, 'Руслан и Людмила', 1)
# book_3 = Book(3, 'Война и Мир', 3)
# book_4 = Book(4, 'Вишневый сад', 2)
#
# session.add(book_1)
# session.add(book_2)
# session.add(book_3)
# session.add(book_4)
# session.commit()
#
# shop_1 = Shop(1, 'Буквоед')
# shop_2 = Shop(2, 'Буква А')
#
# session.add(shop_1)
# session.add(shop_2)
#
# session.commit()
#
# stock_1 = Stock(1, 1, 1, 1)
# stock_2 = Stock(2, 2, 1, 1)
# stock_3 = Stock(3, 3, 2, 1)
# stock_4 = Stock(4, 4, 2, 1)
#
# session.add(stock_1)
# session.add(stock_2)
# session.add(stock_3)
# session.add(stock_4)
#
# session.commit()
#
# sale_1 = Sale(1, 300, '11.09.2021', 1, 1)
# sale_2 = Sale(2, 200, '11.09.2021', 2, 1)
# sale_3 = Sale(3, 100, '11.09.2021', 3, 1)
# sale_4 = Sale(4, 150, '11.09.2021', 4, 1)
#
# session.add(sale_1)
# session.add(sale_2)
# session.add(sale_3)
# session.add(sale_4)
#
# session.commit()

def get_shops()
    result = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale)
    if zapros.isdigit():
        a = result.filter(Publisher_id == zapros).all()
    else:
        a = result.filter(Publisher_name == zapros).all()
    for book_title, shop_name, sale_price, sale_date in a:
                print (f'{book_title: <40} | {shop_name: <10} | {sale_price: <8} | {sale_date.strftime('%d-%m-%Y')}')

if __name__ == '__main__':
    zapros = input('Введите имя или идентификатор издателя: ')
    get_shops(zapros)

session.close()
