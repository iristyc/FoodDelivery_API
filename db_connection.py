from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 資料庫連線設定
# 請將"你的密碼"改成自己的 MySQL 密碼（上、下引號需保留）
DB_PASSWORD = "你的密碼" 
DB_NAME = "delivery_db"

URL = f"mysql+pymysql://root:{DB_PASSWORD}@localhost/{DB_NAME}"
#URL = "mysql+pymysql://root:malay727@127.0.0.1:3306/delivery_db"

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    u_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    city = Column(String(50))
    register_date = Column(Date)

class Order(Base):
    __tablename__ = "Orders"
    o_id = Column(Integer, primary_key=True)
    u_id = Column(Integer, ForeignKey("User.u_id"))
    r_id = Column(Integer)
    amount = Column(Integer)
    status = Column(String(20))
    order_date = Column(Date)