-- 建立 User 資料表
CREATE TABLE User (
  u_id int PRIMARY KEY,
  name varchar(50),
  city varchar(50),
  register_date date
);

-- 建立 Restaurants 資料表
CREATE TABLE Restaurants (
 r_id INT PRIMARY KEY,
 r_name VARCHAR(100),
 category VARCHAR(50)
);

-- 建立 Orders 資料表
CREATE TABLE Orders (
 o_id INT PRIMARY KEY,
 u_id INT,
 r_id INT,
 amount INT,
 status VARCHAR(20),
 order_date DATE,
 FOREIGN KEY (u_id) REFERENCES User(u_id) -- 建立連動關係
);

INSERT INTO User VALUES
(1,'Takeshi','Taipei','2023-01-15'),
(2,'GodTone','Taoyuan','2023-02-28'),
(3,'Yui','Taipei','2023-03-10'),
(4,'Ming','Taichung','2023-10-01'),
(5,'Magic_Grandma','Tainan','2023-11-11'),
(6,'Jay','New_Taipei','2023-11-20'),
(7,'Chiling','Tainan','2023-11-25'),
(8,'Kuan_Chang','New_Taipei','2023-12-01'),
(9,'Miku','Taipei','2023-12-05'),
(10,'Roland','Taichung','2023-12-10');

INSERT INTO Restaurants VALUES
(101,'MacD','Fast_Food'),
(102,'Fried_Chicken','Midnight_Snack'),
(103,'Grandma_Buffet','Bento'),
(104,'Dark_Magic_Kitchen','Midnight_Snack'),
(105,'Healthy_Boiled','Healthy'),
(106,'Happy_Cola','Beverage'),
(107,'Sad_Bitter_Melon','Beverage'),
(108,'Michelin_French','Fine_Dining');

INSERT INTO Orders VALUES
(1001,1,102,150,'Completed','2023-12-01'),
(1002,2,103,250,'Completed','2023-12-02'),
(1003,3,101,1500,'Completed','2023-12-02'),
(1004,4,104,65,'Cancelled','2023-12-03'),
(1005,1,103,300,'Completed','2023-12-03'),
(1006,5,101,199,'Completed','2023-12-04'),
(1007,2,102,200,'Cancelled','2023-12-05'),
(1008,1,104,800,'Completed','2023-12-06'),
(1009,6,105,120,'Completed','2023-12-06'),
(1010,7,106,55,'Completed','2023-12-07'),
(1011,3,108,5000,'Completed','2023-12-07'),
(1012,4,102,180,'Delivering','2023-12-08'),
(1013,5,103,220,'Completed','2023-12-08'),
(1014,6,101,350,'Completed','2023-12-09'),
(1015,1,108,4500,'Cancelled','2023-12-09'),
(1016,2,105,150,'Completed','2023-12-10'),
(1017,7,104,80,'Completed','2023-12-10'),
(1018,3,102,210,'Completed','2023-12-11'),
(1019,4,106,60,'Cancelled','2023-12-11'),
(1020,6,103,250,'Completed','2023-12-12');

-- 確認資料表內容
-- SELECT* FROM USER
-- SELECT* FROM Restaurants
-- SELECT* FROM Orders