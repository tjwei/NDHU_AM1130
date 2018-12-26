這是機器學習的作業。 分成基本及影像兩個：

## 基本分類
資料是 heart.csv,從個人資料來預測是否會有心臟疾病。
最後一欄 `target` 代表是否有疾病, 值為 `1` 或 `0` ，是我們想預測的目標

前面的其他欄位說明如下：
```
age: 
sex: (1 = male; 0 = female)
cp: chest pain type
trestbps: resting blood pressure (in mm Hg on admission to the hospital)
chol: serum cholestoral in mg/dl
fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
restecg: resting electrocardiographic results
thalach: maximum heart rate achieved
exang: exercise induced angina (1 = yes; 0 = no)
oldpeak: ST depression induced by exercise relative to rest
slope: the slope of the peak exercise ST segment
ca: number of major vessels (0-3) colored by flourosopy
thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
```
請用 sklearn 訓練一個分類器， 從這些欄位的數值來預測 `target` 

## 圖片分類

從 https://github.com/ieee8023/deep-learning-datasets/tree/master/chihuahua-muffin 下載吉娃娃和鬆餅的圖片，
寫一個程式，讀入圖片，然後訓練一個簡單的分類器來區分他們。

如果想挑戰真實一點的資料和情境，也可以使用貓狗資料集 https://www.microsoft.com/en-us/download/details.aspx?id=54765
訓練一個貓狗分類器。  


請將過程寫成 ipynb 檔案，上傳 elearn， 評分會以過程來評分。
