
# ⛓ [SELECT](https://programmers.co.kr/learn/courses/30/parts/17042)

[1] 모든 레코드 조회하기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59034)
```sql
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;
```
<br/>

[2] 역순 정렬하기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59035)
```sql
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```
<br/>

[3] 아픈 동물 찾기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59036)
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = "Sick";
```
<br/>

[4] 어린 동물 찾기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59037)
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != "Aged";
```
<br/>

[5] 동물의 아이디와 이름 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59403)
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```
<br/>

[6] 여러 기준으로 정렬하기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59404)
```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```
<br/>

[7] 상위 n개 레코드 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59405)
```sql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
```