"""Minimal integration examples using public framework APIs.

These functions are examples only; dependencies are optional and imported inside
functions so the base fabric remains lightweight.
"""

def ml_example(X, y):
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(max_iter=1000)
    return model.fit(X, y)

def dl_example(input_size: int, classes: int):
    import torch.nn as nn
    return nn.Sequential(nn.Linear(input_size, 128), nn.ReLU(), nn.Linear(128, classes))

def rl_environment(name: str = "CartPole-v1"):
    import gymnasium as gym
    return gym.make(name)

def symbolic_example():
    import sympy as sp
    x = sp.symbols("x")
    return sp.solve(sp.Eq(x**2 - 4, 0), x)

def cv_example(image):
    import cv2
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def nlp_example(text: str):
    import spacy
    nlp = spacy.blank("en")
    return nlp(text)
