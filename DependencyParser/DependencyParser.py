import os
import time
import tensorflow as tf
import numpy as np
from base_model import Model
from params_init import random_uniform_initializer, random_normal_initializer, xavier_initializer
from utils.general_utils import Progbar
from utils.general_utils import get_minibatches
from utils.feature_extraction import load_datasets, DataConfig, Flags, punc_pos, pos_prefix
from utils.tf_utils import visualize_sample_embeddings