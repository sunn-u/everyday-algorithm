
# ⛓ [IS NULL](https://programmers.co.kr/learn/courses/30/parts/17045)

[1] 이름이 없는 동물의 아이디 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59039)
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL;
```
<br/>

[2] 이름이 있는 동물의 아이디 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59407)
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID;
```
<br/>

[3] NULL 처리하기 : [Link](https://programmers.co.kr/learn/courses/30/lessons/59410)
```sql
SELECT ANIMAL_TYPE, IF(NAME IS NULL, "No name", NAME) AS "NAME", SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;
```
```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS "NAME", SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;
```