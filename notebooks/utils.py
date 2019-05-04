import tensorflow as tf

class EarlyStoppingHook(tf.train.SessionRunHook):

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

#         tensor_name = "dnn/head/weighted_loss/Sum:0" #works!!
#         loss_tensor = graph.get_tensor_by_name(tensor_name)

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

