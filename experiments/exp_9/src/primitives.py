"""
src/primitives.py
=================
Custom protected mathematical primitives for gplearn in Experiment 9.
Includes: sin, cos, exp, tan, cosec, sec, mod, ceil, sign, nth_root, gaussian_function, pow.
All primitives are numerical-exception safe (preventing NaN, Inf, overflow, underflow).
"""

import numpy as np
from gplearn.functions import make_function

def _protected_pow(x1, x2):
    with np.errstate(all='ignore'):
        abs_x1 = np.abs(x1)
        abs_x1 = np.where(abs_x1 < 1e-6, 1e-6, abs_x1)
        x2_clip = np.clip(x2, -5.0, 5.0)
        res = np.power(abs_x1, x2_clip)
        return np.nan_to_num(res, nan=1.0, posinf=1e6, neginf=-1e6)

def _protected_sin(x):
    with np.errstate(all='ignore'):
        return np.sin(x)

def _protected_cos(x):
    with np.errstate(all='ignore'):
        return np.cos(x)

def _protected_exp(x):
    with np.errstate(all='ignore'):
        x_clip = np.clip(x, -10.0, 10.0)
        return np.exp(x_clip)

def _protected_tan(x):
    with np.errstate(all='ignore'):
        res = np.tan(x)
        return np.nan_to_num(res, nan=0.0, posinf=100.0, neginf=-100.0)

def _protected_cosec(x):
    with np.errstate(all='ignore'):
        denom = np.sin(x)
        res = np.where(np.abs(denom) < 1e-4, 1.0, 1.0 / denom)
        return np.nan_to_num(res, nan=1.0, posinf=100.0, neginf=-100.0)

def _protected_sec(x):
    with np.errstate(all='ignore'):
        denom = np.cos(x)
        res = np.where(np.abs(denom) < 1e-4, 1.0, 1.0 / denom)
        return np.nan_to_num(res, nan=1.0, posinf=100.0, neginf=-100.0)

def _protected_mod(x1, x2):
    with np.errstate(all='ignore'):
        denom = np.where(np.abs(x2) < 1e-4, 1.0, x2)
        res = np.fmod(x1, denom)
        return np.nan_to_num(res, nan=0.0, posinf=0.0, neginf=0.0)

def _protected_ceil(x):
    with np.errstate(all='ignore'):
        return np.ceil(x)

def _protected_sign(x):
    with np.errstate(all='ignore'):
        return np.sign(x)

def _protected_nth_root(x1, x2):
    with np.errstate(all='ignore'):
        abs_x1 = np.abs(x1)
        abs_x1 = np.where(abs_x1 < 1e-6, 1e-6, abs_x1)
        n = np.where(np.abs(x2) < 1.0, 1.0, np.abs(x2))
        n = np.clip(n, 1.0, 10.0)
        res = np.power(abs_x1, 1.0 / n)
        return np.nan_to_num(res, nan=1.0, posinf=10.0, neginf=0.0)

def _protected_gaussian(x):
    with np.errstate(all='ignore'):
        x_clip = np.clip(x, -10.0, 10.0)
        return np.exp(- (x_clip ** 2))

# Wrap using gplearn's make_function
pow_primitive = make_function(function=_protected_pow, name='pow', arity=2)
sin_primitive = make_function(function=_protected_sin, name='sin', arity=1)
cos_primitive = make_function(function=_protected_cos, name='cos', arity=1)
exp_primitive = make_function(function=_protected_exp, name='exp', arity=1)
tan_primitive = make_function(function=_protected_tan, name='tan', arity=1)
cosec_primitive = make_function(function=_protected_cosec, name='cosec', arity=1)
sec_primitive = make_function(function=_protected_sec, name='sec', arity=1)
mod_primitive = make_function(function=_protected_mod, name='mod', arity=2)
ceil_primitive = make_function(function=_protected_ceil, name='ceil', arity=1)
sign_primitive = make_function(function=_protected_sign, name='sign', arity=1)
nth_root_primitive = make_function(function=_protected_nth_root, name='nth_root', arity=2)
gaussian_primitive = make_function(function=_protected_gaussian, name='gaussian_function', arity=1)

EXTENDED_FUNCTION_SET = (
    'add', 'sub', 'mul', 'div', 'neg', 'abs', 'log',
    pow_primitive, sin_primitive, cos_primitive, exp_primitive,
    tan_primitive, cosec_primitive, sec_primitive, mod_primitive,
    ceil_primitive, sign_primitive, nth_root_primitive, gaussian_primitive
)
