#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def generate_data(num_points=120):
    """
    產生三個群的測試資料點，並回傳同一個 numpy array。
    """
    np.random.seed(42)
    cluster1 = np.random.normal(loc=(2, 2),  scale=0.7, size=(num_points//3, 2))
    cluster2 = np.random.normal(loc=(8, 8),  scale=0.7, size=(num_points//3, 2))
    cluster3 = np.random.normal(loc=(5, 2),  scale=0.7, size=(num_points - 2*(num_points//3), 2))

    data = np.vstack((cluster1, cluster2, cluster3))
    np.random.shuffle(data)
    return data

def initialize_centroids(data, K=3):
    """
    從 data 中隨機挑選 K 個點作為初始 centroids。
    """
    initial_indices = np.random.choice(len(data), K, replace=False)
    return data[initial_indices, :]

def kmeans_assignment(data, centroids):
    """
    將 data 中的每個點分配到最近的 centroid。
    回傳 cluster_labels (每個點對應的群集編號)。
    """
    distances = np.linalg.norm(data[:, np.newaxis, :] - centroids[np.newaxis, :, :], axis=2)
    cluster_labels = np.argmin(distances, axis=1)
    return cluster_labels

def kmeans_update(data, cluster_labels, K=3):
    """
    根據 cluster_labels 計算新的 centroids。  
    如果某群無資料點，則隨機初始化一個 centroid。
    """
    new_centroids = []
    for k in range(K):
        points_in_cluster = data[cluster_labels == k]
        if len(points_in_cluster) > 0:
            new_centroids.append(np.mean(points_in_cluster, axis=0))
        else:
            new_centroids.append(np.random.rand(2)*10)  # 避免空群
    return np.array(new_centroids)

def plot_clusters(ax, data, cluster_labels, centroids, iteration):
    """
    在 ax (matplotlib axes) 上繪製分群結果與 centroids，不同群組使用不同顏色。
    這裡預設最多處理 7 群，若有需要可自行擴充。
    """
    ax.clear()  # 先清空前一次的圖
    K = len(centroids)
    
    # 預先定義一組顏色（若 K>7 可自行擴充或改用 colormap）
    color_palette = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    
    for k in range(K):
        cluster_data = data[cluster_labels == k]
        # 以 cluster k 的顏色繪製
        color_k = color_palette[k % len(color_palette)]
        
        # 繪製該 cluster 的資料點
        ax.scatter(cluster_data[:, 0], cluster_data[:, 1], 
                   c=color_k, label=f'Cluster {k}')
        
        # 繪製該 cluster 的 centroid
        ax.scatter(centroids[k, 0], centroids[k, 1], 
                   marker='X', s=200, c=color_k, 
                   edgecolor='black', linewidth=1.5, 
                   label=f'Centroid {k}')

    ax.set_title(f'K-means Clustering (Iteration {iteration})')
    ax.legend()
    ax.grid(True)

def main():
    # -------------- 參數設定 -------------- #
    K = 3               # 要分成幾群
    NUM_POINTS = 200    # 總共多少資料點
    MAX_ITER = 20       # 最多迭代幾次

    # -------------- 生成測試資料 & 初始化 -------------- #
    data = generate_data(num_points=NUM_POINTS)
    centroids = initialize_centroids(data, K=K)

    # -------------- 啟用互動模式 -------------- #
    plt.ion()
    fig, ax = plt.subplots()

    iteration = 0
    while iteration < MAX_ITER:
        # (1) Assignment
        cluster_labels = kmeans_assignment(data, centroids)
        
        # (2) Update
        centroids = kmeans_update(data, cluster_labels, K=K)
        
        # 更新圖表
        plot_clusters(ax, data, cluster_labels, centroids, iteration)
        fig.canvas.draw()
        plt.pause(0.1)  # 讓 matplotlib 有時間更新畫面
        
        # 終端機互動：按 Enter 進行下一次迭代，或輸入 q 退出
        user_input = input("Press Enter to iterate, or 'q' then Enter to quit: ")
        if user_input.strip().lower() == 'q':
            print("Exit by user request.")
            break
        
        iteration += 1
    
    # -------------- 迭代結束，關閉互動模式 -------------- #
    plt.ioff()
    print(f"K-means finished or reached max iteration ({iteration}/{MAX_ITER}).")
    print("Close the figure window to end the program.")
    plt.show()

if __name__ == "__main__":
    main()

