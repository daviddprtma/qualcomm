# -*- coding: utf-8 -*-
"""IntroductionToQualcommAIHub.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YgAUSoGwLhSzNCXwJ_-C1IkGgCfhHY22
"""

pip install qai-hub

!qai-hub configure --api_token d4a46d95c152fd0151860c201f1b1cea9014eb28

import qai_hub as hub
hub.get_devices()