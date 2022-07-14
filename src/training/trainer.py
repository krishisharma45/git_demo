import logging

LOGGER = logging.getLogger(__name__)


class Trainer:
    def __init__(self, model, args):
        """Trainer is responsible for constructing and training a model."""
        self.model = model
        self.args = args

    def run(self):
        pass
