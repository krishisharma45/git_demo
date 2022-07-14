import os
import random
import logging

import mlflow as mlflow
import numpy as np
from src.training.trainer import Trainer
from src.training.training_session_arg_parser import TrainingSessionArgParser

LOGGER = logging.getLogger(__name__)


class TrainingSession:
    """Responsible for model training setup and configuration."""

    def __init__(self, args):
        self.args = args
        self.model = None
        self.trainer = None

    def run(self):
        self.seed_generators()
        self.configure_logging()
        self.create_directories()
        self.load_data()
        self.create_model()
        self.create_trainer()
        self.run_trainer()

    def seed_generators(self):
        if self.args.seed is not None:
            random.seed(self.args.seed)
            np.random.seed(self.args.seed)

    def configure_logging(self):
        mlflow.log_params(vars(self.args))
        mlflow.autolog()

    def create_directories(self):
        os.makedirs(self.args.log_dir, exist_ok=True)

    def load_data(self):
        pass

    def create_model(self):
        # self.model =
        pass

    def create_optimizer(self):
        pass

    def create_trainer(self):
        self.trainer = Trainer(self.model, self.args)

    def run_trainer(self):
        report = self.trainer.run()
        report.save(self.args.log_dir)


if __name__ == "__main__":
    args = TrainingSessionArgParser().parse_args()
    #mlflow.set_experiment("Test Run")
    with mlflow.start_run():
        session = TrainingSession(args)
        session.run()
