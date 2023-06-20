"""
Utils
=====

.. automodule:: pydra.tasks.fsl.utils.fslchfiletype
.. automodule:: pydra.tasks.fsl.utils.fslfft
.. automodule:: pydra.tasks.fsl.utils.info
.. automodule:: pydra.tasks.fsl.utils.interleave
.. automodule:: pydra.tasks.fsl.utils.merge
.. automodule:: pydra.tasks.fsl.utils.orient
.. automodule:: pydra.tasks.fsl.utils.reorient2std
.. automodule:: pydra.tasks.fsl.utils.roi
.. automodule:: pydra.tasks.fsl.utils.selectvols
.. automodule:: pydra.tasks.fsl.utils.smoothfill
.. automodule:: pydra.tasks.fsl.utils.split
.. automodule:: pydra.tasks.fsl.utils.swapdim
"""

from .fslchfiletype import FSLChFileType
from .fslfft import FSLFFT
from .info import Info
from .interleave import Interleave
from .merge import Merge
from .orient import Orient
from .reorient2std import Reorient2Std
from .roi import ROI
from .selectvols import SelectVols
from .smoothfill import SmoothFill
from .split import Slice, Split
from .swapdim import SwapDim
