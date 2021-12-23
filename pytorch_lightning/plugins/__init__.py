from typing import Union

from pytorch_lightning.plugins.environments import ClusterEnvironment
from pytorch_lightning.plugins.io.checkpoint_plugin import CheckpointIO
from pytorch_lightning.plugins.io.torch_plugin import TorchCheckpointIO
from pytorch_lightning.plugins.io.xla_plugin import XLACheckpointIO
from pytorch_lightning.plugins.precision.apex_amp import ApexMixedPrecisionPlugin
from pytorch_lightning.plugins.precision.deepspeed import DeepSpeedPrecisionPlugin
from pytorch_lightning.plugins.precision.double import DoublePrecisionPlugin
from pytorch_lightning.plugins.precision.fully_sharded_native_amp import FullyShardedNativeMixedPrecisionPlugin
from pytorch_lightning.plugins.precision.ipu import IPUPrecisionPlugin
from pytorch_lightning.plugins.precision.native_amp import NativeMixedPrecisionPlugin
from pytorch_lightning.plugins.precision.precision_plugin import PrecisionPlugin
from pytorch_lightning.plugins.precision.sharded_native_amp import ShardedNativeMixedPrecisionPlugin
from pytorch_lightning.plugins.precision.tpu import TPUPrecisionPlugin
from pytorch_lightning.plugins.precision.tpu_bf16 import TPUBf16PrecisionPlugin
from pytorch_lightning.strategies.ddp import DDPStrategy
from pytorch_lightning.strategies.ddp2 import DDP2Strategy
from pytorch_lightning.strategies.ddp_spawn import DDPSpawnStrategy
from pytorch_lightning.strategies.deepspeed import DeepSpeedStrategy
from pytorch_lightning.strategies.dp import DataParallelStrategy
from pytorch_lightning.strategies.fully_sharded import DDPFullyShardedStrategy
from pytorch_lightning.strategies.horovod import HorovodStrategy
from pytorch_lightning.strategies.ipu import IPUStrategy
from pytorch_lightning.strategies.parallel import ParallelStrategy
from pytorch_lightning.strategies.sharded import DDPShardedStrategy
from pytorch_lightning.strategies.sharded_spawn import DDPSpawnShardedStrategy
from pytorch_lightning.strategies.single_device import SingleDeviceStrategy
from pytorch_lightning.strategies.single_tpu import SingleTPUStrategy
from pytorch_lightning.strategies.tpu_spawn import TPUSpawnStrategy
from pytorch_lightning.strategies.training_type_plugin import Strategy

PLUGIN = Union[Strategy, PrecisionPlugin, ClusterEnvironment, CheckpointIO]
PLUGIN_INPUT = Union[PLUGIN, str]

__all__ = [
    "CheckpointIO",
    "TorchCheckpointIO",
    "XLACheckpointIO",
    "ApexMixedPrecisionPlugin",
    "DataParallelStrategy",
    "DDP2Strategy",
    "DDPStrategy",
    "DDPSpawnStrategy",
    "DDPFullyShardedStrategy",
    "DeepSpeedStrategy",
    "DeepSpeedPrecisionPlugin",
    "DoublePrecisionPlugin",
    "HorovodStrategy",
    "IPUStrategy",
    "IPUPrecisionPlugin",
    "NativeMixedPrecisionPlugin",
    "PrecisionPlugin",
    "ShardedNativeMixedPrecisionPlugin",
    "FullyShardedNativeMixedPrecisionPlugin",
    "SingleDeviceStrategy",
    "SingleTPUStrategy",
    "TPUPrecisionPlugin",
    "TPUBf16PrecisionPlugin",
    "TPUSpawnStrategy",
    "Strategy",
    "ParallelStrategy",
    "DDPShardedStrategy",
    "DDPSpawnShardedStrategy",
]
