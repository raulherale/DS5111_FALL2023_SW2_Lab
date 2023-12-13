import pytest
import sys
sys.path.append(".")

from bin.perceptron import Perceptron

import os
import platform

#test that is expected to pass
def test_perceptron():
    #GIVEN a perceptron object
    the_perceptron = Perceptron()

    #WHEN the perceptron is trained with a known data set and class labels
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    #THEN  the prediction for new data points will be as expected
    assert the_perceptron.predict([1,1]) ==  1, "Incorrect class for data point [1,1]"
    assert the_perceptron.predict([1,0]) ==  1, "Incorrect class for data point [1,0]"
    assert the_perceptron.predict([0,1]) ==  1, "Incorrect class for data point [0,1]"
    assert the_perceptron.predict([0,0]) ==  0, "Incorrect class for data point [0,0]"


#test that is expected to fail
@pytest.mark.xfail(reason="xfail demo", strict=True)
def test_perceptron_fail():
    #GIVEN a perceptron object
    the_perceptron = Perceptron()

    #WHEN the perceptron is trained with a known data set and class labels
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    #THEN  the prediction for new data points will be as expected
    assert the_perceptron.predict([1,1]) ==  0, "Incorrect class for data point [1,1]"


#test that is conditionally skipped
@pytest.mark.skipif(platform.system()!= "Linux", reason="OS is not Linux Ubuntu")
def test_memory():
    # GIVEN we get all memory using os.popen()
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

    #THEN check for minimum amount of memory
    assert total_memory > 0, "Total memory is not >0"
    assert used_memory > 0, "Used memory is not >0"
    assert free_memory > 0, "Free memory is not >0"



#test that is always skipped
@pytest.mark.skip(reason="This test is not yet ready for prime time")
def test_always_skip_demo():
    x=10
    assert x == 5, "Incorrect value for x"


#parameterized test for different data sets
@pytest.mark.parametrize(
    "trainingset, labels, expected",
    [
        ([[1,1],[1,0],[0,1],[0,0]], [1,1,1,0], [1,1,1,0]),
        ([[1,1],[1,0],[0,1],[0,0]], [1,1,1,1], [1,1,1,1]),
        ([[1,1],[1,0],[0,1],[0,0]], [1,1,0,0], [1,1,0,0]),
        ([[1,1],[1,0],[0,1],[0,0]], [1,0,0,0], [1,0,0,0]),
        ([[1,1],[1,0],[0,1],[0,0]], [1,0,1,0], [1,0,1,0])

    ],
)

def test_perceptron_parameterize(trainingset, labels, expected):
    #GIVEN
    the_perceptron = Perceptron()

    #WHEN the perceptron is trained with a known data set and class labels
    the_perceptron.train(trainingset,labels)

    #THEN the prediction for new data points will be as expected
   # assert the_perceptron.predict(trainingset[0]) == expected[0], "Incorrect class"

    for input_data, exp in zip(trainingset, expected):
         assert the_perceptron.predict(input_data) == exp, f"Prediction for {input_data} failed"
