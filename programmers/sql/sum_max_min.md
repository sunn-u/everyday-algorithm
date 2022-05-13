# ⛓ [SUM, MAX, MIN](https://programmers.co.kr/learn/courses/30/parts/17043)

[1] 최댓값 구하기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59415)
```sql
SELECT MAX(DATETIME) AS "시간"
FROM ANIMAL_INS;
```
```sql
SELECT DATETIME AS "시간"
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;
```
<br/>

[2] 최솟값 구하기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59038?language=mysql)
```sql
SELECT MIN(DATETIME) AS "시간"
FROM ANIMAL_INS;
```
```sql
SELECT DATETIME AS "시간"
FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1;
```
<br/>

[3] 동물 수 구하기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59406)
```sql
SELECT COUNT(*) AS "count"
FROM ANIMAL_INS;
```
<br/>

[4] 중복 제거하기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59408)
```sql
SELECT COUNT(DISTINCT NAME) AS "count"
FROM ANIMAL_INS;
```
