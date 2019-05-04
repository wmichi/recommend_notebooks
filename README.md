# レコメンド関連の記事に使用したNotebookリポジトリ

## 構成

- data ... データセットのディレクトリ
- data/MovieLens20M ... MovieLens20Mデータセットのディレクトリ
- data/MovieLens100k ... MovieLens100kデータセットのディレクトリ
- notebooks ... 各手法で試したnotebookのディレクトリ

## 実行推奨環境
RAM 30G以上

## データセットについて

今回はMovieLensのデータセットを二値分類のタスクで用いることができるようネガティブサンプリングし、かつ訓練／評価／予測用に分割している。   


1. データセットを取得しそれぞれのorgディレクトリへ格納   
それぞれ以下のURLより取得   
MovieLens100k:    
MovieLens20M:     


2. CreateClassificationDataset.ipynbを実行しデータセットを作成   
このnotebookで作成したデータセットは各データセットディレクトリのclassificationディレクトリ内に格納される。    
目的変数であるratingをint型でなくstr型にしたものはclassification_strディレクトリに格納される。   
またnotebook内に記載がある通り、train/eval/testの分割はtimestampでソートしたものを時間の若い順に分割している（今後変更する可能性あり）。


## 扱っている手法と記事

|手法|ファイル名|論文|
|:--|:--|:--|
|Factorization Machines|FactorizationMachines.ipynb|[Factorization Machines](https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf)|
|Wide and Deep|WideAndDeep.ipynb|[Wide & Deep Learning for Recommender Systems](https://arxiv.org/pdf/1606.07792.pdf)|
|NeuralFM|NeuralFM.ipynb|[Neural Factorization Machines for Sparse Predictive Analysis](https://arxiv.org/pdf/1708.05027.pdf)|
