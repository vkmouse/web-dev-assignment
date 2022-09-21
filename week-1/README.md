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

## 如何實作導覽列

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
    

### 導覽列實作概念

1. 使用一個外層區塊 ```nav```，包含兩個內層區塊 ```nav-head``` 和 ```nav-links```

    ```
    <div class="nav">
      <div class="nav-head"></div>
      <div class="nav-links"></div>
    </div>
    ```

2. 將 ```nav``` 屬性設為 ```display: flex```，在一行裡面呈現 ```nav-head``` 和 ```nav-links```
3. 在 ```nav-head``` 加入 icon，並且改為 ```display: none```，用以呈現圖 1

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav4.png" width="400px"/>
      <div>圖 4、單行導覽列資訊</div>
    </div>

4. 給移動裝置時，改為多行導覽列，將 ```nav``` 的屬性改為 ```display: block```
5. 將 ```nav-links``` 改為 ```display: none```，icon 改為 ```display: block```，用以呈現圖 2
6. 當 icon 被點擊時，用 javascript 將 ```nav-links``` 改為 ```display: none```，用以呈現圖 3

    <div>
      <img src="https://raw.githubusercontent.com/vkmouse/web-dev-assignment/gh-pages/img/week-1/nav5.png" width="400px"/>
      <div>圖 5、多行導覽列資訊</div>
    </div>
    
    ```
    if (element.style.display !== "flex") {
      element.style.display = "flex";
    } else {
      element.style.display = "";
    }
    ```

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
