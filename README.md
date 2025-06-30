# retico-crisperasr
Local crisper whisper ASR module for ReTiCo. Crisper whisper is better at capturing disfluencies which are often ignored by whisper, and should be more accurate in general. We do not provide support for CrisperWhisper's word-level timestamps, as they use a forked version of transformers that is incompatible with other retico modules. See citation for more details. CrisperWhisper is a relatively large model, and performance might be poor on weaker systems. Consider using `retico-whisperasr` on a weaker setup.

### Requirements

This module was built using `python=3.10`, Requirements can be installed with pip:
```
pip install -r requirements.txt
```
You will likely want `cuBLAS` and `cuDNN` for GPU execution.

### Example

You do not need to specify an language, CrisperWhisper will automatically detect the language. The model was trained only on German and English audio.
```python
import os
import sys

os.environ['RETICO'] = 'retico-core'
os.environ['CRISPER'] = 'retico-crisperasr'
sys.path.append(os.environ['RETICO'])
sys.path.append(os.environ['CRISPER'])

from retico_core import *
from retico_core.audio import MicrophoneModule
from retico_core.debug import DebugModule
from retico_crisperasr.crisperasr import CrisperASRModule


mic = MicrophoneModule()
debug = DebugModule()
asr = CrisperASRModule()

mic.subscribe(asr)
asr.subscribe(debug)

mic.run()
asr.run()
debug.run()

input()

debug.stop()
asr.stop()
mic.stop()
```
### Citation

[CrisperWhisper repo](https://github.com/nyrahealth/CrisperWhisper/tree/main)
```
@inproceedings{zusag24_interspeech,
    title     = {CrisperWhisper: Accurate Timestamps on Verbatim Speech Transcriptions},
    author    = {Mario Zusag and Laurin Wagner and Bernhad Thallinger},
    year      = {2024},
    booktitle = {Interspeech 2024},
    pages     = {1265--1269},
    doi       = {10.21437/Interspeech.2024-731},
    issn      = {2958-1796},
}
```
