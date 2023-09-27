# ai-model-runtime-prediction
Submission for the Google AI Kaggle named "Google - Fast or Slow? Predict AI Model Runtime"

## Task
For a detailed task description look at the [Kaggle challenge](https://www.kaggle.com/competitions/predict-ai-model-runtime/data)

## Data
The TpuGraphs Dataset is described in detail in the [paper](https://arxiv.org/abs/2308.13490) from Google

## Approaches 

### Tile
We get node level embeddings by concatenating the feature vectors with the opcodes using an embedding layer for the opcodes. Together with the edge index we use a GNN and mean pooling to compute a graph level embedding. This is then concatenated with the configuration and put through a final linear layer to reduce to a runtime.

### Layout
For this problem we have vastly more available data which makes it more difficult to work and train with it.