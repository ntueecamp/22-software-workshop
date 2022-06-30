import tensorflow as tf
import numpy as np
from tensorflow.io import gfile
import tensorflow_io as tfio
from tensorflow.python.ops import gen_audio_ops as audio_ops
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
from tensorflow.python.ops import gen_audio_ops as audio_ops
import datetime
from tensorflow import keras
from tensorflow.keras import regularizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D, BatchNormalization
from tensorflow.data import Dataset
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

def get_voice_position(audio, noise_floor):
    audio = audio - np.mean(audio)
    audio = audio / np.max(np.abs(audio))
    return tfio.audio.trim(audio, axis=0, epsilon=noise_floor)

# Work out how much of the audio file is actually voice
def get_voice_length(audio, noise_floor):
    position = get_voice_position(audio, noise_floor)
    return (position[1] - position[0]).numpy()

def get_spectrogram(audio):
    # normalise the audio
    audio = audio - np.mean(audio)
    audio = audio / np.max(np.abs(audio))
    # create the spectrogram
    spectrogram = audio_ops.audio_spectrogram(audio,
                                              window_size=320,
                                              stride=160,
                                              magnitude_squared=True).numpy()
    # reduce the number of frequency bins in our spectrogram to a more sensible level
    spectrogram = tf.nn.pool(
        input=tf.expand_dims(spectrogram, -1),
        window_shape=[1, 6],
        strides=[1, 6],
        pooling_type='AVG',
        padding='SAME')
#     spectrogram = tf.squeeze(spectrogram, axis=0)
    spectrogram = spectrogram[1:, :, :, :] #?
    assert(spectrogram.shape[1]==99)
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
    # get the spectrogram
    return get_spectrogram(audio)

def main():
    spec = process_file(args.input)
    # use the command ffmpeg -i <input file> -ar <sample rate> <output file>
    # such that the target sampling rate is 16000 (spec length is (99, 43))
    # or a runtime error will be raised
    model2 =  keras.models.load_model("trained.model")
    results = model2.predict_on_batch(spec)
    print("------------------------")
    print("predict Results: (forward backward left right invalid)")
    print(results)

if __name__ == '__main__':
    main()