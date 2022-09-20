# 響應式網頁設計

本專案用於學習響應式網頁設計 (Responsive Web Design, RWD)，以下紀錄開發過程中，比較重要的技術細節。

- 如何實作導覽列
- 網格系統的應用
- 長寬比的區塊 (aspect ratio)
- 中心裁剪 (center cropped)
- 彈性成長係數 (flex-grow)

## 如何實作導覽列

### 導覽列基本資訊

1. 給一般使用者，展開所有 Menu items，且不需要摺疊
2. 給移動裝置，在使用者未進行操作時，摺疊所有 Menu items，並顯示選單 icon
3. 給移動裝置，在使用者點擊選單 icon，展開並向下呈現所有 Menu items
