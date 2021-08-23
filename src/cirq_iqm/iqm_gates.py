# Copyright 2020–2021 Cirq on IQM developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""IQM parameterizations of two-qubit gate families, as native Cirq gates
"""
from __future__ import annotations

import cirq
from cirq import ops



def IsingGate(p: cirq.value.TParamVal) -> cirq.ops.ZZPowGate:
    r"""Rotation around the ZZ axis of the two-qubit Hilbert space.

    Generated by the Ising interaction Hamiltonian :math:`H_{\text{Ising}} = Z \otimes Z`.

    .. math::

       \text{Ising}(p) = \exp(-i H_{\text{Ising}} \: \frac{\pi}{2} \: p), \quad \text{where} \: p \in [0, 4).

    Args:
        p: group parameter

    Returns:
        corresponding Cirq gate
    """
    return ops.ZZPowGate(exponent=p, global_shift=-0.5)

def XYGate(p: cirq.value.TParamVal) -> cirq.ops.ISwapPowGate:
    r"""Rotation around the XX+YY axis of the two-qubit Hilbert space.

    Generated by the Hamiltonian :math:`H_{\text{XY}} = X \otimes X +Y \otimes Y`.

    .. math::

       \text{XY}(p) = \exp(-i H_{\text{XY}} \: \frac{\pi}{2} \: p), \quad \text{where} \: p \in [0, 2).

    Args:
        p: group parameter

    Returns:
        corresponding Cirq gate
    """
    return ops.ISwapPowGate(exponent=-2 * p, global_shift=0)