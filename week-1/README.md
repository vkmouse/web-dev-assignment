# 響應式網頁設計

本專案用於學習響應式網頁設計 (Responsive Web Design, RWD)，以下紀錄開發過程中，比較重要的技術細節。

- 如何實作導覽列
- CSS 命名規則之一 BEM
- 網格系統的應用
- 長寬比的區塊 (aspect ratio)
- 中心裁剪 (center cropped)
- 彈性成長係數 (flex-grow)
- 不透明度 (opacity)
- 圖層概念 (z-index)
- 從 KKBOX 到 CSS，選擇器命名規則

## 如何實作導覽列

導覽列的 CSS 選擇器如下，階層以及名稱如下

1. navbar: **導覽列**
2. navbar__toggler: **導覽列切換器**
3. navbar__nav: **所有導覽路徑**
4. nav__item: **導覽路徑**
    
    ```
    navbar
     ├─ navbar__toggler
     └─ navbar__nav
         └─ nav__item
    ```

### 導覽列基本資訊

1. 給一般使用者

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav1.png" width="400px"/>
      <div>圖 1、展開所有 Menu items 且不需要折疊</div>
    </div>
    
2. 給移動裝置，在使用者未進行操作

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav2.png" width="400px"/>
      <div>圖 2、摺疊所有 Menu items 且顯示選單 icon</div>
    </div>

3. 給移動裝置，使用者點擊選單 icon

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav3.png" width="400px"/>
      <div>圖 3、向下展開所有 Menu items 且顯示選單 icon</div>
    </div>
    
### 導覽列實作

1. 先寫 HTML 架構如下

    - navbar 為最外層 ```div```
    - navbar__toggler 做為顯示或隱藏選單的 div
    - navbar__toggler 裡面包含一個 img，使用 hamberger 作為 icon
    - navbar__toggler 在被點擊的時候，呼叫函式 handleNavbarTogglerClick，並傳入 element
    - navbar__nav **所有導覽路徑**的外層 div，包含四個**導覽路徑** Item 1 ~ Item 4
    - nav__item **導覽路徑**的名稱顯示或外層，通常會在裡面包含 ```<a>``` 作為連結


    ```
    <div class="navbar">
      <div class="navbar__toggler" onclick='handleNavbarTogglerClick(this)'>
        <img src="icon/hamberger.svg">
      </div>
      <div class="navbar__nav">
        <li class="nav__item">Item 1</li>
        <li class="nav__item">Item 2</li>
        <li class="nav__item">Item 3</li>
        <li class="nav__item">Item 4</li>
      </div>
    </div>
    ```

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav4.png" width="400px"/>
    </div>

2. 將**所有導覽路徑**水平排列，作為一般使用者的**導覽列**

    ```
    .navbar {
      align-items: center;
      display: flex;
      flex-wrap: wrap;
    }

    .navbar__nav {
      display: flex;
      flex-direction: row;
      list-style: none;
    }
    ```
    
    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav5.png" width="400px"/>
    </div>
    
3. 設定**導覽路徑**邊寬，讓路徑間不要太擁擠

    ```
    .nav__item {
      cursor: pointer;
      padding-left: 0.5em;
      padding-right: 0.5em;
    }
    ```
    
    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav6.png" width="400px"/>
    </div>

4. 設定**導覽列切換器**，在一般使用者下隱藏，**完成一般使用者導覽列 (如圖 1)**

    ```
    .navbar__toggler {
      cursor: pointer;
      display: none;
    }
    ```
    
    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav1.png" width="400px"/>
    </div>

5. 設定移動裝置使用者屬性，**完成移動裝置導覽列 (如圖 2)**

    - 顯示**導覽列切換器**
    - 隱藏**所有導覽路徑**，並調整為一個**導覽路徑**一列
    - 設定**導覽路徑**屬性

    ```
    @media screen and (max-width: 600px) {
      .navbar__toggler {
        display: block;
      }

      .navbar__nav {
        display: none;
        flex-direction: column;
        width: 100%;
      }

      .nav__item {
        padding-top: 0.25em;
        padding-bottom: 0.25em;
        padding-left: 0;
        padding-right: 0;
      }
    }
    ```
    
    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav2.png" width="400px"/>
    </div>

6. 當**導覽列切換器**被點擊，切換 ```display: flex``` 或預設值 (```display: none```)，**完成移動裝置導覽列 (如圖 3)**

    - 傳進來的 element 是 navbar__toggler
    - 父節點是 navbar，在 navbar 底下搜尋子節點 navbar__nav

    ```
    function handleNavbarTogglerClick(element) {
      const parent = element.parentElement;
      element = parent.querySelector('.navbar__nav');
      if (element.style.display !== "flex") {
        element.style.display = "flex";
      } else {
        element.style.display = "";
      }
    }
    ```

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav3.png" width="400px"/>
    </div>

