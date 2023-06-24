'''
第一部分 d2l软件包是轻量级的，仅需要以下软件包和模块作为依赖项
#@save
import collections
import hashlib
import math
import os
import random
import re
import shutil
import sys
import tarfile
import time
import zipfile
from collections import defaultdict
import pandas as pd
import requests
from IPython import display
from matplotlib import pyplot as plt
from matplotlib_inline import backend_inline
d2l = sys.modules[__name__]

第二部分 从PyTorch导⼊模块。
#@save
import numpy as np
import torch
(continues on next page)
(continued from previous page)
import torchvision
from PIL import Image
from torch import nn
from torch.nn import functional as F
from torch.utils import data
from torchvision import transforms
'''

