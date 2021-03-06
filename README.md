# Tetraptych: scripts for the youtube video

*Four ways of visualizing music (from waveform)*

The video: https://youtu.be/LledeXuK5tA 

The source for the visualizations is a waveform of `alone.wav`,
a piece I recorded on a slightly out-of-tune upright piano using a smartphone.

The first visualization is a simple oscillogram of the waveform (`wav2plot2.py`)

The second is an attempt at mapping the spectrogram peaks onto piano keys which obviously didn't work very well.
It needs to be thresholded, filtered and processed properly. The video was generated using `kbd2.svg` animated using `wav2kdb.py`.

The third is a score typeset using Lilypond (`alone.ly`).
This one is the only visualization which is not based on the waveform.

The fourth is a classic spectrogram. The analysis was done using the fast Fourier transform algorithm from Numpy library,
the resulting image was generated by `wav2spectrum.py`.

The music itself (`alone.wav`) is a piece I composed for my wife while she was in Australia for three months.
It's a montage of three music ideas. The first one is just a bunch of chords,
the second one is a groovy theme which reminds me of Radiohead's True love waits.
The third one is a variation of a theme from my other composition: Passacaglia (https://youtu.be/Iu3Da3kMdQE)

The four visualizations were stitched and animated using Kdenlive.
