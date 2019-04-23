import torch
import os
from torch.utils.ffi import create_extension
this_file = os.path.dirname(os.path.realpath(__file__))

extra_objects = ['src/interpolate_cuda_kernel.o']
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]
ffi = create_extension(
    name='_ext.interpolate',
    headers=['src/interpolation_cuda.h'],
    sources=['src/interpolation_cuda.c'],
    define_macros=[('WITH_CUDA', None)],
    with_cuda=True,
    relative_to=__file__,
    extra_objects=extra_objects,
    extra_compile_args=["-I/usr/local/cuda-8.0/include"])
ffi.build()