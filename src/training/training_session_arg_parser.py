import time
import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


class TrainingSessionArgParser(ArgumentParser):
    """Parses TrainingSession command-line options and arguments."""

    def __init__(self):
        super().__init__(
            prog="train.sh",
            description="Train model",
            formatter_class=ArgumentDefaultsHelpFormatter,
        )
        self.timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        self.add_argument(
            "--batch_size",
            type=int,
            default=64,
            help="Number of training examples used per batch.",
        )
        self.add_argument(
            "--epochs",
            type=int,
            default=10,
            help="Number of full training passes over the entire dataset.",
        )
        self.add_argument(
            "--patience",
            type=int,
            default=5,
            help="Number of epochs without improvement after which training stops.",
        )
        self.add_argument(
            "--seed", type=int, default=None, help="Seed for random number generators."
        )
        self.add_argument(
            "--timestamp",
            type=str,
            default=f"{time.strftime('%Y-%m-%d_%H:%M:%S')}",
            help="Timestamp generated at runtime (automatic)",
        )
        self.add_argument(
            "--log_dir",
            type=str,
            default=os.path.join("logs", self.timestamp),
            help="Directory where training progress and model checkpoints are saved.",
        )
