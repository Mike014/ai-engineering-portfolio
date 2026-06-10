# Supervised vs. Unsupervised Learning

## Supervised Learning
In supervised learning, models are trained using **labeled datasets**, where each input is associated with a known output. The objective is to learn a mapping from inputs (X) to outputs (Y).

**Main Categories:**

### Classification
Predicts **discrete classes** (e.g., spam vs. not spam).

- **Examples:**
  - K-Nearest Neighbors (KNN)
  - Support Vector Machines (SVM)
  - Decision Trees
  - Random Forests
  - Naive Bayes
  - Neural Networks

### Regression
Predicts **continuous values** (e.g., housing prices).

- **Examples:**
  - Linear Regression
  - Polynomial Regression
  - Support Vector Regression (SVR)
  - Neural Networks

---

## Unsupervised Learning
In unsupervised learning, models work with **unlabeled data**, aiming to uncover hidden patterns without explicit instructions.

**Main Techniques:**

### Clustering
Groups data based on similarity.

- **Examples:**
  - K-Means
  - DBSCAN
  - Hierarchical Clustering
  - Gaussian Mixture Models (GMM)

### Dimensionality Reduction
Reduces the number of features while preserving data variance.

- **Examples:**
  - Principal Component Analysis (PCA)
  - Autoencoders

---

## Summary
- **Supervised Learning:** Utilizes labeled data for tasks like classification and regression.
- **Unsupervised Learning:** Explores unlabeled data to identify patterns, such as clustering and dimensionality reduction.

Understanding these distinctions is fundamental in selecting the appropriate machine learning approach for a given problem.
## **Quick Summary**
* **Supervised** → With labels → **Classification & Regression**
* **Unsupervised** → Without labels → **Clustering & Pattern Discovery, Latent Representation Learning**


### Examples

### **Supervised Learning Example**

**Scenario:** Spam email recognition.

* **Input data:** Thousands of emails labeled *"spam"* or *"not spam"*.
* **What the model does:** Learns from the data which words, phrases, or patterns indicate spam.
* **Real-world use:** When a new email arrives, the model predicts whether it's spam or not.

Here I have **input (email text)** + **output (spam/not spam label)** → therefore **supervised learning**.

### Output (Y)
- **Label:** `spam` or `not spam`

### Input (X) → Features describing the email
- Email length (number of words/characters)  
- Presence of suspicious keywords (`"free"`, `"lottery"`, `"click here"`, …)  
- Sender's domain type (`@gmail`, `@yahoo`, `@strange.biz`, …)  
- Number of links in the body of the text  
- Frequency of uppercase letters or exclamation points  
- Attachments present or absent  

---

### **Unsupervised Learning Example**

**Scenario:** Customized music playlist.

* **Input data:** Millions of songs, but without "genre" or "mood" labels.
* **What the model does:** Analyzes features (bpm, instruments, key) and groups songs into similar clusters.
* **Real-world usage:** Spotify can recommend songs you don't know, but that fit within the music cluster you listen to.

Here I only have **inputs (song features)** without tags → the model finds **hidden patterns**.

Here I have **only input (email features)**, with **no labels** → therefore **unsupervised learning**.

### Input (X) → Features describing the email
- Email length (number of words/characters)  
- Presence of keywords  
- Sender's domain type (`@gmail`, `@yahoo`, `@biz`, …)  
- Number of links in the body  
- Frequency of uppercase letters or exclamation points  
- Attachments present or absent  

### What the model does
- Groups emails into **clusters** based on similarity.  
- Example results:  
  - **Cluster 1:** marketing/promotions  
  - **Cluster 2:** personal communications  
  - **Cluster 3:** suspicious/spam-like emails  
