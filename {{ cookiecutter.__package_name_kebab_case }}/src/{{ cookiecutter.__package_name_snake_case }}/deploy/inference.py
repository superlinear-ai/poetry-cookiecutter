"""Inference script for a Sagemaker model."""
from sagemaker_inference import encoder
from lib.net import Net

def model_fn(model_dir):
    """Load the PyTorch model from the `model_dir` directory."""


def input_fn(request_body, request_content_type):
    """An input_fn that loads a numpy array from the request body.

    Args:
        request_body (io.BytesIO): Input data. This is data that has already been serialized by sagemaker.serializer.NumpySerializer()
        request_content_type (str): Request content type.
    """


def predict_fn(input_data, model, context):
    """Preprocess input data and make predictions.

    Args:
        input_data (torch.Tensor): Input data.
        model (torch.nn.Module): PyTorch model.
        context (sagemaker_inference.model_server.context.ModelServerContext): Model server context.

    Returns:
        torch.Tensor: Predictions.
    """

def output_fn(prediction, content_type, context):
    """An output_fn that dumps the prediction to a JSON format.

    Args:
        prediction (torch.Tensor): Predictions.
        content_type (str): Response content type (this must be specified as a sagemaker.deserializers.JSONDeserializer() if the output is a dictionary.
        context (sagemaker_inference.model_server.context.ModelServerContext): Model server context.
    """

