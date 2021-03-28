# Alien Invasion 

![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/anishLearnsToCode/alien-invasion)
[![license](https://img.shields.io/badge/LICENSE-MIT-<COLOR>.svg)](LICENSE)
![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

This game has been built as part of the 
[Python Crash Course](https://github.com/anishLearnsToCode/books/blob/master/python/python-crash-course.pdf) 📘 Book. 
For more python books [see here](https://github.com/anishLearnsToCode/books/tree/master/python).

## Running the game
Clone this project into your machine and install __pygame__ module globally.
```bash
git clone https://github.com/anishLearnsToCode/alien-invasion
pip install p  ygame
``` 

enter project and run the driver  file
```bash
cd alien-invasion
python driver.py 
```

Enjoy 😃👾

#### 푸로젝트 기간 2020.10 ~ 2020.12

### [최종 보고서 보기](https://docs.google.com/document/d/1Pdg2EwLL1hMD4CB2dCX6difQQCKKeXRRjbvABmEq1T4/edit) 
### 1) 프로젝트의 목적

본 프로젝트는 게임 관련 오픈 소스 프로젝트인 Alien Invasion을 분석하여 수정하거나 필요한 기능을 추가로 구현한다. 프로젝트 수행을 통해 오픈소스(Github)를 활용한 경험을 쌓고 팀원과의 협동심을 기르고 보고서 작성과 발표 능력을 향상시키는 게 목적이다.

   
### 2) 프로젝트의 기대효과
  -   사용자가 여가시간에 취미로 즐길 수 있는 게임 구현
  -  부족하다고 생각한 기능을 수정 및 추가로 구현하여 사용자가 게임을 쉽고 재미있게 플레이 가능

### 3) 프로젝트팀 구성원 역할

 - 권도엽 : 여러가지 색상 에일리언 추가 및 난이도별 생성되는 에일리언 수와 속도 설정 
 - 김현중 : 게임 난이도(East, Normal, Hard)추가 , 특정 에일리언 격추시 발생하는 효과 이벤트 설정, info 화면 추가 , 보고서 작성
 - 이승민 : 게임 일시정지 기능 BGN, 총알 격추시 효과음 추가, 발표

 - 사용 기술
- Pygame
pygame은 비디오게임을 작성하기 위해 고안된 python 모듈의 크로스 플랫폼 세트이다. 여기에는 python 프로그래밍 언어와 함께 사용하도록 설계된 컴퓨터 그래픽 및 사운드 라이브러리가 포함된다.

  - Sys
   Sys는 인터프리터에 의해 사용되거나 유지되는 일부 변수와 인터프리터와 강하게 상호 작용하는 함수에 대한 액세스를 제공한다.

  - Time
 Time은 다양한 시간 관련 함수를 제공한다. Alien Invasion에서는 Sleep 함수를 사용하기 위해 사용되었다.
 
 
### 4) 프로젝트 방향 
     
  문제점 
    - 스테이지를 클리어하여도 변하는 것이 없이 라이프가 없어질 때까지 반복한다. 
    - 중간에 멈추는 방법이 없다.
    - 게임에서 중요한 BGM이 없어 조용하고 건조하여 지루하게 느껴진다.

 개선점
    - 중간에 색이 다른 UFO를 배치하여 추가 점수, 라이프, 미사일 개수를 늘려주는 특수 UFO를 배치한다.
    - Esc 버튼을 누르면 중간에 멈출 수 있도록 한다.
    - 시작할 때 난이도를 조절할 수 있도록 하여 사용자에게 긴장감을 줄 수 있도록 한다.
    - 게임에 어울리는 BGM을 삽입한다.

  다양한 색의 UFO 이미지 파일을 만들고 UFO에 어떤 아이템을 추가할 것인지를 정하고 난이도 조절을 어떻게 할 것인지 정해야 한다. 해당 게임과 어울리는 BGM을 찾는다. 이러한 공개 소프트웨어의 문제점을 찾고 수정하여 개선하는 과정을 통하여 공개 소프트웨어를 이해할 수 있도록 한다.

     
### 5) 프로젝트 수행시 제약사항
  - 조원이 3명으로  인원이 부족하다.
  - 적절한 인원 배치와 꾸준한 소통을 통해 이를 해결할 수 있도록 한다. 

### 프로젝트 개선점

![image](https://user-images.githubusercontent.com/70426440/112716660-05497d00-8f2b-11eb-8e1c-6e34b0f1e4ec.png)
![image](https://user-images.githubusercontent.com/70426440/112716672-10041200-8f2b-11eb-9957-9a9337edbbb2.png)


### 실행 초기화면 
![image](https://user-images.githubusercontent.com/70426440/112716679-172b2000-8f2b-11eb-90c1-d007f0b784ea.png)
- 게임 플레이 전에 난이도를 선택하여 플레이 하거나 info 버튼을 눌러 게임설명을 볼 수있다.

    
### info 화면
![image](https://user-images.githubusercontent.com/70426440/112716702-55c0da80-8f2b-11eb-9974-679884cae4bd.png)
- Alien Invasion 게임에 대한 간단한 설명과 게임 동작 방법을 설명해준다.

- Play 버튼을 눌러 게임을 실행하면 ufo가 좌우로 움직이면서 내려온다. 사용자는 방향키와 스페이스 바를 이용하여 자신의 우주선을 조종하여 ufo를 제거한다.

### info 두번째 화면
![image](https://user-images.githubusercontent.com/70426440/112716710-5c4f5200-8f2b-11eb-98a1-cbfee2c32552.png)


### 게임 실행화면
![image](https://user-images.githubusercontent.com/70426440/112716719-67a27d80-8f2b-11eb-9411-45af78a2c2d9.png)

- Play 버튼을 눌러 게임을 실행하면 ufo가 좌우로 움직이면서 내려온다. 사용자는 방향키와 스페이스 바를 이용하여 자신의 우주선을 조종하여 ufo를 제거한다.

### 게임 일시정지 화면 
![image](https://user-images.githubusercontent.com/70426440/112716723-6ffab880-8f2b-11eb-8455-3b100febc7f0.png)
- 게임 플레이 도중 ESC 버튼을 눌러 게임을 일시정지하고 메인화면으로 돌아갈
 수 있는 버튼이 나타난다.
 
 ### 게임 종료 화면
 ![image](https://user-images.githubusercontent.com/70426440/112716731-7ee16b00-8f2b-11eb-9274-c6ec2d677a13.png)

- ufo가 사용자의 우주선과 접촉하면 게임이 종료된다. 난이도 선택을 하고 Play 버튼을 눌러 다시 시작할 수 있다.
 
 
 Settings 파일에서 게임 설정 가능 
 ex) 색상별 에일리언 격추시 총알 속도 설정 (권도엽)
 ![image](https://user-images.githubusercontent.com/70426440/112716787-d67fd680-8f2b-11eb-80ac-9e2b2b010ea7.png)

 ex) 총알 발사 속도와 색상별 에일리언 격추시 버프 지속 시간 설정 (김현중)
 ![image](https://user-images.githubusercontent.com/70426440/112716821-f616ff00-8f2b-11eb-941c-5732b61606f6.png)

결론

#### 프로젝트에 대한 자기 평가

 지금까지 해왔던 프로젝트는 직접 설계를 하여 처음부터 개발하는 것이었지만 이번 공개 SW  수업에서는 공개 SW의 특성을 이용하여 기존의 공개된 프로그램의 소스코드를 사용하여 이를 이해하고 팀원들과 함께 협력하여 부족한 부분을 채워나가는 프로젝트이다. github를 사용하여 소스코드를 pull 하여 저장하고, 팀원들과 github를 통하여 소스코드를 공유하면서 협력하면서 수정을 하였다. 이러한 과정을 통해 github의 사용법과 github의 구조를 이해할 수 있었다. 또한, python의 여러 라이브러리를 공부할 수 있었다. 특히 Alien Invasion은 pygame이라는 라이브러리를 사용하여 게임을 구현되었는데 대부분은 pygame을 사용하여 해당 라이브러리의 사용법을 충분히 익힐 기회가 되었다. 흐름도와 상세기능을 작성하면서 python의 기본 구조와 함수 실행 흐름을 이해할 수 있었다. 개선할 부분을 찾기 위해 팀원들과 여러 슈팅게임을 직접 하면서 각 게임의 장, 단점을 찾아보고 Alien Invasion에 개선할 부분을 찾을 수 있었다. 여러 슈팅게임의 코드를 참고 하면서 코드를 작성하였다. 이처럼 공개 소프트웨어의 장점인 사용자가 직접 소프트웨어의 문제를 수정하거나 개선할 수 있었다. 코로나로 인해 직접 만나지 못하였지만 git과 zoom us를 통하여 팀원들과 화상 통화와 코드를 공유하면서 언택트 시대에 맞는 의견 공유를 할 기회가 되었습니다. 이번 프로젝트를 통해 지금까지 배워왔던 공개 SW의 개요, python, git에 대해 이해하고 팀원들과 협력을 통해 팀워크를 향상할 수 있었습니다. 
