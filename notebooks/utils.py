import os
import tensorflow as tf
import pandas as pd
from shutil import copyfile


class EarlyStoppingHook(tf.train.SessionRunHook):
  '''TrainSpecにて使用するEarlyStoppingのhook
  '''
  def __init__(self, early_stopping_rounds=1):
      self._best_loss = None
      self._early_stopping_rounds = early_stopping_rounds
      self._counter = 0

      print("")
      print("*** Early Stopping Hook: - Created")
      print("*** Early Stopping Hook:: Early Stopping Rounds: {}".format(self._early_stopping_rounds))
      print("")

  def before_run(self, run_context):

      graph = run_context.session.graph

      loss_tensor = graph.get_collection(tf.GraphKeys.LOSSES)[1]
      return tf.train.SessionRunArgs(loss_tensor)

  def after_run(self, run_context, run_values):

      last_loss = run_values.results

      if self._best_loss is None:
          self._best_loss = last_loss

      elif last_loss > self._best_loss:

          self._counter += 1
          print("Early Stopping Hook: No improvment! Counter: {}".format(self._counter))

          if self._counter == self._early_stopping_rounds:

              run_context.request_stop()
              print("Early Stopping Hook: Stop Requested: {}".format(run_context.stop_requested))
      else:

          self._best_loss = last_loss
          self._counter = 0

      print("************************")
      print("")


def export_result(model_name, auc, accuracy, config_filename, execute_time):
  '''AUCやAccuracyをcsvに出力する関数

  Parameters:
  --------------------
  model_name: str
    'FactorizationMachines'や'NeuralFM'といったモデル名
  auc: float
    予測結果（AUC）
  accuracy: float
    予測結果（Accuracy)
  config_filename:
    学習時に使用したconfig.iniファイルのファイル名
  execute_time: str
    学習の実行時間

  Return:
  --------------------
  None
  ただしlog/result.csvへの書き込み、configファイルのlog/config_fileディレクトリへのコピーを行なっている。
  '''
  # configファイルのコピー
  # log/result.csvのexecute_timeから探せるようファイル名を変更
  config_filepath = '../log/config_files/' + execute_time + '_config.ini'
  copyfile(config_filename, config_filepath)

  # result.csvに書き込む内容を作成。かなり手作り...
  result = ','.join([model_name, str(auc), str(accuracy), execute_time])
  result_filename = '../log/result.csv'

  with open(result_filename, 'a', newline='\n') as f:
    f.write(result)
    f.write('\n')
