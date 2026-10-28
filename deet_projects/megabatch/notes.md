# How to run deet

```sh
uv run deet experiments evaluate --config-path .\config.yaml
uv run deet experiments evaluate --config-path .\config_deepseek.yaml --run-name deepseek #chooses specific config and names the run
```

# f1 score: geo mean of precision and recall - marks (is lower) also imbalance btw higher and lower value
# accuracy : proportion of decisions that are correct (true pos+trueneg/all decisions)
# n_labels: nb of positives according to humans



