# 🍽️ 재료 맞춤형 레시피 추천 서비스

[cite_start]"오늘 뭐 먹지?"라는 일상적인 고민을 해결하기 위해 기획한 웹 서비스입니다. [cite: 42] [cite_start]사용자가 보유한 재료를 기반으로 만들 수 있는 요리를 추천하고, 웹 크롤링 기술을 활용하여 레시피, 관련 유튜브 영상, 부족한 재료의 구매 정보, 주변 맛집 정보까지 종합적으로 제공합니다. [cite: 49, 54, 73, 75]

<br>

### 📸 주요 기능 및 데모

---
![웹페이지 데모 이미지](URL)

- [cite_start]**맞춤형 요리 추천**: 사용자가 가진 재료를 입력하면 만들 수 있는 요리 목록을 데이터베이스 기반으로 추천 [cite: 77]
- [cite_start]**상세 레시피 제공**: 선택한 요리의 전체 재료, 조리 순서, 칼로리 정보 제공 [cite: 67, 79]
- **실시간 정보 연동**:
    - [cite_start]**유튜브 영상**: 요리 이름으로 유튜브를 실시간 크롤링하여 관련 영상을 함께 제공 [cite: 75]
    - [cite_start]**재료 구매**: 부족한 재료의 온라인 최저가 및 구매처 링크 제공 [cite: 74]
    - [cite_start]**맛집 추천**: 외식을 원하는 사용자를 위해 입력한 메뉴의 주변 맛집 정보를 네이버 지도 기반으로 크롤링하여 제공 [cite: 73]

<br>

### ⚙️ 시스템 구조 (System Architecture)

---
![시스템 구조도](URL)

1.  [cite_start]**Data Collection**: Python(Selenium)으로 레시피 사이트를 크롤링하여 요리 데이터 수집 [cite: 66]
2.  [cite_start]**Database**: 수집한 데이터를 `pandas`와 `sqlite`를 이용해 CSV 파일 생성 후 DB로 구축 [cite: 68, 93]
3.  [cite_start]**Back-end**: `Flask` 프레임워크를 사용하여 웹 서버를 구축하고, 사용자 요청에 따라 DB에서 데이터를 처리 [cite: 69]
4.  [cite_start]**Front-end**: `HTML`로 구성된 웹페이지에 처리된 데이터를 전달하여 사용자에게 시각적으로 보여줌 [cite: 71]

<br>

### 🛠️ 사용 기술 (Tech Stack)

- **Language**: `Python`
- **Web Framework**: `Flask`
- **Crawling**: `Selenium`
- **Data Handling**: `Pandas`, `SQLite3`
- **Front-end**: `HTML`
- **Deployment**: `ngrok`

<br>

### 겪었던 문제 및 해결 (Trouble Shooting)

- [cite_start]**문제**: 맛집 추천 기능 구현 시, 네이버 지도를 Headless 모드로 크롤링하면 지도 UI가 로딩되지 않아 CSS 선택자를 찾지 못하는 Timeout 에러 발생 [cite: 1052, 1053]
- [cite_start]**해결**: 직접 지도 페이지에 접근하는 대신, 네이버 통합 검색 포털에서 '맛집'을 먼저 검색한 후, '지도 바로가기' 링크의 URL을 크롤링하는 방식으로 우회하여 지도 GUI를 직접 로딩하지 않고도 원하는 결과를 얻는 데 성공 [cite: 1060]
