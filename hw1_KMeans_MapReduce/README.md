# K-Means Clustering with MapReduce

This project demonstrates the implementation of the K-means clustering algorithm using the MapReduce programming model in Python. The goal is to simulate distributed computing by processing data across multiple processes.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [TODO](#todo)
- [How to Run](#how-to-run)
- [Submission](#submission)

## Overview

K-means clustering is an unsupervised learning algorithm used to partition a dataset into `k` distinct clusters based on feature similarity. In this implementation, we use the MapReduce paradigm to parallelize the clustering process.

## Requirements

- Python 3.x
- NumPy library
- Multiprocessing library (included with Python)

## File Structure

```
kmeans_mapreduce/
│── README.md
│── main.py
│── mapper.py
│── reducer.py
│── data.txt
```

## TODO

Complete `run()` in mapper.py and reducer.py.

## How to Run

Run K-Means Clustering: Execute the main.py script to start the K-means clustering process.

```
python main.py
```

## Submission

Rename the folder to `hw1_{student_id}` format, for example `hw1_r12345678`, and zip it. Your folder should contain mapper.py and reducer.py only. **If the submission does not follow the specified format, it will be graded as zero.**

```
hw1_r12345678/
│── mapper.py
│── reducer.py
```

# K-means Clustering 中的質心 (Centroid) 意義與應用

---

## 1. 質心的意義 (What is a Centroid?)

在 K-means clustering 中，資料會被分成 `K` 個不同的群集 (clusters)。
- **每個群集** 都對應到一個 **質心 (centroid)**。
- 這個質心可以視為該群集中所有資料點的「平均位置」，也可說是該群集的代表點（中心點）。

若我們將某個群集中所有點的座標取平均（**means**），就能得到該群集的質心。

例如，群集裡有點 \((x_1, y_1)\), \((x_2, y_2)\), …, \((x_n, y_n)\)，  
則此群集的質心 \(C\) 會是：
\[
C = \left(\frac{x_1 + x_2 + \ldots + x_n}{n}, \frac{y_1 + y_2 + \ldots + y_n}{n}\right)
\]

> 在高維度空間中，概念相同：將同個群集的所有向量逐維度加總取平均，就得到該群集的「中心點」。

---

## 2. 質心是怎麼被「挑出」或「計算」的？

### (1) 初始化 (Initialization)

在 K-means 的第一步，通常會「**隨機**」地選擇 K 個初始質心。  
- 例如，從整個資料集中隨機抽取 K 筆資料作為初始質心；  
- 或者在定義的空間範圍內，隨機生成 K 個點；  
- 另外也有一些改進的方法，如 **k-means++** 去選一個較好的初始值。

### (2) 每次迭代 (Iteration) 都會重新計算

K-means 每次「迭代」時，都會經過兩個主要步驟：
1. **Assignment 步驟**：把每個資料點分配給「最近」的質心（使用歐幾里得距離或其他距離度量）。
2. **Update 步驟**：對每個群集的所有資料點「取平均 (mean)」，得到「新的質心」。

這樣一來，每個群集就會有新的中心點（質心），也是常說的「重新計算 centroids」。  
- 這個新的質心通常會比上一輪更能代表當前群集中的所有資料點。  
- 隨著多次迭代，質心逐漸收斂到較穩定的位置（直到大部分點不再改變所屬群集或達到設定的最大迭代次數）。

---

## 3. 迭代 (Iteration) 可以做什麼？

- **迭代**的目標是讓群集劃分越來越好，讓每個群集內的點彼此之間越接近，而群集與群集之間相對越分散。  
- 在每一次迭代過程中：
  1. 根據目前的質心，把資料點歸類到最適合的群集；  
  2. 再重新計算每個群集的質心；  
  3. 重複上一步，直到收斂或達到指定條件。

當迭代完成後（或達到收斂），我們得到的群集就很可能能代表「自然形成的分群」結構。

---

## 4. 常見應用場景

K-means clustering 主要是一種 **無監督**（unsupervised）方法，適合用來發掘資料中隱含的結構，常見應用包含：

1. **顧客分群 (Customer Segmentation)**  
   - 在行銷領域，用於把顧客依照購買行為、使用習慣等維度分群，進行精準行銷。

2. **影像壓縮 (Image Compression)**  
   - 將圖片的像素點分群，找出最適的「色彩聚集中心」。以較少的顏色代表原圖，減少儲存空間。

3. **資料探勘 (Data Mining)**  
   - 對大型資料集中進行分群，找出可能存在的模式或分布趨勢，例如網頁分群、文件分群等。

4. **網路流量分析 / 入侵偵測**  
   - 分析龐大的網路封包 (network traffic) 資料，將相似的流量或行為分為一群，有助快速識別異常流量。

5. **圖像分類 / 特徵壓縮**  
   - 在電腦視覺領域裡，用於把大量相似特徵向量分在同一群，協助後續更精準或更快速的分類與辨識。

6. **使用者行為分群**  
   - 例如在網路應用與遊戲中，分析玩家的行為記錄，將遊玩模式相似或付費習慣相似的玩家歸類在同一族群，利於後續策略與決策。

---

### 總結

- **質心 (centroid)**：每個群集的「中心位置」，透過該群集中所有點的平均值取得。  
- **怎麼被挑出？**  
  - 一開始通常隨機選，之後透過反覆迭代（分配 -> 更新）逐漸收斂到一個能代表該群集的「中心點」。  
- **迭代的作用**：讓整個分群結果越來越好，質心的移動反映了群集中點的平均位置變化，直到整個群集劃分趨於穩定。  
- **應用場景**：廣泛包含顧客分群、影像壓縮、行為模式偵測、文字/文件分群等多種無監督學習需求。

希望以上說明能幫助你更加了解 **K-means clustering** 中質心的概念、重要性與實際應用！