## CSS 命名規則之一 BEM

Block Element Modifier (BEM) 是一種為了讓 CSS 類別更好維護的**命名方式**

1. Block 區塊 ```.block {}```
2. Element 元素 ```.block__element```
3. Modifier 修飾器 ```.block__element--modifier```

### Block 區塊

主要負責描述大範圍功能，例如 ```header```、```container``` 或 ```navbar```

### Element 元素

區塊的小部分，區塊可以不包含元素，但元素一定要包含在區塊，用於表達目的，中間用**雙底線**連結

例如 ```list__item``` 或 ```navbar__toggler```

### Modifier 修飾器

區塊或元素的狀態，同一個區塊或元素可能有多種狀態，使用修飾器表達，中間用**雙中線**連結

例如 ```nav__item--active```、```star--active``` 或 ```star--inactive```

### BEM 觀念

1. 當有重複使用的選擇器時，需要拉出來成為新的選擇器做調用，相當於 has-a 的功用
2. 利用**區塊**和**元素**，表達選擇器的階層關係，由於 CSS 沒有作用域，所以利用 BEM 避免命名重複
3. 利用**修飾器**表達不同狀態
4. 當區塊裡的元素，又有向下階層時，不希望一直下底線連結，只需要元素底線元素或區塊底線元素

    - 例如: ```menu__list__item__link``` 可以寫成 ```menu__link```，代表 link 不一定要在 list 或 item 之下
    
5. 使用抽象畫命名，例如顏色可以 ```text-blue``` 改為 ```text-primary```，```aside``` 和 ```content``` 可以改為 ```col-3```和 ```col-9```

### BEM 參考資料

