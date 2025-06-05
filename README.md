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

Download the SIDD Medium dataset or SIDD Small dataset from  https://abdokamel.github.io/sidd/

Convert the dataset into 64x64 image patches using the scripts in the Patches.py.

2. Train the Model

Train the network in traning.ipynb file

3. Test the Model

Evaluate the trained model on a test dataset using:

Test-HSENet.ipynb
--pretrained weights <a href="https://drive.google.com/file/d/1NrP-TrXpauZUUZT5bRoPu-3RJcDp3wg7/view?usp=share_link" > 'HSENet.weights.h5'</a> and <a href="https://drive.google.com/file/d/1HOOkkIHLQq725ut3i1myPyPama2wXdsd/view?usp=share_link" >HSENet.keras </a>

*Citation*
If you use this work in your research, please cite.
"DEEP DENOISER: A Hybrid Deep Learning Approach for Image Noise Reduction"

