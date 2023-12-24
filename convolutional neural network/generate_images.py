import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt

image_size = (64, 64)
batch_size = 16
image_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)
train_data = image_generator.flow_from_directory(
    'D:/dogscats/images',
    target_size=image_size,
    batch_size=batch_size,
    class_mode='input',
    subset='training'
)
val_data = image_generator.flow_from_directory(
    'D:/dogscats/images',
    target_size=image_size,
    batch_size=batch_size,
    class_mode='input',
    subset='validation'
)

input_shape = (image_size[0], image_size[1], 3)
inputs = Input(shape=input_shape)
x = Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
encoded = MaxPooling2D((2, 2), padding='same')(x)

x = Conv2D(128, (3, 3), activation='relu', padding='same')(encoded)
x = UpSampling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
decoded = Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = Model(inputs, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

epochs = 5
history = autoencoder.fit(
    train_data,
    epochs=epochs,
    validation_data=val_data
)

new_images = autoencoder.predict(val_data)

n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
    # получение сгенерированного изображения и входного изображения для сравнения
    generated_image = new_images[i]
    input_image = val_data[i][0][0]
    # вывод сгенерированного изображения и входного изображения для сравнения
    ax = plt.subplot(2, n, i+1)
    plt.imshow(input_image)
    plt.title("Input")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(2, n, i+n+1)
    plt.imshow(generated_image)
    plt.title("Generated")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()