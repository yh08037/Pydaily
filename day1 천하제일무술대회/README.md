# 천하제일무술대회

## 문제

천하제일무술대회에 n명의 선수가 참가했습니다. 대회 진행은 2인1조로 토너먼트 형식으로 진행되어 한명의 최종 승자가 나올 때까지 진행됩니다.

각 선수들에게 능력치는 숫자로 나타내어져 능력치가 더 큰 선수가 승리합니다.

매 라운드 명단의 가장 마지막에 있는 선수는 부전승 처리될 때, 토너먼트 경기의 결과를 피라미드 형태로 출력하는 프로그램을 작성하시오.

## 입력

천하제일무술대회에 참가한 선수의 수 n을 입력받고, n명의  능력치를 입력받습니다.  

## 출력

경기 진행 과정을 역순으로 출력합니다.

## 입력 예시 1

4

A 10

B 5

C 7

D 9

<br>

## 출력 예시 1

A

A D

A B C D

<br>

해설 : 입력받은 순서대로 (A,B), (C,D) 로 짝지어져 A와 D가 준결승에 진출하였습니다.

<br>

## 입력 예시 2

7

A 10

B 5

C 7

D 9

E 3

F 6

G 12

<br>

## 출력 예시 2

G

A G

A D F G

A B C D E F G 

해설 : 선수 G가 부전승으로 준준결승에 진출하였습니다.



