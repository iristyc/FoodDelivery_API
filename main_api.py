from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db_connection import SessionLocal, Order, User
from typing import Optional # 記得在最上面 import 這個
import datetime

app = FastAPI()

# 取得資料庫 Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1. 下單功能 (Create) 
@app.post("/orders", summary="新增訂單")
def create_new_order(o_id: int, u_id: int, r_id: int, amount: int, db: Session = Depends(get_db)):
    # 新增訂單
    new_order = Order(
        o_id=o_id,
        u_id=u_id,
        r_id=r_id,
        amount=amount,
        status="pending",
        order_date=datetime.date.today()
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "下單成功！資料已寫入 MySQL", "data": new_order}

# 2. 查詢（Read）
@app.get("/users", summary="查詢顧客資料")
def read_users(u_id: Optional[int] = None, name: Optional[str] = None, db: Session = Depends(get_db)):
    
    query = db.query(User)
    
    # 如果有輸入顧客編號，就增加篩選條件
    if u_id:
        query = query.filter(User.id == u_id)
    
    # 如果有輸入姓名，就增加模糊搜尋條件
    if name:
        query = query.filter(User.name.contains(name))
    
    # 執行查詢並回傳結果
    users = query.all()
    return users

# 3. 修改（Update）
@app.put("/orders/{o_id}", summary="修改訂單資料")
def update_order(o_id: int, status: str, db: Session = Depends(get_db)):
    # 找該筆訂單
    db_order = db.query(Order).filter(Order.o_id == o_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="找不到這筆訂單，無法修改")
    
    # 修改金額與狀態
    db_order.status = status
    
    db.commit()
    db.refresh(db_order)
    return {"message": "訂單更新成功！", "data": db_order}

# 4. 刪除訂單（Delete）
@app.delete("/orders/{o_id}", summary="刪除訂單資料")
def delete_order(o_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.o_id == o_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="找不到這筆訂單，無法刪除")
    
    db.delete(db_order)
    db.commit()
    return {"message": f"訂單 {o_id} 已成功刪除"}