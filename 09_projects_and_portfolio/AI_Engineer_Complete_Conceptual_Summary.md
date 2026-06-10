# AI Engineer — Riassunto Concettuale Completo

> Repository: `My_AI_Engineer_Portfolio_Projects`
> Obiettivo: Riordinare cronologicamente e concettualmente tutti gli appunti del percorso di certificazione AI Engineer.

---

## 1. Fondamenti Matematici

Prima di qualsiasi modello, servono gli strumenti matematici. Il percorso inizia con **Algebra Lineare**, **Probabilità** e **Teoria dell'Informazione**.

### Algebra Lineare — Cosa devi ricordare
| Concetto | Ruolo nell'AI |
|---|---|
| **Scalare, Vettore, Matrice, Tensore** | I tensori sono il formato universale dei dati in Deep Learning |
| **Prodotto Matriciale** | Ogni layer di una NN è una trasformazione lineare $y = Wx + b$ |
| **Norme L1/L2** | L1 → regolarizzazione LASSO (sparsità), L2 → Ridge (weight decay) |
| **Autovalori/Autovettori** | Direzioni invarianti di una trasformazione; usati in PCA e analisi di stabilità |
| **SVD ($A = UDV^T$)** | Decomposizione universale: PCA, pseudoinversa, compressione |
| **Pseudoinversa di Moore-Penrose** | Risolve $Ax = y$ anche quando $A$ non è invertibile |
| **PCA** | Proiezione sulla direzione di massima varianza — riduzione dimensionalità lineare |

### Probabilità — Cosa devi ricordare
| Concetto | Ruolo nell'AI |
|---|---|
| **Variabili aleatorie (discrete/continue)** | Descrivono incertezza in dati e modelli |
| **Teorema di Bayes** | $P(y|x) = \frac{P(x|y)P(y)}{P(x)}$ — base del machine learning probabilistico |
| **Massima Verosimiglianza (MLE)** | Metodo standard per stimare parametri: trova $\theta$ che massimizza $P(Dati|\theta)$ |
| **Valore Atteso e Varianza** | Bias e Variance sono aspettative dell'errore |
| **Indipendenza e Indipendenza Condizionale** | Base per factorization di modelli grafici |
| **Modelli Bayesiani (diretto)** | $P(x) = \prod_i P(x_i | parents(x_i))$ |
| **Modelli di Markov (indiretto)** | $P(x) = \frac{1}{Z} \prod_i \phi(C_i)$ normalizzato |

---

## 2. Artificial Intelligence — Visione d'Insieme

La gerarchia dei concetti, dal più generale al più specifico:

```
AI
 └── Machine Learning (apprendere da dati senza programmazione esplicita)
      └── Neural Networks (neuroni artificiali ispirati al cervello)
           └── Deep Learning (reti multi-layer)
                └── Transformers (architettura a self-attention, 2017)
                     └── Generative AI (non analizza, CREA)
                          └── GPT (Generative Pre-trained Transformer)
                               └── LLM (modelli linguistici su larga scala)
                                    └── GPT-4
                                         └── ChatGPT (applicazione conversazionale)
```

### Tipi di AI per capacità
- **Narrow AI** — esegue compiti specifici (es. Siri, raccomandazioni Netflix). È l'unica esistente oggi.
- **AGI (Strong AI)** — capacità cognitiva umana generale. Non esiste ancora.
- **Super AI** — supera l'intelligenza umana. Teorico.

### Aree di applicazione
NLP, Computer Vision, Generative AI, Robotica, Sistemi Esperti, Edge AI.

---

## 3. Machine Learning

### 3.1 Tassonomia dell'Apprendimento

