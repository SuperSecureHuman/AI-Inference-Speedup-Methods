# Speeding up Inference of deep learning models

This is a work in progress. Currently doing this for image classification models.

Will extend this idea to transformers models.


Rough checklist of ideas

- [X] Quantization
- [ ] Using quantized model with FastAPI (all the further techniques will include FastAPI benchmarks too)
- [ ] Checking intel's offerings for model inference (Intel One)
- [ ] Using TensorRT
- [ ] Using ONNX
- [ ] Nvidia triton (for server)

I need a better model, that has decently high inference time on stock pytorch (CPU). Raise an issue if you know an optimal model for this purpose :)

Not actively worked on - Reason https://github.com/nebuly-ai/nebullvm
