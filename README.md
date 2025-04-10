# Deep Denoiser: A Hybrid Deep Learning Approach for Image Noise Reduction

This repository contains the implementation of the proposed method from the research paper:  
**“DEEP DENOISER: A Hybrid Deep Learning Approach for Image Noise Reduction”**.

> 📄 This project introduces **HSENet**, a hybrid encoder-decoder architecture that leverages multi-scale convolutions, attention mechanisms, Squeeze-and-Excitation (SE) blocks, and Swin Transformer layers to robustly denoise real-world images.

---

## 📌 Highlights

- ✅ Hybrid deep learning architecture (CNN + SE + Swin Transformer)
- ✅ Designed for **real-world noise**: handles Gaussian, speckle, salt-and-pepper, Poisson, and complex mixed noise
- ✅ Achieves **state-of-the-art performance** on benchmark datasets: SIDD, DND, RENOIR, NIND, CBSD68

---

Steps to Use

1. Prepare the Dataset

Convert the dataset into 64x64 image patches using the scripts in the data_preprocessing folder.

2. Train the Model

Train the network for a noise level (NL) of 10 using the following command:

python main.py --NL 10 --BatchReNormalization True --input_shape (64,64,3)
3. Test the Model

Evaluate the trained model on a test dataset using:

python main.py --NL 10 --BatchReNormalization True --input_shape (64,64,3) --test_data_name 'Kodak_Test_C_NL30.h5'
Citation

If you use this work in your research, please cite.