```
Apprendimento Automatico
├── Supervisionato (dati etichettati)
│   ├── Classificazione → output discreto (es. spam/non spam)
│   └── Regressione → output continuo (es. prezzo casa)
├── Non Supervisionato (dati senza etichette)
│   ├── Clustering → gruppi basati su similarità
│   └── Riduzione Dimensionalità → PCA, Autoencoder
├── Reinforcement Learning → agente impara per trial-error con reward
└── Apprendimento con pochi esempi
    ├── Few-shot (2-10 esempi per classe)
    ├── One-shot (1 esempio)
    └── Zero-shot (nessun esempio, solo descrizione testuale)
```

### 3.2 Algoritmi di Classificazione (Supervisionati)

| Algoritmo | Meccanismo | Punti Chiave |
|---|---|---|
| **KNN** | Similarità tra punti vicini | K piccolo → overfitting; K grande → underfitting |
| **Decision Trees** | Albero di decisioni basato su feature | Criteri: Gini, Entropia. Soffre di overfitting (→ pruning) |
| **Logistic Regression** | Sigmoid $P(y=1|x) = \frac{1}{1+e^{-z}}$ | Produce probabilità; soglia 0.5 per classificare |
| **SVM** | Iperpiano a massimo margine | Kernel trick (lineare, polinomiale, RBF). Parametro C: soft/hard margin |
| **Random Forest** | Bagging di alberi decisionali | Riduce varianza |
| **XGBoost** | Boosting sequenziale | Riduce bias. Corregge errori dei modelli precedenti |
| **Softmax Regression** | Generalizzazione multi-classe della logistic regression | Assegna probabilità a K > 2 classi |
| **OvR / OvO** | Strategie per multiclass con classificatori binari | OvR: uno-contro-tutti; OvO: uno-contro-uno con voto |

### 3.3 Algoritmi di Regressione (Supervisionati)

| Algoritmo | Meccanismo |
|---|---|
| **Linear Regression** | $Y = \beta_0 + \beta_1 X_1 + \dots + \beta_n X_n + \varepsilon$ |
| **Regression Trees** | Alberi che predicono valori continui con MSE come criterio di split |
| **Random Forest Regressor** | Bagging di regression trees — riduce varianza |
| **SVR** | Trova un iperpiano che si adatti ai dati entro un "epsilon-tube" |

### 3.4 Clustering (Non Supervisionato)

| Algoritmo | Meccanismo |
|---|---|
| **K-Means** | Partiziona in K cluster minimizzando distanza intra-cluster. Metodo elbow per K ottimale |
| **Hierarchical Clustering** | Dendrogramma. Agglomerativo (bottom-up) o Divisivo (top-down) |
| **DBSCAN** | Basato su densità. Gestisce outliers e forme arbitrarie |

### 3.5 Metriche di Distanza
- **Euclidea** — distanza in linea retta
- **Manhattan** — distanza a griglia
- **Minkowski** — generalizzazione delle precedenti
- **Coseno** — similarità angolare (usata in NLP e embeddings)

### 3.6 Concetti Fondamentali ML

| Concetto | Spiegazione |
|---|---|
| **Overfitting** | Modello troppo complesso → impara il rumore, non generalizza |
| **Underfitting** | Modello troppo semplice → non cattura i pattern |
| **Bias (errore sistematico)** | Alto → underfitting |
| **Variance (variabilità)** | Alta → overfitting |
| **Bias-Variance Tradeoff** | Bagging ↓ varianza; Boosting ↓ bias |
| **Feature Scaling** | Standardizzare o normalizzare le feature |
| **One-Hot Encoding** | Codifica variabili categoriali |
| **Regularization** | L1 (LASSO) → sparsità; L2 (Ridge) → pesi piccoli |

---

## 4. Neural Networks

### 4.1 Architettura di Base
- **Neurone artificiale**: combinazione lineare $z = Wx + b$ → funzione di attivazione $a = f(z)$
- **Layer**: Input → Hidden(s) → Output
- **Shallow NN**: 1-2 hidden layer. Adatto a dati strutturati/tabulari
- **Deep NN (DNN)**: 3+ hidden layer. Impara rappresentazioni gerarchiche
- **MLP (Multilayer Perceptron)**: catena di trasformazioni lineari + non-linearità

