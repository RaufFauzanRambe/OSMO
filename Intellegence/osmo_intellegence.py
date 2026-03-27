import argparse
import sys
import logging
import json
import yaml   
from tqdm import tqdm
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("intellegence_osmo.log", mode="a")
    ]
)

def load_config(config_path):
    """Load configuration file (YAML or JSON)."""
    try:
        if config_path.endswith(".json"):
            with open(config_path, "r") as f:
                config = json.load(f)
        elif config_path.endswith(".yaml") or config_path.endswith(".yml"):
            with open(config_path, "r") as f:
                config = yaml.safe_load(f)
        else:
            logging.warning("Unsupported config format. Use .json or .yaml")
            return None

        logging.info("Configuration loaded successfully.")
        return config
    except Exception as e:
        logging.error(f"Failed to load config: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Intellegence OSMO Runner")
    parser.add_argument("--config", type=str, help="Path to configuration file (.json/.yaml)")
    parser.add_argument("--mode", type=str, default="train", help="Execution mode: train/eval/infer")
    parser.add_argument("--system", type=str, default="test", help="System run mode: test/training/execution")
    args = parser.parse_args()

    logging.info(f"Running Intellegence OSMO in mode: {args.mode}")
    logging.info(f"System run mode: {args.system}")

    config = None
    if args.config:
        config = load_config(args.config)

    if args.mode == "train":
        run_training(config)
    elif args.mode == "eval":
        run_evaluation(config)
    elif args.mode == "infer":
        run_inference(config)
    else:
        logging.warning("Unknown mode. Please use train/eval/infer.")

    if args.system == "test":
        run_system_test()
    elif args.system == "training":
        run_system_training()
    elif args.system == "execution":
        run_system_execution()
    else:
        logging.warning("Unknown system mode. Please use test/training/execution.")

def run_training(config):
    """Run training process with progress bar."""
    logging.info(f"Starting training with config: {config}")
    for i in tqdm(range(10), desc="Training Progress", unit="step"):
        time.sleep(0.5)  # simulate work

def run_evaluation(config):
    """Run evaluation process with progress bar."""
    logging.info(f"Starting evaluation with config: {config}")
    for i in tqdm(range(5), desc="Evaluation Progress", unit="step"):
        time.sleep(0.5)

def run_inference(config):
    """Run inference process with progress bar."""
    logging.info(f"Starting inference with config: {config}")
    for i in tqdm(range(3), desc="Inference Progress", unit="step"):
        time.sleep(0.5)

def run_system_test():
    logging.info("Running system in TEST mode...")

def run_system_training():
    logging.info("Running system in TRAINING mode...")

def run_system_execution():
    logging.info("Running system in EXECUTION mode...")

if __name__ == "__main__":
    sys.exit(main())
