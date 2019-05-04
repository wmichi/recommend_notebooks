# レコメンド関連の記事に使用したNotebookリポジトリ

## 構成

- data ... データセットのディレクトリ
- data/MovieLens20M ... MovieLens20Mデータセットのディレクトリ
- data/MovieLens100k ... MovieLens100kデータセットのディレクトリ
- notebooks ... 各手法で試したnotebookのディレクトリ

## 実行推奨環境
RAM 30G以上

## データセットの生成方法
使用しているデータセットを訓練／評価／予測用に分割している。

## 扱っている手法と記事

手法|ファイル名|論文
|:--|:--|:--|:--|:--|:--|:--|
Factorization Machines|FactorizationMachines.ipynb|[Factorization Machines](https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf)
Wide and Deep|WideAndDeep.ipynb|[Wide & Deep Learning for Recommender Systems](https://arxiv.org/pdf/1606.07792.pdf)
NeuralFM|NeuralFM.ipynb|[Neural Factorization Machines for Sparse Predictive Analysis](https://arxiv.org/pdf/1708.05027.pdf)
