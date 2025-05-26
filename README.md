## Tweet Emotion Recognition using TensorFlow

This project focuses on building a deep learning model to **predict emotions from tweets** using NLP techniques and TensorFlow.

### Key Features

- Preprocessing using `Tokenizer` and `pad_sequences`
- Text tokenization with a vocabulary of 10,000 most frequent words
- Input sequences padded to length 50
- Model built with:
  - Embedding layer
  - Bidirectional LSTM (2 layers)
  - Dense output layer with softmax for 6 emotion classes
- Trained for 10 epochs with validation data

### Libraries Used

- `TensorFlow` & `Keras`
- `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`
- `datasets` (for tweet dataset)

### **Training Summary**

-Loss function: sparse_categorical_crossentropy
-Optimizer: adam
- Metrics: accuracy