### 4.2 Funzioni di Attivazione
| Funzione | Output | Uso |
|---|---|---|
| **Sigmoid** | (0, 1) | Classificazione binaria (output layer) |
| **Tanh** | (-1, 1) | Hidden layer (meglio di sigmoid) |
| **ReLU** | $[0, \infty)$ | Hidden layer (default moderno) |
| **Softmax** | Somma = 1 | Classificazione multi-classe (output layer) |

### 4.3 Processo di Training
```
Forward → Errore (Cost Function) → Backward (Backpropagation) → Aggiorna pesi (Gradient Descent) → Ripeti
```

- **Forward Propagation**: i dati attraversano la rete, layer dopo layer
- **Cost Function**: misura quanto la predizione è lontana dal ground truth
  - MSE (regressione), Binary Cross-Entropy (classif. binaria), Categorical Cross-Entropy (multiclasse)
- **Backpropagation**: l'errore torna indietro, calcola gradienti (regola della catena)
- **Gradient Descent**: aggiorna pesi $w_{new} = w_{old} - \alpha \cdot \nabla J$
- **Learning Rate ($\alpha$)**: controlla la velocità di aggiornamento

### 4.4 Ottimizzatori
| Ottimizzatore | Meccanismo |
|---|---|
| **SGD** | Aggiorna con 1 campione per volta |
| **Adam** | Momentum + adattivo. Il più usato in pratica |

### 4.5 Problemi e Soluzioni
| Problema | Soluzione |
|---|---|
| **Vanishing Gradient** | ReLU, Batch Normalization, ResNet |
| **Overfitting** | Dropout, L1/L2, Data Augmentation, Early Stopping |
| **Convergenza lenta** | Adam, Learning Rate scheduling, Batch Normalization |
| **Gradienti troppo piccoli/grandi** | Gradient Clipping, Batch Normalization |

---

## 5. Deep Learning — Architetture Avanzate

### 5.1 CNN (Convolutional Neural Network)
- **Input**: immagini, segnali audio (spettrogrammi)
- **Meccanismo**: filtri convoluzionali estraggono feature, pooling riduce dimensionalità
- **Layer chiave**: Conv2D, MaxPooling2D, Flatten, Dense
- **Stride**: passo del filtro
- **Strati finali**: Fully Connected + Softmax per classificazione
- **Data Augmentation**: rotazioni, flip, zoom → più dati artificialmente

### 5.2 RNN e LSTM
- **Input**: dati sequenziali (testo, serie temporali, audio)
- **Meccanismo**: memoria dello stato precedente passata al passo successivo
- **Problema**: Vanishing Gradient per sequenze lunghe
- **LSTM**: memoria a lungo termine con forget/input/output gate
- **Limitazione**: non parallellizzabile come Transformer

### 5.3 Autoencoder (Non Supervisionato)
- **Struttura**: Encoder → Latent Space → Decoder
- **Output target**: l'input stesso (ricostruzione)
- **Usi**: denoising, dimensionality reduction, feature extraction
- **Limitazione**: data-specific, non generalizza bene
- **VAE (Variational Autoencoder)**: versione probabilistica, genera nuovi dati
- **RBM (Restricted Boltzmann Machine)**: bilanciamento dataset, stima valori mancanti

### 5.4 GAN (Generative Adversarial Network)
- **Due reti in competizione**: Generator (crea) vs Discriminator (giudica)
- **Uso**: generazione immagini, super-resolution
- **Componente chiave**: Transpose Convolution (Conv2DTranspose) per up-sampling

### 5.5 Diffusion Models
- **Meccanismo**: aggiungono rumore gradualmente (forward) → imparano a rimuoverlo (reverse)
- **Superano i GAN** nella qualità dell'immagine generata
- **Rapporto col rumore**: il rumore è una perturbazione casuale aggiunta ai dati
- **Usati in**: Stable Diffusion, DALL·E

