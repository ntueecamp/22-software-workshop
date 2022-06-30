import tensorflow as tf
import numpy as np
import tensorflow_io as tfio
from tensorflow.python.ops import gen_audio_ops as audio_ops
from tensorflow import keras
import sounddevice as sd
import samplerate
import time

input_device = 2
device_info = sd.query_devices(input_device)
config = {
    "device": input_device,
    "channels": device_info["max_input_channels"],
    "samplerate": int(device_info["default_samplerate"]),
    "blocksize": 2048,
}
MODEL_fs = 16000


def get_spectrogram(audio):
    # normalise the audio
    audio = audio - np.mean(audio)
    audio = audio / np.max(np.abs(audio))
    # create the spectrogram
    spectrogram = audio_ops.audio_spectrogram(
        audio, window_size=320, stride=160, magnitude_squared=True
    ).numpy()
    # reduce the number of frequency bins in our spectrogram to a more sensible level
    spectrogram = tf.nn.pool(
        input=tf.expand_dims(spectrogram, -1),
        window_shape=[1, 6],
        strides=[1, 6],
        pooling_type="AVG",
        padding="SAME",
    )
    #     spectrogram = tf.squeeze(spectrogram, axis=0)
    spectrogram = spectrogram[1:, :, :, :]  # ?
    assert spectrogram.shape[1] == 99
    spectrogram = np.log10(spectrogram + 1e-6)
    return spectrogram


# process a file into its spectrogram
def process_file(file_path):
    # load the audio file
    audio_tensor = tfio.audio.AudioIOTensor(file_path)
    # convert the audio to an array of floats and scale it to betweem -1 and 1
    audio = tf.cast(audio_tensor[:], tf.float32)
    audio = audio - np.mean(audio)
    audio = audio / np.max(np.abs(audio))
    print(audio.shape)
    # get the spectrogram
    return get_spectrogram(audio)


model = keras.models.load_model("trained.model")


def predict(spec):
    answers = ["forward", "backward", "left", "right", "invalid"]
    results = model.predict_on_batch(spec)
    answer_ind = int(results.argmax(axis=1))
    if results[0, answer_ind] > 0.7:
        print(answers[answer_ind])
    return results


audio = np.array([])


def audio_callback(indata, frames, time, status):
    global audio

    if status:
        print(status)

    audio = np.append(audio, indata)
    if audio.shape[0] > config["samplerate"]:
        data = audio[: config["samplerate"]]
        audio = audio[config["samplerate"] :]

        data = samplerate.resample(data, MODEL_fs / config["samplerate"], "sinc_best")
        data = data - np.mean(data)
        data = data / np.max(np.abs(data))
        data = np.tile(data.reshape(-1, 1), (1, 2))
        spec = get_spectrogram(data)
        predict(spec)


def main():
    duration = 10

    stream = sd.InputStream(
        device=config["device"],
        channels=config["channels"],
        samplerate=config["samplerate"],
        callback=audio_callback,
        blocksize=config["blocksize"],
    )

    stream.start()
    print("start")
    time.sleep(duration)
    stream.stop()
    print("stop")


if __name__ == "__main__":
    main()
