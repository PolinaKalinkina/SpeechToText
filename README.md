
# Speech Recognition for Device Control

This project focuses on speech recognition for controlling devices, aiming to simplify daily tasks by speeding up routine activities. The process involves several stages, starting with capturing audio signals from a device or processing uploaded files. Key parameters such as sampling rate, bit depth, and the number of audio channels are considered during audio signal capture. The signals are then normalized and filtered to remove noise and unwanted frequency components. Feature extraction and Mel-spectrogram construction follow, with the extracted features fed into a neural network for text conversion.

## Architecture Analysis

### Wav2Vec2
- **Structure**: Consists of a convolutional neural network (CNN) with GELU activation and Layer Normalization.
- **Quantization**: Features are multiplied by a quantization matrix to obtain logits.
- **Transformer**: Uses a 12-block Transformer encoder with a projection layer to maintain input sequence order.
- **Training**: Employs the Masking technique for learning on masked positions.

### Whisper-medium
- **Structure**: Implemented as an encoder-decoder transformer.
- **Spectrogram**: Input sound is converted to a log-Mel spectrogram.
- **Decoder**: Predicts tokens and uses previous predictions to guess the next word.
- **Attention Mechanism**: Utilizes multi-head self-attention and position-wise feed-forward networks.
- **Training**: Also uses the Masking technique with a masked multi-head attention layer.

## Comparison for Computer Control

### Experiment Setup
- **Commands**: Included tasks like opening applications, deleting files, and system updates.
- **Audio Parameters**: High resolution and sampling rate with added echo for complexity.
- **Metrics**: Word Error Rate (WER) used for evaluation.

### Results
- **Whisper-medium**: WER = 0.212 (good recognition with minor errors).
- **Wav2Vec2**: WER = 1.030 (poor recognition due to numerous errors).

### Conclusion
Whisper-medium outperformed Wav2Vec2 in recognizing commands for computer control. This could be attributed to differences in error functions, quantization, and more effective implementation of the Masking technique in Whisper-medium.

## Future Work
Further development includes integrating Whisper-medium for real-time speech-based computer control and exploring additional techniques to improve recognition accuracy.
