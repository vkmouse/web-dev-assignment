# 響應式網頁設計

本專案用於學習響應式網頁設計 (Responsive Web Design, RWD)，以下紀錄開發過程中，比較重要的技術細節。

- 如何實作導覽列
- 網格系統的應用
- 長寬比的區塊 (aspect ratio)
- 中心裁剪 (center cropped)
- 彈性成長係數 (flex-grow)

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
    