### 5.6 Trasferimento di Conoscenze (Transfer Learning)
- **Concetto**: riutilizzare un modello pre-addestrato su un nuovo task
- **Feature Extraction**: congela il convolutional base, allena solo il classificatore
- **Fine-Tuning**: sblocca alcuni layer e ri-allena su dati specifici

### 5.7 Trasformatori (Transformers)
- **Innovazione chiave**: Self-Attention Mechanism — ogni parola "guarda" tutte le altre
- **Multi-Head Attention**: più teste focalizzate su aspetti diversi dei dati
- **Architetture**:
  - **Encoder-only** (BERT) — comprensione del linguaggio
  - **Decoder-only** (GPT, LLaMA) — generazione del testo
  - **Encoder-Decoder** (T5, BART) — traduzione, summarization
- **Vantaggio su RNN**: parallellizzabile, cattura dipendenze lunghe
- **Tokenizzazione**: il testo viene spezzato in token (sub-word)

---

## 6. Large Language Models (LLM)

### 6.1 Concetti Fondamentali
- **Next Token Prediction**: un LLM prevede il prossimo token data la sequenza precedente
- **Modello Autoregressivo**: output generato a un passo diventa input al passo successivo
- **Pre-training**: addestramento iniziale su grandi dataset non etichettati (mascheramento o predizione)
- **Fine-tuning**: adattamento su dati specifici per un task

### 6.2 Strategie di Decodifica
| Strategia | Comportamento |
|---|---|
| **Greedy** | Sceglie sempre il token più probabile |
| **Beam Search** | Considera più sequenze candidate contemporaneamente |
| **Temperature** | Più alta → più creatività/randomicità |
| **Top-p (Nucleus Sampling)** | Campiona dal sottoinsieme di token con probabilità cumulativa ≤ p |

### 6.3 Embedding
- **Word Embedding**: mapping di parole in vettori densi continui
- **Embedding Layer**: rappresenta dati categorici/discreti come vettori
- **Latent Space**: spazio multidimensionale dove elementi simili sono vicini
- **Sentence Similarity**: misura la similarità semantica tra frasi (es. coseno)

### 6.4 Fine-Tuning Avanzato
- **Instruction-Tuned Model**: modello addestrato a seguire istruzioni (chat/comandi)
- **RLHF (Reinforcement Learning from Human Feedback)**: allineamento con preferenze umane
- **LoRA**: fine-tuning efficiente con matrici a basso rango
- **Catastrophic Forgetting**: la rete dimentica conoscenze precedenti imparando nuove
- **EWC (Elastic Weight Consolidation)**: rallenta l'apprendimento su pesi critici per preservare conoscenza passata

### 6.5 Architetture Miste
- **Mixture of Experts (MoE)**: combina modelli "esperti" specializzati per efficienza
- **Multi-Head Attention Layer**: più teste che catturano diversi pattern
- **Layer Normalization**: normalizza attivazioni all'interno di ogni layer (vs BatchNorm che normalizza sul batch)

---

## 7. AI Agents

### 7.1 Cos'è un AI Agent
Sistema che usa un modello AI per **interagire con l'ambiente, ragionare, pianificare ed eseguire azioni**.

### 7.2 Ciclo Fondamentale
```
Thought (pensiero) → Action (azione/tool call) → Observation (osservazione risultato) → Ripeti
```

### 7.3 Componenti Chiave
| Componente | Descrizione |
|---|---|
| **LLM** | Cervello del ragionamento |
| **Tool** | Funzione esterna (calcolo, API, web search, DB query) |
| **Tool Calling** | LLM genera chiamate strutturate (es. JSON) |
| **Memory Integration** | Ricorda interazioni passate |
| **System Message** | Istruzione persistente che definisce il comportamento dell'agente |
| **Chat Template** | Struttura predefinita messaggio utente/assistente |

