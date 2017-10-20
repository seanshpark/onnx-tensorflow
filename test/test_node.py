from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest
import tensorflow as tf
import numpy as np
from onnxtf.backend import run_node
from onnx import helper

class TestStringMethods(unittest.TestCase):
  """ Tests for ops
  """
  def test_relu(self):
    node_def = helper.make_node("Relu", ["X"], ["Y"])
    X = np.random.uniform(-1, 1, 1000)
    output = run_node(node_def, [X])
    with tf.Session() as sess:
      ref_output = sess.run(tf.nn.relu(tf.constant(X)))
    np.testing.assert_almost_equal(output["Y"], ref_output)

if __name__ == '__main__':
  unittest.main()
