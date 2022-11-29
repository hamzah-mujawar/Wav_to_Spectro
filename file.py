import matplotlib.pyplot as plt
from scipy import signal
import os
from scipy.io import wavfile
dataset_path = 'Archive'


for i, (dirpath, dirnames, filenames) in enumerate(
    os.walk(dataset_path)):  # dirpath is the current folder path, dirnames is the names of all the sub folders and file names are all the file names
    # if we are at the dataset folder (not the subfolders for genres/ need to be in genre level)
    if dirpath is not dataset_path:
        # process the files for the specific genre
        for f in filenames:
            file_path = os.path.join(dirpath, f)  # load audio file
            sample_rate, samples = wavfile.read(file_path)
            frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

            plt.pcolormesh(times, frequencies, spectrogram)
            plt.gca().set_axis_off()
            plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                                hspace=0, wspace=0)
            plt.margins(0, 0)
            plt.gca().xaxis.set_major_locator(plt.NullLocator())
            plt.gca().yaxis.set_major_locator(plt.NullLocator())
            filename_without_ext = os.path.splitext(file_path)[0]

            plt.savefig(filename_without_ext + ".png", bbox_inches ='tight', pad_inches = 0)
            print('processing... ' + filename_without_ext)