from tensorflow.keras import layers, models
from tensorflow.keras import regularizers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical


class MaskOrNotNetwork:
    def __init__(self, X, y, test_size=0.2):
        self.model = models.Sequential()
        self.X = X
        self.y = to_categorical(y)
        self.width = len(self.X[0])
        self.height = len(self.X[0][0])
        self.channel = len(self.X[0][0][0])
        print("Input shape: {}*{}*{}".format(self.width, self.height, self.channel))
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,
                                                                                test_size=test_size,
                                                                                random_state=0)
        print('Train: {}. Test: {}.'.format(len(self.X_train), len(self.X_test)))
        self.setup_network()
        print('MaskOrNotNetWork setup.')

    def setup_network(self, lr=1e-4):
        self.model.add(layers.Conv2D(64, (3, 3),
                                     strides=(1, 1),
                                     activation="relu",
                                     padding="same",
                                     kernel_initializer="uniform",
                                     data_format="channels_last",
                                     input_shape=(self.width, self.height, self.channel)))
        self.model.add(layers.Conv2D(64, (3, 3),
                                     strides=(1, 1),
                                     activation="relu",
                                     padding="same",
                                     kernel_initializer="uniform",
                                     data_format="channels_last"))
        self.model.add(layers.MaxPooling2D((2, 2)))

        self.model.add(layers.Conv2D(128, (3, 3),
                                     strides=(1, 1),
                                     activation="relu",
                                     padding="same",
                                     kernel_initializer="uniform",
                                     data_format="channels_last"))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(128, (3, 3),
                                     strides=(1, 1),
                                     activation="relu",
                                     padding="same",
                                     kernel_initializer="uniform",
                                     data_format="channels_last"))
        self.model.add(layers.MaxPooling2D((2, 2)))

        self.model.add(layers.Conv2D(256, (3, 3),
                                     strides=(1, 1),
                                     activation="relu",
                                     padding="same",
                                     kernel_initializer="uniform",
                                     data_format="channels_last"))
        self.model.add(layers.Conv2D(256, (3, 3), strides=(1, 1),
                                     activation="relu",
                                     padding="same",
                                     kernel_initializer="uniform",
                                     data_format="channels_last"))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(512, (3, 3),
                                     strides=(1, 1),
                                     activation="relu",
                                     padding="same",
                                     kernel_initializer="uniform",
                                     data_format="channels_last"))
        self.model.add(layers.Conv2D(512, (3, 3),
                                     strides=(1, 1),
                                     activation="relu",
                                     padding="same",
                                     kernel_initializer="uniform",
                                     data_format="channels_last"))
        self.model.add(layers.MaxPooling2D((2, 2)))

        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(4096, activation="relu", kernel_regularizer=regularizers.l2(0.1)))
        self.model.add(layers.Dense(4096, activation="relu"))
        self.model.add(layers.Dense(1000, activation="relu"))
        self.model.add(layers.Dense(2, activation="softmax"))

        self.model.compile(optimizer=optimizers.Adam(lr=lr),
                           loss=losses.CategoricalCrossentropy(),
                           metrics=['accuracy'])
        print(self.model.summary())

    def train(self, epochs=10, batch_size=16):
        print('Begin training.')
        history = self.model.fit(x=self.X_train, y=self.y_train,
                                 epochs=epochs,
                                 batch_size=batch_size,
                                 shuffle=True,
                                 validation_split=0.2,
                                 use_multiprocessing=True,
                                 verbose=1)
        return history

    def test(self):
        print('Begin testing')
        test_loss, test_acc = self.model.evaluate(self.X_test, self.y_test, verbose=2)
        return test_loss, test_acc

    def save(self, path):
        print('Saving model to {}'.format(path))
        self.model.save(path)
