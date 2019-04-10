from skil import Skil, WorkSpace, Experiment, Model, Deployment
from keras.datasets import mnist


skil_server = Skil()
work_space = WorkSpace(skil_server, name='keras-mnist')
experiment = Experiment(work_space, name='mnist-experiment')
model = Model('model.h5', name="keras-mnist", experiment=experiment)

deployment = Deployment(skil_server)
service = model.deploy(deployment)


(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = x_test.reshape(10000, 784)
x_test = x_test.astype('float32')
x_test /= 255


print(service.predict_single(x_test[0]))
print(service.predict(x_test[:10]))
