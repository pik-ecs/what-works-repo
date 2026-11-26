"""Pre-fetch every HF model the pipeline needs into the local/cluster cache."""

from transformers import pipeline

from what_works_repo.classify.tuning import CANDIDATES
from what_works_repo.settings import settings

names = [m.name for m in settings.ml.pretrained_models]
names += [c.model_name for c in CANDIDATES.values() if c.model_name]

for name in names:
    print(f"Downloading {name}...")
    try:
        pipeline(
            "text-classification", model=name
        )  # Downloads model + tokenizer + config
        print(f"✓ {name}")
    except Exception as e:
        print(f"✗ {name}: {e}")