### 7.4 Tipi di Agenti
- **Function-Calling Agent**: genera chiamate funzioni strutturate (JSON)
- **Code AI Agent**: genera ed esegue codice Python
- **JSON AI Agent**: azioni in formato JSON
- **Dummy Agent**: implementazione minimale didattica

### 7.5 Framework
- **SmolAgents (Hugging Face)**: leggero per workflow semplici
- **LangGraph**: grafi di agenti per workflow complessi
- **LlamaIndex**: retrieval e search per RAG
- **LangChain**: catene di chiamate LLM + tool

### 7.6 RAG (Retrieval-Augmented Generation)
- **Processo**: recupera conoscenza esterna → la inserisce nel contesto → genera risposta
- **Embedding**: vettorizza documenti per retrieval semantico
- **Similarità Coseno**: misura quanto due embedding sono vicini
- **Vector Database**: memorizza e ricerca embedding efficientemente

### 7.7 Concetti Avanzati Agenti
- **Context Length**: massimo numero di token che un LLM può elaborare
- **Conversation History**: sequenza messaggi pregressi nel prompt
- **Planning Interval**: periodo in cui l'agente rivaluta la strategia
- **Workflow**: Osserva → Pensa → Agisci

---

## 8. Reinforcement Learning

### 8.1 Concetti Base
- **Agente**: prende decisioni
- **Ambiente**: mondo simulato con cui interagisce
- **Azione**: ciò che l'agente fa
- **Reward**: feedback positivo/negativo
- **Policy ($\pi$)**: strategia che mappa stato → azione ("il cervello dell'agente")
- **Stato**: situazione corrente dell'ambiente

