# 📌 Recap: Differences Between RNN, CNN, and Shallow Neural Networks

| **Model** | **Type** | **Typical Input** | **Key Features** | **Application Examples** |
|-----------|---------|------------------|------------------|--------------------------|
| **Shallow Neural Networks** | Simple Neural Network | Feature vectors | ✅ 1-2 hidden layers <br> ✅ No temporal memory <br> ✅ Suitable for structured data | 📊 **Financial predictions** <br> 📈 **Tabular data analysis** <br> 🏥 **Medical diagnosis on numerical data** |
| **CNN (Convolutional Neural Networks)** | Supervised Deep Learning | **Images, audio signals (spectrograms)** | ✅ Convolutional layers for feature extraction <br> ✅ Pooling for dimensionality reduction <br> ✅ Invariant to translations | 📷 **Object and face recognition** <br> 🏎 **Self-driving cars** <br> 🩻 **Medical image analysis** |
| **RNN (Recurrent Neural Networks)** | Supervised Deep Learning | **Sequential data (text, audio, video, time series)** | ✅ Maintains memory of past inputs <br> ✅ Suitable for data with temporal dependencies <br> ✅ LSTM solves the vanishing gradient problem | 📝 **Machine translation** <br> 🎤 **Speech recognition** <br> 📈 **Stock market predictions** |

---

## Conclusion
- **Shallow Neural Networks** → Simple models suitable for structured data.  
- **CNN** → Best for images and audio signals, extracting visual features.  
- **RNN** → Handle temporal sequences, essential for NLP, audio, and video.  

Choosing the right model depends on the type of data to be analyzed.