- [竹白記事本-BEM，CSS 設計模式](https://chupainotebook.blogspot.com/2019/05/bemcss.html)
- [鐵人賽 5 - CSS 的命名技巧](https://www.casper.tw/css/2016/12/05/css-naming/)

## 網格系統的應用

- 用途: 網格系統在 RWD 的應用上，可以透過修改一列要呈現的數量，來縮小橫幅所需要的版面
- 需求: 一個網格系統需要 ```display: grid``` 和 ```grid-template-columns```
- 範例: 設定為一列四格可以設為 ```grid-template-columns: repeat(4, 1fr)```，當需要不同數量為二時可以修改為 ```repeat(2, 1fr)```
- 間距: 透過 ```column-gap: 1em``` 和 ```row-gap: 1em``` 可以設定上下左右的間距都是 1em，並且**間距設定不包含邊緣**，若有需求要用 ```margin``` 或 ```padding```

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/grid_system1.png" width="400px"/>
      <div>圖 6、網格系統</div>
    </div>
    
## 長寬比的區塊 (aspect ratio)

- 用途: 將某一區塊設定長寬比，常用於限定影像長寬比
- 需求: 需要有外層 ```container``` 和內層 ```media```
  - 外層設定寬為 1 (width: 100%)，長為 0.5625 (padding-top: 56.25%)，則為 16:9
  - 內層設定為```position: absolute```，**該屬性會往上層找層級最接近的** ```position:relative```，並以它作為絕對座標
- 範例: 16:9 如下，4:3 則設定為 3/4 = 0.75，3:2 則設定為 2/3 = 0.6667

    ```
    .container {
      position: relative;
      width: 100%;
      padding-top: 56.25%; /* 16:9 Aspect Ratio */
    }

    .media {
      position: absolute;
      top: 0;
    }
    ```

參考資料: 
- [New aspect-ratio CSS property supported in Chromium, Safari Technology Preview, and Firefox Nightly](https://web.dev/aspect-ratio/)
- [CSS relative? absolute? 傻傻分不清楚](https://ithelp.ithome.com.tw/articles/10212202)

## 中心裁剪 (center cropped)

- 用途: 將影像中心裁剪到符合長寬需求

    ```
    .center-cropped {
      object-fit: cover;
      object-position: center;
    }
    ```

- 範例: 

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/center_cropped1.png" width="250px"/>
      <div>圖 7、縮放影像</div>
    </div>
    
    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/center_cropped2.png" width="250px"/>
      <div>圖 8、執行中心裁剪</div>
    </div>


    ```
    <div style="width: 250px; height: 250px">
      <img style="width: 100%; height: 100%" src="...">
    </div>
    <div style="width: 250px; height: 250px">
      <img style="width: 100%; height: 100%; object-fit: cover; object-position: center;" src="...">
    </div>
    ```

參考資料: 
- [CSS - Center Crop Image]([https://ithelp.ithome.com.tw/articles/10212202](https://www.andrewnoske.com/wiki/CSS_-_Center_Crop_Image))

## 彈性成長係數 (flex-grow)

- 用途: 在 flex 容器中**剩餘空間**的相對比例，可用於水平 ```flex-direction: colume``` 或垂直 ```flex-direction: row``` 的剩餘空間
- 需求: ```flex-grow: 1```，數字代表權重
- 範例: 尚未加上 flow-grow 前，因為同一列高度不一樣，有些區塊下方仍未填滿，在區塊下方的元素加上 ```flow-grow: 1```，則將剩餘空間都給該元素

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/flow_grow1.png" width="600px"/>
      <div>圖 9、尚未加上 flow-grow</div>
    </div>
    
    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/flow_grow2.png" width="600px"/>
      <div>圖 10、加上 flow-grow</div>
    </div>

## 不透明度 (opacity)

- 用途: 將目標設定為半透明，可以進行半透明疊圖
- 需求: ```opacity: 25```，設定不透明度 25

## 圖層概念 (z-index)

- 用途: 將不同圖層，透過數字進行重疊，**數字越大越圖層前面**
- 需求: ```z-index: 1```，設定為圖層 1，只要其他 z-index 大於該數字且重疊，較大者會在上面

## 從 KKBOX 到 CSS，選擇器命名規則

剛開始寫 CSS 時，我們都知道要有意義的命名，但即使命名都有自己的意義，
卻發現選擇器之間有很多重複的屬性，完成第一份作業後，就有問彭彭老師，老師
就提到選擇器的命名規則是滿值得討論的議題，並讓我查詢「css bem naming」，
我就開始調查，CSS 怎麼樣才是好命名，並查學習一些常見網頁的命名方式。  

### 重要的命名觀念

1. 抽象化命名，例如: ```left``` 就只能放在左邊，改為 ```aside``` 就可以放在左右
2. 避免針對性命名，例如: 作業的歡迎橫幅 ```welcome```，可以改為 ```banner``` 內容就不一定是歡迎
3. 狀態命名，例如: 導航欄連結在當前頁面狀態 ```menu-item``` 加上 ```is-active```，其他頁面則只有 ```menu-item```

### BEM

Block Element Modifier (BEM) 是一種為了讓 CSS 類別更好維護的**命名方式**

1. Block 區塊 ```.block {}```

    主要負責描述大範圍功能，例如 ```header``` 或 ```container```

2. Element 元素 ```.block__element {}```

    區塊的小部分，區塊可以不包含元素，但元素一定要包含在區塊，用於表達目的，中間用**雙底線**連結
    例如 ```list__item``` 或 ```navbar__toggler```

3. Modifier 修飾器 ```.block__element--modifier {}```

    區塊或元素的狀態，同一個區塊或元素可能有多種狀態，使用修飾器表達，中間用**雙中線**連結
    例如 ```nav__item--active```、```star--active``` 或 ```star--inactive```

### KKBOX 的導覽列分解


### 重要的命名觀念

1. 抽象化命名，例如: ```left``` 就只能放在左邊，改為 ```aside``` 就可以放在左右
2. 避免針對性命名，例如: 作業的歡迎橫幅 ```welcome```，可以改為 ```banner``` 內容就不一定是歡迎
3. 狀態命名，例如: 導航欄連結在當前頁面狀態 ```menu-item``` 加上 ```is-active```，其他頁面則只有 ```menu-item```

### BEM

  Block Element Modifier (BEM) 是一種為了讓 CSS 類別更好維護的**命名方式**

1. Block 區塊 ```.block {}```

    主要負責描述大範圍功能，例如 ```header``` 或 ```container```

2. Element 元素 ```.block__element {}```

    區塊的小部分，區塊可以不包含元素，但元素一定要包含在區塊，用於表達目的，中間用**雙底線**連結
    例如 ```list__item``` 或 ```navbar__toggler```

3. Modifier 修飾器 ```.block__element--modifier {}```

    區塊或元素的狀態，同一個區塊或元素可能有多種狀態，使用修飾器表達，中間用**雙中線**連結
    例如 ```nav__item--active```、```star--active``` 或 ```star--inactive```

### KKBOX 的導覽列分解

1. KKBOX 導覽列分為兩個選擇器，並在寬度 1024 切換

    |          |        Mobile        |        Desktop       |
    | -------- | -------------------- | -------------------- | 
    | 0 ~ 1024 | ```display: flex```  | ```display: none```  | 
    | 1024 ~   | ```display: none```  | ```display: flex```  | 

    ```
    pm-header
    ├─ pm-mobile-header
    └─ pm-desktop-header
    ```
    |     |
    | :-: |
    | ![pm-header](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-header.png) | 
    | 圖1 pm-header |
    | ![pm-desktop-header](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-desktop-header.png) | 
    | 圖2 pm-desktop-header |
    | ![pm-mobile-header](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-mobile-header.png) | 
    | 圖3 pm-mobile-header |

2. 桌面版本裡面的 pm-container 有兩個區塊，位於旁邊的 pm-header-aside，和位於另一端的 pm-header-menu

    ```
    pm-header
    ├─ pm-mobile-header
    └─ pm-desktop-header
       └─ pm-container*
          ├─ pm-header-aside*
          └─ pm-header-menu*
    ```

    |     |
    | :-: |
    | ![pm-container](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-container.png) | 
    | 圖4 pm-container|
    | ![pm-header-aside](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-header-aside.png) | 
    | 圖5 pm-header-aside|
    | ![pm-header-menu](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-header-menu.png) | 
    | 圖6 pm-header-menu |

3. 在旁邊的 pm-header-aside 裡面只有一個 pm-logo

    ```
    pm-header
    ├─ pm-mobile-header
    └─ pm-desktop-header
       └─ pm-container-menu
          ├─ pm-header-aside
          |  └─ pm-logo*
          └─ pm-header-menu
    ```

    |     |
    | :-: |
    | ![pm-logo](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-logo.png) | 
    | 圖7 pm-logo |
    
    
4. 而 pm-header-menu 包含的東西就比要多，有 pm-drop-down、pm-search-button 和普通的 a

    - pm-drop-down: 下拉式選單，例如: 特色功能、娛樂情報等
    - pm-search-button: 搜尋按鈕
    - a: 非下拉式選單，例如: 訂閱方案和下載

    ```
    pm-header
    ├─ pm-mobile-header
    └─ pm-desktop-header
       └─ pm-container-menu
          ├─ pm-header-aside
          |  └─ pm-logo
          └─ pm-header-menu
             ├─ pm-drop-down*
             ├─ pm-search-button*
             └─ a*
    ```
    
    |     |
    | :-: |
    | ![pm-drop-down](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-drop-down.png) | 
    | 圖8 pm-drop-down |
    | ![pm-search-button](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-search-button.png) | 
    | 圖9 pm-search-button |
    | ![pm-normal](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-normal.png) ![pm-download](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-download.png) | 
    | 圖10 普通的 a |

    
5. 利用狀態顯示顏色，像是搜尋按鈕和下載都是藍色，使用選擇器 pm-highlight

    |     |
    | :-: |
    | ![pm-search-button](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-search-button.png) | 
    | 圖11 帶有 pm-highlight 的 pm-search-button |
    | ![pm-download](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-download.png) | 
    | 圖12 帶有 pm-highlight 的 a |

6. 接下來介紹 pm-mobile-header，裡面都是圖片 pm-menu-icon、pm-search-icon、pm-logo
其中 pm-logo 和 pm-search-icon (被包含在 pm-search-button 底下) desktop 共用選擇器

    ```
    pm-header
    ├─ pm-mobile-header
    |  ├─ pm-menu-icon*
    |  ├─ pm-search-icon*
    |  └─ pm-logo*
    └─ pm-desktop-header
       └─ pm-container-menu
          ├─ pm-header-aside
          |    └─ pm-logo
          └─ pm-header-menu
             ├─ pm-drop-down
             ├─ pm-search-button
             └─ a
    ```

    |     |
    | :-: |
    | ![pm-menu-icon](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-menu-icon.png) | 
    | 圖13 pm-menu-icon |
    | ![pm-search-icon](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-search-icon.png) | 
    | 圖14 pm-search-icon |
    | ![pm-logo-m](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-logo-m.png) | 
    | 圖15 pm-logo |

7. 最後，當 pm-menu-icon 和 pm-search-icon 被點擊都會展開左或右側的菜單，所以他們都有狀態 pm-active，
這個狀態將背景圖片都改為叉叉，複寫原本的選單或放大鏡

    |     |
    | :-: |
    | ![pm-menu-icon-active](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-menu-icon-active.png) | 
    | 圖16 帶有 pm-active 的 pm-menu-icon |
    | ![pm-search-icon-active](https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/pm-search-icon-active.png) | 
    | 圖17 帶有 pm-active 的 pm-search-icon |

### KKBOX 的導覽列總結

用 BEM 角度看 KKBOX 的導覽列，從中看到 Block 中都是可被單一重複使用，Element 需要依賴在特定 Block 之下，Modifier 則可以直接附加在 Block 或 Element

- Block: pm-header、pm-menu-icon、pm-search-icon、pm-logo、pm-drop-down、pm-search-button
- Element
    - pm-header 的 element: pm-mobile-header、pm-desktop-header
    - pm-desktop-header 的 element: pm-header-aside、pm-header-menu
- Modifier: pm-highlight、pm-active

### 參考資料

- [KKBOX](https://www.kkbox.com/tw/tc/)
- [竹白記事本-BEM，CSS 設計模式](https://chupainotebook.blogspot.com/2019/05/bemcss.html)
- [鐵人賽 5 - CSS 的命名技巧](https://www.casper.tw/css/2016/12/05/css-naming/)
