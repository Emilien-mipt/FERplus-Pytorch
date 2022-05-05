import os

from fer_pytorch.fer import FER

fer = FER()
fer.get_pretrained_model(model_name="mobilenetv2_140")


def test_fer():
    os.system("sh get_data.sh")

    test_result = fer.test_fer()

    assert isinstance(test_result, dict)
    assert ("accuracy" in test_result.keys()) and ("f1" in test_result.keys())
    assert (test_result["accuracy"] > 0.8) and (test_result["f1"] > 0.8)