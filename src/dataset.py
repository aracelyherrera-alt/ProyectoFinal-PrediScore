"""Generación y preparación del dataset sintético del proyecto."""
import numpy as np

def generar_dataset(n=600, seed=42):
    rng = np.random.default_rng(seed)
    horas = rng.uniform(0, 10, n)
    asistencia = rng.uniform(45, 100, n)
    nota = rng.uniform(5, 20, n)
    puntaje = 0.32 * horas + 0.38 * (asistencia / 10) + 0.30 * nota
    ruido = rng.normal(0, 1.25, n)
    y = (puntaje + ruido >= 11.0).astype(int)
    X = np.column_stack([horas, asistencia, nota])
    return X, y.reshape(-1, 1)

def dividir(X, y, train=0.7, val=0.1, seed=42):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    X, y = X[idx], y[idx]
    n = len(X); nt = int(n * train); nv = int(n * val)
    return X[:nt], y[:nt], X[nt:nt+nv], y[nt:nt+nv], X[nt+nv:], y[nt+nv:]

def normalizar(X_train, *otros):
    media = X_train.mean(axis=0)
    std = X_train.std(axis=0)
    std = np.where(std < 1e-8, 1.0, std)
    salida = [(X_train - media) / std]
    salida.extend([(X - media) / std for X in otros])
    return (*salida, media, std)
