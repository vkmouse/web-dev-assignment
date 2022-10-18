## SQL Assignment

- [要求三：SQL CRUD](#要求三sql-crud)
  - [INSERT](#insert)
  - [SELECT 取得所有](#select-取得所有)
  - [SELECT 取得所有，並由近到遠排序 time 欄位](#select-取得所有並由近到遠排序-time-欄位)
  - [SELECT 指令取得第 2 ~ 4，並由近到遠排序 time 欄位](#select-指令取得第-2--4並由近到遠排序-time-欄位)
  - [SELECT 指令取得 username 是 test](#select-指令取得-username-是-test)
  - [SELECT 指令取得 username 是 test 且 password 是 test](#select-指令取得-username-是-test-且-password-是-test)
  - [UPDATE 指令更新 username 是 test 改為 tese2](#update-指令更新-username-是-test-改為-tese2)
- [要求四：SQL Aggregate Functions](#要求四sql-aggregate-functions)
  - [取得資料總數](#取得資料總數)
  - [取得 follower_count 總和](#取得-follower_count-總和)
  - [取得 follower_count 平均](#取得-follower_count-平均)
- [要求五：SQL JOIN (Optional)](#要求五sql-join-optional)
  - [建立新資料表 message](#建立新資料表-message)
  - [取得所有留⾔，須包含姓名](#取得所有留須包含姓名)
  - [取得 username 是 test 的所有留⾔，須包含姓名](#取得-username-是-test-的所有留須包含姓名)
  - [取得 username 是 test 的所有留⾔平均按讚數](#取得-username-是-test-的所有留平均按讚數)

### 要求三：SQL CRUD
#### INSERT
```sql
INSERT INTO member (name, username, password)
VALUES ('Test', 'test', 'test');
INSERT INTO member (name, username, password)
VALUES ('2', '2', '2');
INSERT INTO member (name, username, password)
VALUES ('3', '3', '3');
INSERT INTO member (name, username, password)
VALUES ('4', '4', '4');
INSERT INTO member (name, username, password)
VALUES ('5', '5', '5');
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/1.png)

#### SELECT 取得所有
```sql
SELECT * FROM member;
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/2.png)

#### SELECT 取得所有，並由近到遠排序 time 欄位
```sql
SELECT * FROM member ORDER BY time DESC;
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/3.png)

#### SELECT 指令取得第 2 ~ 4，並由近到遠排序 time 欄位
```sql
SELECT * FROM member ORDER BY time DESC LIMIT 1,3;
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/4.png)

#### SELECT 指令取得 username 是 test
```sql
SELECT * FROM member WHERE username = 'test';
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/5.png)

#### SELECT 指令取得 username 是 test 且 password 是 test
```sql
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/6.png)

#### UPDATE 指令更新 username 是 test 改為 tese2
```sql
UPDATE member SET username = 'test' WHERE username = 'test2';
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/7.png)

### 要求四：SQL Aggregate Functions

#### 取得資料總數
```sql
SELECT COUNT(follower_count) FROM member;
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/8.png)

#### 取得 follower_count 總和
```sql
SELECT SUM(follower_count) FROM member;
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/9.png)

#### 取得 follower_count 平均
```sql
SELECT AVG(follower_count) FROM member;
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/10.png)

### 要求五：SQL JOIN (Optional)

#### 建立新資料表 message
```sql
CREATE TABLE message (
    id          BIGINT        AUTO_INCREMENT,
    member_id   BIGINT        NOT NULL,
    content     VARCHAR(255)  NOT NULL,
    like_count  INT UNSIGNED  NOT NULL DEFAULT 0,
    time        DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY(member_id) REFERENCES member(id)
);
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/11.png)

```sql
INSERT INTO message (member_id, content, like_count)
VALUES 
    (1, 'Today is a good day', 5),
    (1, 'Let\'s learn MySQL for a whole day', 10),
    (2, 'No, don\'t do that', 2),
    (3, 'You will save into database,', 999),
    (3, 'if you learning for a whole day', 998),
    (4, 'Hahaha', 0);
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/12.png)

#### 取得所有留⾔，須包含姓名
```sql
SELECT
    member.name,
    message.content,
    message.time
FROM message
INNER JOIN member
    ON message.member_id=member.id;
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/15.png)

#### 取得 username 是 test 的所有留⾔，須包含姓名
```sql
SELECT
    member.name,
    message.content,
    message.time
FROM message
INNER JOIN member
    ON message.member_id=member.id
WHERE member.username='test';
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/13.png)

#### 取得 username 是 test 的所有留⾔平均按讚數
```sql
SELECT 
    AVG(message.like_count)
FROM message
INNER JOIN member
    ON message.member_id=member.id
WHERE member.username='test';
```
![1](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/week-5/img/14.png)