### 8.2 Algoritmi
| Algoritmo | Descrizione |
|---|---|
| **Q-Learning** | Impara Q(s,a) — valore atteso di fare azione "a" in stato "s" |
| **Deep Q-Network (DQN)** | Usa una NN invece della Q-table per stimare Q(s,a) |
| **Epsilon-Greedy** | Bilancia esplorazione (casuale) e sfruttamento (best action) |
| **Experience Replay** | Buffer FIFO di esperienze passate, campionate casualmente per training stabile |
| **Target Network** | Copia stabile della Q-network usata per calcolare target di training |
| **Bellman Equation** | $Q(s,a) = R(s,a) + \gamma \max_{a'} Q(s',a')$ |

### 8.3 RLHF
Combina Reinforcement Learning con feedback umano per allineare il comportamento dell'LLM ai valori umani. Usato in ChatGPT.

---

## 9. AI Red Teaming & Safety

### 9.1 Cos'è il Red Teaming
Pratica di **simulare attacchi realistici** per trovare vulnerabilità in modelli e sistemi AI PRIMA che vengano sfruttate.

### 9.2 Rischi Osservati (dal tuo case study)
| Rischio | Descrizione |
|---|---|
| **Memory Creep** | Il modello reintroduce argomenti proibiti dopo che l'utente ha posto confini espliciti |
| **Alignment Failure** | Il modello sovrascrive le istruzioni dell'utente con policy interne (es. paternalismo clinico) |
| **Recovery Failure** | Si scusa ma ricade nello stesso errore (correzione solo superficiale) |
| **Persona Bias** | Differenze dannose quando il sistema assume identità demografiche diverse |
| **Guardrail Override** | Barriere di sicurezza che diventano controproducenti e ignorano la volontà dell'utente |

### 9.3 Framework di Riferimento

| Framework | Focus |
|---|---|
| **NIST AI RMF** | Gestione rischio AI (Map, Measure, Manage, Govern) |
| **NIST GenAI Profile** | Estensione per rischi specifici GenAI (allucinazioni, prompt injection, memoria) |
| **OWASP Top 10 LLM** | Lista vulnerabilità (prompt injection, data leakage, insecure output) |
| **MITRE ATLAS** | Tattiche e tecniche avversarie contro AI |

### 9.4 Mitigazioni Proposte
- **Hard Context Decay**: blocca/strip entità vietate dal contesto attivo
- **Respect-User-Steer Mode**: interruttore che dà priorità alle istruzioni utente
- **Recovery Verification Loop**: dopo una violazione, monitora le successive N risposte
- **Human-in-the-Loop**: validazione umana obbligatoria per azioni di enforcement
- **Blocklist**: filtro pre-processing che rimuove token specifici

---

## 10. Fondamenti Filosofici e Teorici

Basati sul libro *The Emperor's New Mind* di Penrose.

### 10.1 Computabilità
- **Turing Machine**: modello astratto con stati finiti, nastro infinito, testina r/w
- **Universal Turing Machine**: legge la descrizione di un'altra TM e la emula
- **Halting Problem**: non esiste algoritmo che decida se un programma termina (indecidibile)
- **Church-Turing Thesis**: "computabile" = calcolabile da una TM
- **Gödel**: limiti dei sistemi assiomatici formali

### 10.2 Filosofia della Mente
- **Penrose**: sostiene che la coscienza non è (solo) algoritmica — usa processi fisici non computabili
- **Searle — Chinese Room**: obiezione: eseguire un algoritmo non equivale a "capire"
- **Turing Test**: se indistinguibile da un umano in conversazione, "pensa" (tesi dibattuta)

---

## 11. Etica e Sfide dell'AI

- **Bias** → dati distorti producono risultati discriminatori
- **Privacy** → raccolta e uso intrusivo di dati personali
- **Manipolazione** → GenAI può creare fake news
- **Trasparenza** → i modelli devono essere spiegabili
- **Trust Calibration** → bilanciare fiducia e scetticismo nell'output AI

---

## 12. Toolchain & Framework

### Python per AI
| Strumento | Ruolo |
|---|---|
| **TensorFlow/Keras** | Building e training di reti neurali |
| **PyTorch** | Framework flessibile per ricerca e produzione |
| **Hugging Face Transformers** | Modelli pre-addestrati NLP |
| **SmolAgents** | Agenti AI leggeri |
| **LangChain / LangGraph** | Orchestrazione agenti e catene LLM |
| **LlamaIndex** | RAG e indicizzazione documenti |
| **Stable-Baselines3** | RL su PyTorch |
| **NLTK** | NLP classico (tokenizzazione, stemming) |
| **ONNX** | Formato aperto per scambio modelli tra framework |

### MLOps / LLMOps
- **Hyperparameter Tuning**: Keras Tuner, ricerca a griglia
- **Mixed Precision Training**: FP16 + FP32 per accelerare e ridurre memoria
- **Model Optimization**: quantizzazione, pruning, distilazione
- **Observability & Evaluation**: monitoraggio performance e sicurezza in produzione

---

## Mappa Concettuale — Cronologia degli Studi

```
1. Fondamenti Matematici (Algebra Lineare, Probabilità)
       ↓
2. AI — Panoramica Generale (tassonomia, tipi, aree)
       ↓
3. Machine Learning (supervised, unsupervised, algoritmi)
       ↓
4. Neural Networks (neurone, forward/backward, training loop)
       ↓
5. Deep Learning (CNN, RNN, Autoencoder, GAN, Diffusion)
       ↓
6. Transformers (self-attention, encoder/decoder, pre-training)
       ↓
7. LLM & Generative AI (GPT, fine-tuning, RLHF, embedding)
       ↓
8. AI Agents & RAG (tool calling, agent cycle, retrieval)
       ↓
9. Reinforcement Learning (Q-learning, DQN, policy)
       ↓
10. AI Safety & Red Teaming (allineamento, rischi, mitigazioni)
       ↓
11. Filosofia & Teoria (computabilità, Penrose, Searle)
       ↓
12. Etica, Toolchain, MLOps
```

---

*Riassunto generato il 09/06/2026 da tutto il materiale presente nella repository.*
